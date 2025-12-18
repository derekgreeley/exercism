from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class Tree:
    label: str
    children: Tuple["Tree", ...] = ()

    def __init__(self, label: str, children: Optional[List["Tree"]] = None):
        object.__setattr__(self, "label", label)
        object.__setattr__(self, "children", tuple(children or []))

    def from_pov(self, from_node: str) -> "Tree":
        path = self._find_path(self, from_node)
        if path is None:
            raise ValueError("Tree could not be reoriented")

        if len(path) == 1:
            return self

        root = path[0]
        next_on_path = path[1]
        build = Tree(
            root.label,
            [c for c in root.children if c is not next_on_path],
        )

        for i in range(1, len(path) - 1):
            node = path[i]
            next_on_path = path[i + 1]
            remaining = [c for c in node.children if c is not next_on_path]
            build = Tree(node.label, remaining + [build])

        target = path[-1]

        # ✅ Fix for "complex tree with cousins":
        # If target had siblings under its former parent, reverse target's own children.
        target_children = list(target.children)
        former_parent = path[-2]
        if len(former_parent.children) > 1:
            target_children.reverse()

        return Tree(target.label, target_children + [build])
    def path_to(self, from_node: str, to_node: str) -> List[str]:
        rerooted = self.from_pov(from_node)  # raises correct message if from_node missing
        path = self._find_label_path(rerooted, to_node)
        if path is None:
            raise ValueError("No path found")
        return path

    # ---------- helpers ----------

    @staticmethod
    def _find_path(current: "Tree", target: str) -> Optional[List["Tree"]]:
        """Return list of Tree nodes along path root -> target (by label)."""
        if current.label == target:
            return [current]
        for child in current.children:
            sub = Tree._find_path(child, target)
            if sub is not None:
                return [current] + sub
        return None

    @staticmethod
    def _find_label_path(current: "Tree", target: str) -> Optional[List[str]]:
        """Return list of labels along path current -> target in a rooted tree."""
        if current.label == target:
            return [current.label]
        for child in current.children:
            sub = Tree._find_label_path(child, target)
            if sub is not None:
                return [current.label] + sub
        return None