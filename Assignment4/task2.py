user_input = int(input("Enter a number: "))

if user_input == 25:
    with open("data2.txt","w+") as file:
        data_input = input("Enter text to write to file:" )
        data=file.writelines(data_input + "\n")
        print("Data Sucessfully Written to file",file.name)

    with open("data2.txt","a") as file:
        data_in=input("Enter aditional text to write to file: ")
        file.writelines(data_in)

    with open("data2.txt","r") as file:
        data_read=file.read()
        print(f"Final content of file {file.name} \n {data_read}")
else:
    print("Enter Worng number Plz right number enter")