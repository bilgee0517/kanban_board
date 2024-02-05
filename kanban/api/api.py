from flask import Flask, jsonify, request


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    status = db.Column(db.String(20), nullable=False, default='todo')

    def __repr__(self):
        return f'<Task {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()




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
    },

    {
        'id': 3,
        'title': 'Task 3',
        'description': 'Description of Task 3',
        'status': 'done'
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
    new_task['id'] = len(tasks) + 1  # Simple way to generate a unique ID
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