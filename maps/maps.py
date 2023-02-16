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
        movies_twomore_contries = filter(lambda x: "," in x["country"], list_of_movies)
        movies_twomore_rating = filter(
            lambda x: x["rating_kinopoisk"] not in ["", "0"], movies_twomore_contries
        )
        rating_list = [movie["rating_kinopoisk"] for movie in movies_twomore_rating]
        return sum(list(map(float, rating_list))) / len(rating_list)

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
        movies_filtred = [
            movie["name"]
            for movie in list_of_movies
            if (movie["rating_kinopoisk"] != "" and float(movie["rating_kinopoisk"]) >= rating)
        ]
        search_letter = "и"
        ressult_count_letter = list(map(lambda x: x.count(search_letter), movies_filtred))
        return sum(ressult_count_letter)
