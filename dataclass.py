from dataclasses import dataclass

@dataclass
class Fruit:
    name: str
    price: float
    origin: str


def main():
    fruits = [
        Fruit("apple",2,"US"),
        Fruit("coconut",4,"China"),
        Fruit("mango",2,"Canada")
    ]

    print(fruits[1])
    print("The apples are from", fruits[0].origin)
    
if __name__=="__main__":
    main()