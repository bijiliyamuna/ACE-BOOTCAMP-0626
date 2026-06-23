try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print("I am try just started")
    if b%2==0:
        raise Exception
    else:
        print(a/b)
    print("I am try I am done")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("division by even is not allowed")
else:
    print("I am alive because try is executed")
finally:
    print("Im done")
