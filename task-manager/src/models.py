from src import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    full_name = db.Column(db.String(100))
    profile_picture = db.Column(db.Text, default='https://ui-avatars.com/api/?name=User&background=007bff&color=fff')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_display_name(self):
        return self.full_name if self.full_name else self.username

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    
    # Priority: 1=Baja, 2=Media, 3=Alta, 4=Urgente
    priority = db.Column(db.Integer, default=2)
    
    # Status: pending, in_progress, completed, cancelled
    status = db.Column(db.String(20), default='pending')
    
    # Category
    category = db.Column(db.String(50), default='personal')
    
    # Dates
    start_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Time tracking
    estimated_time = db.Column(db.Integer)  # in minutes
    
    # Recurrence
    is_recurring = db.Column(db.Boolean, default=False)
    recurrence_pattern = db.Column(db.String(20))  # daily, weekly, monthly, custom
    recurrence_end_date = db.Column(db.DateTime)
    recurrence_days = db.Column(db.String(50))  # For weekly: "1,3,5" (Mon, Wed, Fri)
    
    # Relations
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def to_dict(self):
        """Convert task to dictionary for JSON responses"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'priority': self.priority,
            'status': self.status,
            'category': self.category,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'estimated_time': self.estimated_time,
            'is_recurring': self.is_recurring,
            'recurrence_pattern': self.recurrence_pattern,
            'recurrence_end_date': self.recurrence_end_date.isoformat() if self.recurrence_end_date else None,
            'recurrence_days': self.recurrence_days,
            'user_id': self.user_id
        }
    
    def get_priority_label(self):
        """Get priority label"""
        labels = {1: 'Baja', 2: 'Media', 3: 'Alta', 4: 'Urgente'}
        return labels.get(self.priority, 'Media')
    
    def get_priority_color(self):
        """Get priority color class"""
        colors = {1: 'success', 2: 'info', 3: 'warning', 4: 'danger'}
        return colors.get(self.priority, 'info')
    
    def get_status_label(self):
        """Get status label in Spanish"""
        labels = {
            'pending': 'Pendiente',
            'in_progress': 'En Progreso',
            'completed': 'Completada',
            'cancelled': 'Cancelada'
        }
        return labels.get(self.status, 'Pendiente')
    
    def get_status_color(self):
        """Get status color class"""
        colors = {
            'pending': 'secondary',
            'in_progress': 'primary',
            'completed': 'success',
            'cancelled': 'dark'
        }
        return colors.get(self.status, 'secondary')
    
    def is_overdue(self):
        """Check if task is overdue"""
        if self.due_date and not self.completed:
            return datetime.utcnow() > self.due_date
        return False
    
    def calculate_due_date(self):
        """Calculate due date from start date and estimated time"""
        if self.start_date and self.estimated_time:
            from datetime import timedelta
            return self.start_date + timedelta(minutes=self.estimated_time)
        return None