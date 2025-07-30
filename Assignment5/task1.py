name=input("Enter your name: ")
#mark=int(input("Enter Your Total Mark out of 100:"))

res_dict={"Name":"Gaurav","Mark":99}
if res_dict["Name"]==name:
    print(f"{name} mark is  {res_dict["Mark"]} of 100" )

else:
    print(f"student not found")

