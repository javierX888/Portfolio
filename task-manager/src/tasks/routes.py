from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from src.models import db, Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', endpoint='index')
@login_required
def index():
    return render_template('tasks/index.html')

@tasks_bp.route('/api/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed
    } for task in tasks])

@tasks_bp.route('/api/tasks/<int:id>', methods=['GET'])
@login_required
def get_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return jsonify({'error': 'No autorizado'}), 403
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed
    })

@tasks_bp.route('/api/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'El título es obligatorio'}), 400
    
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        user_id=current_user.id
    )
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'message': 'Tarea creada correctamente'
    }), 201

@tasks_bp.route('/api/tasks/<int:id>', methods=['PUT'])
@login_required
def update_task(id):
    task = Task.query.get_or_404(id)
    
    if task.user_id != current_user.id:
        return jsonify({'error': 'No autorizado'}), 403
    
    data = request.get_json()
    
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'completed' in data:
        task.completed = data['completed']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Tarea actualizada correctamente',
        'task': {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed
        }
    })

@tasks_bp.route('/api/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    
    if task.user_id != current_user.id:
        return jsonify({'error': 'No autorizado'}), 403
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Tarea eliminada correctamente'})