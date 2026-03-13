list_ = [1,2,3,4,5,6,7,8,9]
print(list_)
# Append
list_.append(10)
print(list_)
list_.remove(5)
print(list_)
list_.insert(4,5)
print(list_)
list__ = [11,12,13,14,15]

new_list = list_ + list__
print(new_list)
rm_val_1 = new_list.pop(13)
rm_val_2 = new_list.pop()
print(rm_val_1)
print(rm_val_2)

del new_list[0]
print(new_list)

del new_list[1:4]
print(new_list)