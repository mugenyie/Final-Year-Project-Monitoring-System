function CreateLog(){ 
    event.preventDefault();

    let id = create_UUID();
    let title = document.getElementById('r-title').value;
    let description = document.getElementById('r-description').value;
    let file_links = document.getElementById('r-files').value;
    let source_link = document.getElementById('r-source').value;
    let week = document.getElementById('week_select').value;

    PostData(baseurl+'projectlog/',{
        id:id,
        title:title,
        description:description, 
        files:file_links,
        source_link:source_link,
        student_id:getCookie('id'),
        project_id:getCookie('project_id'),
        group_id:getCookie('group_id'),
        week:week
    })
    .then(data => {
        console.log(data);
        if(data.created_by != 'null'){
            alert("Successfuly Added Log");
        }
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

function displayWeekSelect(){
    var select_items="";
    for(var x = 1; x <= 20; x++){
        select_items+=`<option value="week_${x}">Week ${x}</option>`;
    }
    console.log(select_items);
    document.getElementById('week_select').innerHTML = select_items;
}