def merge(xpath: str, ypath: str) -> str:
    return urlerslasher(xpath) + unstarter(ypath, '/')

def urlerslasher(xpath: str) -> str:
    return ender(urler(xpath), '/')

def starter(xpath:str, ypath: str) -> str:
    if xpath[0] != ypath:
        return ypath + xpath
    return xpath

def unstarter(xpath:str, ypath: str) -> str:
    if xpath[0] == ypath:
        return xpath[1:]
    return xpath

def ender(xpath: str, ypath: str) -> str:
    if xpath[-1] != ypath:
        return xpath + ypath
    return xpath

def unender(xpath: str, ypath: str) -> str:
    if xpath[-1] == ypath:
        return xpath[:-1]
    return xpath

def urler(xpath: str) -> str:
    if not '://' in xpath:
        return "http://" + xpath
    return xpath

def unurler(xpath: str) -> str:
    if '://' in xpath:
        return xpath.split('://')[-1]
    return xpath
