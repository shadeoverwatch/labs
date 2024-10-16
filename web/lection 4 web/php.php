<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = trim($_POST["name"]);
    $email = trim($_POST["email"]);
    $password = $_POST["password"];

    $errors = [];

    // Валидация имени
    if (empty($name) || strlen($name) < 2 || strlen($name) > 50) {
        $errors[] = "Имя должно содержать от 2 до 50 символов.";
    }

    // Валидация email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Неверный формат email.";
    }

    // Валидация пароля
    if (!preg_match("/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{6,}$/", $password)) {
        $errors[] = "Пароль должен содержать не менее 6 символов, включая заглавные, строчные буквы, цифры и специальные символы.";
    }

    // Если есть ошибки, выводим их
    if (!empty($errors)) {
        foreach ($errors as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
    } else {
        // Обработка успешной регистрации (например, сохранение данных в БД)
        echo "<p style='color:green;'>Регистрация успешна!</p>";
    }
}
?>
