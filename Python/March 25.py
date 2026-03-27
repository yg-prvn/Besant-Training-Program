# Split Operations

input = "Arya, Sansa, Danerys, John, Robb"

format = {
    "id": 1,
    "enrolled": "Yes"
}

result = []

code = input.split(", ")

for i in code:
    value = {
        "name": i
    }
    value.update(format)
    result.append(value)

print(result)

# Words Joining

w = ["Hola,", "Praveen!"]
s = " ".join(w)
print(s)

# Replace

n = "I love Java"
n = n.replace("Java", "Python")
print(n)