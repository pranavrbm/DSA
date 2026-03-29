def isUnique(string:str):
    if len(string) > 128: return False
    
    charset = [False] * 128
    
    for s in string:
        s=ord(s)
        print(s)
        if charset[s]: return False
        charset[s] = True
    return True
def isUnique2(string:str):
    checker =0
    for i in string:
        val = ord(i) - ord("a")
        # print("val:",val)
        # print("checker:",checker)
        # print("1<<val",1<<val)
        # print("&:",checker&(1<<val))
        if ((checker & (1 << val)) >0): return False
        checker |= (1<< val)
        # print("checker:",checker)
    return True
print(isUnique2("hello"))
