class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number
    
    def __str__(self) -> str:
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size
    
    def hash_function(self, key: str) -> int:
        """
        Computes a hash value for the given key using ord() values
        """
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size
    
    def insert(self, key: str, number: str) -> None:
        """
        Creates a new Contact object and adds it to the table.
        If a contact with the same name exists, updates the number.
        """
        contact = Contact(key, number)
        index = self.hash_function(key)
        
        # If the slot is empty, create new node
        if self.data[index] is None:
            self.data[index] = Node(key, contact)
            return
        
        # If key exists, update the number
        current = self.data[index]
        while current is not None:
            if current.key == key:
                current.value = contact
                return
            current = current.next
        
        # If key doesn't exist, add to front of chain
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node
    
    def search(self, key: str) -> Contact | None:
        """
        Searches for a contact by name and returns the Contact object if found.
        Returns None if no contact is found.
        """
        index = self.hash_function(key)
        
        current = self.data[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def print_table(self) -> None:
        """
        Prints each index of the hash table and all contacts stored at that index.
        """
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current is not None:
                    print(f"{current.value}", end=" -> " if current.next else "\n")
                    current = current.next

# Test your hash table implementation here.  
if __name__ == "__main__":
    # Create a new hash table
    table = HashTable(10)
    
    # Print empty table
    print("Empty table:")
    table.print_table()
    
    print("\nAdding contacts:")
    # Add some contacts
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()
    
    print("\nSearching for contacts:")
    # Search for contacts
    john = table.search("John")
    print(f"Found John: {john}")
    rebecca = table.search("Rebecca")
    print(f"Found Rebecca: {rebecca}")
    bob = table.search("Bob")
    print(f"Found Bob: {bob}")
    
    print("\nUpdating John's number:")
    # Update a contact
    table.insert("John", "999-999-9999")
    table.print_table()

# A: Hash tables allow for faster lookups. Instead of searching through the entire data structure (like you would with a list) or traversing nodes (like in a tree), you can jump directly to where the data should be. 
# B: For collisions, when two names hash the same index, a linked list is created at that index to store multiple entries. Each entry points to the next one, allowing for efficient storage and retrieval of colliding keys.
# C:  It's a good choice to pick a hash table for projects like contact lists and indexing, since order doesnt always matterand data has unique keys that can be hashed efficiently.