function CreateLog(){ 
    event.preventDefault();

    let id = create_UUID();
    let title = document.getElementById('r-title').value;
    let description = document.getElementById('r-description').value;
    let file_links = document.getElementById('r-files').value;
    let source_link = document.getElementById('r-source').value;

    PostData(baseurl+'projectlog/',{
        id:id,
        title:title,
        description:description, 
        files:file_links,
        source_link:source_link,
        student_id:getCookie('id'),
        project_id:getCookie('project_id'),
        group_id:getCookie('group_id')
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error(error));  
}

let log_list = "";
function displayStudentLogs(){
    GetData(baseurl+`projectlog/${getCookie('id')}/student`)
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            log_list += `
            <tr>
            <td>${element.created_on}</td>
            <td>${element.title}</td>
            <td>${element.description}</td>
            <td>${element.score}</td>
            </tr>
            `;
        });
        
        document.getElementById('log_list').innerHTML = log_list;
    })
    .catch(error => console.error(error));  
}