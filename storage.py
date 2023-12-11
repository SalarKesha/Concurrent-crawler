import csv

products = list()


def store():
    f = csv.writer(open('./data.csv', 'w', encoding='utf-8'))
    for number, product in enumerate(products):
        f.writerow([number, product['title'], product['image'], product['price']])
