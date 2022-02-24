
from main import EngineGame


class HumanGuessTheNumber(EngineGame):
    def play(self) -> None:
        print(f"Я загадал число в диапозоне от {self.min_num} до {self.max_num} . Попробуй отгадать его.")

        while True:
            enter_hint = input(f"Может быть это число {self.get_random_num}?\n")
            if self.human_check_num(enter_hint):
                break

        print('Молодец получай электронную печеньку')


HumanGuessTheNumber()




