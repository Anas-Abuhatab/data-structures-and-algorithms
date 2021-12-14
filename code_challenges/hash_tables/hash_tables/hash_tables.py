from hash_tables.linked_list_for_hash import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        hash_total = sum([ord(ch) for ch in key])
        return (hash_total * 211) % self.size

    def add(self, key, value):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].add((key, value))
        


    def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            current =current.next

    def contains(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]
        if not bucket == None:
            current = bucket.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        return False

if __name__=='__main__':
    hashtable= Hashtable()
    hashtable.add("AHMAD",30)
    hashtable.add("YAHYA",22)
    hashtable.add("HAMAD",55)

    for index,item in enumerate(hashtable._buckets):
        if item:
            print(index, item.display())

    print(hashtable.get("AHMAD"))
    print(hashtable.get("YAHYA"))
    print(hashtable.get("HAMAD"))
