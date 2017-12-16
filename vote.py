class option():
    def __init__(self, name, count):
        self.count = int(count)
        self.name = name
        
    def upvote(self):
        self.count += 1

    def display(self):
        print("{} : {}".format(self.name, self.count))



