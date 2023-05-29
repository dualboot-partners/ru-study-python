from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        if len(input_array) == 0:
            return input_array

        map_results = map(func, input_array)
        result = []
        for element in map_results:
            if element[0]:
                result.append(element[1])

        return result
