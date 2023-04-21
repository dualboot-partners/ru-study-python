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
        max_elem = 0

        for elem in input_list:
            if elem > max_elem:
                max_elem = elem

        for elem in input_list:
            if elem > 0:
                out_list.append(max_elem)
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

        start = 0
        end = len(input_list) - 1
        
        while start <= end:
            mid_pos = (start + end) // 2
            
            if query == input_list[mid_pos]:
                return mid_pos

            if query > input_list[mid_pos]:
                start = mid_pos + 1
                ListExercise.search(input_list[start:], query)
                
            if query < input_list[mid_pos]:
                end = mid_pos - 1
                ListExercise.search(input_list[start:end], query)
            
        return -1
