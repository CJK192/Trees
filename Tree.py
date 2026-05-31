class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def __str__(self) -> str:
        pass

    def insert(self, node) -> None:
        pass



    def pre_order_traversal(self, node):
        if node is None:
            return
        print(node)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

    def in_order_traversal(self):
        pass

    def post_order_traversal(self):
        pass