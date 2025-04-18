document.addEventListener('DOMContentLoaded', () => {
    const tasksContainer = document.getElementById('tasks-container');
    const taskForm = document.getElementById('taskForm');
    const taskModal = new bootstrap.Modal(document.getElementById('taskModal'));
    
    // Cargar tareas al iniciar
    loadTasks();
    
    // Manejar envío del formulario
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const taskId = document.getElementById('taskId').value;
        const taskData = {
            title: document.getElementById('taskTitle').value,
            description: document.getElementById('taskDescription').value
        };
        
        // Si estamos editando, incluir estado completado
        if (taskId) {
            taskData.completed = document.getElementById('taskCompleted').checked;
        }
        
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
                showToast(taskId ? 'Tarea actualizada' : 'Tarea creada');
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Error al guardar la tarea', 'danger');
        }
    });
    
    async function loadTasks() {
        try {
            const response = await fetch('/api/tasks');
            const tasks = await response.json();
            
            if (tasks.length === 0) {
                tasksContainer.innerHTML = `
                    <div class="list-group-item text-center py-4">
                        <p class="mb-0 text-muted">No tienes tareas pendientes.</p>
                        <button class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#taskModal" onclick="resetForm()">
                            Crear tu primera tarea
                        </button>
                    </div>
                `;
                return;
            }
            
            tasksContainer.innerHTML = tasks.map(task => {
                const titleClass = task.completed ? 'task-complete' : '';
                return `
                    <div class="list-group-item">
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="check-${task.id}" 
                                    ${task.completed ? 'checked' : ''} onchange="toggleTaskStatus(${task.id}, this.checked)">
                                <label class="form-check-label ${titleClass}" for="check-${task.id}">
                                    <span class="fw-bold">${task.title}</span>
                                </label>
                            </div>
                            <div>
                                <button class="btn btn-sm btn-outline-primary me-2 btn-task"
                                    onclick="editTask(${task.id})">Editar</button>
                                <button class="btn btn-sm btn-outline-danger btn-task"
                                    onclick="deleteTask(${task.id})">Eliminar</button>
                            </div>
                        </div>
                        ${task.description ? `<p class="ms-4 mb-0 text-muted ${titleClass}">${task.description}</p>` : ''}
                    </div>
                `;
            }).join('');
        } catch (error) {
            console.error('Error:', error);
            tasksContainer.innerHTML = `
                <div class="list-group-item text-center py-3">
                    <p class="text-danger mb-0">Error al cargar las tareas. Intenta de nuevo.</p>
                    <button class="btn btn-sm btn-outline-primary mt-2" onclick="loadTasks()">Reintentar</button>
                </div>
            `;
        }
    }
    
    window.editTask = async (id) => {
        try {
            const response = await fetch(`/api/tasks/${id}`);
            if (!response.ok) throw new Error('Error al obtener la tarea');
            
            const task = await response.json();
            
            document.getElementById('taskId').value = task.id;
            document.getElementById('taskTitle').value = task.title;
            document.getElementById('taskDescription').value = task.description || '';
            
            const completedContainer = document.getElementById('completedContainer');
            completedContainer.style.display = 'block';
            document.getElementById('taskCompleted').checked = task.completed;
            
            taskModal.show();
        } catch (error) {
            console.error('Error:', error);
            showToast('Error al cargar los datos de la tarea', 'danger');
        }
    };
    
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
                showToast(`Tarea marcada como ${completed ? 'completada' : 'pendiente'}`);
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Error al actualizar el estado de la tarea', 'danger');
        }
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