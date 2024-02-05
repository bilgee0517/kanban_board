from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description of Task 1',
        'status': 'todo'
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description of Task 2',
        'status': 'in-progress'
    }
    # Add more tasks as needed
]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404


@app.route('/task', methods=['POST'])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task.update(request.json)
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'})