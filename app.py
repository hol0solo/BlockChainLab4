import requests


def get_something_from_ATAIX(url, name):
    crypto_book = []
    response = requests.get(url)
    for element in response.json()["result"]:
        crypto_book.append(element[name])
    return crypto_book


names = get_something_from_ATAIX(url='https://api.ataix.kz/api/currencies', name="name")
print(f"Список валют: {str(names)[1:].replace('[', '').replace(']', '')}")
print(f"Количество валют: {len(names)}")


trading_pairs = get_something_from_ATAIX(url='https://api.ataix.kz/api/symbols', name="symbol")
print(f"Список торговых пар: {str(trading_pairs)[1:].replace('[', '').replace(']', '')}")
print(f"Количество торговых пар: {len(trading_pairs)}")


trading_pairs_price = get_something_from_ATAIX(url='https://api.ataix.kz/api/prices', name="lastTrade")
trading_pairs_names = get_something_from_ATAIX(url='https://api.ataix.kz/api/prices', name="symbol")


result = zip(trading_pairs_price, trading_pairs_names)
for element in result:
    print(element)
