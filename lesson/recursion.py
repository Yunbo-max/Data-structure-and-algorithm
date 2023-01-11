def tostr(num,base):
    string="0123456789ABCDEF"
    if num<base:
        return string[num]
    else:
        return tostr(num//base,base)+string[num%base]


print(tostr(6,2))