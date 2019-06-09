function SendMessage(){
    event.preventDefault();

    let id = create_UUID();
    let subject = document.getElementById('subject').value;
    let message = document.getElementById('message').value;
    let from_id = document.getElementById('from_id').value;
    let to_id = document.getElementById('to_id').value;

    console.log(subject + message + from_id + to_id);

    PostData(baseurl+'message/', {
        id:id,
        subject:subject,
        message:message,
        from_id:from_id,
        to_id:to_id
    })
    .then(data => {
        console.log(JSON.stringify(data));
        if(data.id != 'null'){
            alert("Successfuly Sent Message");
        }
    })
    .catch(error => alert(error));  
}

var message_count = 0;
let message_list = "";
function GetMessagesTo(to_id){

    GetData(baseurl+`message/to/${to_id}`)
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            message_count +=1;
            message_list += `
            <tr>
            <td>${element.subject}</td>
            <td>${element.message}</td>
            <td>${element.created_on}</td>
            <td><a href="reply?to_id=${element.from_id}">Reply</a></td>
            </tr>
            `;
        });

        document.getElementById('message_count').textContent = message_count;
        document.getElementById('message_list').innerHTML = message_list;
    })
    .catch(error => console.log(error));  
}

function GetMessagesToSupervisor(to_id){

    GetData(baseurl+`message/to/${to_id}`)
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            message_count +=1;
            message_list += `
            <tr>
            <td>${element.subject}</td>
            <td>${element.message}</td>
            <td>${element.created_on}</td>
            <td><a href="supervisor_message?group_id=${element.from_id}">Reply</a></td>
            </tr>
            `;
        });

        document.getElementById('message_count').textContent = message_count;
        document.getElementById('message_list').innerHTML = message_list;
    })
    .catch(error => console.log(error));  
}