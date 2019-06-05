function random_rgba() {
    var o = Math.round, r = Math.random, s = 255;
    return 'rgba(' + o(r()*s) + ',' + o(r()*s) + ',' + o(r()*s) + ',' + r().toFixed(1) + ')';
}

 async function GenerateNames(group_id){
    var config = new Object();
    var chartData = {};
    var x_list = new Array();

    var data = GetData(baseurl+'student/group/'+group_id+'/members')
        .then(groupData => {
    
            groupData.forEach(element => {
                let color = random_rgba();
                let dataset = {
                    label: element.name,
                    backgroundColor: color,
                    borderColor: color,
                    data: [
                        Math.floor(Math.random() * 100),
                        Math.floor(Math.random() * 100),
                        Math.floor(Math.random() * 100),
                        Math.floor(Math.random() * 100),
                        Math.floor(Math.random() * 100),
                        Math.floor(Math.random() * 100),
                        Math.floor(Math.random() * 100),
                        Math.floor(Math.random() * 100)
                    ],
                    fill: false
                }
                x_list.push(dataset);
            });
            
                chartData['type'] = 'line';
                chartData['data'] = {
                    labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8'],
                    datasets: x_list
                };
                chartData['options'] = {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Student Group Performance. (Ploted using chart.js)'
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Week'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Performance (%)'
                            }
                        }]
                    }
                }

            config = JSON.stringify(chartData);
            return config;
        })
        .catch(error => {
            console.error(error);
        });
        
        return await data;
    };