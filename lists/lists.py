class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        return [max(input_list) if i > 0 else i for i in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        low = 0
        high = len(input_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if input_list[mid] < query:
                low = mid + 1
            elif input_list[mid] > query:
                high = mid - 1
            else:
                return mid
        return -1
