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


class Stack(object):
    """
    Stack using Singly Linked List.
    """
    def __init__(self):
        self.__top = None
        self.__len = 0

    def __len__(self) -> int:
        return self.__len

    def __repr__(self) -> str:
        if not self.__len:
            return '<Empty Stack>'

        string = 'TOP-->|'

        current = self.__top

        while current.next:
            string += f' {current.data} |'
            current = current.next

        string += f' {current.data} |'

        return string

    @property
    def top(self) -> int:
        """Get data at TOP of the Stack"""
        if not self.__len:
            return -1

        return self.__top.data

    def push(self, data: int) -> None:
        """
        Push data.

        Parameters:
        ----------
            data -> int : data to be stored

        Returns:
        ----------
            None
        """
        new_node = Node(data)

        if not self.__len:
            self.__top = new_node
        else:
            new_node.next = self.__top
            self.__top = new_node

        self.__len += 1

    def pop(self) -> int:
        """
        Remove node from TOP of the stack,
        return removed data.

        Parameter:
        ---------
            None

        Returns:
        ---------
            int : data
        """
        if not self.__len:
            return -1

        data = self.__top.data
        self.__top = self.__top.next
        self.__len -= 1

        return data
