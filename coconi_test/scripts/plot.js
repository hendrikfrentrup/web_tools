$(document).ready(function(){
    var chart = new Highcharts.Chart({
            chart: {
                renderTo: 'container',
                type: 'scatter',
                zoomType: 'xy'
            },
            title: {
                text: 'Heart Rate Deflection Point Test',
                x: -20 //center
            },
            subtitle: {
                text: 'by Hendrik Frentrup',
                x: -20
            },
            xAxis: {
                title: {
                    enabled: true,
                    text: 'Speed (km/h)'
                },
                startOnTick: true,
                endOnTick: true,
                showLastLabel: true
            },
            yAxis: {
                title: {
                    text: 'Heart Rate (bpm)'
                }
            },
    //            legend: {
    //                layout: 'vertical',
    //                align: 'left',
    //                verticalAlign: 'top',
    //                x: 100,
    //                y: 70,
    //                floating: true,
    //                backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
    //                borderWidth: 1
    //            },
            plotOptions: {
                scatter: {
                    marker: {
                        radius: 5,
                        states: {
                            hover: {
                                enabled: true,
                                lineColor: 'rgb(100,100,100)'
                            }
                        }
                    },
                    states: {
                        hover: {
                            marker: {
                                enabled: false
                            }
                        }
                    },
                    tooltip: {
                        headerFormat: '<b>{series.name}</b><br>',
                        pointFormat: '{point.x} km/h, {point.y} bpm'
                    }
                }
            },
            series: [{
                name: 'Your measurements',
                color: 'rgba(223, 83, 83, .5)',
                data: []//[[9.0,100],[9.5,110]]
            }]
    });
    
    // the button action
    $('#plot').click(function() {
        //$('#output').css('background-color','#FF0000')
        chart.series[0].setData(split_data);
    });
    
    $('#splitbutton').click(function() {
        if (splitcounter%1==0){
            //$('#output').css('background-color','#FF0000')
            chart.series[0].setData(split_data);
        }
        
    });
       
});




