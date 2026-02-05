# markdown.py
import re

# --- helpers ---------------------------------------------------------------

_HEADER_RE = re.compile(r"^(#{1,6}) (.*)$")
_LIST_RE = re.compile(r"^\* (.*)$")

# NOTE: canonical tests only need "one occurrence per line" behavior.
# The original code used re.match('(.*)__(.*)__(.*)') which effectively
# replaces only one bold segment (the leftmost, due to greediness).
_BOLD_RE = re.compile(r"^(.*)__(.*)__(.*)$")
_ITALIC_RE = re.compile(r"^(.*)_(.*)_(.*)$")

# Lines that already became HTML tags should not be wrapped in <p>.
_HTML_START_RE = re.compile(r"^<(h[1-6]|ul|li|p)")


def _apply_inline(text: str) -> str:
    """
    Apply inline markdown in the same way as the original implementation:
    - at most one bold replacement and at most one italic replacement
    - bold is applied before italics
    - patterns are greedy: (.*)__(.*)__(.*) and (.*)_(.*)_(.*)
    """
    m = _BOLD_RE.match(text)
    if m:
        text = f"{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}"

    m = _ITALIC_RE.match(text)
    if m:
        text = f"{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}"

    return text


def _to_block(line: str) -> tuple[str, bool]:
    """
    Convert a raw markdown line to a block-level HTML fragment.

    Returns:
      (html_fragment, is_list_item)
    """
    # headers
    m = _HEADER_RE.match(line)
    if m:
        level = len(m.group(1))
        # IMPORTANT: header text should not be further parsed for inline markdown
        # (matches canonical tests).
        return f"<h{level}>{m.group(2)}</h{level}>", False

    # list item
    m = _LIST_RE.match(line)
    if m:
        content = _apply_inline(m.group(1))
        return f"<li>{content}</li>", True

    # paragraph
    content = _apply_inline(line)
    return f"<p>{content}</p>", False


# --- public API ------------------------------------------------------------

def parse(markdown: str) -> str:
    """
    Parse Exercism's simplified markdown into HTML.

    Refactor notes (vs original):
    - isolated inline parsing into _apply_inline()
    - isolated block detection into _to_block()
    - simplified list state handling with explicit open/close
    - preserved original behavior:
        * headers don't parse inline markdown
        * list items & paragraphs parse inline markdown
        * list closes immediately when a non-list line appears
        * output is concatenated with no extra whitespace/newlines
    """
    lines = markdown.split("\n")
    out: list[str] = []
    in_list = False

    for line in lines:
        block, is_list_item = _to_block(line)

        if is_list_item and not in_list:
            out.append("<ul>")
            in_list = True

        if (not is_list_item) and in_list:
            out.append("</ul>")
            in_list = False

        out.append(block)

    if in_list:
        out.append("</ul>")

    return "".join(out)
