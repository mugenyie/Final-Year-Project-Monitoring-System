let supervisor_list = "";
let count = 0;
function displaySupervisors(){
    GetData(baseurl+'supervisor/')
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            count+=1;
            supervisor_list += `
            <tr>
            <td>${element.name}</td>
            <td>${element.title}</td>
            <td>${element.department}</td>
            <td>${element.email}</td>
            <td>${element.phonenumber}</td>
            <td>${element.created_on}</td>
            </tr>
            `;
        });
        
        document.getElementById('supervisor-list').innerHTML = supervisor_list;
        document.getElementById('count').textContent = count;
    })
    .catch(error => console.error(error));  
}