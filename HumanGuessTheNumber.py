from main import EngineGame

class HumanGuessTheNumber(EngineGame):
    def play(self):
        random_num = self.get_random_num

        print(f"Угадай число в диапазоне от {self.min_num} до {self.max_num}")

        # игровая механика
        while True:
            try:
                guess = int(input("Попробуй угадать число: "))
            except ValueError:
                print("Написано попробуй угадать число, а ты что вводишь!!!!")
                continue

            if self.game_check_num(random_num, guess):
                break


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


HumanGuessTheNumber()