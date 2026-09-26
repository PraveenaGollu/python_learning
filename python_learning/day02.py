# identity tokens and statement
# a = 45
# b = 35
# c = 20
# print(a + b + c)#100

# #keywords
# import keyword 
# print(keyword.kwlist)#'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not','or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# print(len(keyword.kwlist))#35

# # #Identifiers
# num1 = 10 #executes
# n2m = 20 #executes
# n_m = 30#executes
# _num4 = 40#executes
# # 3num = 30#error
# # n@m = 40 #error
# # for = 30#error
# a = 30 
# A = 20
# print(a)#30
# print(A)#20
# #variables 
# name = 'rakesh'#exe
# age = 23#exe

# #assignment 
# a = 40 #exe
# b = 50#exe

# #multiple assignment
# a, b, c = 10, 20, 30
# print(a, b, c)#10,20,30
# a = b = c = 10
# print(a, b, c)#10,10,10

# # #reassignment
# z = 10
# z = 20 
# z = 30
# print(z)#30

#deleting variable
# a = [1,2,3]
# b = a #[1,2,3]
# del a #a is deleted
# # print(a)#error a is not defined
# print(b)#[1,2,3]

# #swapping variables
# a = 10
# b = 20 
# a,b = b,a #10,20=20,10
# print(a, b)#20 10

# #without third variable
# #using + and - 
# a = 10
# b = 20
# a = a + b #10+20=30
# b = a - b #30-20=10
# a = a - b #30-10=20
# print(a, b)#20,10

# #using * and /
# a = 10
# b = 20
# a = a * b#10*20=200
# b = a / b #200/20=10.0
# a = a / b#200/10=20.0
# print(a, b)#(20.0,10.0)

#using ^. A^A = 0, A^0 = A. (A^B)^C  = A^(B^C) 
a = 10  #^ cannot be used for float
b = 20
a = a ^ b 
b = a ^ b  #(a^b) ^ b = a ^ b ^ b = a ^ 0 = a
a = a ^ b  # (a^b) ^ a = a ^ b ^ a = b
print(a, b)

# #single line comment
# '''multi
# line
# comment
# '''
