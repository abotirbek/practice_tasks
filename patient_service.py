# Vazifalar:
# Eng katta bill kimda?
# Eng yoshi katta bemor kim?
# "Flu" kasalligi bilan nechta bemor bor?
# Umumiy tushum qancha?
# 50 yoshdan kattalarni chiqar
from patient_data import get_patients

def highest_bill():
    data = get_patients()
    bills = {}
    for d in data:
        bills[d['name']]=d['bill']
    maximum = max(bills.values())
    for k,v in bills.items():
        if maximum == v:
            patient = k
            bill = v
    return f"Eng katta bill {patient}da bor, undagi bill: {bill}"

def oldest_patient():
    data = get_patients()
    ages = []
    for d in data:
        ages.append(d['age'])
    maximum = max(ages)
    for d in data:
        if maximum == d['age']:
            oldest = d['name']
            age = d['age']
    return f"Eng yoshi katta bemor {oldest}, u {age} yoshda"

def find_flu():
    data = get_patients()
    have_flu = ''
    for d in data:
        if d['disease']=='Flu':
            have_flu += f"{d['name']}\t"
    return f"Flu kasalligi bor bemorlar: {have_flu}"

def total_income():
    data = get_patients()
    total = 0
    for d in data:
        total += d['bill']
    return f"Jami tushum: {total}"

def find_fiftiers():
    data = get_patients()
    fiftiers = ''
    for d in data:
        if d['age']>50:
            fiftiers += f"{d['name']}\t"
    return f"Yoshi 50dan kattalar: {fiftiers}"

def get_info():
    a = highest_bill()
    b = oldest_patient()
    c = find_flu()
    d = total_income()
    e = find_fiftiers()
    return f"{a}\n{b}\n{c}\n{d}\n{e}"
print(get_info())