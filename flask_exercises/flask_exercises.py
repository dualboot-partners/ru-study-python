from flask import Flask, request, jsonify


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.
    """

    users_db: dict = {}

    # FIXME: Так как все комментарии на русском, пишу на русском.
    """Базовая структура API обернута в класс, не смог придумать изящного способа,
    как передать self в методы класса. В связи с чем применил статический метод для каждой функции.
    Кроме того, users_db является глобальной переменной,
    а не определена в инициализацию класса по той же причине."""

    @staticmethod
    def create_user(users_db: dict = users_db) -> tuple:
        """POST /user - создание пользователя.
        В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
        Ответ должен вернуться так же в JSON в формате
        {"data": "User <имя пользователя> is created!"}
        со статусом 201.
        Если в теле запроса не было ключа "name", то в ответ возвращается JSON
        {"errors": {"name": "This field is required"}} со статусом 422"""

        try:
            user_data = request.get_json()
            new_user = user_data["name"]
            users_db[new_user] = {}
            response = {"data": f"User {new_user} is created!"}

            return jsonify(response), 201
        except KeyError:
            error_message = {"errors": {"name": "This field is required"}}

            return jsonify(error_message), 422

    @staticmethod
    def retrieve_user(username: str, users_db: dict = users_db) -> tuple:
        """GET /user/<name> - чтение пользователя
        В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200"""

        try:
            users_db[username]
            response = {"data": f"My name is {username}"}

            return jsonify(response), 200
        except KeyError:
            error_message = {"errors": {"name": f"{username} not exists"}}

            return jsonify(error_message), 404

    @staticmethod
    def update_user(username: str, users_db: dict = users_db) -> tuple:
        """PATCH /user/<name> - обновление пользователя
        В теле запроса приходит JSON в формате {"name": <new_name>}.
        В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200"""

        try:
            updated_data = request.get_json()
            old_name = username
            new_name = updated_data["name"]

            if new_name:
                users_db[old_name] = new_name
                response = {"data": f"My name is {new_name}"}

                return jsonify(response), 200
            else:
                error_message = {"errors": {"name": "New name is required"}}

                return jsonify(error_message), 422
        except KeyError:
            error_message = {"errors": {"name": f"{username} not exists"}}

            return jsonify(error_message), 404

    @staticmethod
    def delete_user(username: str, users_db: dict = users_db) -> tuple:
        """DELETE /user/<name> - удаление пользователя
        В ответ должен вернуться статус 204"""

        try:
            del users_db[username]

            return "", 204
        except KeyError:
            error_message = {"errors": {"name": f"{username} not exists"}}

            return jsonify(error_message), 404

    @staticmethod
    def configure_routes(app: Flask) -> None:
        app.add_url_rule(
            rule="/user",
            endpoint="create_user",
            view_func=FlaskExercise.create_user,
            methods=["POST"],
        )
        app.add_url_rule(
            rule="/user/<username>",
            endpoint="retrieve_user",
            view_func=FlaskExercise.retrieve_user,
            methods=["GET"],
        )
        app.add_url_rule(
            rule="/user/<username>",
            endpoint="update_user",
            view_func=FlaskExercise.update_user,
            methods=["PATCH"],
        )
        app.add_url_rule(
            rule="/user/<username>",
            endpoint="delete_user",
            view_func=FlaskExercise.delete_user,
            methods=["DELETE"],
        )
