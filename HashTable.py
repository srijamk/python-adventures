class HashTable:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function(self, value):
        return value % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        while self.keys[hash_value] != None:
            if self.keys[hash_value] == key:
                self.values[hash_value] = value
                return
            hash_value = self.rehash(hash_value)
            
        self.values[hash_value] = value
        self.keys[hash_value] = key

    def get(self, key):
        original_hash_value = self.hash_function(key)

        if self.values[original_hash_value] != None:
            return self.values[original_hash_value]
        
        hash_value = self.has_function(original_hash_value)
        while hash_value != original_has_value and self.values[hash_value] == None:
            hash_value = self.rehash(hash_value)

        if self.values[hash_value] != None:
            return self.values[hash_value]
        else:
            return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
H[20] = "duck"
print(H.keys)
print(H.values)
    

 
