from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import cowsay

def main():
    r = Rectangle("синего", 4, 4)
    c = Circle("зеленого", 4)
    s = Square("красного", 4)
    print(r)
    print(c)
    print(s)
    cowsay.beavis("Парадигмы и конструкции языков программирования - это круто")
if __name__ == "__main__":
    main()