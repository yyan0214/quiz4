from dataclasses import dataclass
@dataclass
class Fruit:
    name: str
    price: float
    origin: str

    def incre_price(self,num:float)->float:
        self.price += num


def main():
    fruits = [
        Fruit("apple",2,"US"),
        Fruit("coconut",4,"China"),
        Fruit("mango",2,"Canada")
    ]

    print(fruits[1])
    fruits[1].incre_price(1)
    print(f"The new price of the coconut is {fruits[1].price}")

    
if __name__=="__main__":
    main()