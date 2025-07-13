const createTaskForm = document.getElementById('createTaskForm');
const listTasks = document.getElementById('listTasks');
const apiUrl = 'http://localhost:8000';


// Загрузка списка задач
async function loadTasks() {
    try {
        const response = await fetch(`${apiUrl}/tasks/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const tasks = await response.json();
        displayTasks(tasks);
    } catch (error) {
        console.error('Ошибка при загрузке задач:', error);
        showMessage('Ошибка при загрузке задач: ' + error.message, 'error');
    }
}

// Отображение задач
function displayTasks(tasks) {
    const container = document.getElementById('tasksContainer');
    
    if (tasks.length === 0) {
        container.innerHTML = '<p>Задач пока нет. Создайте первую!</p>';
        return;
    }

    container.innerHTML = tasks.map(task => `
        <div class="task-item ${task.is_completed ? 'completed' : ''}">
            <div class="task-title">${task.title}</div>
            <div class="task-description">${task.description || 'Без описания'}</div>
            <div class="task-actions">
                <span class="status ${task.is_completed ? 'completed' : 'pending'}">
                    ${task.is_completed ? 'Завершена' : 'В работе'}
                </span>
                <button onclick="toggleTask(${task.id}, ${!task.is_completed})">
                    ${task.is_completed ? 'Отменить' : 'Завершить'}
                </button>
                <button onclick="editTask(${task.id})">Редактировать</button>
                <button class="delete" onclick="deleteTask(${task.id})">Удалить</button>
            </div>
        </div>
    `).join('');
}

// Переключение статуса задачи
async function toggleTask(taskId, isCompleted) {
    try {
        const response = await fetch(`${apiUrl}/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ is_completed: isCompleted })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        showMessage('Статус задачи обновлен!', 'success');
        loadTasks();
    } catch (error) {
        console.error('Ошибка при обновлении задачи:', error);
        showMessage('Ошибка при обновлении задачи: ' + error.message, 'error');
    }
}

// Редактирование задачи
async function editTask(taskId) {
    const newTitle = prompt('Введите новое название задачи:');
    if (!newTitle) return;

    const newDescription = prompt('Введите новое описание задачи:');
    
    try {
        const response = await fetch(`${apiUrl}/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: newTitle,
                description: newDescription
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        showMessage('Задача обновлена!', 'success');
        loadTasks();
    } catch (error) {
        console.error('Ошибка при обновлении задачи:', error);
        showMessage('Ошибка при обновлении задачи: ' + error.message, 'error');
    }
}

// Удаление задачи
async function deleteTask(taskId) {
    if (!confirm('Вы уверены, что хотите удалить эту задачу?')) {
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/tasks/${taskId}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        showMessage('Задача удалена!', 'success');
        loadTasks();
    } catch (error) {
        console.error('Ошибка при удалении задачи:', error);
        showMessage('Ошибка при удалении задачи: ' + error.message, 'error');
    }
}

// Показать сообщение
function showMessage(message, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = type;
    messageDiv.textContent = message;
    
    document.body.insertBefore(messageDiv, document.body.firstChild);
    
    setTimeout(() => {
        messageDiv.remove();
    }, 3000);
}

// Загружаем задачи при загрузке страницы
if (window.location.pathname.endsWith('task.php')) {
    loadTasks();
}
if (window.location.pathname === '/' || window.location.pathname === '/index.php') {
    createTaskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const is_completed = false;
        const task = { 
            title: title,
            description: description,
            is_completed: is_completed
        };
        fetch(`${apiUrl}/tasks/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(task)
            
        })
        .then(response => response.json())
        .then(data => {
            showMessage('Задача создана!', 'success');
        });
    });
}