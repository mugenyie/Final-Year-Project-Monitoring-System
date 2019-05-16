let member_list = "";
let member_count = 0;
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

function createStudent(name, email, phonenumber, student_number, password){
    console.log("create student "+name)
    PostData('https://csc-fypms.herokuapp.com/api/v1/student/', {
        course:getCookie('course'),
        email:email, 
        name:name,
        password:password,
        phonenumber:phonenumber,
        student_number:student_number,
        group_id:getCookie('group_id')
    })
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error));  
}

function AddStudent(){
    event.preventDefault();

    console.log("Adding new student");

    createStudent(
        document.getElementById('r-name').value,
        document.getElementById('r-email').value,
        document.getElementById('r-phonenumber').value,
        document.getElementById('r-student_number').value,
        document.getElementById('r-password').value
    );
}

function GetGroupMembers(){
    GetData('https://csc-fypms.herokuapp.com/api/v1/student/group/'+getCookie('group_id')+'/members')
    .then(function(data) {
        data.forEach(element => {
            member_count+=1;
            member_list += `
            <tr>
                <td>Member ${member_count}: &nbsp;</td>&nbsp;&nbsp;
                <td>${element.name}</td>&nbsp;&nbsp;
                <td>${element.email}</td>&nbsp;&nbsp;
                <td>${element.phonenumber}</td>&nbsp;&nbsp;
                <td>${element.student_number}</td>
            </tr>
            <br /><br />
            `
        });
        console.log(data);
        var div = document.getElementById('member-list');
        div.innerHTML = member_list;
    })
    .catch(error => console.error(error));  
}