# Vazifalar:
# Eng katta balance kimda?
# Eng yosh user kim?
# 18 dan katta userlarni chiqar
# Balancelarni yig‘indisini top
from database_users import get_users

def highest_balance():
    data = get_users()
    balances = {}
    for d in data:
        balances[d['name']]=d['balance']
    maximum = max(balances.values())
    for k,v in balances.items():
        if v == maximum:
            rich = k
            amount = v
    return f"Eng ko'p balans {k}da bo'lin qiymati: {v}"

def find_youngest():
    data = get_users()
    ages = {}
    for d in data:
        ages[d['name']]=d['age']
    minimum = min(ages.values())
    for k,v in ages.items():
        if v == minimum:
            child = k
            age = v
    return f"Eng yosh user {child}, u {age} yosh"

def find_eighteen():
    data = get_users()
    eighteeners = ''
    for d in data:
        if d['age']>18:
            eighteeners += f'{d['name']}\t'
    return f"18 yoshdan katta bo'lganlar: {eighteeners}"

def find_total_balance():
    data = get_users()
    total = 0
    for d in data:
        total += d['balance']
    return f"Jami balans: {total}"

def get_info():
    a = highest_balance()
    b = find_youngest()
    c = find_eighteen()
    d = find_total_balance()
    return f"{a}\n{b}\n{c}\n{d}"
print(get_info())