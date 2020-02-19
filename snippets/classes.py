class Car:
    '''
    Docstring describing the class Car
    With tires and enginer
    '''

    def __init__(self, engine, tires):
        '''
        Docstring describing method
        '''
        self.engine = engine
        self.tires = tires
        print('Object of class Car instantiated with {} HP engine  and {} tires'.format(self.engine, self.tires))


