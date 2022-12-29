from requests import get
from pprint import PrettyPrinter

URL='https://uselessfacts.jsph.pl/random.json'
data=get(URL).json()
printer=PrettyPrinter()

def get_text(data):
    text=data['text']
    return text

text=get_text(data)
printer.pprint(text)