class SinglyLinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        node = SinglyLinkedListNode(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def insertNodeAtPosition(self, data, position):
        current = self.head
        cursor = 0
        temp_node = None

        while current:
            if cursor == position - 1:
                temp_node = current.next
                node = SinglyLinkedListNode(data)
                current.next = node
            if cursor == position:
                current.next = temp_node
            current = current.next
            cursor += 1

    def print_list(self):
        current = self.head
        result = []
        while(current):
            result.append(current.data)
            current = current.next
        # print(result)
        delimiter = ' '
        print(delimiter.join((map(str, result))))
#     # Write your code here


if __name__ == '__main__':

    print("Enter the size: ")
    linked_list_count = int(input())
    print("Enter the value to add: ")
    data = int(input())
    print("Enter the position: ")
    position = int(input())

    singly_linked_list = SinglyLinkedList()
    # Initialise linked list with values
    for i in range(linked_list_count):
        singly_linked_list.insert_node(i)

    print("Show init list:")
    singly_linked_list.print_list()

    # Insert to the position
    singly_linked_list.insertNodeAtPosition(data, position)

    print("Show result list:")
    singly_linked_list.print_list()
