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
        self.node = None
        self.height = -1
        self.balance = 0
        self.cont = 0

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, key):
        tree = self.node

        new_node = Node(key)

        if tree is None:
            self.node = new_node
            self.node.left = avl()
            self.node.right = avl()

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        self.rebalance()

    def rebalance(self):

        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        a = self.node
        b = self.node.left.node
        t = b.right.node

        self.node = b
        b.right.node = a
        a.left.node = t

    def lrotate(self):
        # Rotate left pivoting on self
        A = self.node
        b = self.node.right.node
        t = b.left.node

        self.node = b
        b.left.node = A
        A.right.node = t

    def update_heights(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def view_in_order(self):
        if self.node is None:
            return []

        inlist = []
        l = self.node.left.view_in_order()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.view_in_order()
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
                        cost.append(p)
                        cost2.append(tree_bst.cont)
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
                tree_avl = avl()
                for _ in range(number_nodes):
                    tree_avl.insert(elements[_])
                    print(elements[_], end=' ')
                    if _ % 1000 == 0:
                        cost.append(tree_avl.cont)
                        cost2.append(p)
                    p += 1
                print()
                for _ in tree_avl.view_in_order():
                    print(_, end=' ')
            elif type_tree == 2:
                print('tree rbt')
            else:
                break

        except EOFError:
            break
