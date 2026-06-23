try:
    with open("test1.txt","r") as f:
        print(f.read())
except Exception as e:
    print("create a file")