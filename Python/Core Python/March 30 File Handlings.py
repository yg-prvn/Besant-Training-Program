# result = []

# with open("names.txt", "r") as f:
#     content = f.read()
#     result = content.split(",")
#     print(result)
#     print(result[0])


# final_list = []
# with open("names.txt", "r") as f:
#     for line in f:
#         splitted = line.strip()
#         result = splitted.split(",")

#         final_list.extend(result)


# with open("text.txt", "w") as f:
#     for name in result:
#         f.write(name + "\n")


# with open("text.txt", "a") as f:
#     f.write("\nHola!")

# Pandas - Also used for Advanced Files Handlings. It handlings various file formats too!
import pandas as pd

output = pd.read_csv("text.txt")
print(output)


result = output.to_dict("records")

print(result)
print(type(result))