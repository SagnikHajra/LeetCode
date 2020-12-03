class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("Previous Node is None")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def node_at_the_end(self,new_data):
        new_node = Node(new_data)
        print new_data
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next

    def delete_a_node(self,delete_node):
        if self.head is None:
            print "List is empty"
            return
        temp = self.head
        prev_node = self.head
        while temp.data != delete_node:
            prev_node = temp
            temp=temp.next
        prev_node.next = temp.next

    def reverse_print(self,cur_node):
        if cur_node:
            self.reverse_print(cur_node.next)
            print cur_node.data,
            return




if __name__ == '__main__':
    llist = LinkedList()
    llist2 = LinkedList()

    llist.node_at_the_end(8)
    llist.node_at_the_end(18)
    llist.node_at_the_end(38)

    llist.push(-8)

    cur_node = llist.head
    while cur_node.data != 18:
        cur_node = cur_node.next

    llist.insert_after(cur_node,28)
    llist.print_list()
    llist.delete_a_node(18)
    llist.print_list()
    llist2.delete_a_node(18)
    llist.reverse_print(llist.head)