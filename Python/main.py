# # print("Hello, World!")

# # name  = "Praveen"
# # exp  = 1
# # is_actice = True
# # value = 15000.00

# # print(type(name))
# # print(type(exp))
# # print(type(is_actice))
# # print(type(value))

# # Arithmatic Operator
# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# # print(a%b)
# # print(a//b)
# # print(a**b)

# # Comparison Operators
# '''
# ==, !=, >, <, >=, <=
# '''

# if a == b :
#     print("A ans B are Equal")
# else:
#     print("A ans B are Not Equal")


for i in range(11):
    print(i)

list_ = [1,2,3,4,5,6,7,8,9,0]

for i in list_:
    print(i)



def isPrime(n):
    if n == 2: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3,int(n**0.5)+1, 2):
        if n % i == 0: return False
    else: return True

print(isPrime(7))