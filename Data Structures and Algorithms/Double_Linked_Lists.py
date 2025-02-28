class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If the node to be deleted is the head
        if temp and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return

        # Search for the node to delete
        while temp and temp.data != key:
            temp = temp.next

        if temp is None:  # Key not found
            return

        # Unlink the node
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None

    # Display the list in forward direction
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display the list in reverse direction
    def display_reverse(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next  # Move to the last node
        
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)

print("Forward Traversal:")
dll.display_forward()

print("Reverse Traversal:")
dll.display_reverse()

dll.delete_node(20)
print("After Deleting 20:")
dll.display_forward()
  