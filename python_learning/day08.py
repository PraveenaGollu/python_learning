# #if
# n = 1
# if n == 1:
#     print(1) #prints 1 if condn is true
# print(2)#2 outside if block
# print()#blank prints

#if-else 
# n = 10
# if n == 10:
#     print(1)#1 if condn is true
# else:
#     print(2)#not prints
# print(3)#3 coz outside if block
# print() #blank
# if n == 20:
#     print(1)#not prints coz condn is false
# else:
#     print(2)#2
# print(3)#3
# print()#blank

# #if-elif-else
# n = 3
# if n == 1:
#     print(1)#not prints condn is not satisfied
# elif n == 2:
#     print(2) #not prints 
# elif n == 3:
#     print(3)#3
# else:
#     print(10)#not prints
# print(11)#11 outside block
# print()#blank space
# n = 5
# if n == 1:
#     print(1)#not prints condn false
# elif n == 2:
#     print(2) #not prints condn false
# elif n == 3:
#     print(3) #not prints condn false
# else:
#     print(10)#10
# print(11)#11

#nested-if
# ch = 'A'  #one char #Range 65–90 Uppercase A–Z 97–122 Lowercase a–z 
# if ch.isalpha():
#     if 65 <= ord(ch) <= 90: #65<=65<=90 is true
#         print('upper case letter')#upper case letter
#     elif 97 <= ord(ch) <= 122:#97<=65 is false
#         print('lower case letter')#not prints
# else:
#     print('not an letter')
# print(1)#1

# #match case 
day = 5 
match day:
    case 1: 
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')#thursday
    case 6:
        print('Friday') 
    case 7:
        print('Saturday')