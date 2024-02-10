class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        def find_max(input_list: list[int]) -> int:
            max_so_far = float("-inf")
            for num in input_list:
                if num > max_so_far:
                    max_so_far = num
            return max_so_far

        def replace_list(input_list: list[int]) -> list[int]:
            maximum = find_max(input_list)
            for index, num in enumerate(input_list):
                if num < maximum and num > 0:
                    input_list[index] = maximum
            return input_list

        return replace_list(input_list)

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def recursive(input_list: list[int], query: int, lo=0, hi=None):
            if hi is None:
                hi = len(input_list) - 1
            if lo > hi:
                return -1

            mid = (lo + hi) // 2
            aux = input_list[mid]

            if aux == query:
                return mid
            if aux > query:
                return recursive(input_list, query, lo, mid - 1)
            return recursive(input_list, query, mid + 1, hi)

        return recursive(input_list, query)
