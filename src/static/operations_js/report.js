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
    var student_list = new Array();

    GetData(baseurl+'student/group/'+group_id+'/members')
    .then(function(data) {
        data.forEach(element => {
            student_list.push(element.name);
        });
    }) 
    .catch(error => console.error(error)); 
    console.log(student_list);
    return ['a','b','c'];
}