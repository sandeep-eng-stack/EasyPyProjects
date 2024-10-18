class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(self.root,data)
    def _insert(self,new,data):
        if new.data>data:
            if new.left is None:
                new.left=Node(data)
            else:
                self._insert(new.left,data)
        else:
            if new.right is None:
                new.right=Node(data)
            else:
                self._insert(new.right,data)
    def delete(self,key,node):
        if node is None:
            print("HI")

        if node.data>key:
            self.delete(key,node.right)
        else:
            self.delete(key,node.left)
            

bt=BinaryTree()
bt.insert(50)
bt.insert(40)
bt.insert(45)
bt.insert(30)
bt.root=Node(50)
print(bt.delete(45,bt.root))



