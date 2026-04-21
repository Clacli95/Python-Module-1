def media(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(media(1, 2, 3, 4, 5))
print(media(10, 20, 30))
print(media())