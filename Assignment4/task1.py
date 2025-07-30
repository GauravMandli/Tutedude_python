from fileinput import filename

try:
    with open("data.txt", "r") as f:
      content = f.read()
    print(content)

    data=open("data1.txt","r")
    content1=data.read()
    print(content1)
    data.close()
except FileNotFoundError as e:
    print("File not found",e.filename)
else:
    print("File found")
finally:
    print("Try again")
