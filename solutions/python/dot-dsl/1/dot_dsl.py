NODE = 1
EDGE = 2
ATTR = 3


class Node:
    def __init__(self, name, attrs=None):
        self.name = name
        self.attrs = attrs if attrs is not None else {}

    def __eq__(self, other):
        return (
            isinstance(other, Node)
            and self.name == other.name
            and self.attrs == other.attrs
        )


class Edge:
    def __init__(self, src, dst, attrs=None):
        self.src = src
        self.dst = dst
        self.attrs = attrs if attrs is not None else {}

    def __eq__(self, other):
        return (
            isinstance(other, Edge)
            and self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is None:
            data = []

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

        for item in data:
            if not isinstance(item, tuple):
                raise TypeError("Graph data malformed")

            if len(item) < 2:
                raise TypeError("Graph item incomplete")

            item_type = item[0]

            if item_type == NODE:
                if len(item) != 3:
                    raise ValueError("Node is malformed")

                _, name, attrs = item

                if not isinstance(name, str) or not isinstance(attrs, dict):
                    raise ValueError("Node is malformed")

                self.nodes.append(Node(name, attrs))

            elif item_type == EDGE:
                if len(item) != 4:
                    raise ValueError("Edge is malformed")

                _, src, dst, attrs = item

                if (
                    not isinstance(src, str)
                    or not isinstance(dst, str)
                    or not isinstance(attrs, dict)
                ):
                    raise ValueError("Edge is malformed")

                self.edges.append(Edge(src, dst, attrs))

            elif item_type == ATTR:
                if len(item) != 3:
                    raise ValueError("Attribute is malformed")

                _, key, value = item

                if not isinstance(key, str) or not isinstance(value, str):
                    raise ValueError("Attribute is malformed")

                self.attrs[key] = value

            else:
                raise ValueError("Unknown item")