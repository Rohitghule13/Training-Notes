function greeting() {
    console.log("im in function")
    const time = new Date();
    const hur = time.getHours();
    if (hur > 5 && hur < 12) {
        document.getElementById('greetings').innerHTML = "Good Morning";

    } else if (hur > 12 && hur < 4) {
        document.getElementById('greetings').innerHTML = "Good Afternoon";

    } else {
        document.getElementById('greetings').innerHTML = "Good Evening";

    }
}

document.getElementById('leonardo').addEventListener("click", greeting);
var x = "I love you";
console.log(`i wanted to say ${x}`)