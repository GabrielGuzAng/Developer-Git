
class Tree:
    def __init__(self):
        self.root=None
    
    def add_node(self,value):
        if self.root:
            self.root.add_node(value)
        else:
            self.root=Nodo_tree(value)

    def buscar_valor(self, value):
        if self.root:
            self.root.buscar_valor(value)
        else:
            print("\n Non existent value \n")

    def node_Print(self):
        if self.root:
            self.root.node_Print()


class Nodo_tree:
    def __init__(self,value):
        self.value=value
        print("\n The value:",value," was added ","\n")
        self.right=None
        self.left=None

    def add_node(self, value):
        if value>self.value:
            if self.right:
                self.right.add_node(value)
            else:
                self.right=Nodo_tree(value)
        elif value<self.value:
            if self.left:
                self.left.add_node(value)
            else:
                self.left=Nodo_tree(value)

    def buscar_valor(self,value):
        if value==self.value:
            print("\n The value has been found \n")
        elif value<self.value:
            if self.left:
                self.left.buscar_valor(value)
            else:
                print("\n Non existent value \n")
        else:
            if self.right:
                self.right.buscar_valor(value)
            else:
                print("\n Non existent value \n")   
        
    def node_Print(self):
        if self:
            print("\n The value of the node is:",self.value,"\n")
            if self.right:
                self.right.node_Print()
            if self.left:
                self.left.node_Print()


