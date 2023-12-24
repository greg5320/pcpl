from classes import Computer, ComputerDisplay, Display


displays = [
    Display(1, 'Первый дисплей'),
    Display(2, 'Второй дисплей'),
    Display(3, 'Третий дисплей'),
]

computers = [
    Computer(1, 'Admin', 100000, 1),
    Computer(2, 'Hero', 60000, 1),
    Computer(3, 'CoolComputer', 75000, 2),
    Computer(4, 'MasterOfComputers', 80000, 2),
    Computer(5, 'PusherForever',167000, 2),
]

computerDisplays = [
    ComputerDisplay(1, 1),
    ComputerDisplay(1, 3),

    ComputerDisplay(2, 1),
    ComputerDisplay(2, 3),

    ComputerDisplay(3, 2),

    ComputerDisplay(4, 2),
    ComputerDisplay(4, 3),

    ComputerDisplay(5, 2),
]
