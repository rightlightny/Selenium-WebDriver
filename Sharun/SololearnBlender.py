
# Вам дан класс Juice, который имеет свойства name и capacity.
# Вам необходимо завершить код, чтобы сложить два объекта Juice, которые в результате дадут новый объект Juice,
# объединяющий в себе свойства "name" и "capacity" тех двух, из которых он получен.
# Например, если совместить апельсиновый сок объемом 1.0 и яблочный 2.5, то в результате вы получите:
# имя: Orange&Apple
# объем: 3.5

# имена объединяются с использованием символа &.

# Используйте метод __add__ для определения поведения оператора + и выведите результат.

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        return Juice(self.name + "&" + other.name, self.capacity + other.capacity)

    def __str__(self):
        return self.name + ' (' + str(self.capacity) + 'L)'


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)