class DoctorNode:

class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side):
        # Only left and right are valid sides.
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        # An empty tree has no parent to search for.
        if self.root is None:
            return False

        # Search for the parent using preorder traversal.
        stack = [self.root]

        while stack:
            current = stack.pop()

            if current.name == parent_name:
                if getattr(current, side) is not None:
                    raise ValueError(
                        f"The {side} child of {parent_name} is occupied."
                    )

                setattr(current, side, DoctorNode(doctor_name))
                return True

            # Push right first so left is searched first.
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

        # Parent was not found.
        return False

    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    # Edge-case tests
    print("Missing parent:", tree.insert(
        "Dr. Unknown", "Dr. New", "left"
    ))

    try:
        tree.insert("Dr. Croft", "Dr. New", "middle")
    except ValueError as error:
        print("Invalid side:", error)
