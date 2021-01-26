class HashMap(object):
    def __init__(self):
        self.__num_of_buckets = 1000
        self.__buckets = [[] for _ in range(self.__num_of_buckets)]
    
    @staticmethod
    def __hash(key):
        return hash(key)
    
    def put(self, key, value):
        hash_key = self.__hash_key(key)
        bucket = self.__buckets[hash_key]
        
        key_exists = False
        
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                key_exists = True
                break
        
        if key_exists is True:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))
    
    def get(self, key):
        hash_key = self.__hash_key(key)
        bucket = self.__buckets[hash_key]
        
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                return v
        
        return -1
    
    def remove(self, key):
        hash_key = self.__hash_key(key)
        bucket = self.__buckets[hash_key]
        
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                del bucket[i]
                return
    
    def __hash_key(self, key):
        return HashMap.__hash(key) % self.__num_of_buckets
   
    
if __name__ == '__main__':
    # Create hash map instance
    hash_map = HashMap()

    # Add two key-value pairs
    hash_map.put(2, 3)
    hash_map.put(4, 10)
    hash_map.put('a', 'b')

    # Print values added before and a incorrect key
    print(hash_map.get(2))
    print(hash_map.get('fake-key'))
    print(hash_map.get(4))
    print(hash_map.get('a'))

    # Remove a previously added key-value
    hash_map.remove(2)

    # Check if it still exists
    print(hash_map.get(2))