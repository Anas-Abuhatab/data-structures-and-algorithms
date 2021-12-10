# Hashtables
* A hash table stores key/value pairs by hashing the key and storing the pair in the index result.

## Challenge
* Create a hash table implementation that allows adding, getting values, checking if a given key exists, and actually hashing a key.

## Approach & Efficiency
All of the methods above exist in the Hashtable class. The hash table is instantiated with 1024 buckets that have a default value of None. Collisions are handled with the linked list data structure. Efficiency:

Method |Time |Space
-------|-----|------
hash   | O(1) | O(1)
add    | O(1) | O(1)
get    | O(n) | O(n)
contain| O(n) | O(n)

## API

Method | Params | Output
-------|--------|--------
hash   | key    | hash code (int)
add    | key,val| None 
get    | key    | value
contain| key    | True or False