class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def _init_(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)
        if not self.root:
            self.root=new_node
            break
        temp=self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left=new_node
                    break
                temp=temp.left
            elif data>temp.data:
                if temp.right is None:
                    temp.right=new_node
                temp=temp.right
                
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inoder(root.right)
            
bst = BST()
values = [50, 30, 20, 40, 70, 60, 80]
for value in values:
    bst.insert(value)
