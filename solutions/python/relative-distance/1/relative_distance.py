from collections import defaultdict, deque


class RelativeDistance:
    def __init__(self, family_tree):
        self.graph = defaultdict(set)
        self.people = set(family_tree)

        # Include people who appear only as children
        for children in family_tree.values():
            self.people.update(children)

        # Build bidirectional parent-child relationships
        for parent, children in family_tree.items():
            for child in children:
                self.graph[parent].add(child)
                self.graph[child].add(parent)

        # Add direct sibling relationships
        for parent, children in family_tree.items():
            for i in range(len(children)):
                for j in range(i + 1, len(children)):
                    sibling_a = children[i]
                    sibling_b = children[j]

                    self.graph[sibling_a].add(sibling_b)
                    self.graph[sibling_b].add(sibling_a)

    def degree_of_separation(self, person_a, person_b):
        # Validate both individuals
        if person_a not in self.people:
            raise ValueError("Person A not in family tree.")

        if person_b not in self.people:
            raise ValueError("Person B not in family tree.")

        # Same person has zero degrees of separation
        if person_a == person_b:
            return 0

        # Breadth-first search
        queue = deque([(person_a, 0)])
        visited = {person_a}

        while queue:
            current_person, distance = queue.popleft()

            for relative in self.graph[current_person]:
                if relative == person_b:
                    return distance + 1

                if relative not in visited:
                    visited.add(relative)
                    queue.append((relative, distance + 1))

        # Both people exist, but there is no relationship
        raise ValueError(
            "No connection between person A and person B."
        )