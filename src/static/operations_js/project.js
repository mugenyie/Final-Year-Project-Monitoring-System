function CreateOrUpdateProject(){
    event.preventDefault();
    if(getCookie('project_id') == 'null' || getCookie('project_id') == 'undefined'){
        CreateProject(
            document.getElementById('r-project_name').value,
            document.getElementById('r-git_url').value,
            document.getElementById('r-web_url').value,
            document.getElementById('r-proposal_file').value,
            document.getElementById('r-documentation_file').value,
            document.getElementById('r-description').value
        );
    }else{
        UpdateProject(
            document.getElementById('r-project_name').value,
            document.getElementById('r-git_url').value,
            document.getElementById('r-web_url').value,
            document.getElementById('r-proposal_file').value,
            document.getElementById('r-documentation_file').value,
            document.getElementById('r-description').value
        );
    }
}

function CreateProject(name,git,web,proposal,documentation,description){ 
    let id = create_UUID();
    PostData(baseurl+'project/',{
        id:id,
        name:name,
        git_url:git, 
        web_url:web,
        proposal_file:proposal,
        documentation_file:documentation,
        description:description,
        created_by:getCookie('id'),
        group_id:getCookie('group_id')
    })
    .then(data => {
        console.log(data);
        updateGroupProjectId(data.id);
        setCookie('project_id', data.id);
    })
    .catch(error => console.error(error));  
}

function GetProject(){
    if(getCookie('project_id') != 'null'){
        GetData(baseurl+'project/'+getCookie('project_id'))
        .then(data => {
            console.log(data)
            document.getElementById('r-project_name').value = data.name;
            document.getElementById('r-git_url').value = data.git_url;
            document.getElementById('r-web_url').value = data.web_url;
            document.getElementById('r-proposal_file').value = data.proposal_file;
            document.getElementById('r-documentation_file').value = data.documentation_file;
            document.getElementById('r-description').value = data.description;
        })
        .catch(error => console.error(error));  
    }
}

function UpdateProject(name,git,web,proposal,documentation,description){
    UpdateData(baseurl+'project/'+getCookie('project_id'), {
        name:name,
        git_url:git, 
        web_url:web,
        proposal_file:proposal,
        documentation_file:documentation,
        description:description,
        group_id:getCookie('group_id')
    })
    .then(data => console.log(data))
    .catch(error => console.error(error));  
}

function updateGroupProjectId(project_id){
    UpdateData(baseurl+`groups/${getCookie('group_id')}/update`, {
        project_id:project_id
    })
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error)); 
}