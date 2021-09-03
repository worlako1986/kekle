
class Sknode:
    """
    Singly linklist node
    """
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def display(self):
        return self.__repr__()

    def __repr__(self):
        """
        Display the content of knode.
        This operation takes O(1) time and O(1) space
        """
        return "<Node Data: {}>".format(self.data)

class SklinkList:
    """
    Singly linklist
    Abbreviation: skl
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        is_empty()
        Check if head of sklinlist if None
        """
        return self.head is None

    def size(self):
        """
        size()
        Count and return total number of nodes contain in the sklinlist
        This operation takes O(n) time and O(1) space
        """
        count = 0
        if self.is_empty(): return count

        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def search(self,key):
        """
        search(key)
        Lookup for key and return related node object,
        if found or None if not found
        This operation takes O(n) time and O(1) space
        """
        current = self.head
        while current:
            if current.data == key:
                break
            current = current.next_node
        return current

    def find(self,key):
        """
        find(key)
        Lookup for key and return True,
        if found or False if not found
        This operation takes O(n) time and O(1) space
        """
        current = self.head
        while current:
            if current.data == key:
                break
            current = current.next_node
        if current is not None: return True
        return False

    def index(self,key):
        """
        index(key)
        Lookup for key and return index,
        if found or None if not found
        This operation takes O(n) time and O(1) space
        """
        index = 0
        current = self.head
        while current:
            if current.data == key:
                break
            current = current.next_node
            index += 1

        if current is not None: return index
        return None

    def get_node_at_index(self,index):
        """
        get_node_at_index(index)
        Lookup for node at index and return node object,
        if found or None if not found
        This operation takes O(n) time and O(1) space
        """
        if index == 0 or self.is_empty(): return self.head
        
        current = self.head
        position =0
        while position < index:
            current = current.next_node
            position += 1
        return current

    def prepend(self,data):
        """
        prepend(data)
        Add data element as head of the sklinlist
        This operation takes O(1) time and O(1) space
        """
        new_node = Sknode(data)
        new_node.next_node = self.head
        self.head = new_node

    def postpend(self,data):
        """
        postpend(data)
        Add data element as tail of the sklinlist
        This operation takes O(n) time and O(1) space
        """
        new_node = Sknode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node=new_node

    def insert(self,data,index):
        """
        insert(data,index)
        Insert data element at the position of the index - 1
        This operation takes O(n) time and O(1) space
        """
        # Base case
        if index == 0:
            self.prepend(data)
            return True

        new_node = Sknode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            position = 0

            while current.next_node:
                if position == index-1:
                    break
                current = current.next_node
                position += 1;

            # Get provious node and current node
            previous = current
            current = current.next_node

            # Assign current node to new_node.next_node
            # Assign new_node to provious.next_node
            new_node.next_node = current
            previous.next_node = new_node

        return True

    def remove(self,key):
        """
        remove(data,key)
        Remove data element at the position of the key
        This operation takes O(n) time and O(1) space
        """

        if self.head is None:
            return False
        else:
            previous = self.head
            current =self.head.next_node

            # Base case
            if previous.data == key:
                self.head = provious.next_node
                return True

            while current:
                if current.data == key:
                    break
                previous = current
                current = current.next_node

            if current is not None:
                # Assign current.next_node to provious.next_node
                previous.next_node = current.next_node

            else:
                return False

        return True

    def display(self):
        """
        display()
        Display the content of sklinlist
        This operation takes O(n) time and O(1) space
        """
        return self.__repr__()

    def __repr__(self):
        """
        Display the content of sklinlist
        This operation takes O(n) time and O(1) space
        """
        list_kl = []
        if self.head is None: return "Linklist is is empty."

        current = self.head
        while current:#Takes O(n) time
            if current is self.head:
                list_kl.append("[Head: {}]".format(current.data))
                current = current.next_node

            elif current.next_node is None:
                list_kl.append("[Tail: {}]".format(current.data))
                current = current.next_node

            else:
                list_kl.append("[{}]".format(current.data))
                current = current.next_node

        return " => ".join(list_kl)
