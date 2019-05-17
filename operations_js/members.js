let member_list = "";
let member_count = 0;

async function PostmemberData(url = '', data = {}) {
    // Default options are marked with *
      const response = await fetch(url, {
        method: 'POST',
        mode:"cors",
        headers: {
            'Content-Type': 'application/json',
            'api-token': getCookie('auth_token')
        },
        body: JSON.stringify(data),
    });
    return await response.json(); // parses JSON response into native Javascript objects 
}
function AddMember(){
    event.preventDefault();
    console.log("signup student");
    let id = create_UUID();
    console.log(id);
    let group_id = getCookie('group_id');
    let course = getCookie('course');
    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    let student_number = document.getElementById('r-student_number').value;
    fetch(baseurl+'student/', {
        method: 'POST',
        mode:"no-cors",
        headers : {
            'Content-Type': 'application/json',
            'api-token': getCookie('auth_token')
        },
        body:JSON.stringify({
            id:id,
            course:course,
            email:email, 
            name:name,
            password:password,
            phonenumber:phonenumber,
            student_number:student_number,
            group_id:group_id
        })
    });   
}

function AddStudent(){
    event.preventDefault();

    console.log("Adding new student");

    createStudent(
        create_UUID(),
        document.getElementById('r-name').value,
        document.getElementById('r-email').value,
        document.getElementById('r-phonenumber').value,
        document.getElementById('r-student_number').value,
        document.getElementById('r-password').value,
        getCookie('course'),
        getCookie('group_id')
    );
}

function GetGroupMembers(){
    GetData(baseurl+'student/group/'+getCookie('group_id')+'/members')
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