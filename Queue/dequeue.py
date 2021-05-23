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


class Dequeue(object):
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__len = 0

    def __len__(self) -> int:
        return self.__len

    def __repr__(self) -> str:
        if len(self) == 0:
            return '<Empty Queue>'

        string = 'FRONT-->|'

        current = self.__front

        while current.next:
            string += f' {current.data} |'
            current = current.next

        string += f' {current.data} |<--REAR'

        return string

    @property
    def front(self) -> int:
        """Get FRONT of Queue."""
        if len(self) == 0:
            return -1

        return self.__front.data

    @property
    def rear(self) -> int:
        """Get REAR of Queue."""
        if len(self) == 0:
            return -1

        return self.__rear.data

    def insert_front(self, data: int) -> None:
        """
        Add data to FRONT.

        Parameters:
        ----------
            data -> int : data to be stored

        Returns:
        ----------
            None
        """
        new_node = Node(data)
        if len(self) == 0:
            self.__front = new_node
            self.__rear = self.__front
        else:
            new_node.next = self.__front
            self.__front.prev = new_node
            self.__front = new_node

        self.__len += 1

    def remove_front(self) -> int:
        """
        Remove data from FRONT.

        Parameters:
        ----------
            None

        Returns:
        ----------
            int : data
        """
        if len(self) == 0:
            return -1

        data = self.__front.data
        self.__front = self.__front.next
        self.__len -= 1

        return data

    def insert_rear(self, data: int) -> None:
        """
        Add data to REAR.

        Parameters:
        ----------
            data -> int : data to be stored

        Returns:
        ----------
            None
        """
        new_node = Node(data)
        if len(self) == 0:
            self.__front = new_node
            self.__rear = self.__front
        else:
            self.__rear.next = new_node
            new_node.prev = self.__rear
            self.__rear = new_node

        self.__len += 1

    def remove_rear(self) -> int:
        """
        Remove data from REAR.

        Parameters:
        ----------
            None

        Returns:
        ----------
            int : data
        """
        if len(self) == 0:
            return -1

        data = self.__rear.data
        self.__rear = self.__rear.prev
        self.__rear.next = None
        self.__len -= 1

        return data
