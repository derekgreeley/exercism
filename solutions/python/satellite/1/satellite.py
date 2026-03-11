# satellite.py

def tree_from_traversals(preorder, inorder):
    # Validate lengths
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    # Validate uniqueness
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    # Validate same elements
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    def build(pre, ino):
        if not pre:
            return {}

        root = pre[0]
        root_index = ino.index(root)

        left_in = ino[:root_index]
        right_in = ino[root_index + 1 :]

        left_size = len(left_in)
        left_pre = pre[1 : 1 + left_size]
        right_pre = pre[1 + left_size :]

        return {
            "v": root,
            "l": build(left_pre, left_in),
            "r": build(right_pre, right_in),
        }

    return build(preorder, inorder)