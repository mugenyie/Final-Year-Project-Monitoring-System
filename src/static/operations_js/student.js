function getStudentSupervisor(){
    GetData(baseurl+'group/'+getCookie('group_id'))
    .then(data => {
        console.log(data);
        setCookie('supervisor_id', data.supervisor_id, 30);
        setCookie('group_name', data.name, 30);
    })
    .catch(error => alert(error));  
}

getStudentSupervisor();

function getStudentDetails(){
    var user_data = document.cookie;
    console.log(user_data);
    var detail_list ="";
    detail_list += `
            <p>Name: ${getCookie('name')}</p>
            <p>Email: ${getCookie('email')}</p>
            <p>Course: ${getCookie('course')}</p>
            <p>Phone: ${getCookie('phonenumber')}</p>
            <p>Student Number: ${getCookie('student_number')}</p>
            <p>Group Name: ${getCookie('group_name')}</p>
            <p>Project Name: ${getCookie('project_name')}</p>
        `;

    var div = document.getElementById('userDetails');
    div.innerHTML = detail_list;
}

let student_list = "";
let count = 0;
function displayStudents(){
    GetData(baseurl+'student/')
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            count+=1;
            student_list += `
            <tr>
            <td>${element.name}</td>
            <td>${element.email}</td>
            <td>${element.course}</td>
            <td>${element.phonenumber}</td>
            <td>${element.group_id}</td>
            <td>${element.project_id}</td>
            <td>${element.created_on}</td>
            </tr>
            `;
        });
        
        document.getElementById('student-list').innerHTML = student_list;
        document.getElementById('count').textContent = count;
    })
    .catch(error => console.error(error));  
}