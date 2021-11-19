def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Errorrr!!!!!")
a = increment('h')
print(a)