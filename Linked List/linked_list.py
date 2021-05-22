class Node(object):
    """
    Linked List Node.

    Parameters:
    ----------
        data -> int : data to be stored
    """

    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'<Node>[{self.data}]'


class LinkedList(object):
    """
    Singly Linked List.
    """
    __ERROR_INDEX = 'ERROR: Invalid Index:'
    __ERROR_EMPTY = 'ERROR: List Empty'

    def __init__(self):
        self.__head = None
        self.__len = 0

    @property
    def head(self) -> Node:
        """Get head of Linked List."""
        return self.__head

    def __len__(self) -> int:
        return self.__len

    def __repr__(self) -> str:
        if not self.__len:
            return '<Empty Linked List>'

        string = ''
        current = self.__head

        while current.next:
            string += f'{current.data}-->'
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

        if not self.__head:
            self.__head = new_node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node

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
        if index <= 0:
            print(self.__ERROR_INDEX, index)
            return

        new_node = Node(data)

        if index == 1:
            if not self.__len:
                self.append(data)
            else:
                new_node.next = self.__head
                self.__head = new_node
        else:
            current = self.__head
            c_position = 1

            while current.next and c_position < index - 1:
                current = current.next
                c_position += 1

            if c_position < index - 1:
                print(self.__ERROR_INDEX, index)
                return

            new_node.next = current.next
            current.next = new_node

            self.__len += 1

    def get(self, index: int) -> int or None:
        """
        Get data at specified index,
        if index is not present returns None.

        Parameters:
        ----------
            index -> int : index to look for

        Returns:
        ----------
            int: data at specified index
        """
        if not self.__len:
            print(self.__ERROR_EMPTY)
            return

        if index > self.__len or index <= 0:
            print(self.__ERROR_INDEX)
            return

        c_position = 1
        current = self.__head

        while c_position < index:
            current = current.next
            c_position += 1

        return current.data

    def pop(self, index: int = None) -> int or None:
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

        if index > self.__len or index <= 0:
            print(self.__ERROR_INDEX)
            return

        if index == 1:
            data = self.__head.data
            if self.__head.next:
                self.__head = self.__head.next
            else:
                self.__head = None
        else:
            c_position = 1
            current = self.__head

            while c_position < index - 1:
                current = current.next
                c_position += 1

            data = current.next.data

            if current.next.next:
                current.next = current.next.next
            else:
                current.next = None

        self.__len -= 1

        return data

    def find(self, data: int) -> int or None:
        """
        Search data in Linked List,
        if found return index of first occurrence else,return None.

        Parameters:
        ----------
             data -> int : data to search for

        Return:
        ----------
            int: index
        """
        if not self.__len:
            print(self.__ERROR_EMPTY)
            return

        current = self.__head
        c_position = 1

        while current:
            if current.data == data:
                return c_position

            current = current.next
            c_position += 1

    def get_middle(self) -> int or None:
        """Get data at middle node."""
        if not self.__len:
            print(self.__ERROR_EMPTY)
            return

        slow = self.__head
        fast = self.__head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow.data

    def reverse(self) -> None:
        """Reverse Linked List."""
        if not self.__len:
            print(self.__ERROR_EMPTY)
            return

        if self.__len == 1:
            return

        current = self.__head
        previous = None

        while current:
            next_ = current.next
            current.next = previous

            previous = current
            current = next_

        self.__head = previous

    def join(self, other) -> None:
        """
        Attach other Linked List to end of Linked List.

        Parameters:
        -----------
             other -> LikedList : Liked List to be attached
        """
        if not self.__len:
            self.__head = other.head
            self.__len = len(other)
        else:
            current = self.__head

            while current.next:
                current = current.next

            current.next = other.head
            self.__len += len(other)

    def remove_duplicates(self) -> None:
        """Remove nodes with duplicate data."""
        if not self.__len:
            print(self.__ERROR_EMPTY)
            return

        if self.__len == 1:
            return

        data = {self.__head.data}

        current = self.__head.next

        while current.next:
            if current.next.data in data:
                current.next = current.next.next
            else:
                data.add(current.next.data)
                current = current.next

