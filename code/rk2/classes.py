class Computer:
    """ Класс компьютер"""

    def __init__(self, id_: int, name: str, cost: int, display_id: int):
        self.id = id_
        self.name = name
        self.cost = cost
        self.display_id = display_id


class Display:
    """Дисплейный класс"""

    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name


class ComputerDisplay:
    """
    'Компьютеры дисплейного класса' для реализации
    связи многие-ко-многим
    """

    def __init__(self, computer_id: int, display_id: int):
        self.computer_id = computer_id
        self.display_id = display_id