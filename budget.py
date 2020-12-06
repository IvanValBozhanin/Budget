class Category:
    name = ""
    ledger = []
    balance = 0
    spent = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spent = 0

    def check_funds(self, amount):
        return self.balance >= amount

    def get_balance(self):
        return self.balance

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            self.spent += amount
            return True
        return False

    def transfer(self, amount, new_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + new_category.name)
            new_category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def __str__(self):
        fl = '*'*(int((30-len(self.name))/2)) + self.name + '*'*(int((30-len(self.name))/2)) + '\n'
        for i in range(len(self.ledger)):
            k = self.ledger[i]["amount"]
            fl += self.ledger[i]["description"][:23]
            offset = 30 - len(str("{0:.2f}".format(k))) - len(self.ledger[i]["description"][:23])
            fl += ' ' * offset
            fl += str("{0:.2f}".format(k))
            fl += '\n'
        b = self.balance
        fl += "Total: " + str("{0:.2f}".format(b))
        return fl


def create_spend_chart(categories):
    total = 0
    max_rows = 0
    for i in categories:
        total += i.spent
        max_rows = max(max_rows, len(i.name))
    percent = []
    for i in categories:
        percent.append(int(10 * i.spent / total))
    out = "Percentage spent by category\n";
    for i in range(11):
        current_percent = 11 - i - 1
        out += (' ' if current_percent != 10 and current_percent != 0 else ('  ' if current_percent == 0 else '')) + str(current_percent if current_percent != 0 else '') + '0| '
        for j in percent:
            if j >= current_percent:
                out += 'o  '
            else:
                out += '   '
        out += '\n'
    out += '    -'
    out += '---'*len(categories)
    for i in range(max_rows):
        out += '\n     '
        for j in categories:
            if i < len(j.name):
                out += j.name[i] + '  '
            else:
                out += '   '
    return out
