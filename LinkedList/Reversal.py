from linked_list import LinkedList

def reverse_iterative(linkedlist):
    prev= None
    curr = linkedlist.head

    while curr:
        tempnext = curr.next
        curr.next = prev
        prev = curr
        curr = tempnext
    return prev

def reverse_recursive(head):
    # TODO
    return

ll = LinkedList()   
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.print()
ll.get_length() 
ll.remove_at(4)
ll.print()
ll.insert_at(4,5)
ll.print()
ll.head = reverse_iterative(ll)
ll.print()


