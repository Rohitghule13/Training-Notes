function greeting(value) {
    console.log("im in function")
    const time = new Date();
    const hur = time.getHours();
    if (hur > 5 && hur < 12) {
        document.getElementById('greetings').innerHTML = "Good Morning! " + value;

    } else if (hur > 12 && hur < 4) {
        document.getElementById('greetings').innerHTML = "Good Afternoon! " + value;

    } else {
        document.getElementById('greetings').innerHTML = "Good Evening!" + value;

    }
}
document.getElementById('avatar').src = 'https://robohash.org/blanditiisquiaquo.png?size=300x300&set=set1';
var text = fetch('https://run.mocky.io/v3/010e898c-a05c-4a0a-b947-2a65b5a267c5')
    .then(function(res) {
        return res.json();
    }).then(function(data) {
        var jsonfile = data;
    }).catch(function(err) {
        console.error("somthing went wrong with json");
        console.log(error);
    });
console.log(jsonfile);