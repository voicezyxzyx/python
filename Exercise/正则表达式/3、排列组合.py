import  itertools

mylist=("".join(x) for x in itertools.product("0123456789",repeat=6))
print(mylist)


while True:
    try:
        str=next(mylist)
        print(str)
    except StopIteration as e:
        break