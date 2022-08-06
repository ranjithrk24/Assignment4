x=[int(x) for x in input().split(" ")]
def square(x):
    return x**2
result=list(map(square,x))
print(result)
