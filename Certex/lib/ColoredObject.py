class Color:
    def __init__(self):
        self.colors = ['information', 'good', 'bad', 'other']
        self.information = '\x1b[33m[!]\x1b[0m'
        self.good = '\x1b[32m[+]\x1b[0m'
        self.bad = '\x1b[31m[-]\x1b[0m'
        self.other = '\x1b[34m[*]\x1b[0m'

    def list(self):
        for color in self.colors:
            print('self' + '.' + color + '=' + eval('self' + '.' + color))
