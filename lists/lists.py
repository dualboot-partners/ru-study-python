class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        if not input_list:
            return []

        max_value = max(input_list)
        final_list = [max_value if x > 0 else x for x in input_list]

        return final_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        left, right = 0, len(input_list) - 1

        while left <= right:
            mid = (left + right) // 2

            if input_list[mid] == query:
                return mid
            elif input_list[mid] < query:
                left = mid + 1
            else:
                right = mid - 1

        return -1
