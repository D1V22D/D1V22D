# ml=[ [1,4,3,8], [2,3,7,1], [3,6,9,2,5,8] ] 
# # for i in range(len(ml)): 
# #     for j in range(len(ml[i])): 
# #         print(ml[i][j],sep=",",end=" ") 
# #     print()
# print(*ml[0],sep=",",end=" ")

# k = [[0 for i in range(3)] for j in range(3)]
# print(k)

x=(lambda n,m:(n>m and 'First' or 'Second')) 
print(x(30,20),"number is greater")