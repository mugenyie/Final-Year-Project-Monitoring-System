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
var x_list = [];
function GenerateNames(group_id){
    GetData(baseurl+'student/group/'+group_id+'/members')
    .then(function(data) {
        Getnames(data);
    }) 
    .catch(error => console.error(error)); 
}

function GenerateReport(student_data,){
    let student_list = new Array();
    student_data.forEach(element => {
        student_list.push(element.name);
        x = element.name;
    });
    return student_list;
}