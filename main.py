from Node import Node
from Tree import Tree

n1 = Node(5)
n2 = Node(3)
n3 = Node(2)
n4 = Node(6)
n5 = Node(7)
n6 = Node(1)


my_tree = Tree(n1)
my_tree.insert(n2)
my_tree.insert(n3)
my_tree.insert(n4)
my_tree.insert(n5)
my_tree.insert(n6)

print(n1.left)
print(n1.left.right)

my_tree.pre_order_traversal(my_tree.root)