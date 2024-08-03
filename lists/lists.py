class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list
        max_value = max(input_list)
        return [max_value if x > 0 else x for x in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:

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
