from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

class Todo:
    _id_counter = 1  # Class variable for ID generation

    def __init__(self, task):
        self.id = Todo._id_counter
        self.task = task
        self.completed = False
        Todo._id_counter += 1

# Sample data
todos = []

@app.route('/api/todos', methods=['GET', 'POST'])
def handle_todos():
    if request.method == 'GET':
        return jsonify(todos)

    elif request.method == 'POST':
        data = request.json
        if 'task' not in data:
            return jsonify({'error': 'Task is required'}), 400
        new_todo = Todo(task=data['task'])
        todos.append(new_todo.__dict__)
        return jsonify(new_todo.__dict__), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT', 'DELETE'])
def handle_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404

    if request.method == 'PUT':
        data = request.json
        if 'completed' not in data:
            return jsonify({'error': 'Completed status is required'}), 400
        todo['completed'] = data['completed']
        return jsonify(todo)

    elif request.method == 'DELETE':
        todos.remove(todo)
        return jsonify({'result': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
