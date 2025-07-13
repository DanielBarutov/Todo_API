<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo - Список задач</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"></script>
    <link rel="stylesheet" href="/public/style.css">
    
</head>
<body>
    <ul class="nav">
        <li class="nav-item">
            <a class="nav-link" href="/">Создание задачи</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/task.php">Список задач</a>
        </li>
    </ul>
   
    <!-- Список задач -->
    <div class="container" id="tasksList">
        <h2>Список задач</h2>
        <button onclick="loadTasks()">Обновить список</button>
        <div id="tasksContainer"></div>
    </div>
</div>
    <script src="/public/script.js"></script>
</body>
</html>