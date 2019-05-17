let created_by = getCookie('id');
let auth_token = getCookie('auth_token') == null?"":getCookie('auth_token');
let baseurl = "https://csc-fypms.herokuapp.com/api/v1/";
console.log(created_by);
console.log(auth_token);

async function PostData(url = '', data = {}) {
    // Default options are marked with *
      const response = await fetch(url, {
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'omit',
        method: 'POST',
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
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'omit',
        method: 'GET',
        headers: {
            'api-token': auth_token
        },
    });
    return await response.json(); // parses JSON response into native Javascript objects 
}

async function UpdateData(url = '', data = {}) {
    // Default options are marked with *
      const response = await fetch(url, {
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'omit',
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'api-token': auth_token
        },
        body: JSON.stringify(data),
    });
    return await response.json(); // parses JSON response into native Javascript objects 
}

function create_UUID(){
    var dt = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (dt + Math.random()*16)%16 | 0;
        dt = Math.floor(dt/16);
        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
    });
    return uuid;
}

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