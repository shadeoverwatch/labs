<script>
    document.getElementById('registrationForm').addEventListener('submit', function(event) {
        let valid = true;
        
        // Проверка имени
        let name = document.getElementById('name').value;
        let nameError = document.getElementById('nameError');
        if (name.length < 2 || name.length > 50) {
            valid = false;
            nameError.textContent = "Имя должно содержать от 2 до 50 символов.";
        } else {
            nameError.textContent = "";
        }

        // Проверка email
        let email = document.getElementById('email').value;
        let emailError = document.getElementById('emailError');
        let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        if (!emailPattern.test(email)) {
            valid = false;
            emailError.textContent = "Неверный формат email.";
        } else {
            emailError.textContent = "";
        }

        // Проверка пароля
        let password = document.getElementById('password').value;
        let passwordError = document.getElementById('passwordError');
        let strongPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{6,}$/;
        if (!strongPassword.test(password)) {
            valid = false;
            passwordError.textContent = "Пароль должен содержать не менее 6 символов, включая заглавные, строчные буквы, цифры и специальные символы.";
        } else {
            passwordError.textContent = "";
        }

        if (!valid) {
            event.preventDefault();
        }
    });
</script>
