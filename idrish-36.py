symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
def check(id):
    c=0
    for i in id:
        if i in symbol:
           c+=1
    return c
print(check(input()))
