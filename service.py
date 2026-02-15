from database import get_products

def get_expensive():
    products = get_products()
    prices = []
    for p in products:
        prices.append(p['price'])
    maximum = max(prices)
    for p in products:
        if maximum == p['price']:
            a = p['name']
            b = p['price']
    result = f"Eng qimmat mahsulot: {a}, {b} so'm turadi."
    return result

def get_cheap():
    products = get_products()
    prices = []
    for p in products:
        prices.append(p['price'])
    minimum = min(prices)
    for p in products:
        if minimum == p['price']:
            a = p['name']
            b = p['price']
    result = f"Eng arzon mahsulot: {a}, {b} so'm turadi."
    return result

def popular_pro():
    products = get_products()
    stock_nums = []
    for p in products:
        stock_nums.append(p['stock'])
    popular = max(stock_nums)
    for p in products:
        if popular == p['stock']:
            a = p['name']
            b = p['stock']
    result = f"Eng ko'p stock bor mahsulot: {a}, soni: {b}"
    return result

def find_hundred():
    products = get_products()
    hundred = ''
    for p in products:
        if p['price'] > 100:
            hundred += f"{p['name']} "
    if not hundred:
        hundred = 'mavjud emas'
    return f"Narxi 100dan katta bo'lgan mahsulotlar: {hundred}"

def find_ten():
    products = get_products()
    ten = ''
    for p in products:
        if p['price'] < 10:
            ten += f"{p['name']} "
    if not ten:
        ten = 'mavjud emas'
    return f"Narxi 10dan kichik bo'lgan mahsulotlar: {ten}"

def total_info():
    a = get_expensive()
    b = find_ten()
    c = find_hundred()
    d = popular_pro()
    e = get_cheap()
    return f"{a}\n{b}\n{c}\n{d}\n{e}"
print(total_info())