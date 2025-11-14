class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def is_empty(self):
        return self.length == 0
    
    def get_length(self):
        return self.length
    

    def __str__(self):
        arr = []
        current = self.head
        while current:
            arr.append(str(current.data))
            current = current.next
        return " -> ".join(arr) if arr else "Empty"
    

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    

    def propend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range nigga")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def find(self, data):
        current = self.head
        current_index = 0
        while current:
            if current.data == data:
                return current_index
            current = current.next
            current_index += 1
        return "Alarm tupoy eblan, net takogo "
    
    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def delete_first(self):

        if self.is_empty():
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        new_head = self.head.next
        self.head = None
        self.head = new_head
        self.length -= 1
    
    def delete_last(self):

        if self.is_empty():
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        
        current = self.head
        while current:
            if current.next == self.tail:
                value = self.tail.value
                current.next = None
                self.tail = current
            current = current.next
        self.length -= 1
        return value
    

    def insert(self, data, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out negritos")
        if index == 0:
                self.propend(data)
        elif index == self.length:
                self.append(data)
        else:
            new_node = Node(data)
            current = self.head

            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1

            

    def reverse(self):
        current = self.head
        prev = None
        self.tail = self.head  

        while current:
            next_node = current.next  
            current.next = prev      
            prev = current            
            current = next_node       

        self.head = prev  

            

        

        

        
        
        



    

first = LinkedList()
first.append(2)
first.append(9)
first.append(19)
first.propend(11)
print(first)
first.reverse()
print(first)

    
