import unittest

from hash_map import HashMap


class TestHashMap(unittest.TestCase):
    def test_hash_map(self):
        hash_map = HashMap()
    
        # Add two key-value pairs
        hash_map.put(2, 3)
        hash_map.put(4, 10)
        hash_map.put('a', 'b')
        
        self.assertEqual(hash_map.get(2), 3)
        self.assertEqual(hash_map.get('fake-key'), -1)
        self.assertEqual(hash_map.get(4), 10)
        
        hash_map.remove(2)
        
        self.assertEqual(hash_map.get(2), -1)
