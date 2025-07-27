def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

num=int(input("Enter a number: "))
ans=fact(num)
print(ans)


def fact1(num1):
    f1=1
    if num1<2:
        return 1
    else:
        return num1* fact1(num1-1)

num1=int(input("Enter a number: "))
ans1=fact1(num1)
print(ans1)