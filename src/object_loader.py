class ObjectLoader():

    """
    As the name suggests, this class drives the game. It is 
    responsible for asynchronously generating new fruit/bomb,
    randomly, from one of the 8 locations.
    """

    def __init__(self):
        pass
    
    def load_object(self):
        
        """
        This function should randomly load a fruit/bomb, and
        then put then keep them moving.

        Should also take of the fruits/bomb when they reach the boundaries
        or is touched by mouse pointer.
        """