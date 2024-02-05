from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort
from .models import Task
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('kanban.html', tasks=tasks)


@main.route('/add-task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='todo')
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/update-task-status/<int:task_id>/<string:new_status>', methods=['POST'])
def update_task_status(task_id, new_status):
    if new_status not in ['todo', 'in-progress', 'done']:
        abort(400, description="Invalid status")

    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    try:
        task.status = new_status
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@main.route('/delete-task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500