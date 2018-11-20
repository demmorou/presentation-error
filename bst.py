import random
import sys
sys.setrecursionlimit(12000)

cont = 0


def create_vector_to_insertion(case, nodes):
    """
    :param case: number of test cases
    :param nodes: number of insertion nodes
    :return: list with all numbers drawn for insertion
    """

    insertion = []

    if case == 0:
        for _ in range(nodes):
            insertion.append(_)
    elif case == 1:
        while len(insertion) < nodes:
            n = random.randint(0, 11000)
            if n not in insertion:
                insertion.append(n)

    return insertion


def generate_numbers_to_search():
    """
    this function was used to generate numbers for searches
    :return: list with all index to search
    """

    index = []

    while len(index) < 100:
        n = random.randint(0, 9999)
        if n not in index:
            index.append(n)

    return index


class Node:
    """
    this class implement the Node for the trees avl and bst.
    """

    def __init__(self, key):
        """
        :param key: key to insert
        """
        self.key = key
        self.left = None
        self.right = None


class bst:
    """
    this class implement the methods of the bst tree
    """

    def __init__(self):

        self.root = None  # root node
        self.cont = 0

    def insert(self, key):
        """
        this function implement the insertion
        :param key: key to insert
        :return: does not exist
        """

        if self.root is None:
            self.root = Node(key)  # insert element in root node
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(key)
                        break

                elif key > current_node.key:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(key)
                        break

                else:
                    break

    def view_in_order(self, node):
        """
        this function implement the method of view in order
        :param node: initially, with root node
        :return: does not exist
        """

        if node is not None:
            self.view_in_order(node.left)
            print(node.key, end=' ')
            self.view_in_order(node.right)

    def search(self, node, key_search):
        """
        this function was used to search in the tree bst
        :param node: current node
        :param key_search: key to search
        :return: does not exist
        """
        if node is not None:
            if key_search < node.key:
                self.cont += 1
                self.search(node.left, key_search)

            elif key_search > node.key:
                self.cont += 1
                self.search(node.right, key_search)


class avl:

    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

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

        self.balance_tree()

    def balance_tree(self):

        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:  # while the balance factor > 1, apply the rotations
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_heights()
                    self.update_balances()
                self.right_rotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.left_rotate()
                self.update_heights()
                self.update_balances()

    def right_rotate(self):
        a = self.node
        b = self.node.left.node
        t = b.right.node

        self.node = b
        b.right.node = a
        a.left.node = t

    def left_rotate(self):
        a = self.node
        b = self.node.right.node
        t = b.left.node

        self.node = b
        b.left.node = a
        a.right.node = t

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

        tree = self.node

        if tree is not None:
            self.node.left.view_in_order()
            print(tree.key, end=' ')
            self.node.right.view_in_order()

    def search(self, key_search):
        global cont
        tree = self.node

        if tree is not None:
            if key_search < tree.key:
                cont += 1
                self.node.left.search(key_search)
            elif key_search > tree.key:
                cont += 1
                self.node.right.search(key_search)


class Node_rbt:
    RED = True
    BLACK = False

    def __init__(self, key, color=RED):
        if not type(color) == bool:
            raise TypeError("Bad value for color parameter, expected True/False but given %s" % color)
        self.color = color
        self.key = key
        self.left = self.right = self.parent = NilNode_rbt.instance()

    def __str__(self, level=0, indent="   "):
        s = level * indent + str(self.key)
        if self.left:
            s = s + "\n" + self.left.__str__(level + 1, indent)
        if self.right:
            s = s + "\n" + self.right.__str__(level + 1, indent)
        return s

    def __nonzero__(self):
        return True

    def __bool__(self):
        return True


class NilNode_rbt(Node_rbt):
    __instance__ = None

    @classmethod
    def instance(self):
        if self.__instance__ is None:
            self.__instance__ = NilNode_rbt()
        return self.__instance__

    def __init__(self):
        self.color = Node_rbt.BLACK
        self.key = None
        self.left = self.right = self.parent = None

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False


class rbt:
    def __init__(self):
        self.cont = 0
        self.root = NilNode_rbt.instance()
        self.size = 0

    def __str__(self):
        return ("(root.size = %d)\n" % self.size) + str(self.root)

    def add(self, key):
        self.insert(Node_rbt(key))

    def insert(self, x):
        self.insert_helper(x)

        x.color = Node_rbt.RED
        while x != self.root and x.parent.color == Node_rbt.RED:
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y and y.color == Node_rbt.RED:
                    x.parent.color = Node_rbt.BLACK
                    y.color = Node_rbt.BLACK
                    x.parent.parent.color = Node_rbt.RED
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.left_rotate(x)
                    x.parent.color = Node_rbt.BLACK
                    x.parent.parent.color = Node_rbt.RED
                    self.right_rotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y and y.color == Node_rbt.RED:
                    x.parent.color = Node_rbt.BLACK
                    y.color = Node_rbt.BLACK
                    x.parent.parent.color = Node_rbt.RED
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.right_rotate(x)
                    x.parent.color = Node_rbt.BLACK
                    x.parent.parent.color = Node_rbt.RED
                    self.left_rotate(x.parent.parent)
        self.root.color = Node_rbt.BLACK

    def minimum(self, x=None):
        if x is None: x = self.root
        while x.left:
            x = x.left
        return x

    def maximum(self, x=None):
        if x is None: x = self.root
        while x.right:
            x = x.right
        return x

    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def view_in_order(self, x=None):
        if x is None: x = self.root
        x = self.minimum()
        while x:
            yield x.key
            x = self.successor(x)

    def search(self, key, x=None):
        if x is None: x = self.root
        while x and x.key != key:
            if key < x.key:
                self.cont += 1
                x = x.left
            else:
                self.cont += 1
                x = x.right
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right: y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.right = x
        x.parent = y

    def insert_helper(self, z):
        y = NilNode_rbt.instance()
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if not y:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

        self.size += 1


if __name__ == "__main__":

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
                tree_bst = bst()
                print('bst')

                for _ in range(number_nodes):
                    tree_bst.insert(elements[_])
                    print(elements[_], end=' ')  # view insertion sequence

                print()
                tree_bst.view_in_order(tree_bst.root)
                '''
                index_search = generate_numbers_to_search()
                print('searching for {}'.format(len(index_search)), 'numbers')
                for _ in range(len(index_search)):
                     tree_bst.search(tree_bst.root, elements[index_search[_]])

                print('media = {}'.format(tree_bst.cont / 100))
                '''

            elif type_tree == 1:
                print('tree avl')
                tree_avl = avl()
                for _ in range(number_nodes):
                    tree_avl.insert(elements[_])
                    print(elements[_], end=' ')  # view insertion sequence

                print()
                tree_avl.view_in_order()
                '''
                index_search = generate_numbers_to_search()
                print('searching for {}'.format(len(index_search)), 'numbers')
                for _ in range(len(index_search)):
                    tree_avl.search(elements[index_search[_]])

                print('media = {}'.format(cont / 100))
                '''

            elif type_tree == 2:
                print('tree rbt')
                tree_rbt = rbt()
                for _ in range(number_nodes):
                    tree_rbt.add(elements[_])
                    print(elements[_], end=' ')
                print()

                # for _ in tree_rbt.view_in_order():
                #    print(_, end=' ')
                index_search = generate_numbers_to_search()
                print('searching for {}'.format(len(index_search)), 'numbers')
                for _ in range(len(index_search)):
                    tree_rbt.search(elements[index_search[_]])

                print('media = {}'.format(tree_rbt.cont / 100))

            else:
                break

        except EOFError:
            break
