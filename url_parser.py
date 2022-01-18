# Name : url_parser.py v0.0.1
# Author : thCyberTech
# Date : 16th Jan 2022
# Description : A class based python file that receives a URL and performs various parsing actions

from urllib.parse import urlparse
import requests
import sys

class Parser:

    def __init__(self, url):
        self.url = url
        self.url_parsed = None
        self.mydict = None
        self.schemes = {"http","https"}

    @property
    def parse_url(self):
        self.url_parsed = urlparse(self.url)
        self.mydict = {}

        if self.url_parsed.scheme in self.schemes:
            self.mydict = {
                'Scheme': self.url_parsed.scheme,
                'netloc': self.url_parsed.netloc,
                'path': self.url_parsed.path,
                'params': self.url_parsed.params,
                'query': self.url_parsed.query,
                'fragment': self.url_parsed.fragment
            }
            return self.mydict

class Curl:
    
    def __init__(self, url):
        self.url = url
        self.status = None

    #@property
    def get_status(self):
        self.status = requests.get(self.url)

        return self.status

def main():
    
    while True:
        supplied_url = input("Enter URL: ")
        p_url = Parser(supplied_url)

        if (answer:=p_url.parse_url):
            print(answer)
            p_status = Curl(supplied_url)
            p_status.get_status()
            print(p_status.status)
            sys.exit(-1)
        else:
            print("URLs should HTTP or HTTPS only. Please resubmit valid URL")
            sys.exit(-1)

if __name__ == '__main__':
    main()