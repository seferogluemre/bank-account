class BankAccount:
    def __init__(self,account_holder,account_type="Vadesiz",amount=0):
        self.account_holder=account_holder
        self.amount=amount
        self.account_type=account_type;

    def display_account_info(self):
        print(f"Hesabın Sahibi: ${self.account_holder}")
        print(f"Hesabın Türü: ${self.account_type}")
        print(f"Hesap Bakiyesi: ${self.amount}")


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")
        else:
            print("Yatırılacak miktar pozitif olmalı!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL")
        else:
            print("Yetersiz bakiye veya geçersiz tutar!")

    def check_balance(self):
        print(f"Hesaptaki bakiye: {self.balance} TL")

hesap = BankAccount("Mehmet Yılmaz", 750)


# İşlemler
hesap.check_balance()  # Bakiye kontrol
hesap.deposit(200)     # Para yatırma
hesap.withdraw(100)    # Para çekme
hesap.withdraw(700)    # Fazla çekim denemesi
hesap.check_balance()  # Son bakiye kontrol