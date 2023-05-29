from flask import Flask, make_response, Response, request
from http import HTTPStatus
import json


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        users = {}
        @app.route("/user", methods=['POST'])
        def create_user() -> Response:
            data_string = request.get_data()
            data = json.loads(data_string)
            try:
                name = data['name']
                users[name] = data
                return make_response({"data": f"User {name} is created!"}, HTTPStatus.CREATED)
            except:
                return make_response({"errors": {"name": "This field is required"}}, HTTPStatus.UNPROCESSABLE_ENTITY)
                
        @app.route("/user/<username>", methods=['GET', 'PATCH', 'DELETE'])
        def user_actions(username) -> Response:
            if not username:
                return make_response('', HTTPStatus.NOT_FOUND)
            try:
                user = users[username]
            except:
                return make_response('', HTTPStatus.NOT_FOUND)
            
            match request.method:
                case 'GET':
                    user_name = user['name']
                    return make_response({"data": f"My name is {user_name}"}, HTTPStatus.OK)

                case 'PATCH':
                    data_string = request.get_data()
                    data = json.loads(data_string)
                    users[username] = data
                    new_user_name = users[username]['name']
                    return make_response({"data": f"My name is {new_user_name}"}, HTTPStatus.OK)
            
                case 'DELETE':
                    del users[username]
                    return make_response('', HTTPStatus.NO_CONTENT)
                