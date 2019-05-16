// logout

function logOut(){
    deleteCookie("auth_token");
    window.location.replace('index.html');
}


function getCookie(name) {
    var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return v ? v[2] : null;
}

function deleteCookie(name) { setCookie(name, '', -1); }

function setCookie(name, value, days) {
    var d = new Date;
    d.setTime(d.getTime() + 24*60*60*1000*days);
    document.cookie = name + "=" + value + ";path=/;expires=" + d.toGMTString();
}

function checkToken() {
    var token=getCookie("auth_token");

    console.log("auth_token=> "+token)
    
    if (token == null) {
        window.location.replace('index.html');
    }else{
        document.getElementById("username").textContent=getCookie('name');
    }
}

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