import requests
import re


def main():
    webpage = requests.get("https://janpoonthong.github.io/portfolio/")
    webpage = webpage.text
    print(webpage)
    extracting(webpage)


def extracting(webpage):
    print(f"Title: {title_tag(webpage)[0]}")
    print(f"Paragraph: {p_tag(webpage)}")


def p_tag(webpage):
    #  <\s*p.*?>(.|\s*?)<\/p>
    # <\s*p.*?>(.|\s*?)<\/p>
    return re.findall(r"<\s*p.*?>(.*?)<\/p>", webpage)


def title_tag(webpage):
    return re.findall(r"<\s*title.*?>(.*?)<\/title>", webpage)


main()
