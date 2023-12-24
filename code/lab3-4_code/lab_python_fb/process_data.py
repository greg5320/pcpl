import json
from unique import Unique
from cm_timer import cm_timer_1
from field import field
from print_result import print_result
from gen_random import gen_random

path = "//lab3-4_code//data_light.json"

with open(path) as f:
    data = json.load(f)
    

def programmist_filter(data):
    return list(filter(lambda x: x.startswith("Программист"), data))

def unique_things(data):
    return list(Unique(field(data,"job-name")))

def add_python_exp(data):
    return list(map(lambda x: f"{x}, с опытом Python", data))

def add_salary(data):
    salaries = gen_random(2000,100000,200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(data, salaries)]



@print_result
def f1(arg):
    return unique_things(arg)


@print_result
def f2(arg):
    return programmist_filter(arg)


@print_result
def f3(arg):
    return add_python_exp(arg)


@print_result
def f4(arg):
    return add_salary(arg)


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
        
        
