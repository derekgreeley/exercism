# tree_building.py

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Record:
    record_id: int
    parent_id: int


@dataclass
class Node:
    node_id: int
    children: List["Node"] = field(default_factory=list)


def BuildTree(records: List[Record]) -> Optional[Node]:
    """
    BuildTree(records) -> root Node or None if records is empty.

    Raises ValueError with *exact* messages required by the tests:
      - "Record id is invalid or out of order."
      - "Only root should have equal record and parent id."
      - "Node parent_id should be smaller than its record_id."
    """
    if not records:
        return None

    n = len(records)
    ordered = sorted(records, key=lambda r: r.record_id)

    # Must be continuous 0..n-1 in order (root must exist and be id 0)
    for expected_id, rec in enumerate(ordered):
        if rec.record_id != expected_id:
            raise ValueError("Record id is invalid or out of order.")

        if rec.record_id == 0:
            # Root must point to itself
            if rec.parent_id != 0:
                raise ValueError("Node parent_id should be smaller than its record_id.")
        else:
            # Non-root may not point to itself
            if rec.parent_id == rec.record_id:
                raise ValueError("Only root should have equal record and parent id.")
            # Parent must be strictly smaller
            if rec.parent_id > rec.record_id:
                raise ValueError("Node parent_id should be smaller than its record_id.")

    # Create nodes
    nodes = [Node(i) for i in range(n)]

    # Attach children to parents in id order (ensures children lists are sorted by id)
    for rec in ordered:
        if rec.record_id == 0:
            continue
        nodes[rec.parent_id].children.append(nodes[rec.record_id])

    return nodes[0]
