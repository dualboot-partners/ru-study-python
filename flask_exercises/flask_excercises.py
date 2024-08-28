from flask import Flask, request, jsonify


class FlaskExercise:

    @staticmethod
    def configure_routes(app: Flask) -> None:

        users = {}
        @app.route('/user', methods=['POST'])
        def create_user():
            data = request.json
            if 'name' not in data:
                return jsonify({"errors": {"name": "This field is required"}}), 422
            username = data['name']
            users[username] = {"age": data.get('age', None)}
            return jsonify({"data": f"User {username} is created!"}), 201

        @app.route('/user/<name>', methods=['GET'])
        def read_user(name):
            if name not in users:
                return jsonify({"errors": {"name": "User not found"}}), 404
            return jsonify({"data": f"My name is {name}"}), 200

        @app.route('/user/<name>', methods=['PATCH'])
        def update_user(name):
            if name not in users:
                return jsonify({"errors": {"name": "User not found"}}), 404
            data = request.json
            if 'name' not in data:
                return jsonify({"errors": {"name": "This field is required"}}), 422
            new_name = data['name']
            users[new_name] = users.pop(name)
            return jsonify({"data": f"My name is {new_name}"}), 200

        @app.route('/user/<name>', methods=['DELETE'])
        def delete_user(name):
            if name not in users:
                return jsonify({"errors": {"name": "User not found"}}), 404
            del users[name]
            return '', 204
