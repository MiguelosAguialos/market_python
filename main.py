import xlsxwriter
import os
from model.product import Product, CartProduct

mainPath = os.path.join('C:\\Users', 'labsfiap', 'Documents', 'docs')

wb = xlsxwriter.Workbook(os.path.join(mainPath, 'Nota Fiscal.xlsx'))
ws = wb.add_worksheet('Nota Fiscal')

catalog = [
    Product(1, "Maçã", 12.9),
    Product(2, "Pera", 10.5),
    Product(3, "Banana", 11.9),
    Product(4, "Laranja", 15.0),
    Product(5, "Melancia", 25.2),
]

table = []
data = []

def ask():
    try:
        qty = float(input('Digite a quantidade (KG) da fruta que deseja comprar: '))
        if qty <= 0:
            raise
        return qty
    except Exception as e:
        print('Quantidade inválida')
        raise


def format_table(items):
    for item in items:
        data.append([item.code, item.name, item.price, item.qty])


while True:
    try:
        choice = int(input('Digite a fruta que deseja comprar conforme o código das frutas: '))
        if choice == 0:
            break
        qty = ask()
        products = list(filter(lambda pr: pr.code == choice, catalog))
        if len(products) == 0:
            print('Esse código não corresponde à nenhum produto, digite outro código')
            continue
        product = products[0]
        cartProduct = list(filter(lambda cart_pd: cart_pd.code == choice, table))
        if len(cartProduct) > 0:
            cartProduct[0].qty += qty
        else:
            table.append(CartProduct(product, qty))
    except Exception as e:
        print(e)
        continue

format_table(table)
print(data)

if len(data) == 0:
    print('Nenhum produto no carrinho')
    exit()

currency_format = wb.add_format({'num_format': '$0.00'})

options = {
    "name": 'Nota_Fiscal',
    "data": data,
    "style": 'Table Style Light 15',
    "total_row": 1,
    "columns": [
        {"header": "Código do Produto", "total_string": "Total:"},
        {"header": "Produto"},
        {"header": "Preço", "format": currency_format},
        {"header": "Quantidade"},
        {
            "header": "Total por Produto",
            "formula": "=[@Preço] * [@Quantidade]",
            "format": currency_format,
            "total_function": "sum",
        },
    ]
}

ws.add_table('A1:E' + str(len(data) + 2), options)
wb.close()

print('Se tudo deu certo, a nota fiscal tá aí')
