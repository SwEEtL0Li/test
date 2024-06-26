let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let item = "";

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");


document.getElementById("btn2").addEventListener("click", function(){
	document.getElementById("home").style.display = "none";
    document.getElementById("page1").style.display = "block";
});
document.getElementById("back1").addEventListener("click", function(){
    document.getElementById("page1").style.display = "none";
    document.getElementById("home").style.display = "block";
});


Telegram.WebApp.onEvent("mainButtonClicked", function(){
	tg.sendData(item);
});


let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;

usercard.appendChild(p);


async function fetchData() {
    try {
        const response = await fetch('http://localhost:3000/data');
        const data = await response.json();
        document.getElementById('sensorValue').innerText = `Показание датчика: ${data.value.toFixed(2)}`;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Получение данных каждые 5 секунд
setInterval(fetchData, 5000);

// Начальная загрузка данных
fetchData();