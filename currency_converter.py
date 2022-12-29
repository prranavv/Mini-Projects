from requests import get
from pprint import PrettyPrinter

BASE_URL="https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies"
ALL_JSON=".json"
data=get(BASE_URL+ALL_JSON).json()
printer=PrettyPrinter()

def show_currency_list(currencies):
    printer.pprint(currencies)


def currency_converter(currency1,currency2):
    CURR_URL=f"/{currency1}/{currency2}"
    data=get(BASE_URL+CURR_URL+ALL_JSON).json()
    value=data[currency2]
    return value

def main():
    
    print("Welcome to my currency converter!")
    print("List-lists the different currencies:")
    print("Convert-know the convertion rate from one currency to another")
    print("Press q to exit program")
    
    while True:
        input1=input("Choose one of the commands above").lower()
        if input1=='q':
            break
        
        elif input1=='list':
            show_currency_list(data)
        
        elif input1=='convert':
            currency1=input("Enter the currency:    ")
            currency2=input("Enter the second currency:    ")
            value=currency_converter(currency1,currency2)
            print(f"The conversion rate between {currency1} and {currency2} is {value}")
        else:
            print("you have entered a wrong input. pls try again")

main()