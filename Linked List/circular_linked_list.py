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


class CircularLinkedList(object):
    """
    Circular  Linked List.
    """
    __ERROR_INDEX = 'ERROR: Invalid Index:'
    __ERROR_EMPTY = 'ERROR: List Empty'

    def __init__(self):
        self.__head = None
        self.__len = 0

    def __repr__(self) -> str:
        if not self.__len:
            return '<Empty Circular Linked List>'

        string = ''

        if self.__len == 1:
            string += f'{self.__head.data}-->\n<---'
        else:
            current = self.__head

            while current.next != self.__head:
                string += f'{current.data}-->'
                current = current.next

            string += f'{current.data}\n'
            string += '<' + '-' * (len(string) - 2)

        return string

    def __len__(self) -> int:
        return self.__len

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
            self.__head.next = self.__head
        else:
            new_node.next = self.__head.next
            self.__head.next = new_node
            self.__head.data, new_node.data = new_node.data, self.__head.data
            self.__head = new_node

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
        if index > self.__len + 1 or index <= 0:
            print(self.__ERROR_INDEX, index)
            return

        if index == self.__len:
            self.append(data)
            return

        new_node = Node(data)

        if index == 1:
            new_node.next = self.__head.next
            self.__head.next = new_node
            self.__head.data, new_node.data = new_node.data, self.__head.data
        else:
            current = self.__head
            c_pos = 1

            while c_pos < index - 1:
                current = current.next
                c_pos += 1

            new_node.next = current.next
            current.next = new_node

        self.__len += 1

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

        if index > self.__len:
            print(self.__ERROR_INDEX, index)
            return

        if index == 1:
            data = self.__head.data
            self.__head.data = self.__head.next.data
            self.__head.next = self.__head.next.next
        else:
            current = self.__head
            c_pos = 1

            while c_pos < index - 1:
                current = current.next
                c_pos += 1

            data = current.next.data
            current.next = current.next.next

        self.__len -= 1
        return data
