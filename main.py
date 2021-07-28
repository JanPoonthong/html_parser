import requests 
import re

def main():
    webpage = requests.get("https://janpoonthong.github.io/portfolio/")
    webpage = webpage.text
    print(webpage)
    extracting(webpage)


def extracting(webpage):
    string = "<title>Jan Poonthong</title>"
    print(re.search(r"\s*<title>\w[A-Za-z]* \w[A-Za-z]*</title>", webpage))

main()
