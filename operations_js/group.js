let created_by = getCookie('id');
let auth_token = getCookie('auth_token');
console.log(created_by);
console.log(auth_token);

async function PostData(url = '', data = {}) {
    // Default options are marked with *
      const response = await fetch(url, {
        method: 'POST',
        mode: 'no-cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'api-token': auth_token
        },
        body: JSON.stringify(data),
    });
    return await response.json(); // parses JSON response into native Javascript objects 
}

async function GetData(url = '') {
    // Default options are marked with *
      const response = await fetch(url, {
        method: 'GET',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'api-token': auth_token
        },
    });
    return await response.json(); // parses JSON response into native Javascript objects 
}

async function UpdateData(url = '', data = {}) {
    // Default options are marked with *
      const response = await fetch(url, {
        method: 'PUT',
        mode: 'no-cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'api-token': auth_token
        },
        body: JSON.stringify(data),
    });
    return await response.json(); // parses JSON response into native Javascript objects 
}

function getCookie(name) {
    var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return v ? v[2] : null;
}

function setCookie(name, value, days) {
    var d = new Date;
    d.setTime(d.getTime() + 24*60*60*1000*days);
    document.cookie = name + "=" + value + ";path=/;expires=" + d.toGMTString();
}

function GetUserGroup(){
    GetData('https://csc-fypms.herokuapp.com/api/v1/group/'+getCookie('group_id'))
    .then(data => {
        console.log(JSON.stringify(data));
        setCookie('group_id', data.id, 30);
        setCookie('group_name', data.name, 30);
        setCookie('group_number', data.number, 30);
    })
    .catch(error => console.error(error));  
}

function CreateGroup(){
    event.preventDefault()

    createNewGroup(document.getElementById('r-group_name').value, document.getElementById('r-group_number').value)
    //Update my group id
    updateStudent();
}

function createNewGroup(name, number){
    console.log("Create group");
    PostData('https://csc-fypms.herokuapp.com/api/v1/group/', {
        name:name,
        number:number,
        created_by:created_by
    })
    .then(data => {
        console.log(JSON.stringify(data));
        setCookie('group_id', data.id, 30);
    })
    .catch(error => console.error(error));  
}

function updateStudent(){
    UpdateData('https://csc-fypms.herokuapp.com/api/v1/student/me', {
        group_id:getCookie('group_id')
    })
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error)); 
}