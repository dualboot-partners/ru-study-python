from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        if not list_of_movies:
            raise ValueError("List is empty")
        key, rating = "country", "rating_kinopoisk"
        filtered = list(
            filter(
                lambda sub: "," in (sub[key])
                and not not (sub[rating])
                and not (sub[rating]) == "0",
                list_of_movies,
            )
        )
        ratings = list(map(lambda sub: float((sub[rating])), filtered))
        average = sum(ratings) / len(ratings)
        return average

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        if not list_of_movies or not rating:
            raise ValueError("List or rating is empty")
        set_rating, key, count_key, letter = rating, "rating_kinopoisk", "name", "и"
        filtered = list(
            filter(lambda sub: not not (sub[key]) and not (sub[key]) == "0", list_of_movies)
        )
        ranged = list(filter(lambda sub: float((sub[key])) >= set_rating, filtered))
        names = list(map(lambda sub: (sub[count_key]), ranged))
        count = list(map(lambda sub: (sub.count(letter)), names))
        sum_up = sum(count)
        return sum_up
