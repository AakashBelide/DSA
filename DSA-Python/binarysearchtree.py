class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if(data == self.data):
            return
        
        if(data<self.data):
            if(self.left):
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if(self.right):
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        # visit left tree
        if(self.left):
            elements += self.left.in_order_traversal()
        
        # visit base node
        elements.append(self.data)

        # visit right tree
        if(self.right):
            elements += self.right.in_order_traversal()    

        return elements
    
    def search(self, val):
        if(self.data == val):
            return True
        
        if(val<self.data):
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if(val>self.data):
            if self.right:
                return self.right.search(val)
            else:
                return False
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.search(21))
    print(numbers_tree.search(200))

    countires = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countires)
    print(country_tree.in_order_traversal())
    print("UK is in the tree?", country_tree.search("UK"))
    print("Sweden is in the tree?", country_tree.search("Sweden"))