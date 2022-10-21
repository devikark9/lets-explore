# L = [1,2,3,4,7]
# # L = [1,2,8,9]
# # L = [0]
# nl=[]
# ln=len(L)
# for i in range(ln):
#     # print(i)
#     if L[i]+L[i+1]==10:
#         nl.append(L[0]+L[i])
#         print(nl)
#
# def is_leap(year):
#     leap = False
#     # result1=year/4
#     # result2=year/400
#     # result3=year/100
#
#     # Write your logic here
#     if year % 4 == 0 or year % 400 == 0:
#         leap = True
#     if year%100==0:
#         leap=False
#
#     return leap
#
#
# year = int(2100)
# print(is_leap(year))
#
# print(2100%4)
# print(2100%400)
# print(2100%100)
#
# 1800, 1900, 2100, 2200, 2300,2500
#
# e = input()
# el = '1 2 3 4 5 6 7 8 9'
# f = input()
# fl = set(map(int,raw_input().split('')))
#
# u = el.union(fl)
# m=input()
# a=input()
# n=set(map(int,input().split()))
# b=set(map(int,input().split()))
#
# # print(m)
# print(n)
# print(type(n))
# # print(a)
# print(b)
# # print(len(n|b))
#
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# # output = [[x, y, z] for x + y + z != n]
# print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k != n)])
#
# n = int(input())
# arr = map(int, input().split())
# # arr1=[i for i in arr]
# list2=list(set(arr))
# list2.sort()
# print(list2)
# print(list2[-2])
#
# print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k != n)])
#
#
#
# scores=[]
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     scores.append([name,score])
# print(scores)
# scores.sort()
# print(scores)
#
#
#
#
#
#

lst=[45,56,78,99,101,345]
# (RR) [78,99,101,345,45,56]
rst=[]

for i in range(len(lst)) :
    rst.append(lst[i+2] )
print(rst)

#
#
#
#
#
#
#
#
