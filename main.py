import random


class GuessNumberGame:
    def __init__(self):
        self.min_num = 1
        self.easy_level = 10
        self.medium_level = 20


    # метод начала игры
    def play(self):
        input_level = int(input("Выберите уровень сложности игры, где 1-easy, 2 - medium :"))
        level_game = self.select_level_difficulties(input_level)
        random_num = self.get_random_num(level_game)

        print(f"Угадай число в диапазоне от {self.min_num } до {level_game}")

        # игровая механика
        while True:
            try:
                guess = int(input("Введи число: "))
            except ValueError:
                print(' Неверное значение, попробуй снова.')
                continue

            if self.check_number(random_num, guess):
                break


    def get_random_num(self, level_game):
        return random.randint(self.min_num, level_game)


    def select_level_difficulties(self, input_level):
        if input_level == 1:
            select_level = self.easy_level
        elif input_level == 2:
            select_level = self.medium_level
        return select_level


    def check_number(self, random_num, guess):
        if guess == random_num:
            print(f"верное число {random_num}")
            return True
        elif guess < random_num:
            print("Твое число меньше загаданного")
            return False
        else:
            print("Твое число больше загаданного")
            return False


GuessNumberGame().play()