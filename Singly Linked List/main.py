from list import Singly_list 
from node import Node

def main(): 
    first_node = Node(10)

    my_list = Singly_list(first_node)

    print("Front value:", my_list._front._value)
    print("Back value:", my_list._back._value)
    print("Size:", my_list._size)


if __name__ == "__main__":
    main()