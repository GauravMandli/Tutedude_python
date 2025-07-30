num_list=[]
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)
ans=num_list[:5]
print("first five extract number's: ",ans)
ans.reverse()
print(f"reverse extract number's: {ans}")