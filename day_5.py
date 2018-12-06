class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def main():
    with open('./inputs/day_5_1.txt', 'r') as f:
        l = f.readline()[:-1]

    print('Case 1: %d' % solve_case_1(l))

def solve_case_1(l):
    head_node = create_linked_list(l)

    current = head_node

    while current is not None:
        if current.next is not None and abs(current.val - current.next.val) == 32:
            # react with next
            next_node = current.next
            
            # remove next node
            current.next = next_node.next
            if current.next is not None:
                current.next.prev = current

            # remove current node
            if current.prev is None:
                head_node = current.next
                current.next.prev = None
                current = head_node 
            else:
                new_current = current.prev
                new_current.next = current.next
                current.next.prev = new_current
                current = new_current
        else:
            # proceed
            current = current.next

    letters = list()
    current_node = head_node
    while current_node is not None:
        letters.append(chr(current_node.val))
        current_node = current_node.next

    return len(letters)

def create_linked_list(l):
    result = Node(ord(l[0]))
    current = result
    for c in l[1:]:
        new_node = Node(ord(c))
        current.next = new_node
        new_node.prev = current
        current = new_node

    return result

if __name__ == '__main__':
    main()
