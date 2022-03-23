// ===== greeting function =====//
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

function removePerson(row_no) {
    console.log("im in remove fun")
    const elem = document.getElementById(row_no);
    elem.remove();
}
// Array for Person Info //
var Arr_person = []
    // ===== json fetch ===== //

fetch("https://run.mocky.io/v3/010e898c-a05c-4a0a-b947-2a65b5a267c5").then(
        res => {
            res.json().then(
                data => {
                    console.log(data);
                    if (data.length > 0) {
                        var temp = "";
                        var i = 0;
                        data.forEach((itemData) => {
                            temp += `<tr id="obj${i}" onclick="addEventListener('click',greeting('${itemData.first_name}'))"><td>${itemData.first_name}</td>
                        <td>${itemData.last_name}</td>
                        <td>${itemData.username}</td>
                        <td>${itemData.employment.title}</td>
                        <td>${itemData.address.country}</td>
                        <td><button onclick="greeting('${itemData.first_name}')">view</button>
                        <button onclick="removePerson(obj${i})">Remove</button></td></tr>`;
                            i += 1;
                            /*temp += "<tr>";
                            temp += "<td>" + itemData.first_name + "</td>";
                            temp += "<td>" + itemData.last_name + "</td>";
                            temp += "<td>" + itemData.username + "</td>";
                            temp += "<td>" + itemData.employment.title + "</td>"
                            temp += "<td>" + itemData.address.country + "</td></tr>"*/


                        });
                        document.getElementById('data').innerHTML = temp;
                    }
                }
            )
        }
    )
    // ==== Right side of card ====//