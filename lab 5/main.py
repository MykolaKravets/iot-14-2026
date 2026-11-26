import random
from enum import Enum
from functools import wraps

def frame(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"{method.__name__}")
        return method(self, *args, **kwargs)
    return wrapper

class Taste(Enum):
    SWEET = 'солодкий'
    SOUR = 'кислий'
    NEUTRAL = 'нейтральний'


class Fruit:
    def __init__(self, name, size, color, taste):
        self.name = name
        self.size = size
        self.color = color
        self.taste = taste

    def __str__(self):
        return f'name: {self.name}  size: {self.size}  color: {self.color}  taste: {self.taste.value}'


class Topping(Enum):
    HONEY = ('мед', Taste.SWEET)
    CHOCOLATE = ('шоколад', Taste.SWEET)
    YOGURT = ('йогурт', Taste.SOUR)
    LEMON_JUICE = ('лимонний сік', Taste.SOUR)
    CREAM = ('вершки', Taste.NEUTRAL)

    def __init__(self, title, taste):
        self.title = title
        self.taste = taste

    def __str__(self):
        return f'{self.title} ({self.taste.value})'


class Apple(Fruit):   
    def __init__(self, name, size, color, taste, size_2):
        super().__init__(name, size, color, taste)
        self.size_2 = size_2e_2 = size_2

    def __str__(self):
        return super().__str__()

class FruitSalad:
    def __init__(self, name, fruits=None, topping=None):
        self.name = name
        self.fruits = list(fruits) if fruits is not None else []        
        self.topping = topping

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def dominant_taste(self):
        if len(self.fruits) == 0:
            return None

        sweet = 0
        sour = 0
        neutral = 0

        for fruit in self.fruits:
            if fruit.taste == Taste.SWEET:
                sweet += 1
            elif fruit.taste == Taste.SOUR:
                sour += 1
            else:
                neutral += 1

        if sweet > sour and sweet > neutral:
            return Taste.SWEET
        elif sour > sweet and sour > neutral:
            return Taste.SOUR
        else:
            return Taste.NEUTRAL   

    def choose_topping(self):
        taste = self.dominant_taste()

        if taste is None:
            print('Салат порожній, топінг не потрібен')
            return None

        if taste == Taste.SOUR:
            options = [Topping.HONEY, Topping.CHOCOLATE]
        elif taste == Taste.SWEET:
            options = [Topping.YOGURT, Topping.LEMON_JUICE]
        else:
            options = [Topping.CREAM]

        self.topping = random.choice(options)
        return self.topping
    
    @staticmethod                      
    def toppings_for(taste):           
        if taste == Taste.SOUR:
            return [Topping.HONEY, Topping.CHOCOLATE]
        elif taste == Taste.SWEET:
            return [Topping.YOGURT, Topping.LEMON_JUICE]
        else:
            return [Topping.CREAM]
    
    
    
    def mix(self):
        random.shuffle(self.fruits)

    def __str__(self):
        lines = [f'Салат "{self.name}":']
        for fruit in self.fruits:
            lines.append(f'{fruit}')
        lines.append(f'  Топінг: {self.topping if self.topping else "не вибрано"}')
        return '\n'.join(lines)


if __name__ == '__main__':
    apple = Fruit('яблуко', 'середній', 'зелений', Taste.SOUR)
    lemon = Fruit('лимон', 'малий', 'жовтий', Taste.SOUR)
    kiwi = Fruit('ківі', 'малий', 'зелений', Taste.SOUR)
    banana = Fruit('банан', 'великий', 'жовтий', Taste.SWEET)
    mango = Fruit('манго', 'великий', 'помаранчевий', Taste.SWEET)
    avocado = Fruit('авокадо', 'середній', 'зелений', Taste.NEUTRAL)

    salad = FruitSalad('Кислинка')
    for fruit in (apple, lemon, kiwi, banana):
        salad.add_fruit(fruit)

    print(salad)
    print()

    print('Переважний смак:', salad.dominant_taste().value)
    print('Вибраний топінг:', salad.choose_topping())
    print()
    print(FruitSalad.toppings_for(Taste.SOUR))

    salad.mix()
    print('Після перемішування:')
    print(salad)
    print()

    sweet_salad = FruitSalad('Солодкий', [banana, mango, avocado])
    sweet_salad.choose_topping()
    print(sweet_salad)