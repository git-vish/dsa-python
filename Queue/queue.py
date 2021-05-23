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


class Queue(object):
    """
    Queue using Singly Linked List.
    """
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

    def enqueue(self, data: int) -> None:
        """
        Enqueue data,
        Add data to REAR of Queue.

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
            self.__rear = new_node

        self.__len += 1

    def dequeue(self) -> int:
        """
        Dequeue data,
        Remove data from FRONT of Queue.

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
