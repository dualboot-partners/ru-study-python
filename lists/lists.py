class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        max_item = 0
        result = []
        for i in range(0, len(input_list)):
            if input_list[i] > max_item:
                max_item = input_list[i]
        for i in range(len(input_list)):
            if input_list[i] > 0:
                result.append(max_item)
            else:
                result.append(input_list[i])
        return result

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        if input_list == []:
            return -1
        start = 0
        end = len(input_list) - 1
        mid = len(input_list) // 2
        while input_list[mid] != query and start <= end:
            if query > input_list[mid]:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) // 2
        if end < start:
            return -1
        else:
            return mid
