class CyclicList:
    """
    A class used to represent a Cyclic List.

    ...

    Attributes
    ----------
    collection : list
        a list of elements in the cyclic list
    index : int
        the current index in the cyclic list

    Methods
    -------
    current():
        Returns the current element in the cyclic list.
    next():
        Moves to the next element in the cyclic list and returns it.
    reset():
        Resets the index to the start of the cyclic list.
    __len__():
        Returns the length of the cyclic list.
    """

    def __init__(self, collection):
        """
        Constructs all the necessary attributes for the cyclic list object.

        Parameters
        ----------
            collection : list
                a list of elements in the cyclic list
        """
        self.collection = collection
        self.index = 0

    def current(self):
        """
        Returns the current element in the cyclic list.

        Returns
        -------
        element
            the current element in the cyclic list
        """
        return self.collection[self.index]

    def next(self):
        """
        Moves to the next element in the cyclic list and returns it.

        Returns
        -------
        element
            the next element in the cyclic list
        """
        self.index = (self.index + 1) % len(self.collection)
        return self.current()

    def reset(self):
        """
        Resets the index to the start of the cyclic list.
        """
        self.index = 0

    def __len__(self):
        """
        Returns the length of the cyclic list.

        Returns
        -------
        int
            the length of the cyclic list
        """
        return len(self.collection)



