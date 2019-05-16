// Login
function PostLoginData(){
    event.preventDefault();

    let email = document.getElementById('r-email').value;
    let password = document.getElementById('r-password').value;
    let category = document.getElementById('r-category').value;

    console.log(email);
    console.log(password);
    console.log(category);

    if(category == 0){
        console.log("student");
        LoginStudent(email, password);
    }
    if(category == 1){
        LoginAdmin();
    }
    if(category == 2){
        LoginSupervisor();
    }
}

async function PostData(url = '', data = {}) {
    // Default options are marked with *
      const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    return await response.json(); // parses JSON response into native Javascript objects 
}

function registerStudentCookies(data){
    setCookie('auth_token', data.api_token, 30);
    setCookie('id', data.user.id, 30);
    setCookie('email', data.user.email, 30);
    setCookie('name', data.user.name, 30);
    setCookie('course', data.user.course, 30);
    setCookie('group_id', data.user.group_id, 30);
    setCookie('student_number', data.user.student_number, 30);
    setCookie('phonenumber', data.user.phonenumber, 30);
    setCookie('user_role_name', data.user.user_role_name, 30);
    setCookie('user_role_value', data.user.user_role_value, 30);

    console.log("Cookie data => "+document.cookie);
}

function LoginStudent(email, password){
    console.log("student login called "+email+" "+password);
    PostData('https://csc-fypms.herokuapp.com/api/v1/student/login', {email:email, password:password})
    .then(data => {
        registerStudentCookies(data);
        window.location.href = "student_.html"; 
    }) 
    .catch(error => console.error(error));    
}

function SignUpStudent(){
    event.preventDefault();
    console.log("signup student");
    let course = document.getElementById('r-course').value;
    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    let student_number = document.getElementById('r-student_number').value;
    
    PostData('https://csc-fypms.herokuapp.com/api/v1/student/', {
        course:course,
        email:email, 
        name:name,
        password:password,
        phonenumber:phonenumber,
        student_number:student_number
    })
    .then(data => {
        registerStudentCookies(data);
        window.location.href = "student_.html"; 
    })
    .catch(error => console.error(error));    
}


function LoginSupervisor(){
    event.preventDefault();

    let email = document.getElementById('r-email').value;
    let password = document.getElementById('r-password').value;
    
    fetch('https://csc-fypms.herokuapp.com/api/v1/supervisor/login', {
        method: 'POST',
        body:JSON.stringify({
            email:email, 
            password:password
        })
    }).then((res) => res.json())
    .then(data => {
        if(data.error != null){

        }else{
            setCookie('auth-token', data.api-token, 30);
            setCookie('id', data.data[0].id, 30);
            setCookie('email', data.data[0].email, 30);
            setCookie('name', data.data[0].user.name, 30);
            setCookie('phonenumber', data.data[0].user.phonenumber, 30);
            setCookie('user_role_name', data.data[0].user.user_role_name, 30);
            setCookie('user_role_value', data.data[0].user.user_role_value, 30);
            setCookie('department', data.data[0].user.department, 30);
            setCookie('title', data.data[0].user.title, 30);
            
            window.location.href = "supervisor_.html"; 
        } 
    })
    .catch(err => {
        console.log(err);
    });
}

function LoginAdmin(){
    event.preventDefault();

    let email = document.getElementById('r-email').value;
    let password = document.getElementById('r-password').value;
    
    fetch('https://csc-fypms.herokuapp.com/api/v1/admin/login', {
        method: 'POST',
        body:JSON.stringify({
            email:email, 
            password:password
        })
    }).then((res) => res.json())
    .then(data => {
        if(data.error != null){

        }else{
            setCookie('auth-token', data.api-token, 30);
            setCookie('id', data.data[0].id, 30);
            setCookie('email', data.data[0].email, 30);
            setCookie('name', data.data[0].user.name, 30);
            setCookie('phonenumber', data.data[0].user.phonenumber, 30);
            setCookie('user_role_name', data.data[0].user.user_role_name, 30);
            setCookie('user_role_value', data.data[0].user.user_role_value, 30);
            
            window.location.href = "admin_.html"; 
        } 
    })
    .catch(err => {
        console.log(err);
    });
}


// SignUp



function SignUpSupervisor(){
    event.preventDefault();

    let department = document.getElementById('r-department').value;
    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    let title = document.getElementById('r-title').value;
    
    fetch('https://csc-fypms.herokuapp.com/api/v1/supervisor/', {
        method: 'POST',
        body:JSON.stringify({
            department:department,
            email:email, 
            name:name,
            password:password,
            phonenumber:phonenumber,
            title:title
        })
    }).then((res) => res.json())
    .then(data => {
        if(data.error != null){
            
        }else{
            setCookie('auth-token', data.token, 30);
            
            window.location.href = "supervisor_.html"; 
        } 
    })
    .catch(err => {
        console.log(err);
    });
}

function SignUpAdmin(){
    event.preventDefault();

    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    
    fetch('https://csc-fypms.herokuapp.com/api/v1/admin/', {
        method: 'POST',
        body:JSON.stringify({
            email:email, 
            name:name,
            password:password,
            phonenumber:phonenumber
        })
    }).then((res) => res.json())
    .then(data => {
        if(data.error != null){
            
        }else{
            setCookie('auth-token', data.token, 30);
            setCookie('id', data.data[0].id, 30);
            setCookie('email', data.data[0].email, 30);
            setCookie('name', data.data[0].user.name, 30);
            setCookie('phonenumber', data.data[0].user.phonenumber, 30);
            setCookie('user_role_name', data.data[0].user.user_role_name, 30);
            setCookie('user_role_value', data.data[0].user.user_role_value, 30);
            
            window.location.href = "admin_.html"; 
        } 
    })
    .catch(err => {
        console.log(err);
    });
}

 
// Cookie management

function setCookie(name, value, days) {
    var d = new Date;
    d.setTime(d.getTime() + 24*60*60*1000*days);
    document.cookie = name + "=" + value + ";path=/;expires=" + d.toGMTString();
}
