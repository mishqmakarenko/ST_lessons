from main import EngineGame

class GameGuessTheNumber(EngineGame):
    def play(self):
        random_num = self.get_random_num

        print(f"Угадай число в диапазоне от {self.min_num} до {self.max_num}")

        # игровая механика
        while True:
            try:
                guess = int(input("Попробуй угадать число: "))
            except ValueError:
                print(' написано попробуй угадать число, а ты что вводишь!!!!')
                continue

            if self.game_check_num(random_num, guess):
                break


GameGuessTheNumber()