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


    def __del__(self):
        print('Если хочешь еще сыграть, начинай игру!')



