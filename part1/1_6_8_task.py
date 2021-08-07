"""Реализуйте структуру данных, представляющую собой расширенную структуру стек.
 Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека,
  и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.

Операция сложения на стеке определяется следующим образом.
 Со стека снимается верхний элемент (top1), затем снимается следующий верхний элемент (top2),
  и затем как результат операции сложения на вершину стека кладется элемент, равный top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления
 (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.
Требуемая структура класса:

class ExtendedStack(list):
    def sum(self):
        # операция сложения

    def sub(self):
        # операция вычитания

    def mul(self):
        # операция умножения

    def div(self):
        # операция целочисленного деления

Примечание
Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop.
Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента."""


class ExtendedStack(list):
    list_with_stack_properties = []

    def __init__(self, name):
        self.list_with_stack_properties = name

    def sum(self):
        if len(self.list_with_stack_properties) > 2:
            a = self.list_with_stack_properties.pop()
            b = self.list_with_stack_properties.pop()
            self.list_with_stack_properties.append(a + b)

    def sub(self):
        if len(self.list_with_stack_properties) > 2:
            a = self.list_with_stack_properties.pop()
            b = self.list_with_stack_properties.pop()
            self.list_with_stack_properties.append(a - b)

    def mul(self):
        if len(self.list_with_stack_properties) > 2:
            a = self.list_with_stack_properties.pop()
            b = self.list_with_stack_properties.pop()
            self.list_with_stack_properties.append(a * b)

    def div(self):
        if len(self.list_with_stack_properties) > 2:
            a = self.list_with_stack_properties.pop()
            b = self.list_with_stack_properties.pop()
            self.list_with_stack_properties.append(a // b)

    def print_stack(self):
        print(self.list_with_stack_properties)



ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
ex_stack.print_stack()
print("--------------------------------------------")

ex_stack.div()
ex_stack.print_stack()

print("--------------------------------------------")
ex_stack.sub()
ex_stack.print_stack()

print("--------------------------------------------")
ex_stack.mul()
ex_stack.print_stack()

print("--------------------------------------------")
ex_stack.sum()
ex_stack.print_stack()
