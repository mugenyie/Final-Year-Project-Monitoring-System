function CreateOrUpdateProject(){
    event.preventDefault();
    var project = GetProject(getCookie('project_id'));
    console.log(project);
    if(project == null){
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
    fetch(baseurl+'project/', {
        method: 'POST',
        mode:"no-cors",
        headers : {
            'Content-Type': 'application/json',
            'api-token': getCookie('auth_token')
        },
        body:JSON.stringify({
            id:id,
            name:name,
            git_url:git, 
            web_url:web,
            proposal_file:proposal,
            documentation_file:documentation,
            description:description,
            created_by:getCookie('id')
        })
    }); 
    setCookie('project_id')=id;
}

function GetProject(){
    if(getCookie('project_id') != 'null'){
        GetData(baseurl+'project/'+getCookie('project_id'))
        .then(data => {
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

function UpdateProject(){
    UpdateData(baseurl+'project/', {
        name:name,
        git_url:git, 
        web_url:web,
        proposal_file:proposal,
        documentation_file:documentation,
        description:description
    })
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error));  
}