from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        db = {}

        def view(user=None):
            if request.method == "POST":
                json_data = request.get_json(force=True)
                name = json_data.get("name", "")
                if not name:
                    return {"errors": {"name": "This field is required"}}, 422
                db[name] = {}
                return {"data": f"User {name} is created!"}, 201
            elif request.method == "GET":
                if not user in db:
                    return {}, 404
                return {"data": f"My name is {user}"}, 200
            elif request.method == "PATCH":
                json_data = request.get_json(force=True)
                name = json_data.get("name")
                return {"data": f"My name is {name}"}, 200
            elif request.method == "DELETE":
                if not user in db:
                    return "", 404
                db.pop(user)
                return "", 204

        app.add_url_rule("/user", view_func=view, methods=["POST"])
        app.add_url_rule("/user/<user>", view_func=view, methods=["GET", "PATCH", "DELETE"])