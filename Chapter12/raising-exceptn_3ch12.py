def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Manish")


a = increment(364)
# a = increment('df364') # This throw an Error
print(a)
