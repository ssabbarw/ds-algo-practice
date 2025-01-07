from sorts.bucket_sort import ListNode


class MyQueue:
    def __init__(self):
        """Initialize an empty queue."""
        self.__first_element = None
        self.__last_element = None
        self.__size = 0

    def dequeue(self):
        """Remove and return the front element of the queue.

        Returns:
             The data of the front element if the queue is not empty, otherwise None.
        """
        first_element = None

        if self.__first_element:
            first_element = self.__first_element
            self.__first_element = self.__first_element.next

            if self.__first_element is None:
                self.__last_element = None

        self.__size -= 1
        return first_element.data

    def enqueue(self, data):
        """Add an element to the end of the queue.

        Args:
            data: The data to be added to the queue.
        """
        new_node = ListNode(data=data, next=None)
        if self.__last_element:
            self.__last_element.next = new_node
        else:
            self.__first_element = new_node

        self.__last_element = new_node
        self.__size += 1


    def is_empty(self):
        """Check if the queue is empty."""
        return self.__first_element is None

    def size(self):
        """Get the number of elements in the queue.

        Returns:
            The size of the queue as an integer.
        """
        return self.__size

queue = MyQueue()
queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(13)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())