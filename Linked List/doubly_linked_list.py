class Node(object):
    """
    Doubly Linked List Node.

    Parameters:
    ----------
        data -> int : data to be stored
    """

    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f'<Node>[{self.data}]'


class DoublyLinkedList(object):
    """
    Doubly Linked List.
    """
    __ERROR_INDEX = 'ERROR: Invalid Index:'
    __ERROR_EMPTY = 'ERROR: List Empty'

    def __init__(self):
        self.__head = None
        self.__len = 0

    def __len__(self) -> int:
        return self.__len

    def __repr__(self) -> str:
        if not self.__len:
            return '<Empty Doubly Linked List>'

        string = ''
        current = self.__head

        while current.next:
            string += f'{current.data}<-->'
            current = current.next

        string += f'{current.data}'

        return string

    def append(self, data: int) -> None:
        """
        Add node to end.

        Parameters:
        ----------
            data -> int : data to be stored

        Returns:
        ----------
            None
        """
        new_node = Node(data)

        if not self.__len:
            self.__head = new_node
        else:
            current = self.__head

            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current

        self.__len += 1

    def insert(self, data: int, index: int) -> None:
        """
        Insert node at specified index.

        Parameters:
        ----------
            data -> int : data to be stored
            index -> int : index to insert at

        Returns:
        ----------
            None
        """
        if index <= 0 or index > self.__len + 1:
            print(self.__ERROR_INDEX, index)
            return

        new_node = Node(data)

        if index == 1:
            new_node.next = self.__head

            if self.__head:
                self.__head.prev = new_node

            self.__head = new_node
        else:
            current = self.__head
            c_pos = 1

            while c_pos < index - 1:
                current = current.next
                c_pos += 1

            new_node.next = current.next
            new_node.prev = current

            current.next = new_node

            if new_node.next:
                new_node.next.prev = new_node

        self.__len += 1

    def remove(self, index=None) -> int or None:
        """
        Remove node at specified index and return data,
        if index not specified remove last node.

        Parameter:
        ---------
            index -> int : index to look for

        Returns:
        ---------
            int : data
        """
        if not self.__len:
            print(self.__ERROR_EMPTY)
            return

        if not index:
            index = self.__len

        if index <= 0 or index > self.__len:
            print(self.__ERROR_INDEX)
            return

        if index == 1:
            data = self.__head.data

            self.__head = self.__head.next
            self.__head.prev = None
        else:
            current = self.__head
            c_pos = 1

            while c_pos < index:
                c_pos += 1
                current = current.next

            data = current.data

            current.prev.next = current.next

            if current.next:
                current.next.prev = current.prev

        self.__len -= 1
        return data

    def reverse(self) -> None:
        """Reverse Doubly Linked List."""
        if self.__len in (0, 1):
            return

        current = self.__head
        previous = None

        while current:
            next_ = current.next
            current.next = previous
            current.prev = next_

            previous = current
            current = next_

        self.__head = previous
