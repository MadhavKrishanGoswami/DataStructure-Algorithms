from linked_list import LinkedList

def find_loop(linkedlisthead):
    slow = linkedlisthead
    fast = linkedlisthead
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
