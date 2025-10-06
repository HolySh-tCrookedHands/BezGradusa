document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM загружен, можно ебашить');
    
    // Вот так получаешь элементы по ID
    const form = document.getElementById('registrationForm');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const passwordRepat = document.getElementById('password_r');
    

    // Слушаем ввод в реальном времени
    username.addEventListener('input', function() {
        console.log('Пользователь печатает:', this.value);
    });

    // Отправка формы
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Останавливаем стандартную отправку
        console.log('Форма пытается отправиться, но мы её ебём');
        
        // Вот тут будет ваша валидация
        validateForm();
    });

    function validateForm() {
        let isValid = true;
        
        // Валидация username
        if (username.value.trim().length < 3) {
            console.log('Юзернейм слишком короткий');
            username.style.borderColor = 'red';
            isValid = false;
        } else {
            username.style.borderColor = 'green';
        }
        
        // Валидация email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value)) {
            console.log('Email хуйня');
            email.style.borderColor = 'red';
            isValid = false;
        } else {
            email.style.borderColor = 'green';
        }
        
        // Валидация пароля
        if (password.value.length < 6) {
            password.style.borderColor = 'red';
            isValid = false;
        } else {
            password.style.borderColor = 'green';
        }

        if (password.value != passwordRepat.value) {
            password.style.borderColor = 'red'
            passwordRepat.style.borderColor = 'red'
            isValid = false;
        } else {
            password.style.borderColor = 'green'
            passwordRepat.style.borderColor = 'green'
        }
        
        return isValid;
    }
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        if (validateForm()) {
            alert('Всё ок, можно отправлять на сервер!');
            // form.submit(); // Раскомментируешь когда всё будет работать
        } else {
            alert('Исправь ошибки, долбоёб!');
        }
    });

});