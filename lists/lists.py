class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        sorted_list = input_list.copy()
        sorted_list.sort()
        return [sorted_list[-1] if elem > 0 else elem for elem in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if len(input_list) == 0:
            return -1

        mid = len(input_list) // 2

        if input_list[mid] == query:
            return mid

        elif input_list[mid] > query:
            return ListExercise.search(input_list[:mid], query)

        else:
            x = ListExercise.search(input_list[mid + 1 :], query)
            if x == -1:
                return -1
            else:
                return x + mid + 1