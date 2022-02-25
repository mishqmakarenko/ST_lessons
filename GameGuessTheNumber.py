from main import EngineGame


class GameGuessTheNumber(EngineGame):
    def play(self) -> None:
        print(f"Я загадал число в диапозоне от {self.min_num} до {self.max_num} . Попробуй отгадать его.")

        while True:
            print(f"Возможно ты загадал число: {self.get_random_num}?\n")
            enter_hint = input(f"Если я отгадал число поставь =. Если промахнулся дай подсказку используя знак > или <")
            if self.human_check_num(enter_hint):
                break
        print("Молодец получай электронную печеньку")


    def human_check_num(self, enter_hint):
        if enter_hint == '=':
            return True
        elif enter_hint == '>':
            self.min_num = int(self.get_random_num) + 1
            self.get_random_num = randint(self.min_num, self.max_num)
            return False
        elif enter_hint == '<':
            self.max_num = (self.get_random_num) - 1
            self.get_random_num = randint(self.min_num, self.max_num)
            return False
        else:
            print('Ты можешь выбрать только  < или > или =')
            return False



GameGuessTheNumber()




