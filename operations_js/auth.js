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
        LoginStudent();
    }
    if(category == 1){
        LoginAdmin();
    }
    if(category == 2){
        LoginSupervisor();
    }
}

function LoginStudent(){
    console.log("student login called");
    let email = document.getElementById('r-email').value;
    let password = document.getElementById('r-password').value;
    
    fetch('https://csc-fypms.herokuapp.com/api/v1/student/login', {
        method: 'POST',
        headers : new Headers(),
        body:JSON.stringify({
            email:email, 
            password:password
        })
    }).then((res) => res.json())
    .then(data => {
        if(data.error != null){
            console.log(data.error);
        }else{
            console.log(data);
            setCookie('auth-token', data.api-token, 30);
            setCookie('id', data.data[0].id, 30);
            setCookie('email', data.data[0].email, 30);
            setCookie('name', data.data[0].user.name, 30);
            setCookie('phonenumber', data.data[0].user.phonenumber, 30);
            setCookie('user_role_name', data.data[0].user.user_role_name, 30);
            setCookie('user_role_value', data.data[0].user.user_role_value, 30);
            setCookie('project_id', data.data[0].user.project_id, 30);
            setCookie('group_id', data.data[0].user.group_id, 30);
            setCookie('course', data.data[0].user.course, 30);
            
            window.location.href = "student_.html"; 
        } 
    })
    .catch(err => {
        console.log(err);
    });
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

function SignUpStudent(){
    event.preventDefault();

    let course = document.getElementById('r-course').value;
    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    let student_number = document.getElementById('r-student_number').value;
    
    fetch('https://csc-fypms.herokuapp.com/api/v1/student/', {
        method: 'POST',
        body:JSON.stringify({
            course:course,
            email:email, 
            name:name,
            password:password,
            phonenumber:phonenumber,
            student_number:student_number
        })
    }).then((res) => res.json())
    .then(data => {
        if(data.error != null){
            
        }else{
            setCookie('auth-token', data.token, 30);
            
            window.location.href = "student_.html"; 
        } 
    })
    .catch(err => {
        console.log(err);
    });
}

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


// logout

function logOut(){
    deleteCookie("auth-token");
    window.location.replace('index.html');
}

 
// Cookie management

function setCookie(name, value, days) {
    var d = new Date;
    d.setTime(d.getTime() + 24*60*60*1000*days);
    document.cookie = name + "=" + value + ";path=/;expires=" + d.toGMTString();
}

function getCookie(name) {
    var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return v ? v[2] : null;
}

function deleteCookie(name) { setCookie(name, '', -1); }

function checkToken() {
    var token=getCookie("auth-token");
    if (token == "") {
        window.location.replace('index.html');
    }else{
        document.getElementById("username").textContent=getCookie('username');
    }
}