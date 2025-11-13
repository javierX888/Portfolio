document.addEventListener('DOMContentLoaded', () => {
    const tasksContainer = document.getElementById('tasks-container');
    const taskForm = document.getElementById('taskForm');
    const taskModal = new bootstrap.Modal(document.getElementById('taskModal'));
    
    // Cargar tareas y estadísticas al iniciar
    loadTasks();
    loadStats();
    
    // Event listeners para calcular fecha de vencimiento automáticamente
    const startDateInput = document.getElementById('taskStartDate');
    const startTimeInput = document.getElementById('taskStartTime');
    const estimatedTimeInput = document.getElementById('taskEstimatedTime');
    const dueDateDisplay = document.getElementById('taskDueDate');
    
    [startDateInput, startTimeInput, estimatedTimeInput].forEach(input => {
        input.addEventListener('change', calculateAndDisplayDueDate);
        input.addEventListener('input', calculateAndDisplayDueDate);
    });
    
    function calculateAndDisplayDueDate() {
        const startDate = startDateInput.value;
        const startTime = startTimeInput.value;
        const estimatedMinutes = parseInt(estimatedTimeInput.value);
        
        if (startDate && startTime && estimatedMinutes > 0) {
            const startDateTime = new Date(`${startDate}T${startTime}`);
            const dueDateTime = new Date(startDateTime.getTime() + estimatedMinutes * 60000);
            
            // Formatear para mostrar en el campo readonly
            const formattedDueDate = dueDateTime.toLocaleString('es-ES', {
                year: 'numeric',
                month: 'short',
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit'
            });
            
            dueDateDisplay.value = formattedDueDate;
        } else {
            dueDateDisplay.value = '';
        }
    }
    
    // Manejar envío del formulario
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const taskId = document.getElementById('taskId').value;
        
        // Combinar fecha y hora de inicio
        const startDate = document.getElementById('taskStartDate').value;
        const startTime = document.getElementById('taskStartTime').value;
        const startDateTime = startDate && startTime ? `${startDate}T${startTime}` : null;
        
        // Combinar fecha y hora de recurrencia
        const recurrenceEndDate = document.getElementById('taskRecurrenceEndDate').value;
        const recurrenceEndTime = document.getElementById('taskRecurrenceEndTime').value;
        const recurrenceEndDateTime = recurrenceEndDate && recurrenceEndTime ? `${recurrenceEndDate}T${recurrenceEndTime}` : (recurrenceEndDate ? `${recurrenceEndDate}T00:00` : null);
        
        // Recopilar todos los datos del formulario
        const taskData = {
            title: document.getElementById('taskTitle').value,
            description: document.getElementById('taskDescription').value,
            priority: parseInt(document.getElementById('taskPriority').value),
            status: document.getElementById('taskStatus').value,
            category: document.getElementById('taskCategory').value,
            start_date: startDateTime,
            estimated_time: document.getElementById('taskEstimatedTime').value ? parseInt(document.getElementById('taskEstimatedTime').value) : null,
            is_recurring: document.getElementById('taskIsRecurring').checked,
            recurrence_pattern: document.getElementById('taskIsRecurring').checked ? document.getElementById('taskRecurrencePattern').value : null,
            recurrence_end_date: recurrenceEndDateTime
        };
        
        try {
            const url = taskId ? `/api/tasks/${taskId}` : '/api/tasks';
            const method = taskId ? 'PUT' : 'POST';
            
            const response = await fetch(url, {
                method: method,
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(taskData)
            });
            
            if (response.ok) {
                taskModal.hide();
                loadTasks();
                loadStats();
                showToast(taskId ? 'Tarea actualizada correctamente' : 'Tarea creada correctamente');
            } else {
                const error = await response.json();
                showToast(error.error || 'Error al guardar la tarea', 'danger');
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Error al guardar la tarea', 'danger');
        }
    });
    
    async function loadTasks() {
        try {
            // Obtener parámetros de filtros
            const status = document.getElementById('filter-status').value;
            const priority = document.getElementById('filter-priority').value;
            const category = document.getElementById('filter-category').value;
            const sortBy = document.getElementById('sort-by').value;
            
            const params = new URLSearchParams({
                status,
                priority,
                category,
                sort_by: sortBy,
                sort_order: 'asc'
            });
            
            const response = await fetch(`/api/tasks?${params}`);
            const tasks = await response.json();
            
            if (tasks.length === 0) {
                tasksContainer.innerHTML = `
                    <div class="col-12 text-center py-5">
                        <i class="fas fa-inbox fa-4x text-muted mb-3"></i>
                        <p class="mb-3 text-muted">No tienes tareas que coincidan con los filtros.</p>
                        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#taskModal" onclick="resetForm()">
                            <i class="fas fa-plus me-2"></i>Crear tu primera tarea
                        </button>
                    </div>
                `;
                return;
            }
            
            tasksContainer.innerHTML = tasks.map(task => renderTaskCard(task)).join('');
        } catch (error) {
            console.error('Error:', error);
            tasksContainer.innerHTML = `
                <div class="col-12 text-center py-5">
                    <i class="fas fa-exclamation-triangle fa-4x text-danger mb-3"></i>
                    <p class="text-danger mb-3">Error al cargar las tareas. Intenta de nuevo.</p>
                    <button class="btn btn-primary" onclick="loadTasks()">
                        <i class="fas fa-redo me-2"></i>Reintentar
                    </button>
                </div>
            `;
        }
    }
    
    function renderTaskCard(task) {
        const priorityColors = {1: 'success', 2: 'info', 3: 'warning', 4: 'danger'};
        const priorityLabels = {1: 'Baja', 2: 'Media', 3: 'Alta', 4: 'Urgente'};
        const statusColors = {pending: 'secondary', in_progress: 'primary', completed: 'success', cancelled: 'dark'};
        const statusLabels = {pending: 'Pendiente', in_progress: 'En Progreso', completed: 'Completada', cancelled: 'Cancelada'};
        const categoryIcons = {
            personal: 'fa-user',
            work: 'fa-briefcase',
            study: 'fa-graduation-cap',
            health: 'fa-heart-pulse',
            shopping: 'fa-shopping-cart',
            other: 'fa-ellipsis'
        };
        
        const isOverdue = task.due_date && new Date(task.due_date) < new Date() && task.status !== 'completed';
        const dueDate = task.due_date ? new Date(task.due_date).toLocaleString('es-ES', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        }) : null;
        
        return `
            <div class="col-md-6 col-lg-4 mb-3">
                <div class="card h-100 shadow-sm ${task.completed ? 'opacity-75' : ''}">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <span class="badge bg-${priorityColors[task.priority]} me-2">
                                ${priorityLabels[task.priority]}
                            </span>
                            <span class="badge bg-${statusColors[task.status]}">
                                ${statusLabels[task.status]}
                            </span>
                        </div>
                        
                        <h5 class="card-title ${task.completed ? 'text-decoration-line-through text-muted' : ''}">
                            ${task.title}
                        </h5>
                        
                        ${task.description ? `
                            <p class="card-text text-muted small ${task.completed ? 'text-decoration-line-through' : ''}">
                                ${task.description.substring(0, 100)}${task.description.length > 100 ? '...' : ''}
                            </p>
                        ` : ''}
                        
                        <div class="mb-3">
                            <span class="badge bg-light text-dark">
                                <i class="fas ${categoryIcons[task.category]} me-1"></i>${task.category}
                            </span>
                            
                            ${task.due_date ? `
                                <span class="badge ${isOverdue ? 'bg-danger' : 'bg-light text-dark'} ms-1">
                                    <i class="fas fa-calendar-day me-1"></i>${dueDate}
                                </span>
                            ` : ''}
                            
                            ${task.is_recurring ? `
                                <span class="badge bg-info ms-1">
                                    <i class="fas fa-repeat me-1"></i>Recurrente
                                </span>
                            ` : ''}
                        </div>
                        
                        ${task.estimated_time ? `
                            <p class="small text-muted mb-2">
                                <i class="fas fa-clock me-1"></i>Estimado: ${task.estimated_time} min
                            </p>
                        ` : ''}
                    </div>
                    
                    <div class="card-footer bg-transparent border-top-0">
                        <div class="d-flex justify-content-between">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="check-${task.id}" 
                                    ${task.completed ? 'checked' : ''} 
                                    onchange="toggleTaskStatus(${task.id}, this.checked)">
                                <label class="form-check-label small" for="check-${task.id}">
                                    Completar
                                </label>
                            </div>
                            <div class="btn-group btn-group-sm" role="group">
                                <button class="btn btn-outline-primary" onclick="editTask(${task.id})" title="Editar">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button class="btn btn-outline-danger" onclick="deleteTask(${task.id})" title="Eliminar">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    async function loadStats() {
        try {
            const response = await fetch('/api/tasks/stats');
            const stats = await response.json();
            
            document.getElementById('stat-total').textContent = stats.total;
            document.getElementById('stat-in-progress').textContent = stats.in_progress;
            document.getElementById('stat-completed').textContent = stats.completed;
            document.getElementById('stat-overdue').textContent = stats.overdue;
        } catch (error) {
            console.error('Error loading stats:', error);
        }
    }
    
    window.loadTasks = loadTasks;
    window.loadStats = loadStats;
    
    window.editTask = async (id) => {
        try {
            const response = await fetch(`/api/tasks/${id}`);
            if (!response.ok) throw new Error('Error al obtener la tarea');
            
            const task = await response.json();
            
            // Llenar todos los campos del formulario
            document.getElementById('taskId').value = task.id;
            document.getElementById('taskTitle').value = task.title;
            document.getElementById('taskDescription').value = task.description || '';
            document.getElementById('taskPriority').value = task.priority;
            document.getElementById('taskStatus').value = task.status;
            document.getElementById('taskCategory').value = task.category;
            
            // Separar fecha y hora de inicio
            if (task.start_date) {
                const startDate = new Date(task.start_date);
                document.getElementById('taskStartDate').value = startDate.toISOString().split('T')[0];
                document.getElementById('taskStartTime').value = startDate.toTimeString().slice(0, 5);
            } else {
                document.getElementById('taskStartDate').value = '';
                document.getElementById('taskStartTime').value = '';
            }
            
            document.getElementById('taskEstimatedTime').value = task.estimated_time || '';
            
            // Calcular y mostrar fecha de vencimiento
            calculateAndDisplayDueDate();
            
            document.getElementById('taskIsRecurring').checked = task.is_recurring;
            
            if (task.is_recurring) {
                document.getElementById('recurrenceSection').style.display = 'block';
                document.getElementById('taskRecurrencePattern').value = task.recurrence_pattern || '';
                
                // Separar fecha y hora de recurrencia
                if (task.recurrence_end_date) {
                    const recurrenceDate = new Date(task.recurrence_end_date);
                    document.getElementById('taskRecurrenceEndDate').value = recurrenceDate.toISOString().split('T')[0];
                    document.getElementById('taskRecurrenceEndTime').value = recurrenceDate.toTimeString().slice(0, 5);
                } else {
                    document.getElementById('taskRecurrenceEndDate').value = '';
                    document.getElementById('taskRecurrenceEndTime').value = '';
                }
            } else {
                document.getElementById('recurrenceSection').style.display = 'none';
            }
            
            document.getElementById('taskModalLabel').innerHTML = '<i class="fas fa-edit me-2"></i>Editar Tarea';
            taskModal.show();
        } catch (error) {
            console.error('Error:', error);
            showToast('Error al cargar los datos de la tarea', 'danger');
        }
    };
    
    function formatDateForInput(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        return `${year}-${month}-${day}T${hours}:${minutes}`;
    }
    
    window.deleteTask = async (id) => {
        if (confirm('¿Estás seguro de que deseas eliminar esta tarea?')) {
            try {
                const response = await fetch(`/api/tasks/${id}`, {method: 'DELETE'});
                if (response.ok) {
                    loadTasks();
                    showToast('Tarea eliminada correctamente');
                }
            } catch (error) {
                console.error('Error:', error);
                showToast('Error al eliminar la tarea', 'danger');
            }
        }
    };
    
    window.toggleTaskStatus = async (id, completed) => {
        try {
            const response = await fetch(`/api/tasks/${id}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ completed })
            });
            
            if (response.ok) {
                loadTasks();
                loadStats();
                showToast(`Tarea marcada como ${completed ? 'completada' : 'pendiente'}`);
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Error al actualizar el estado de la tarea', 'danger');
        }
    };
    
    window.resetForm = () => {
        document.getElementById('taskForm').reset();
        document.getElementById('taskId').value = '';
        document.getElementById('taskDueDate').value = '';
        document.getElementById('recurrenceSection').style.display = 'none';
        document.getElementById('taskModalLabel').innerHTML = '<i class="fas fa-tasks me-2"></i>Nueva Tarea';
    };
    
    window.toggleRecurrence = () => {
        const isRecurring = document.getElementById('taskIsRecurring').checked;
        document.getElementById('recurrenceSection').style.display = isRecurring ? 'block' : 'none';
    };
    
    function showToast(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0 position-fixed bottom-0 end-0 m-3`;
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;
        document.body.appendChild(toast);
        
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        // Eliminar el toast después de cerrarse
        toast.addEventListener('hidden.bs.toast', () => {
            document.body.removeChild(toast);
        });
    }
});