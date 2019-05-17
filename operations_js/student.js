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
            <p>Group ID: ${getCookie('group_id')}</p>
        `;

    var div = document.getElementById('userDetails');
    div.innerHTML = detail_list;
}