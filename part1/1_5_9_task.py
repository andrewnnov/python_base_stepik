class Buffer:

    def __init__(self):
        # конструктор без аргументов
        self.new_list = []

    def add(self, *a):
        # добавить следующую часть последовательности
        list_from_arg = list(a)
        for el in list(list_from_arg):
            if len(self.new_list) < 6:
                self.new_list.append(el)
            if len(self.new_list) == 5:
                sum = 0
                for elem_in_list in self.new_list:
                    sum += elem_in_list
                print(sum)
                self.new_list = []


    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        print(self.new_list)



buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]