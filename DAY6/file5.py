with open("/workspaces/ACE-BOOTCAMP-0626/DAY6/flower.jpg","rb") as f:
    content=f.read()
    with open("flowercopy.jpg","wb") as cf:
        cf.write(content)