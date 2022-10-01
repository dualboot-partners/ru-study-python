class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Replaces positive elements in the list by max element.
        :param input_list: Input list
        :return: Replaced list
        """
        if len(input_list) < 2:
            return input_list

        max_element = ListExercise.__get_max(input_list)
        replaced_list = input_list[:]

        for index, element in enumerate(input_list):
            if element > 0:
                replaced_list[index] = max_element

        return replaced_list

    @staticmethod
    def __get_max(input_list: list[int]) -> int:
        """
        Returns the item with the highest value in the list.
        :param input_list: Input list
        :return: Max element
        """
        max_element = input_list[0]

        for element in input_list:
            if element > max_element:
                max_element = element

        return max_element

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Returns the index of searched element using binary search.
        If element not in a list returns -1.
        :param input_list: Input list
        :param query: Searched element
        :return: Index of searched element
        """
        sorted_list = sorted(input_list)
        low = 0
        high = len(sorted_list) - 1

        searched_index = ListExercise.__binary_search(sorted_list, query, low, high)

        return searched_index

    @staticmethod
    def __binary_search(sorted_list: list[int], query: int, low: int, high: int) -> int:
        """
        Returns the index of searched element using recursive binary search.
        If element not in a list returns -1.
        :param sorted_list: Sorted list
        :param query: Searched element
        :low: Lowest pointer
        :high: Highest pointer
        :return: Index of searched element
        """
        if high >= low:

            mid = (high + low) // 2
            if sorted_list[mid] == query:
                return mid

            elif sorted_list[mid] > query:
                return ListExercise.__binary_search(sorted_list, query, low, mid - 1)

            else:
                return ListExercise.__binary_search(sorted_list, query, mid + 1, high)

        else:
            return -1
