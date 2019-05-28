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
    let id = create_UUID();
    await createNewGroup(id,document.getElementById('r-group_name').value, document.getElementById('r-group_number').value)
}

function createNewGroup(id,name, number){
    console.log("Create group");
    PostData(baseurl+'group/', {
        id:id,
        name:name,
        number:number,
        created_by:created_by
    })
    .then(data => {
        console.log(JSON.stringify(data));
        updateMyGroupId(data.id);
        setCookie('group_id', data.id, 30);
    })
    .catch(error => console.error(error));  
}

function updateMyGroupId(group_id){
    UpdateData(baseurl+'student/me', {
        group_id:id
    })
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error)); 
}

let unassigned_list = "";
let group_count = 0;
function displayUnassigned(){
    GetData(baseurl+'groups/unassigned')
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            group_count+=1;
            unassigned_list += `
            <tr>
            <td>${element.name}</td>
            <td>${element.number}</td>
            <td>${element.project_id}</td>
            <td>${element.supervisor_id}</td>
            <td>${element.created_on}</td>
            <td><a href="edit_group?id=${element.id}">edit</a></td>
            </tr>
            `;
        });
        
        document.getElementById('group-list').innerHTML = unassigned_list;
        document.getElementById('group-count').textContent = group_count;
    })
    .catch(error => console.error(error));  
}

let assigned_list = "";
let group_count_assigned = 0;
function displayAssigned(){
    GetData(baseurl+'groups/assigned')
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            group_count_assigned+=1;
            assigned_list += `
            <tr>
            <td>${element.name}</td>
            <td>${element.number}</td>
            <td>${element.project_id}</td>
            <td>${element.supervisor_id}</td>
            <td>${element.created_on}</td>
            <td><a href="edit_group?id=${element.id}">edit</a></td>
            </tr>
            `;
        });
        
        document.getElementById('group-list').innerHTML = assigned_list;
        document.getElementById('group-count').textContent = group_count_assigned;
    })
    .catch(error => console.error(error));  
}

group_detail = "";
function editGroup(){
    var group_id = window.location.search.substr(1)
    GetData(baseurl+`group/${group_id.slice(3)}`)
    .then(data => {
        console.log(JSON.stringify(data));
        group_detail = `
            <p>Name: ${data.name}</p>
            <p>Number: ${data.number}</p>
            <p>Project Id: ${data.project_id}</p>
            <p>Supervisor Id: ${data.supervisor_id}</p>
        `;
        document.getElementById('group-detail').innerHTML = group_detail;
    })
    .catch(error => console.error(error));  
}

available = '<option value="">Select Supervisor</option>';
function availableSupervisors(){
    GetData(baseurl+'supervisor/')
    .then(data => {
        data.forEach(element => {
            available += `
            <option value="${element.id}">${element.name}</option>
            `;
        });
        document.getElementById('available-supervisors').innerHTML = available;
    })
    .catch(error => console.error(error));  
}

function UpdateGroupSupervisor(){
    event.preventDefault();
    let group_id = window.location.search.substr(1).slice(3)
    let supervisor_id = document.getElementById('available-supervisors').value;

//     var x =UpdateData(baseurl+`groups/${group_id}/update`, JSON.stringify({supervisor_id:supervisor_id}))
// console.log(x);
    fetch(baseurl+`groups/${group_id}/update`,{
        method: 'PATCH',
        mode: 'cors',
        headers: {
            'api-token': getCookie('auth_token')
        },
        body: JSON.stringify({supervisor_id:supervisor_id})
    })
    .then(data => {
        console.log(JSON.stringify(data));
    })
    .catch(error => console.error(error)); 
}