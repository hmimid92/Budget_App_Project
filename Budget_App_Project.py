class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        total = 0
        categoryName = len(self.name)
        interval = 30 - categoryName
        str_return = ''
        for star in range(interval):
            if star < interval/2:
                str_return += '*'
            else:
                if star < interval/2 + 1:
                  str_return += f'{self.name}*'
                else: 
                  str_return += '*'
        str_return += '\n'
        for e in self.ledger:
               amount_num_char = len(str("{:.2f}".format(e['amount'])))
               amount_char = str("{:.2f}".format(e['amount']))
               description_str = len(e['description'])
               description_str_slice = ''
               if description_str > 23:
                  description_str_slice = e['description'][:23]
               else:
                   description_str_slice = e['description']
               for space in range(30):
                   if space == 0:
                       str_return += description_str_slice
                   elif space + description_str <= 23:
                       str_return += ' '
                   else:
                       if amount_num_char == 7:
                           str_return += f'{amount_char}\n'
                           total += float(amount_char)
                           break
                       elif amount_num_char== 6:
                           str_return += f' {amount_char}\n'
                           total += float(amount_char)
                           break
                       elif amount_num_char == 5:
                           str_return += f'  {amount_char}\n'
                           total += float(amount_char)
                           break
                       elif amount_num_char == 4:
                           str_return += f'   {amount_char}\n'
                           total += float(amount_char)
                           break
                       elif amount_num_char == 3:
                           str_return += f'    {amount_char}\n'
                           total += float(amount_char)
                           break
                       elif amount_num_char == 2:
                           str_return += f'    {amount_char}\n'
                           total += float(amount_char)
                           break
                       elif amount_num_char == 1:
                           str_return += f'     {amount_char}\n'
                           total += float(amount_char)
                           break
                       else:
                           str_return += '\n'
                           break
        str_return += f'Total: {total}'
        return str_return
    
    def deposit(self,amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
           return False
        
    def get_balance(self):
        deposits = 0
        balance = self.balance 
        for element in self.ledger:
            if element['amount'] < 0:
                balance+= element['amount'] 
            if element['description'] == 'initial deposit':
                deposits = element['amount']
            elif element['description'] == 'deposit':
                deposits += element['amount']
        return deposits + balance 
    
    def transfer(self, amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.name}')
            category.deposit(amount,f'Transfer from {self.name}')
            category.balance += amount
            return True
        else:
            return False
        
    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    ls_withdraw = []
    rounded = []
    category_number = len(categories.__str__().split(','))
    for j in range(category_number):
        withdraw_temp = 0
        for i in categories[j].__str__().split():
            try:
                if float(i) < 0:
                    withdraw_temp += abs(float(i))
            except:
                x = 0
        ls_withdraw.append(withdraw_temp)
    rounded = list(map( lambda el: (int((el/sum(ls_withdraw))* 10) / 10)*100 , ls_withdraw ))
    bar_chart = 'Percentage spent by category\n'
    k = 0
    while k < category_number:
        if k == 0:
            if rounded[k] >= 100:
                bar_chart += '100| o'
            else:
                bar_chart += '100|  '
        else:
            if rounded[k] >= 100:
                bar_chart += '  o'
            else:
                bar_chart += '   '
        if k + 1 == category_number:
            bar_chart += '  \n'
        k += 1
    k = 0
    for el in range(90,9,-10):
        k = 0
        while k < category_number:
            if k == 0:
                if rounded[k] >= el:
                    bar_chart += f' {el}| o'
                else:
                    bar_chart += f' {el}|  '
            else:
                if rounded[k] >= el:
                    bar_chart += '  o'
                else:
                    bar_chart += '   '
            if k + 1 == category_number:
                bar_chart += '  \n'
            k += 1
    k = 0
    while k < category_number:
        if k == 0:
            if rounded[k] >= 0:
                bar_chart += '  0| o'
            else:
                bar_chart += '  0|  '
        else:
            if rounded[k] >= 0:
                bar_chart += '  o'
            else:
                bar_chart += '  '
        if k + 1 == category_number:
            bar_chart += '  \n'
        k += 1
    k = 0
    while k < category_number:
        if k == 0:
            bar_chart += '    ---'
        elif k == 1:
            bar_chart += '---'
        elif k == 2:
            bar_chart += '---'
        else:
            bar_chart += '---'
        if k + 1 == category_number:
            bar_chart += '-\n'
        k += 1
    b = '\n'
    if category_number == 1:
        max_name = len(categories[0].name)
        for ch in range(max_name):
            bar_chart += f'     {categories[0].name[ch]}  {b if ch < max_name - 1 else ""}'
    elif category_number == 2:
        category0 = len(categories[0].name)
        category1 = len(categories[1].name)
        max_name = max(category0,category1)
        for j in range(max_name):
            bar_chart += f'     {categories[0].name[j] if j < category0 else " "}  {categories[1].name[j] if j < category1 else " "}  {b if j < max_name - 1 else ""}'
    elif category_number == 3:
        category0 = len(categories[0].name)
        category1 = len(categories[1].name)
        category2 = len(categories[2].name)
        max_name = max(category0,category1,category2)
        for j in range(max_name):
            bar_chart += f'     {categories[0].name[j] if j < category0 else " "}  {categories[1].name[j] if j < category1 else " "}  {categories[2].name[j] if j < category2 else " "}  {b if j < max_name - 1 else ""}'
    else:
        category0 = len(categories[0].name)
        category1 = len(categories[1].name)
        category2 = len(categories[2].name)
        category3 = len(categories[3].name)
        max_name = max(category0,category1,category2,category3)
        for j in range(max_name):
            bar_chart += f'     {categories[0].name[j] if j < category0 else " "}  {categories[1].name[j] if j < category1 else " "}  {categories[2].name[j] if j < category2 else " "}  {categories[3].name[j] if j < category3 else " "}  {b if j < max_name - 1 else ""}'

    return bar_chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
print(food.get_balance())
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category('Auto')
auto.deposit(1000,'initial deposit')
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing,auto]))