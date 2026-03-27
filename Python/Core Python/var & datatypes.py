# Numeric Datatypes
a = 10
b = 5.0
c = 3 + 4j

# Sequences Datatypes [ Ordered Collections ]
# String
# Ordered collection of characters
# Immutable
s = "Hello"

# List
# Ordered
# Mutable
# Allows duplicates
l = [1,2,3,4,5,4,5,7,8]

# Tuple
# Ordered
# Immutable
# Allows duplicates
t = (3,4,5,5,3,5,6)

# Set Types [ Unordered Collections ]
# Set
# Unordered
# Mutable
# No duplicates
sett = {1,2,3,4,5}

# Frozen Set
# Unordered
# Immutable
# No duplicates
f_sett = frozenset([1,2,3,4,5,6])

# Mapping Type
# Dictionary (dict)
# Key-value pairs
# Ordered (Python 3.7+)
# Mutable
d = {
    "name": "Yuga",
    "age": 23
}

# Boolean Type
# bool → True or False
t = True
f = False

# Binary Types
# Used for raw binary data.
#
# bytes → Immutable
# Stores binary data (0–255 values)
# Cannot change after creation
data = b"hello"
# print(data)        # b'hello'
# print(data[0])     # 104 (ASCII of 'h')

# bytearray → Mutable
data = bytearray(b"hello")
data[0] = 72   # Change 'h' → 'H'
# print(data)    # bytearray(b'Hello')

# memoryview → Memory-efficient view - (Advanced, Fast)
# Direct memory access (no copy)
# Used for performance optimization
data = bytearray(b"hello")
mv = memoryview(data)
mv[0] = 72
print(data)   # bytearray(b'Hello')
print(mv)


# None Type
# Represents no value
x = None