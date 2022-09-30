from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def check(movie: dict) -> float:
            import re

            movie["rating_kinopoisk"] = (
                float(movie["rating_kinopoisk"])
                if movie["rating_kinopoisk"] not in [None, ""]
                else None
            )
            movie["country"] = (
                len(re.split(",|, | ,", movie["country"]))
                if movie["country"] not in [None, ""]
                else 0
            )
            if (
                movie["rating_kinopoisk"] is not None
                and movie["rating_kinopoisk"] != 0
                and movie["country"] >= 2
            ):
                return movie["rating_kinopoisk"]
            else:
                return None

        temp = map(check, list_of_movies)
        list_valid_ratings = [item for item in temp if item is not None]
        div = len(list_valid_ratings)
        sum_ratings = 0.0

        for rating in list_valid_ratings:
            sum_ratings += rating

        return sum_ratings / div

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def check(movie: dict) -> str:
            movie["rating_kinopoisk"] = (
                float(movie["rating_kinopoisk"])
                if movie["rating_kinopoisk"] not in [None, ""]
                else None
            )
            if movie["rating_kinopoisk"] is not None and movie["rating_kinopoisk"] >= rating:
                return movie["name"]
            else:
                return None

        def my_count(name: str, symbol: str) -> int:
            count = 0
            for item in name:
                if item == symbol:
                    count += 1
            return count

        temp = map(check, list_of_movies)
        list_valid_names = [item for item in temp if item is not None]
        sum_symbols = 0
        for name in list_valid_names:
            sum_symbols += my_count(name, "и")
        return sum_symbols
