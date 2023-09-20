from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rating(movie: dict) -> float:
            country_count = len(movie["country"].split(","))
            return (
                float(movie["rating_kinopoisk"])
                if country_count >= 2 and movie["rating_kinopoisk"]
                else 0
            )

        rating_list = list(map(get_rating, list_of_movies))
        valid_rating = list(filter(lambda rating: rating > 0, rating_list))
        average_rating = sum(valid_rating) / len(valid_rating) if valid_rating else 0.0

        return average_rating

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

        def is_movie_valid(movie: dict) -> dict:
            return (
                movie
                if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating
                else None
            )

        def get_chars_count(movie_name: str) -> int:
            return movie_name.count("и")

        valid_movies = list(filter(None, map(is_movie_valid, list_of_movies)))
        movie_names = [movie_name["name"] for movie_name in valid_movies]
        list_of_chars = list(map(get_chars_count, movie_names))
        chars_count = sum(list_of_chars)

        return chars_count
