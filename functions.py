def encripting(name):
    lst = [hex(ord(ch)).replace("0x", "") for ch in name]
    sep = ","
    txt = sep.join(lst)
    scnd = [oct(int(bin(ord(ch1)).replace("0b", ""))).replace("0o", "") for ch1 in txt]
    cripto = sep.join(scnd)
    return cripto.replace(",", "-")
    
def decripting(source):
    fst = source.replace("-", ",").split(",")
    trash = [str(int(b, 8)) for b in fst]
    bin = [int(b, 2) for b in trash]
    url = [chr(std) for std in bin]
    sep = ""
    txt = sep.join(url)
    napi = txt.split(",")
    nene = [int(b, 16) for b in napi]
    last = [chr(new) for new in nene]
    result = sep.join(last)
    return result
