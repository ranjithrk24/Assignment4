x=[int(x) for x in input().split(" ")]
def triple(x):
    return x*3
result=list(map(triple,x))
print(result)
