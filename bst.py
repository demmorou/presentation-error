import random
import matplotlib.pyplot as plt


def create_vector_to_insertion(case, nodes):
    insertion = []

    if case == 0:
        for _ in range(nodes):
            insertion.append(_)
    elif case == 1:
        while len(insertion) < nodes:
            n = random.randint(0, 100000)
            if n not in insertion:
                insertion.append(n)

    return insertion


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class bst:

    def __init__(self):

        self.root = None  # root node
        self.cont = 0

    def insert(self, key):

        if self.root is None:
            self.root = Node(key)  # insert element in root node
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        self.cont += 1
                        current_node.left = Node(key)
                        break

                elif key > current_node.key:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        self.cont += 1
                        current_node.right = Node(key)
                        break

                else:
                    break

    def view_in_order(self, node):

        if node is not None:
            self.view_in_order(node.left)
            print(node.key, end=' ')
            self.view_in_order(node.right)


class avl:

    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def height(self):
        if self.root:
            return self.root.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, key):
        node = self.root

        current_node = Node(key)

        if node is None:
            self.root = current_node
            self.root.left = avl()
            self.root.right = avl()

        elif key < node.key:
            self.root.left.insert(key)

        elif key > node.key:
            self.root.right.insert(key)

        self.rebalance()

    def rebalance(self):

        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        A = self.root
        B = self.root.left.node
        T = B.right.node

        self.root = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        A = self.root
        B = self.root.right.node
        T = B.left.node

        self.root = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.root == None:
            if recurse:
                if self.root.left != None:
                    self.root.left.update_heights()
                if self.root.right != None:
                    self.root.right.update_heights()

            self.height = max(self.root.left.height,
                              self.root.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.root is None:
            if recurse:
                if self.root.left is not None:
                    self.root.left.update_balances()
                if self.root.right is not None:
                    self.root.right.update_balances()

            self.balance = self.root.left.height - self.root.right.height
        else:
            self.balance = 0

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.root is not None:
            if self.root.key == key:
                if self.root.left.node is None and self.root.right.node is None:
                    self.root = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.root.left.node is None:
                    self.root = self.root.right.node
                elif self.root.right.node is None:
                    self.root = self.root.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.root)
                    if replacement is not None:  # sanity check
                        self.root.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.root.right.delete(replacement.key)

                self.rebalance()
                return
            elif key < self.root.key:
                self.root.left.delete(key)
            elif key > self.root.key:
                self.root.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):

        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):

        node = node.right.node
        if node is not None:  # just a sanity check

            while node.left is not None:
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self is None or self.root is None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.root.left.check_balanced() and self.root.right.check_balanced()

    def inorder_traverse(self):
        if self.root is None:
            return []

        inlist = []
        l = self.root.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.root.key)

        l = self.root.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist


if __name__ == "__main__":

    cost = []
    cost2 = []
    p = 0
    while True:
        try:

            number_nodes = int(input())

            if number_nodes == 3:
                break

            input_reader = input()
            slots = input_reader.split()

            test_case = int(slots[0])
            type_tree = int(slots[1])

            elements = create_vector_to_insertion(test_case, number_nodes)

            if type_tree == 0:

                print('bst')
                tree_bst = bst()

                for _ in range(number_nodes):
                    tree_bst.insert(elements[_])
                    print(elements[_], end=' ')
                    if _ % 1000 == 0:
                        cost.append(tree_bst.cont)
                        cost2.append(p)
                    p += 1

                print()
                # tree_bst.view_in_order(tree_bst.root)

                plt.plot(cost, cost2, color='red')
                plt.title('complexity')
                plt.xlabel('elements')
                plt.ylabel('search')
                plt.show()

            elif type_tree == 1:
                print('tree avl')
            elif type_tree == 2:
                print('tree rbt')
            else:
                break

        except EOFError:
            break
