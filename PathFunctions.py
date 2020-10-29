def merge(self, xpath: str, ypath: str) -> str:
    xpath = self.urlerslasher(xpath)
    ypath = self.unstarter(ypath, '/')
    return xpath + ypath

def urlerslasher(self, xpath: str) -> str:
    return self.ender(self.urler(xpath), '/')

def starter(self, xpath:str, ypath: str) -> str:
    if xpath[0] != ypath:
        return ypath + xpath
    return xpath

def unstarter(self, xpath:str, ypath: str) -> str:
    if xpath[0] == ypath:
        return xpath[1:]
    return xpath

def ender(self, xpath: str, ypath: str) -> str:
    if xpath[-1] != ypath:
        return xpath + ypath
    return xpath

def unender(self, xpath: str, ypath: str) -> str:
    if xpath[-1] == ypath:
        return xpath[:-1]
    return xpath

def urler(self, xpath: str) -> str:
    if not xpath.startswith('http://') and not xpath.startswith('https://'):
        return "http://" + xpath
    return xpath

def unurler(self, xpath: str) -> str:
    if '://' in xpath:
        return xpath.split('://')[-1]
    return xpath
