let member_list = "";
let member_count = 0;

function createStudent(student_id,name, email, phonenumber, student_number, password, course, group_id){
    console.log("create student "+name)
    PostData(baseurl+'student/', {
        id:student_id,
        course:course,
        email:email, 
        name:name,
        password:password,
        phonenumber:phonenumber,
        student_number:student_number,
        group_id:group_id
    })
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error));  
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