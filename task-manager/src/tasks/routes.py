from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from flask_login import login_required, current_user
from src.models import db, Task
from datetime import datetime, timedelta
from sqlalchemy import or_, and_

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def home():
    """Ruta principal que redirecciona según autenticación"""
    if current_user.is_authenticated:
        return redirect(url_for('tasks.index'))
    return redirect(url_for('auth.login'))

@tasks_bp.route('/tasks', endpoint='index')
@login_required
def index():
    return render_template('tasks/index.html')

@tasks_bp.route('/api/tasks', methods=['GET'])
@login_required
def get_tasks():
    """Get all tasks for current user with optional filters"""
    # Get filter parameters
    status_filter = request.args.get('status', 'all')
    priority_filter = request.args.get('priority', 'all')
    category_filter = request.args.get('category', 'all')
    sort_by = request.args.get('sort_by', 'due_date')
    sort_order = request.args.get('sort_order', 'asc')
    
    # Build query
    query = Task.query.filter_by(user_id=current_user.id)
    
    # Apply filters
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    if priority_filter != 'all':
        query = query.filter_by(priority=int(priority_filter))
    
    if category_filter != 'all':
        query = query.filter_by(category=category_filter)
    
    # Apply sorting
    sort_column = getattr(Task, sort_by, Task.due_date)
    if sort_order == 'desc':
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())
    
    tasks = query.all()
    
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route('/api/tasks/<int:id>', methods=['GET'])
@login_required
def get_task(id):
    """Get a single task by ID"""
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return jsonify({'error': 'No autorizado'}), 403
    
    return jsonify(task.to_dict())

@tasks_bp.route('/api/tasks', methods=['POST'])
@login_required
def create_task():
    """Create a new task with enhanced fields"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'El título es obligatorio'}), 400
    
    try:
        # Parse dates if provided
        start_date = None
        due_date = None
        recurrence_end_date = None
        
        if data.get('start_date'):
            start_date = datetime.fromisoformat(data['start_date'].replace('Z', '+00:00'))
        
        if data.get('due_date'):
            due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
        
        if data.get('recurrence_end_date'):
            recurrence_end_date = datetime.fromisoformat(data['recurrence_end_date'].replace('Z', '+00:00'))
        
        # Auto-calculate due_date if start_date and estimated_time are provided
        estimated_time = data.get('estimated_time')
        if start_date and estimated_time and not due_date:
            due_date = start_date + timedelta(minutes=int(estimated_time))
        
        # Create task
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            priority=int(data.get('priority', 2)),
            status=data.get('status', 'pending'),
            category=data.get('category', 'personal'),
            start_date=start_date,
            due_date=due_date,
            estimated_time=estimated_time,
            is_recurring=data.get('is_recurring', False),
            recurrence_pattern=data.get('recurrence_pattern'),
            recurrence_end_date=recurrence_end_date,
            recurrence_days=data.get('recurrence_days'),
            user_id=current_user.id
        )
        
        db.session.add(task)
        db.session.commit()
        
        return jsonify({
            **task.to_dict(),
            'message': 'Tarea creada correctamente'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al crear tarea: {str(e)}'}), 500

@tasks_bp.route('/api/tasks/<int:id>', methods=['PUT'])
@login_required
def update_task(id):
    """Update an existing task"""
    task = Task.query.get_or_404(id)
    
    if task.user_id != current_user.id:
        return jsonify({'error': 'No autorizado'}), 403
    
    data = request.get_json()
    
    try:
        # Update basic fields
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'priority' in data:
            task.priority = int(data['priority'])
        if 'status' in data:
            task.status = data['status']
            # Set completed_at if marking as completed
            if data['status'] == 'completed' and not task.completed_at:
                task.completed_at = datetime.utcnow()
            elif data['status'] != 'completed':
                task.completed_at = None
        if 'category' in data:
            task.category = data['category']
        if 'completed' in data:
            task.completed = data['completed']
            if data['completed']:
                task.status = 'completed'
                task.completed_at = datetime.utcnow()
            else:
                task.status = 'pending'
                task.completed_at = None
        
        # Update dates
        if 'start_date' in data:
            task.start_date = datetime.fromisoformat(data['start_date'].replace('Z', '+00:00')) if data['start_date'] else None
        if 'due_date' in data:
            task.due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00')) if data['due_date'] else None
        
        # Update time tracking
        if 'estimated_time' in data:
            task.estimated_time = data['estimated_time']
        
        # Auto-calculate due_date if start_date and estimated_time changed
        if task.start_date and task.estimated_time:
            task.due_date = task.start_date + timedelta(minutes=int(task.estimated_time))
        
        # Update recurrence
        if 'is_recurring' in data:
            task.is_recurring = data['is_recurring']
        if 'recurrence_pattern' in data:
            task.recurrence_pattern = data['recurrence_pattern']
        if 'recurrence_end_date' in data:
            task.recurrence_end_date = datetime.fromisoformat(data['recurrence_end_date'].replace('Z', '+00:00')) if data['recurrence_end_date'] else None
        if 'recurrence_days' in data:
            task.recurrence_days = data['recurrence_days']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Tarea actualizada correctamente',
            'task': task.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al actualizar tarea: {str(e)}'}), 500

@tasks_bp.route('/api/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):
    """Delete a task"""
    task = Task.query.get_or_404(id)
    
    if task.user_id != current_user.id:
        return jsonify({'error': 'No autorizado'}), 403
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Tarea eliminada correctamente'})

@tasks_bp.route('/api/tasks/stats', methods=['GET'])
@login_required
def get_stats():
    """Get task statistics for current user"""
    total = Task.query.filter_by(user_id=current_user.id).count()
    completed = Task.query.filter_by(user_id=current_user.id, status='completed').count()
    pending = Task.query.filter_by(user_id=current_user.id, status='pending').count()
    in_progress = Task.query.filter_by(user_id=current_user.id, status='in_progress').count()
    
    # Overdue tasks
    overdue = Task.query.filter(
        Task.user_id == current_user.id,
        Task.status != 'completed',
        Task.due_date < datetime.utcnow()
    ).count()
    
    # Tasks by priority
    urgent = Task.query.filter_by(user_id=current_user.id, priority=4).count()
    high = Task.query.filter_by(user_id=current_user.id, priority=3).count()
    medium = Task.query.filter_by(user_id=current_user.id, priority=2).count()
    low = Task.query.filter_by(user_id=current_user.id, priority=1).count()
    
    return jsonify({
        'total': total,
        'completed': completed,
        'pending': pending,
        'in_progress': in_progress,
        'overdue': overdue,
        'by_priority': {
            'urgent': urgent,
            'high': high,
            'medium': medium,
            'low': low
        }
    })