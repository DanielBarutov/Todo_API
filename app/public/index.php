<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"></script>
    <link rel="stylesheet" href="public/style.css">
    
</head>
<body>
    <ul class="nav">
        <li class="nav-item">
            <a class="nav-link" href="/">Создание задачи</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="public/task.php">Список задач</a>
        </li>
    </ul>
    
    <div class="container" style="align-items: center; justify-content: center; display: flex; flex-direction: column; height: 100vh;">
        <h1>Авторизация</h1>
        <form id="authForm" style="display: flex; flex-direction: column; gap: 10px;">
            <input id="login" type="text" name="login" placeholder="Логин">
            <input id="password" type="password" name="password" placeholder="Пароль">
            <button type="submit" class="btn btn-primary">Войти</button>
        </form>
    </div>
    <div class="container" id="createTask">
        <h1>Создание задачи</h1>
        <form id="createTaskForm">
            <input id="title" type="text" name="title" placeholder="Название задачи">
            <input id="description" type="text" name="description" placeholder="Описание задачи">
            <button type="submit">Создать</button>
        </form>
    </div>
    
</div>
    <script src="public/script.js"></script>
</body>
</html>