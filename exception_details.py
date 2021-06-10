# ZeroDivisionError
try:
    1/0
except Exception as e:
    print(type(e))
    print(e, '\n')

# ValueError
try:
    int("a")
except Exception as e:
    print(type(e))
    print(e, '\n')

# NameError
try:
    print(x)
except Exception as e:
    print(type(e))
    print(e, '\n')

# FileNotFoundError
try:
    f = open("nofile.txt")
except Exception as e:
    print(type(e))
    print(e, '\n')

# ImportError
try:
    import non_existing_module
except Exception as e:
    print(type(e))
    print(e, '\n')

# TypeError
try:
    1/"f"
except Exception as e:
    print(type(e))
    print(e, '\n')

# AttributeError
try:
    x = 10
    x.append(6)
except Exception as e:
    print(type(e))
    print(e, '\n')

# StopIteration
try:
    pass # code that creates exception
except Exception as e:
    print(type(e))
    print(e, '\n')

# KeyError
try:
    pass # code that creates exception
except Exception as e:
    print(type(e))
    print(e, '\n')