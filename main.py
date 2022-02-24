from random import randint


class EngineGame:
    def __init__(self):
        self.min_num = 1
        self.max_num = self.select_level_difficulties()
        self.get_random_num = randint(self.min_num, self.max_num)
        self.play()

    def select_level_difficulties(self):
        while True:
            try:
                maxNum = int(input("Введи максимальное число диапазона:"))
            except ValueError:
                print('Написанно число, а ты что вводишь!!!!!')
                continue
            return maxNum

    def game_check_num(self, random_num, guess):
        if guess == random_num:
            print(f"верное число {random_num}")
            return True
        elif guess < random_num:
            print("Твое число меньше загаданного")
            return False
        else:
            print("Твое число больше загаданного")
            return False

    def __del__(self):
        print('Если хочешь еще сыграть, начинай игру!')


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


