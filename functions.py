def smart_sub(n1,n2):
    res=n1-n2 if n1>n2 else n2-n1
    return res

print(smart_sub(10,20))