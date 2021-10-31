class Node:
    def __init__(self, value, id):
      self.left = None
      self.right = None
      self.value = value
      self.ids = [id]

    def insert(self, value, id):
        if self.value != None:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, id)
                else:
                    self.left.insert(value, id)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value, id)
                else:
                    self.right.insert(value, id)
            else: 
                self.ids.append(id)
        else:
            self.value = value
            self.ids = [id]

    def find(self, value):
        current = self
        while current != None:
            if value < current.value:
                current = current.left 
            elif value > current.value:
                current = current.right
            else: return current.ids
        return []

    
    def getAllIDsMore( self, value, equal):
        allIDs = []
        current = self
        while current != None:
            if current.value > value:
                allIDs += current.ids
                if current.right:
                    current.right.getAllIDs(allIDs)
                if current.left:
                    current = current.left
                else:
                    return allIDs
            elif current.value < value:
                if current.right:
                    current = current.right
                else:
                    return allIDs
            else:
                if equal:
                    allIDs += current.ids
                if current.right:
                    current.right.getAllIDs(allIDs)
                    return allIDs
                else: return allIDs

    def getAllIDs(self, arr = []):
        if self.left:
            self.left.getAllIDs(arr)
        arr += self.ids
        if self.right:
            self.right.getAllIDs(arr)
        return arr


    def getAllIDsLess(self, value, equal ):
        allIDs = []
        current = self
        while current != None:
            if current.value < value:
                allIDs += current.ids
                if current.left:
                    current.left.getAllIDs(allIDs)
                if current.right:
                    current = current.right
                else:
                    return allIDs
            elif current.value > value:
                if current.left:
                    current = current.left
                else:
                    return allIDs
            else:
                if equal:
                    allIDs += current.ids
                if current.left:
                    current.left.getAllIDs(allIDs)
                    return allIDs  
                return allIDs

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value,self.ids, end=', ')
        if self.right:
            self.right.PrintTree()
'''
root = Node(11,11)
root.insert(10,10)
root.insert(14,14)
root.insert(9.5,9.5)
root.insert(9.4,9.4)
root.insert(16,16)
root.insert(9.7,9.7)
root.insert(9.6,9.6)
root.insert(3,3)
print('is:',root.find(9))
root.PrintTree()

print('a0', root.getAllIDsMore(11, True))
print('a0', root.getAllIDsMore(0, True))
print('a0', root.getAllIDsLess(9.4, True))
print('a0', root.getAllIDsLess(4, True))
print('a0', root.getAllIDsLess(9.4, True))
print('a0', root.getAllIDsLess(1000, True))
print('a0', root.getAllIDsLess(9.4, True))
'''






