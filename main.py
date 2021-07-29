import requests 
import re

def main():
    webpage = requests.get("https://janpoonthong.github.io/portfolio/")
    webpage = webpage.text
    extracting(webpage)

def extracting(webpage):
    print(f"Title: {title_tag(webpage)[0]}")

def title_tag(webpage):
    return re.findall(r'<\s*title.*?>(.*?)<\/title>', webpage)

main()
