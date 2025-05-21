def outside ():
    a = 10;
    def inside():
        nonlocal a
        a = 20
        print("indse")