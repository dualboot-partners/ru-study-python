class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        out_list = []

        for elem in input_list:
            if elem > 0:
                out_list.append(max(input_list))
            else:
                out_list.append(elem)

        return out_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        pass

a = ListExercise()

print(a.replace([3, 2, -8, 4, 100, -6, 7, 8, -99]))