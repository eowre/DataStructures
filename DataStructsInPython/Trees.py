import sys

class BSTNode:
    def __init__(self, val = None):
        self.val = val
        self.lchild, self.rchild = None, None
        
    def insert(self, val):
        if not self.val:
            self.val = val
            return self
        if val == self.val:
            return
        if val > self.val:
            if self.rchild:
                self.rchild.insert(val)
                return
            self.rchild = BSTNode(val)
            return
                        
        if val < self.val:
            if self.lchild:
                self.lchild.insert(val)
                return
            self.lchild = BSTNode(val)
            
    def get_min(self):
        current = self
        while current.lchild:
            current = current.lchild
        return current.val
    
    def get_max(self):
        current = self
        while current.rchild:
            current = current.rchild
        return current.rchild
    
    def delete(self, val):
        if self == None: # check if node is initlaized
            return self
        if self.rchild == None:
            return self.lchild 
        if self.lchild == None:
            return self.rchild
        if val < self.val: # if val is less than node val we travel down left side
            self.lchild = self.lchild.delete(val) # assigning the left child to the returned node from the recursive delete function
            return self
        if val > self.val: # if val is greater than the node travel down right side
            self.rchild = self.rchild.delete(val) # assigning the right child to the returned node from the recursive delete function
            return self
        min_larger_node = self.rchild
        while min_larger_node.lchild:
            min_larger_node = min_larger_node.lchild
        self.val = min_larger_node.val
        self.rchild = self.rchild.delete(min_larger_node.val)
        return self
    
    def exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.lchild == None:
                return False
            return self.lchild.exists(val)
        if self.rchild == None:
            return False
        return self.rchild.exists(val)
    
    def inorder(self, vals):
        if self.lchild is not None:
            self.lchild.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.rchild is not None:
            self.rchild.inorder(vals)
        return vals
    
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.lchild is not None:
            self.lchild.inorder(vals)
        if self.rchild is not None:
            self.rchild.inorder(vals)
        return vals
    
    def postorder(self, vals):
        if self.lchild is not None:
            self.lchild.inorder(vals)
        if self.rchild is not None:
            self.rchild.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
    
def BSTree():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")
    
    print("6 exists:")
    print(bst.exists(6))

    nums = [2, 6, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    print("#")
    print("6 exists:")
    print(bst.exists(6))

    print("4 exists:")
    print(bst.exists(4))
    print("2 exists:")
    print(bst.exists(2))
    print("12 exists:")
    print(bst.exists(12))
    print("18 exists:")
    print(bst.exists(18))

class AVLNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.height = 1
        
class AVLTree(object):
    
    def insert(self, root, val):
        if not root:
            return AVLNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
            
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balanceFactor = self.getBalance(root)
        
        if balanceFactor > 1:
            if val < root.left.val:
                return self.rightRotate(root)
            else: 
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if val > root.right.val:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root        
    
    def delete(self, root, val):
        if not root: # Null tree case 1
            return root
        elif val < root.val: # case 2 with one child
            root.left = self.delete(root.left, val)
        elif val > root.val: # case 2 with ond child
            root.right = self.delete(root.right, val)
        else: # case 3 with 2 children 
            if root.left is None: # one child null left side
                temp = root.right
                root = None
                return temp
            elif root.right is None: # one child null right side
                temp = root.left 
                root = None
                return temp
            temp = self.getMinvalueNode(root.right) #inorder trafersel to replace node
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        
        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balanceFactor = self.getBalance(root)
        
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else: 
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    def leftRotate(self, x):
        y = x.right
        temp = y.left
        y.left = x
        x.right = temp
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def rightRotate(self, x):
        y = x.left
        temp = y.right
        y.left = x
        x.right = temp
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))        
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
    def getHeight(self, root):
        if not root: 
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def getMinvalueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def preOrder(self, root):
        if not root:
            return
        print("{0}".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    def printHelper(self, currPtr, indent, last):
       if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.val)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
            
def AVLTreeDriver():
    myTree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        root = myTree.insert(root, num)
    myTree.printHelper(root, "", True)
    key = 13
    root = myTree.delete(root, key)
    print("After Deletion: ")
    myTree.printHelper(root, "", True)

