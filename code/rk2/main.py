from operator import itemgetter
from collections import Counter
from typing import Dict, List
import data
from classes import Computer, ComputerDisplay, Display
# Соединение данных один-ко-многим

def getOneToMany(displays: List[ComputerDisplay],computers: List[Computer]):
    return [(computer.name, computer.cost, display.name)
        for display in displays
        for computer in computers
        if computer.display_id == display.id]
                   

    # Соединение данных многие-ко-многим
def getManyToMany(displays: List[Display], computerDisplays: List[ComputerDisplay], computers: List[Computer]):
    manyToManyTemp = [(display.name, computerDisplay.display_id, computerDisplay.computer_id)
            for display in displays
            for computerDisplay in computerDisplays
            if display.id == computerDisplay.display_id]        
    return [(computer.id, computer.name, computer.cost, display_name)
                    for display_name, display_id, computer_id in manyToManyTemp
                    for computer in computers if computer.id == computer_id]    
              
def getDisplayForEachComputer(manyToMany, computers: List[Computer]):
    result: Dict[str, List[str]] = {}
    for computer in computers:
        displaysWithComputer = [m[3] for m in filter(lambda i: i[0] == computer.id, manyToMany)]
        result[computer.name] = displaysWithComputer
    return result

def getQuantityOfComputersInDisplays(displays: List[ComputerDisplay], computers: List[Computer]):
    displaysCounter = Counter([computer.display_id for computer in computers])
    return [(l.name, displaysCounter[l.id]) for l in computers]

def main():
    # «Дисплейный класс» и «Компьютер» связаны соотношением один-ко-многим.
    # Выведите список всех связанных компьютеров и дисплеев, отсортированный по названию компьютера,
    # сортировка по дисплеям произвольная.
    oneToMany = getOneToMany(data.displays, data.computers)

    # Соединение данных многие-ко-многим
    manyToMany = getManyToMany(data.displays, data.computerDisplays, data.computers)
    print('Задание Б1')
    resultA = sorted(oneToMany, key=itemgetter(0))
    print(resultA)

    # «Дисплей» и «Компьютер» связаны соотношением один-ко-многим.
    # Выведите список дисплеев с количеством комьютеров в каждом дисплее, отсортированный по количеству компьютеров.
    print('\nЗадание Б2')
    result_b_unsorted = getQuantityOfComputersInDisplays(data.displays, data.computers)
    print(sorted(result_b_unsorted, key=itemgetter(1), reverse=True))

    # «Дисплей» и «Компьютер связаны соотношением многие-ко-многим.
    # Выведите список всех компьютеров, у которых название заканчивается на «r», и названия их дисплеев.
    print('\nЗадание Б3')
    print(getDisplayForEachComputer(manyToMany, list(filter(lambda x: x.name.endswith('r'), data.computers))))


if __name__ == '__main__':
    main()