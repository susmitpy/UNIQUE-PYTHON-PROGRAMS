class MaxHeap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        
    def HeapifyUp(self):
        for i in reversed(range(1, self.size+1)):
            self.SiftUp(i)

    def HeapifyDown(self):
        for i in range(1, self.size + 1):
            self.SiftDown(i)

    def GetParent(self, i):
        return i//2

    def GetLeftChild(self, i):
        return 2*i

    def GetRightChild(self, i):
        return (2*i) + 1

    def HasLeftChild(self, i):
        return (2*i) <= self.size

    def HasRightChild(self, i):
        return ((2*i) + 1) <= self.size

    def HasParent(self, i):
        return ((i//2) > 0 and (i//2) <= self.size)

    def Swap(self, a, b):
        self.arr[a-1], self.arr[b-1] = self.arr[b-1], self.arr[a-1]

    def GetValue(self, i):
        return self.arr[i-1]

    def SiftUp(self, i):
        if self.HasParent(i) and (self.GetValue(self.GetParent(i)) < self.GetValue(i)):
            self.Swap(self.GetParent(i), i)
            
    def SiftDown(self, i):
        if self.HasLeftChild(i) and ((self.GetValue(i) < self.GetValue(self.GetLeftChild(i)))):
            if self.HasRightChild(i) and ((self.GetValue(i) < self.GetValue(self.GetRightChild(i)))):   
                if self.GetValue(self.GetLeftChild(i)) < self.GetValue(self.GetRightChild(i)):
                    self.Swap(i, self.GetRightChild(i))
                else:
                    self.Swap(i, self.GetLeftChild(i))
            else:
                self.Swap(i, self.GetLeftChild(i))

    def InsertLastLeaf(self, value):
        self.arr.insert(self.size, value)
        self.size += 1
        self.HeapifyUp()

    def ExtractMax(self):
        maximum = self.arr[0]
        self.arr[0] = self.arr.pop(self.size - 1)
        self.size -= 1
        self.HeapifyDown()
        return maximum
        
    def Get(self):
        return self.arr

    

