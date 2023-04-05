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

        if input_list:
            low = 0
            high = len(input_list) - 1

            if high == 0:
                mid = 0
            else:
                mid = len(input_list) // 2

            input_list.sort()

            while input_list[mid] != query and low <= high:
                if query > input_list[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                mid = (low + high) // 2
            
            if low > high:
                return -1
            else:
                return mid

        else:
            return -1
