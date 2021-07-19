

# change algorithm

def change(n):
    dicts = {}
    total = n
    quarter = 0
    dime = 0
    nickles = 0
    pennies = 0
    
    while total != 0:
        if total % 25 >= 0 :
            quarter = total//25
            total %= 25
            dicts['quarter'] = quarter
        if total % 10 >= 0:
            dime = total // 10
            dicts['dime'] = dime
            total %= 10
        if total % 5 >= 0:
            nickles = total // 5
            dicts['nickles'] = nickles
            total %= 5
        if total % 1 >= 0:
            pennies = total // 1
            dicts['pennies'] = pennies
            total %= 1
            #print(total)
        #print(dicts)

    return dicts
print(change(999))
print(change(0))
print(change(205))
print(change(2529))
        
            
