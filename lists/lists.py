class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if len(input_list) == 0:
            return input_list

        max_value = max(input_list)

        return list(map(lambda element: element if element < 0 else max_value, input_list))

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        start_index = 0
        end_index = len(input_list)
        search_list = input_list
        while len(search_list) > 0:
            middle_index = (end_index + start_index) // 2
            if input_list[middle_index] == query:
                return middle_index
            if input_list[middle_index] > query:
                end_index = middle_index
            else:
                start_index = middle_index + 1
            search_list = input_list[start_index:end_index]

        return -1
