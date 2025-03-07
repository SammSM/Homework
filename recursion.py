# ex173
# def num_sum():
#     x=input('Enter number: ')
#     if x!='':
#         return float(x)+num_sum()
#     else:
#         return 0
    
# print(num_sum())
#--------------------------------------------------------------------------
# ex174
# def evklid(a, b):
#     if a==0 and b==0:
#         return
#     elif a==0:
#         return b
#     elif b==0:
#         return a
#     else:
#         c=a%b
#         return evklid(b, c)

# print(evklid(9999999999, 33333333))
#--------------------------------------------------------------------------
# ex176
# words_dict={
#     'A': "Alpha", 'B': "Bravo", 'C': "Charlie",
#     'D': "Delta", 'E': "Echo", 'F': "Foxtrot",
#     'G': "Golf", 'H': "Hotel", 'I': "India",
#     'J': "Juliet", 'K': "Kilo", 'L': "Lima",
#     'M': "Mike", 'N': "November", 'O': "Oscar",
#     'P': "Papa", 'Q': "Quebec", 'R': "Romeo",
#     'S': "Sierra", 'T': "Tango", 'U': "Uniform",
#     'V': "Victor", 'W': "Whiskey", 'X': "Xray",
#     'Y': "Yankee", 'Z': "Zulu"
# }

# def dictRec(word):
#     if word!='':
#         return str(words_dict[word[0]])+' '+str(dictRec(word[1:]))
#     else:
#         return ''

# print(dictRec('BAREV'))
#--------------------------------------------------------------------------
# ex181
# def money(dollars, coins):
#     if dollars!=0 and coins==0 or dollars==0 and coins!=0:
#         return False
#     elif dollars==0 and coins==0:
#         return True
    
#     return (money(dollars-25/100, coins-1) or money(dollars-10/100, coins-1) 
#             or money(dollars-5/100, coins-1) or money(dollars-1/100, coins-1))

# print(money(1.25, 9))
#--------------------------------------------------------------------------
# ex184
# def flatList(nestedList):
#     new_list=[]
#     for i in nestedList:
#         if isinstance(i, list):
#             new_list.extend(flatList(i))
#         else:
#             new_list.append(i)
#     return new_list

# mylist=[1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
# print(flatList(mylist))
#--------------------------------------------------------------------------
# ex185
# def func(mylist):
#     if mylist!=[]:
#         return [mylist[0]]*mylist[1]+func(mylist[2:])
#     else:
#         return []

# print(func(['A', 12, 'B', 4, 'A', 6, 'B', 1]))
#--------------------------------------------------------------------------
# ex186
# newlist=['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a', 'b']

# def mylist(listpass):
#     if listpass!=[]:
#         c=0
#         while c<len(listpass) and listpass[0]==listpass[c]:
#             c+=1
#         return [listpass[0]] + [c] + mylist(listpass[c:])
#     else:
#         return []

# print(mylist(newlist))