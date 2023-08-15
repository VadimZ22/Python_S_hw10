# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


class Bankomat:

    def __init__(self):
        self._total_cash = 0
        self._count_operation = 0

    def __check_count_operation(self):
        if not self._count_operation % 3:
            self._total_cash *= 1.03

    def __check_total_cash(self):
        if self._total_cash > 5_000_000:
            self._total_cash *= 0.9

    def show_cash(self):
        print(f'{self._total_cash = }')


    def cash_in(self):
        self.__check_total_cash()
        add = int(input("внесите сумму кратную 50: "))
        if add % 50 == 0:
            self._total_cash += add
            self._count_operation += 1
        else:
            print("Неверная сумма")
        self.__check_count_operation()
        self.show_cash()


    def cash_out(self):
        self.__check_total_cash()
        take = int(input("введите сумму снятия, кратнуб 50: "))
        if take % 50 == 0:
            percent = take * 1.5 * 0.01
            if percent < 30: percent = 30
            if percent > 600: percent = 600
            if self._total_cash < (take + percent):
                print("недостаточно средств")
            else:
                self._total_cash -= (take + percent)
                self._count_operation += 1
        else:
            print("Неверная сумма")
        self.__check_count_operation()
        self.show_cash()


b = Bankomat()
while True:
    print("1 - cash in \n"
          "2 - cash out \n"
          "0 - exit")
    action = input("Введите номер операции: ")
    match action:
        case '1':
            b.cash_in()
        case '2':
            b.cash_out()
        case '0':
            quit()