class RBNode():
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
        self.color = 1
        
class RBTree():
    def _init__(self):
        self.NULL = RBNode( 0 )
        self.NULL.color = 0
        self.NULL.left, self.NULL.right = None, None
        self.root = self.NULL
        
    def insert(self, key):
        node = RBNode( 0 )
        node.val = key
        node.parent = None
        node.left = self.NULL
        node.right = self.NULL
        self.root = self.NULL
        
        x = self.root
        y = None
        
        while x != self.NULL:
            y = x
            if node.val < x.val:
                x = x.left
            else: 
                x = x.right
                
        node.parent = y
        
        if y == None:
            self.roote = node
        elif node.val < y.val:
            y.left = node
        else: 
            y.right = node
        
        if node.parent == None:
            node.color = 0
            return
        
        if node.parent.parent == None:
            return
            
        self.fixInsert(node)
        
    def fixInsert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color ==1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rightRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotation(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.leftRotation(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)
            if k == self.root:
                break
            self.root.color = 0
            
    def fixDelete ( self , x ) :
        while x != self.root and x.color == 0 :          
            if x == x.parent.left :                       
                s = x.parent.right                        
                if s.color == 1 :                         
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.leftRotation ( x.parent )                  
                    s = x.parent.right
             
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                           
                    x = x.parent
                else :
                    if s.right.color == 0 :               
                        s.left.color = 0                  
                        s.color = 1                       
                        self.rightRotate ( s )                     
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0                    
                    s.right.color = 0
                    self.leftRotation ( x.parent )                  
                    x = self.root
            else :                                        
                s = x.parent.left                         
                if s.color == 1 :                         
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.rightRotate ( x.parent )                  
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.parent
                else :
                    if s.left.color == 0 :                
                        s.right.color = 0                 
                        s.color = 1
                        self.leftRotation ( s )                     
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rightRotate ( x.parent )
                    x = self.root
        x.color = 0
            
    def rbTransplat(self, u, v):
        if u.parent == None:
            self.root =v 
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.ritght = v
        v.parent = u.parent
            
    def deleteNodeHelper(self, node, key):
        z = self.NULL
        while node != self.NULL:
            if node.val == key:
                z = node
            if node.val <= key:
                node = node.right
            else:
                node = node.left
        if z == self.NULL:
            print("value not present in tree")
            return
        
        y = z
        yOriginalColor = y.color
        if z.left == self.NUll:
            x = z.right
            self.rbTransplant(z, z.right)
        elif (z.right == self.NULL):
            x = z.left
            self.rbTransplant(z, z.left)
        else:
            y = self.min(z.right)
            yOriginalColor = y.color
            x = y.right
            if y.parent == z :                              # If y is child of z
                x.parent = y                                # Set parent of x as y
            else :
                self.ebTransplant ( y , y.right )
                y.right = z.right
                y.right.parent = y

            self.rbTransplant ( z , y )
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if yOriginalColor == 0 :                          # If color is black then fixing is needed
            self.fixDelete ( x )
            
    def delete(self, val):
        self.deleteNodeHelper(self.root, val)
            
    def min(self, node):
        while node.left != self.NULL:
            node = node.left
        return node
        
    def leftRotation(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL :
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None :
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.right = y
        else: 
            x.parent.left = y
        y.right = x
        x.parent = y
        
        # Function to print
    
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )

def RBDriver():
    bst = RBTree()

    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.insert(5)
    bst.insert(4)
    bst.insert(2)

    bst.print_tree()

    print("\nAfter deleting an element")
    bst.delete(2)
    bst.print_tree()
    
class TwoThreeTree(object):

    class _2Node(object):
        def __init__(self, val):
            self.val = val
            self.left, self.right = None, None

    class _3Node(object):
        def __init__(self, lval, rval):
            self.lval = lval
            self.rval = rval
            self.left, self.middle, self.right = None, None, None
        

def main():
    BSTree()
    AVLTreeDriver()
    # RBDriver()

if __name__ == '__main__':
    main()