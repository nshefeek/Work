class Sentence:

    def __init__(self, line):
        self.line = line
        self.pos = 0
        self.words = self.line.split()


    def __iter__(self):
        return self
    
    
    def __next__(self):
        
        if self.pos >= len(self.words):
            raise StopIteration
        
        index = self.pos
        self.pos += 1
        return self.words[index]



mysentence = Sentence('This is my sentence to test')

#for word in mysentence:
#    print(word)


print(next(mysentence))
print(next(mysentence))
print(next(mysentence))
print(next(mysentence))
print(next(mysentence))
print(next(mysentence))
print(next(mysentence))
print(next(mysentence))

