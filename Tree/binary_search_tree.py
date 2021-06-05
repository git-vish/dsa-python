from typing import List


class Node(object):
    """
    Tree Node.

    Parameters:
    ----------
        data -> int : data to be stored
    """

    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'<Node>[{self.data}]'


class BST(object):
    """ Binary Search Tree. """
    __ERROR_ORDER = 'ERROR: Invalid Order:'
    __ERROR_EMPTY = 'ERROR: Tree Empty'

    def __init__(self):
        self.__root = None

    def __height(self, root: Node) -> int:
        if not root:
            return 0
        return 1 + max(self.__height(root.left), self.__height(root.right))

    def __size(self, root: Node) -> int:
        if not root:
            return 0
        return 1 + self.__size(root.left) + self.__size(root.right)

    @property
    def height(self) -> int:
        """
        Return height of tree.

        Parameters:
        ----------
            None

        Returns:
        ---------
            int : height
        """
        return self.__height(self.__root)

    @property
    def size(self) -> int:
        """
        Return size of tree.

        Parameters:
        ----------
            None

        Returns:
        ---------
            int : size
        """
        return self.__size(self.__root)

    def insert(self, data: int) -> None:
        """
        Insert a node in BST.

        Parameters:
        ----------
            data -> int : data to be inserted

        Returns:
        ---------
             None
        """
        '''
        RECURSIVE: Space Complexity = O(h)
            def insert(root, data):
                if not root:
                    return Node(data)
                elif root.data > data:
                    root.left = insert(root.left, data)
                elif root.data < data:
                    root.right = insert(root.right, data)
                return root
        -----------------------------------------
        ITERATIVE: Space Complexity = O(1)
        '''
        new_node = Node(data)
        if not self.__root:
            self.__root = new_node
        else:
            current = self.__root
            parent = None

            while current:
                parent = current
                if current.data > data:
                    current = current.left
                elif current.data < data:
                    current = current.right
                else:
                    return

            if parent.data > data:
                parent.left = new_node
            else:
                parent.right = new_node

    def __in_order(self, node: Node, lst: List[int]) -> None:
        if node:
            self.__in_order(node.left, lst)
            lst.append(node.data)
            self.__in_order(node.right, lst)

    def __pre_order(self, node: Node, lst: List[int]) -> None:
        if node:
            lst.append(node.data)
            self.__pre_order(node.left, lst)
            self.__pre_order(node.right, lst)

    def __post_order(self, node: Node, lst: List[int]) -> None:
        if node:
            self.__post_order(node.left, lst)
            self.__post_order(node.right, lst)
            lst.append(node.data)

    def __level_order(self, lst: List[int]) -> None:
        queue = [self.__root]
        while queue:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            lst.append(current.data)

    def traverse(self, order: int) -> List[int]:
        """
        Traverse the tree in specified order,
        Return traversal list.

        Parameters:
        ----------
            order -> int : order of traversal
                    1 : In-order
                    2 : Pre-order
                    3 : Post-order
                    4 : Level-order
        Returns:
            List[int] : traversal list.
        """
        if not self.__root:
            print('<Empty BST>')
            return []

        lst = []
        if order == 1:
            self.__in_order(self.__root, lst)
        elif order == 2:
            self.__pre_order(self.__root, lst)
        elif order == 3:
            self.__post_order(self.__root, lst)
        elif order == 4:
            self.__level_order(lst)
        else:
            print(self.__ERROR_ORDER, order)
            return []

        return lst

    def find(self, data: int) -> bool:
        """
        Checks if the data is present in the BST.

        Parameters:
        ----------
            data -> int : data to be searched

        Returns:
        ---------
            bool : data present or not
        """
        if not self.__root:
            print(self.__ERROR_EMPTY)
            return False
        current = self.__root
        while current:
            if current.data == data:
                return True
            elif current.data > data:
                current = current.left
            else:
                current = current.right
        return False

    @staticmethod
    def __get_successor(node: Node) -> Node:
        """
        Get In-order successor of given Node.

        Parameters:
        ----------
            node -> Node

        Returns:
        ----------
            Node : in-order successor
        """
        node = node.right
        while node and node.left:
            node = node.left
        return node

    def __delete(self, root: Node, data: int) -> Node:
        if not root:
            return root
        elif root.data > data:
            root.left = self.__delete(root.left, data)
        elif root.data < data:
            root.right = self.__delete(root.right, data)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self.__get_successor(root)
                root.data = successor.data
                root.right = self.__delete(root.right, successor.data)
        return root

    def delete(self, data: int) -> None:
        """
        Delete data from BST if present.

        Parameters:
        ----------
            data -> int : data to be deleted.

        Returns:
        ----------
             None
        """
        if not self.__root:
            print(self.__ERROR_EMPTY)
            return
        self.__root = self.__delete(self.__root, data)
