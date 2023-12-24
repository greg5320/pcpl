import unittest
import data
from main import getOneToMany, getManyToMany, getQuantityOfComputersInDisplays, getDisplayForEachComputer


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.data = data

    def testGetOneToMany(self):
        want = [('Admin', 100000, 'Первый дисплей'), ('Hero', 60000, 'Первый дисплей'),
                 ('CoolComputer', 75000, 'Второй дисплей'), ('MasterOfComputers', 80000, 'Второй дисплей'),
                   ('PusherForever', 167000, 'Второй дисплей')]
        actual = getOneToMany(self.data.displays, self.data.computers)

        self.assertCountEqual(want, actual)

    def testGetManyToMany(self):
        want = [(1, 'Admin', 100000, 'Первый дисплей'), (2, 'Hero', 60000, 'Первый дисплей'),
                 (3, 'CoolComputer', 75000, 'Второй дисплей'), (4, 'MasterOfComputers', 80000, 'Второй дисплей'),
                   (5, 'PusherForever', 167000, 'Второй дисплей'), (1, 'Admin', 100000, 'Третий дисплей'),
                     (2, 'Hero', 60000, 'Третий дисплей'), (4, 'MasterOfComputers', 80000, 'Третий дисплей')]

        actual = getManyToMany(self.data.displays, self.data.computerDisplays, self.data.computers)

        self.assertCountEqual(want, actual)

    def testGetQuantityOfComputersInDisplays(self):
        want = [('Admin', 2), ('Hero', 3), ('CoolComputer', 0), ('MasterOfComputers', 0), ('PusherForever', 0)]
        actual = getQuantityOfComputersInDisplays(self.data.displays, self.data.computers)

        self.assertCountEqual(want, actual)

    def testGetDisplayForEachComputer(self):
        manyToMany = getManyToMany(self.data.displays, self.data.computerDisplays, self.data.computers)
        want = {'Admin': ['Первый дисплей', 'Третий дисплей'], 'Hero': ['Первый дисплей', 'Третий дисплей'],
                 'CoolComputer': ['Второй дисплей'],
                   'MasterOfComputers': ['Второй дисплей', 'Третий дисплей'], 'PusherForever': ['Второй дисплей']}
        actual = getDisplayForEachComputer(manyToMany, self.data.computers)

        self.assertDictEqual(want, actual)