$(document).ready(function () {

    $.ajax({
        dataType: "json",
        url: "http://192.168.1.228:8090/data",
        success: function (data) {

            $("#plot_spinner").remove()

            // Highcharts
            $("#parameters").append('<div id="parameters_plot" style="height: 400px; min-width: 310px"></div>')

            Highcharts.stockChart('parameters_plot', {
//                rangeSelector: {selected: 2},
                title: {text: 'Water Parameters'},
                chart: {
                    displayErrors: true,
                    zoomType: 'x',
                },
                tooltip: {shared: true},

                yAxis: [{
                    title: {
                        text: 'Water Temperature',
                    },
                    labels: {
                        format: '{value} °C',
                    },
                    opposite: false,
                },
                {
                    title: {
                        text: 'pH',
                    },
                    labels: {
                        format: '{value}',
                    },
                    min: 5.5,
//                    minRange: 8,
                    max: 8.5,
                }],

                series: [
                    {
                        name: 'Temperature',
                        data: (() => {
                            return data['temperature'].map(function(point) {
                            return [Date.parse(point[0]), point[1]]})
                        })(),
                        type: 'line',
                        lineWidth: 1,
                        tooltip: {
                            valueDecimals: 2,
                            valueSuffix: ' °C'
                        },
                        yAxis: 0,
                    },
                    {
                        name: 'pH',
                        data: (() => {
                            return data['ph'].map(function(point) {
                            return [Date.parse(point[0]), point[1]]})
                        })(),
                        type: 'line',
                        lineWidth: 1,
                        tooltip: {valueDecimals: 2},
                        yAxis: 1,
                    },
                ],

                xAxis: {
//                    ordinal: false,
                    type: 'datetime',
//                    categories: data['temperature'][0],
                    labels: {
                        format: '{value:%Y-%b-%e %l:%M %p }'
                    },
                },
            });
        }
    });
});