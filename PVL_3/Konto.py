class Konto:
    def __init__(self, name, bank_balance):
        self.name = name
        self.bank_balance = bank_balance
        self.prev = None
        self.next = None
           

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.bank_balance


    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_prev(self, konto):
        self.prev = konto


    def set_next(self, konto):
        self.next = konto

