# Dictionaries
d = {
    "name": "Praveen",
    "degree": "B.E"
}

print(d)

print(d.get("degree"))

print(d.get("degree", "Unknown"))
print(d.get("address", "Unknown"))

d["age"] = 22
d["age"] = 23
print(d)

edit = {
    "degree" : "M.E",
    "occ": "Student"
}

d.update(edit)
print(d)

# delete
del d["occ"]
print(d)

pop_operation = d.pop("age")
print(d)
print(pop_operation)
d.clear()
print(d)