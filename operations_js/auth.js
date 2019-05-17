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
        console.log('supervisor')
        LoginSupervisor(email, password)
    }
    if(category == 2){
        console.log('Admin')
        LoginAdmin(email, password)
    }
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
    setCookie('project_id', data.user.project_id, 30);

    console.log("Cookie data => "+document.cookie);
}

function registerSupervisorCookies(data){
    setCookie('auth_token', data.api_token, 30);
    setCookie('id', data.user.id, 30);
    setCookie('email', data.user.email, 30);
    setCookie('name', data.user.name, 30);
    setCookie('department', data.user.course, 30);
    setCookie('Title', data.user.group_id, 30);
    setCookie('phonenumber', data.user.phonenumber, 30);
    setCookie('user_role_name', data.user.user_role_name, 30);
    setCookie('user_role_value', data.user.user_role_value, 30);

    console.log("Cookie data => "+document.cookie);
}

function registerAdminCookies(data){
    setCookie('auth_token', data.api_token, 30);
    setCookie('id', data.user.id, 30);
    setCookie('email', data.user.email, 30);
    setCookie('name', data.user.name, 30);
    setCookie('Title', data.user.group_id, 30);
    setCookie('phonenumber', data.user.phonenumber, 30);
    setCookie('user_role_name', data.user.user_role_name, 30);
    setCookie('user_role_value', data.user.user_role_value, 30);

    console.log("Cookie data => "+document.cookie);
}

function LoginStudent(email, password){
    console.log("student login called "+email+" "+password);
    PostData(baseurl+'student/login', {email:email, password:password})
    .then(data => {
        console.log(JSON.stringify(data));
        registerStudentCookies(data);
        window.location.href = "student_.html"; 
    }) 
    .catch(error => console.error(error));    
}

function LoginSupervisor(email, password){
    console.log("supervisor login called "+email+" "+password);
    PostData(baseurl+'supervisor/login', {email:email, password:password})
    .then(data => {
        console.log(JSON.stringify(data));
        registerStudentCookies(data);
        window.location.href = "supervisor_.html"; 
    }) 
    .catch(error => console.error(error)); 
}

function LoginAdmin(email, password){
    console.log("Admin login called "+email+" "+password);
    PostData(baseurl+'admin/login', {email:email, password:password})
    .then(data => {
        console.log(JSON.stringify(data));
        registerStudentCookies(data);
        window.location.href = "admin_.html"; 
    }) 
    .catch(error => console.error(error)); 
}

function SignUpStudent(){
    event.preventDefault();
    console.log("signup student");
    let id = create_UUID();
    let course = document.getElementById('r-course').value;
    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    let student_number = document.getElementById('r-student_number').value;
    
    PostData(baseurl+'student/', {
        id:id,
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

function SignUpSupervisor(){
    event.preventDefault();
    console.log("signup supervisor");
    let id = create_UUID();
    let title = document.getElementById('r-title').value;
    let department = document.getElementById('r-department').value;
    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    
    PostData(baseurl+'supervisor/', {
        id:id,
        title:title,
        department:department,
        email:email, 
        name:name,
        password:password,
        phonenumber:phonenumber
    })
    .then(data => {
        console.log(JSON.stringify(data))
        registerSupervisorCookies(data);
        window.location.href = "supervisor_.html"; 
    })
    .catch(error => console.error(error));    
}

function SignUpAdmin(){
    event.preventDefault();
    console.log("signup admin");
    let id = create_UUID();
    let title = document.getElementById('r-title').value;
    let email = document.getElementById('r-email').value;
    let name = document.getElementById('r-name').value;
    let password = document.getElementById('r-password').value;
    let phonenumber = document.getElementById('r-phonenumber').value;
    
    PostData(baseurl+'admin/', {
        id:id,
        title:title,
        email:email, 
        name:name,
        password:password,
        phonenumber:phonenumber
    })
    .then(data => {
        console.log(JSON.stringify(data))
        registerAdminCookies(data);
        window.location.href = "admin_.html"; 
    })
    .catch(error => console.error(error));    
}