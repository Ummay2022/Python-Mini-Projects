from Konto import Konto


class Bank:
    def __init__(self):
        self.head = None
        

    def append(self, name, bank_balance):
        new_konto = Konto(name, bank_balance)
        if self.head is None:
            self.head = new_konto
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_konto)
            new_konto.set_prev(current)

    def get(self, index):
        current = self.head
        i = 0
        while current and i < index:
            current = current.get_next()
            i += 1
        return current if current else None

    def get_head(self):
        return self.head

    def insert(self, index, name, bank_balance):
        if index == 0:
            new_konto = Konto(name, bank_balance)
            if self.head:
                new_konto.set_next(self.head)
                self.head.set_prev(new_konto)
            self.head = new_konto
            return True
        else:
            current = self.get(index - 1)
            if current:
                new_konto = Konto(name, bank_balance)
                next_konto = current.get_next()
                new_konto.set_next(next_konto)
                new_konto.set_prev(current)
                if next_konto:
                    next_konto.set_prev(new_konto)
                current.set_next(new_konto)
                return True
        return False


    def delete(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.get_next()
                if self.head:
                    self.head.set_prev(None)
                return True
        else:
            current = self.get(index)
            if current:
                prev_konto = current.get_prev()
                next_konto = current.get_next()
                if prev_konto:
                    prev_konto.set_next(next_konto)
                if next_konto:
                    next_konto.set_prev(prev_konto)
                return True
        return False


    def print_accounts(self):
        current = self.head
        while current:
            print(f"Name: {current.get_name()}, Balance: {current.get_balance()}")
            current = current.get_next()


    def swap(self, index1, index2):
        konto1 = self.get(index1)
        konto2 = self.get(index2)
        if konto1 and konto2:
            prev1 = konto1.get_prev()
            next1 = konto1.get_next()
            prev2 = konto2.get_prev()
            next2 = konto2.get_next()

            # Update predecessor and successor references
            if prev1:
                prev1.set_next(konto2)
            else:
                self.head = konto2
            if next1:
                next1.set_prev(konto2)

            if prev2:
                prev2.set_next(konto1)
            else:
                self.head = konto1
            if next2:
                next2.set_prev(konto1)

            # Swaping predecessor and successor for the accounts
            konto1.set_prev(prev2)
            konto1.set_next(next2)
            konto2.set_prev(prev1)
            konto2.set_next(next1)

            return True

        return False

    def sort_by_balance(self):
        if self.head:
            sorted_list = []
            current = self.head
            while current:
                sorted_list.append(current)
                current = current.get_next()
            sorted_list.sort(key=lambda x: x.get_balance())

            self.head = sorted_list[0]
            current = self.head
            for i in range(1, len(sorted_list)):
                current.set_next(sorted_list[i])
                sorted_list[i].set_prev(current)
                current = current.get_next()
            current.set_next(None)


    def get_median(self):
        if self.head is None:
            return None

        # Counting the number of accounts
        current = self.head
        count = 0
        while current:
            current = current.get_next()
            count += 1

        # Getting the account balances and sorting them
        balances = []
        current = self.head
        while current:
            balances.append(current.get_balance())
            current = current.get_next()
        balances.sort()

        # Calculating the median based on the number of accounts
        if count % 2 == 0:
            mid1 = count // 2 - 1
            mid2 = count // 2
            median = (balances[mid1] + balances[mid2]) / 2
        else:
            median = balances[count // 2]

        return median



if __name__ == '__main__':
    bank = Bank()
    bank.append("Max", 100)
    bank.append("Maxie", 150)
    bank.append("Ulla", 200)
    assert bank.insert(2, "Hans", 5000) == True
    assert bank.delete(5) == False
    assert bank.get(8) is None
    assert bank.get(0).name == "Max"
