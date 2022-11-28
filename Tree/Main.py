
from Tree_Lib import Tree
from Tree_Lib import Nodo_tree



arbolito=Tree()
arbolito.add_node(5)
arbolito.add_node(4)
arbolito.add_node(70)
arbolito.add_node(90)
arbolito.add_node(2)
arbolito.node_Print()
arbolito.add_node(int(input("\n Enter a number for add it to the tree\n")))
arbolito.buscar_valor(int(input("\n Enter a number for looking for\n")))