# l=[1,1,2,3,4,4,5,1]
# i=0
# c=1
# a=[]
# q=[]
# while i<len(l)-1:
#     if l[i]==l[i+1]:
#         c+=1
#         a.append(c)
#         a.append(l[i])
#         q.append(a)
#     else:
#         a.append(l[i])
#         q.append(a)
#     i+=1
# print(a)


# i=1
# j=0
# user=int(input("enter the number:"))
# while user>=i:
#     if user%i==0:
#         j=j+1
# if j==2:
#     print("prime number")
# else:
#     print("composite number")


# num=int(input("enter the number:"))
# a=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     b=num%10
#     sum=temp**a+sum
#     digit=temp//10
# if num==sum:
#     print("armstrong number")
# else:
#     print("not armstrong")

# i=1
# j=0
# user=int(input("enter the number:"))
# while i<=user:
#     if user % i==0:
#         j=j+1
#     i=i+1
    
# if j==2:
#     print("prime number")
# else:
#     print("composite")


# i=1
# sum=0
# user=int(input("enter the number:"))
# while i<user:
#     if user%i==0:
#         sum=sum+i
#     i=i+1
# if sum==user:
#     print("perfect number")
# else:
#     print("not perfect number")

# i=1
# product=1
# user=int(input("enter the num:"))
# while i<=user:
#     if user>=1:
#         product=product*i
#         i=i+1
# print(product)