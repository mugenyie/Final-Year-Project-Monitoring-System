// var GraphData = new google.visualization.DataTable();
// GraphData.addColumn('number', 'Week'); 

// function GenerateReport(group_id){
//     GetData(baseurl+`projectlog/${group_id}/group`)
//     .then(data => {
//         console.log(JSON.stringify(data));
//         data.forEach(element => {
            
//         });
//         document.getElementById('group_log').innerHTML = group_log;
//     })
//     .catch(error => console.error(error));
// }

function GenerateNames(group_id){
    var x;
    GetData(baseurl+'student/group/'+group_id+'/members')
    .then(function(data) {
        return Getname(data);
    }) 
    .catch(error => console.error(error)); 
}

function Getname(data){
    let student_list = new Array();
    data.forEach(element => {
        student_list.push(element.name);
        x = element.name;
    });
    return student_list;
}