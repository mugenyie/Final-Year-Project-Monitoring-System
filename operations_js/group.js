// document.getElementById('r-group_name').value = getCookie('group_name');
// document.getElementById('r-group_number').value = getCookie('group_name');

function GetUserGroup(){
    GetData(baseurl+'group/'+getCookie('group_id'))
    .then(data => {
        console.log(JSON.stringify(data));
        setCookie('group_id', data.id, 30);
        setCookie('group_name', data.name, 30);
        setCookie('group_number', data.number, 30);
    })
    .catch(error => console.error(error));  
}

async function CreateGroup(){
    event.preventDefault()

    await createNewGroup(document.getElementById('r-group_name').value, document.getElementById('r-group_number').value)
    //Update my group id
    updateStudent();
}

function createNewGroup(name, number){
    console.log("Create group");
    PostData(baseurl+'group/', {
        name:name,
        number:number,
        created_by:created_by
    })
    .then(data => {
        console.log(JSON.stringify(data));
        setCookie('group_id', data.id, 30);
    })
    .catch(error => console.error(error));  
}

function updateStudent(){
    UpdateData(baseurl+'student/me', {
        group_id:getCookie('group_id')
    })
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error)); 
}