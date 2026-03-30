products = [
    {"id": 1, "name": "Laptop", "price": 1200, "stock": 5},
    {"id": 2, "name": "Phone", "price": 800, "stock": 10},
    {"id": 3, "name": "Mouse", "price": 25, "stock": 50},
    {"id": 4, "name": "Keyboard", "price": 100, "stock": 20},
]

def get_products():
    return products

# def find_expensive():
#     products=get_products()
#     prices = []
#     stocks = []
#     for p in products:
#         stock = p['stock']
#         stocks.append(stock)
#         price = p['price']
#         prices.append(price)
#     max_stock = max(stocks)
#     maximum = max(prices)
#     minimum = min(prices)
#     pro_hundred = ''
#     pro_ten = ''
#     for x in products:
#         if maximum == x['price']:
#             print(f"Eng qimmat mahsulot: {x['name']}, {x['price']} so'm turadi")
#         if minimum == x['price']:
#             print(f"Eng arzon mahsulot: {x['name']}, {x['price']} so'm turadi")
#         if max_stock == x['stock']:
#             print(f"Eng ko'p stock bor mahsulot: {x['name']}, soni: {x['stock']}")
#         for price in prices:
#             if price > 100:
#                 if price == x['price']:
#                     pro_hundred += f"{x['name']}, "
#             if price < 10:
#                 if price == x['price']:
#                     pro_ten += f"{x['name']}. "
#     print(f"Narxi 100dan katta bo'lga mahsulotlar: {pro_hundred}")
#     if not pro_ten:
#         pro_ten = "mavjud emas"
#     print(f"Narxi 10dan kichik bo'lgan mahsuotlar: {pro_ten}")
#     return find_expensive
# find_expensive()






# def get_expensive():
#     products = get_products()
#     prices = []
#     for p in products:
#         prices.append(p['price'])
#     maximum = max(prices)
#     for p in products:
#         if maximum == p['price']:
#             print(f"Eng qimmat mahsulot: {p['name']}, {p['price']} so'm turadi.")
# get_expensive()
#
#
# def get_cheap():
#     products = get_products()
#     prices = []
#     for p in products:
#         prices.append(p['price'])
#     minimum = min(prices)
#     for p in products:
#         if minimum == p['price']:
#             print(f"Eng arzon mahsulot: {p['name']}, {p['price']} so'm turadi.")
# get_cheap()
#
# def popular_pro():
#     products = get_products()
#     stock_nums = []
#     for p in products:
#         stock_nums.append(p['stock'])
#     popular = max(stock_nums)
#     for p in products:
#         if popular == p['stock']:
#             print(f"Eng ko'p stock bor mahsulot: {p['name']}, soni: {p['stock']}")
#
# def find_hundred():
#     products = get_products()
#     hundred = ''
#     for p in products:
#         if p['price'] > 100:
#             hundred += f"{p['name']} "
#     if not hundred:
#         hundred = 'mavjud emas'
#     print(f"Narxi 100dan katta bo'lgan mahsulotlar: {hundred}")
# find_hundred()
#
# def find_ten():
#     products = get_products()
#     ten = ''
#     for p in products:
#         if p['price'] < 10:
#             ten += f"{p['name']} "
#     if not ten:
#         ten = 'mavjud emas'
#     print(f"Narxi 100dan katta bo'lgan mahsulotlar: {ten}")
# find_ten()