class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # key -> Node
        self.head = None # least recently used

        self.tail = None # most recently used
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 #DNE
        
        # should move to be the most recently used
        node = self.cache[key]
        self.remove(node)
        self.add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
        
            self.remove(node)
            self.add_to_tail(node)
        else:
            # add to cache and list
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_tail(node)

        if len(self.cache) > self.capacity:
            # remove LRU (head)
            if self.head:
                head_key = self.head.key 
                self.remove(self.cache[head_key])
                del self.cache[head_key]


    def remove(self, node) -> None:


        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        node.prev = None
        node.next = None

    def add_to_tail(self, node) -> None:
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node