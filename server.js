const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());

// Имитация данных из базы данных
let sensorData = { value: 0 };

// Эндпоинт для получения данных
app.get('/data', (req, res) => {
    res.json(sensorData);
});

// Запуск сервера
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

// Эмуляция обновления данных каждые 5 секунд
setInterval(() => {
    sensorData.value = Math.random() * 100; // Генерация случайного значения для демонстрации
}, 5000);