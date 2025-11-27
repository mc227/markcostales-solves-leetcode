class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self,key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_item = self.head
        while last_item.next:
            last_item = last_item.next
        
        last_item.next = new_node
    

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.print_list()
    ll.append(55)
    ll.print_list()
