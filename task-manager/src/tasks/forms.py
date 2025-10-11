from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeLocalField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, NumberRange, Length

class TaskForm(FlaskForm):
    """Enhanced Task Form with all new fields"""
    
    # Basic info
    title = StringField('Título', validators=[
        DataRequired(message='El título es obligatorio'),
        Length(max=100, message='El título no puede exceder 100 caracteres')
    ])
    
    description = TextAreaField('Descripción', validators=[
        Optional(),
        Length(max=500, message='La descripción no puede exceder 500 caracteres')
    ])
    
    # Priority and Status
    priority = SelectField('Prioridad', 
        choices=[
            ('1', 'Baja'),
            ('2', 'Media'),
            ('3', 'Alta'),
            ('4', 'Urgente')
        ],
        default='2',
        coerce=str
    )
    
    status = SelectField('Estado',
        choices=[
            ('pending', 'Pendiente'),
            ('in_progress', 'En Progreso'),
            ('completed', 'Completada'),
            ('cancelled', 'Cancelada')
        ],
        default='pending'
    )
    
    # Category
    category = SelectField('Categoría',
        choices=[
            ('personal', 'Personal'),
            ('work', 'Trabajo'),
            ('study', 'Estudio'),
            ('health', 'Salud'),
            ('shopping', 'Compras'),
            ('other', 'Otra')
        ],
        default='personal'
    )
    
    # Dates
    start_date = DateTimeLocalField('Fecha de Inicio', 
        format='%Y-%m-%dT%H:%M',
        validators=[Optional()]
    )
    
    due_date = DateTimeLocalField('Fecha de Vencimiento',
        format='%Y-%m-%dT%H:%M',
        validators=[Optional()]
    )
    
    # Time estimation
    estimated_time = IntegerField('Tiempo Estimado (minutos)',
        validators=[
            Optional(),
            NumberRange(min=1, max=10080, message='El tiempo debe estar entre 1 minuto y 1 semana')
        ]
    )
    
    # Recurrence
    is_recurring = BooleanField('Tarea Recurrente')
    
    recurrence_pattern = SelectField('Patrón de Repetición',
        choices=[
            ('', 'No se repite'),
            ('daily', 'Diaria'),
            ('weekly', 'Semanal'),
            ('monthly', 'Mensual')
        ],
        default='',
        validators=[Optional()]
    )
    
    recurrence_end_date = DateTimeLocalField('Repetir Hasta',
        format='%Y-%m-%dT%H:%M',
        validators=[Optional()]
    )
    
    # For weekly recurrence: days of week
    recurrence_days = StringField('Días de la Semana',
        validators=[Optional()]
    )


class TaskFilterForm(FlaskForm):
    """Form for filtering and sorting tasks"""
    
    status_filter = SelectField('Filtrar por Estado',
        choices=[
            ('all', 'Todos'),
            ('pending', 'Pendientes'),
            ('in_progress', 'En Progreso'),
            ('completed', 'Completadas'),
            ('cancelled', 'Canceladas')
        ],
        default='all'
    )
    
    priority_filter = SelectField('Filtrar por Prioridad',
        choices=[
            ('all', 'Todas'),
            ('4', 'Urgente'),
            ('3', 'Alta'),
            ('2', 'Media'),
            ('1', 'Baja')
        ],
        default='all'
    )
    
    category_filter = SelectField('Filtrar por Categoría',
        choices=[
            ('all', 'Todas'),
            ('personal', 'Personal'),
            ('work', 'Trabajo'),
            ('study', 'Estudio'),
            ('health', 'Salud'),
            ('shopping', 'Compras'),
            ('other', 'Otra')
        ],
        default='all'
    )
    
    sort_by = SelectField('Ordenar por',
        choices=[
            ('due_date', 'Fecha de Vencimiento'),
            ('priority', 'Prioridad'),
            ('created_at', 'Fecha de Creación'),
            ('title', 'Título')
        ],
        default='due_date'
    )
    
    sort_order = SelectField('Orden',
        choices=[
            ('asc', 'Ascendente'),
            ('desc', 'Descendente')
        ],
        default='asc'
    )
