function displaySiteStat(){
    GetData(baseurl+'statistics/')
    .then(data => {
        console.log(JSON.stringify(data));
        document.getElementById('admin-count').textContent = data.admin;
        document.getElementById('student-count').textContent = data.student;
        document.getElementById('group-count').textContent = data.group;
        document.getElementById('supervisor-count').textContent = data.supervisor;
    })
    .catch(error => console.error(error));  
}