class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return None
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            print(root.val, end=" ")
            root = root.right()


def min_value_node(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr

def max_value_node(root):
    curr = root
    while curr.right:
        curr = curr.right
    return curr


def delete(root, val):
    if not root:
        return root

    if val < root.val:
        root.left = delete(root.left, val)
    
    elif val > root.val:
        root.right = delete(root.right, val)

    else:
        # Root with one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root

#Itiretive delete method while assuming no duplicates allowed
def delete(root, val):
    curr = root

    while curr.val != val:
        prev = curr
        if val < curr.val:
            curr = curr.left
            
        else:
            curr = curr.right

    if curr not None:
        if curr.left is None: 
            oneChild(curr, prev, curr.right)

        elif curr.right is None:
            oneChild(curr, prev, curr.left)
        
        else:
            twoChdren(curr)

#method to get the parent node
def parent_node(root):
    curr = root
    while curr.left:
        prev = curr
        curr = curr.left
    return prev

#method to delete when node has one child
def oneChild(curr, prev, child):
    if prev:
        if curr == prev.left:
            prev.left = child
        else:
            prev.right = child
   
#method to delete when node has 2 children
def twoChdren(curr):
    temp = min_value_node(curr.right)
    prnt = parent_node(curr.right)
    curr.val = temp.val
    oneChild(temp,prnt ,temp.right)





    
