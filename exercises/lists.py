class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        len_list = len(input_list)
        output_list: list[int]
        output_list = list()

        if len_list == 0:
            return output_list

        max_value = input_list[0]
        for item in input_list:
            if item > max_value:
                max_value = item

        for elem in range(len_list):
            if input_list[elem] > 0:
                output_list.append(max_value)
            else:
                output_list.append(input_list[elem])
        return output_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def helper(start: int, end: int) -> int:
            mid = (end + start) // 2
            if start > end:
                return -1
            elif input_list[mid] < query:
                return helper(mid + 1, end)
            elif input_list[mid] > query:
                return helper(start, mid - 1)
            else:
                return mid

        return helper(0, len(input_list) - 1)
