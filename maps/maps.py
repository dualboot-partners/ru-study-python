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

        rating_kino = []
        for items in list_of_movies:
            if (len(items['country'].split(',')) >= 2 and
                    items['rating_kinopoisk'] not in ('0', '', '0.0', ' ', None)):
                rating_kino.append(items['rating_kinopoisk'])

        total_lists = list(map(float, rating_kino))
        total = 0.0
        for num in total_lists:
            total += num
        return total / len(total_lists)

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
        rating_films = filter(lambda item: item['rating_kinopoisk'] != '', list_of_movies)

        count_map = map(lambda movie:
                        movie['name'].count('и')
                        if float(movie['rating_kinopoisk']) >= rating else 0, rating_films)

        return sum(count_map)
