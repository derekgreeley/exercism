# sgf_parsing.py

from dataclasses import dataclass, field


@dataclass(eq=True)
class SgfTree:
    properties: dict[str, list[str]] = field(default_factory=dict)
    children: list["SgfTree"] = field(default_factory=list)


class _Parser:
    def __init__(self, text: str):
        self.text = text
        self.i = 0
        self.n = len(text)

    def parse(self) -> SgfTree:
        if not self.text or self._peek() != "(":
            raise ValueError("tree missing")

        tree = self._parse_tree()

        if self.i != self.n:
            raise ValueError("tree missing")

        return tree

    def _parse_tree(self) -> SgfTree:
        self._expect("(")

        if self._peek() != ";":
            raise ValueError("tree with no nodes")

        nodes = []
        while self._peek() == ";":
            nodes.append(self._parse_node())

        if not nodes:
            raise ValueError("tree with no nodes")

        # Variations attach to the last node in the main sequence
        while self._peek() == "(":
            nodes[-1].children.append(self._parse_tree())

        self._expect(")")

        # Convert linear node sequence into linked children chain
        root = nodes[0]
        current = root
        for node in nodes[1:]:
            current.children.append(node)
            current = node
        return root

    def _parse_node(self) -> SgfTree:
        self._expect(";")
        props: dict[str, list[str]] = {}

        while True:
            ch = self._peek()
            if ch is None or ch in ";()":
                break

            key = self._parse_prop_ident()
            if self._peek() != "[":
                raise ValueError("properties without delimiter")

            values = []
            while self._peek() == "[":
                values.append(self._parse_prop_value())

            props[key] = values

        return SgfTree(properties=props)

    def _parse_prop_ident(self) -> str:
        start = self.i
        while self._peek() is not None and self._peek().isalpha():
            self.i += 1

        ident = self.text[start:self.i]
        if not ident:
            raise ValueError("properties without delimiter")
        if not ident.isupper():
            raise ValueError("property must be in uppercase")
        return ident

    def _parse_prop_value(self) -> str:
        self._expect("[")
        out = []

        while True:
            ch = self._peek()
            if ch is None:
                raise ValueError("properties without delimiter")
            if ch == "]":
                self.i += 1
                return "".join(out)
            if ch == "\\":
                self.i += 1
                esc = self._peek()
                if esc is None:
                    raise ValueError("properties without delimiter")

                # Escaped newline disappears entirely
                if esc == "\n":
                    self.i += 1
                    continue

                # Escaped whitespace other than newline becomes a space
                if esc.isspace():
                    self.i += 1
                    out.append(" ")
                    continue

                # Any other escaped character is inserted as-is
                self.i += 1
                out.append(esc)
                continue

            # Unescaped whitespace: newline stays, other whitespace -> space
            self.i += 1
            if ch == "\n":
                out.append("\n")
            elif ch.isspace():
                out.append(" ")
            else:
                out.append(ch)

    def _peek(self):
        if self.i >= self.n:
            return None
        return self.text[self.i]

    def _expect(self, ch: str) -> None:
        if self._peek() != ch:
            raise ValueError("tree missing")
        self.i += 1


def parse(input_string: str) -> SgfTree:
    return _Parser(input_string).parse()