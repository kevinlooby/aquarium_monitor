$(document).ready(function () {

    $.ajax({
        dataType: "json",
        url: "http://192.168.1.228:8090/data",
        success: function (data) {

            $("#plot_spinner").remove()

            // Highcharts
            $("#parameters").append('<div id="parameters_plot" style="height: 400px; min-width: 310px"></div>')

            const chart = Highcharts.stockChart('parameters_plot', {
                title: {text: 'Water Parameters'},
                chart: {
                    displayErrors: true,
                    zoomType: 'x',
                },


                yAxis: [
                {
                    title: {
                        text: 'Temperature',
                    },
                    labels: {
                        format: '{value} °C',
                    },
                },
                {
                    title: {
                        text: 'pH',
                    },
                    labels: {
                        format: '{value}',
                    },
                    min: 5.5,
                    max: 8.5,
                    opposite: false,
                }],

                series: [
                    {
                        name: 'Water Temperature',
                        id: 'temp-water',
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
                        name: 'Ambient Temperature',
                        id: 'temp-ambient',
                        data: (() => {
                            return data['temperature_ambient'].map(function(point) {
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
                        id: 'ph',
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
                    ordinal: false,
                    type: 'datetime',
//                    tickInterval: 6 * 3600 * 1000,
                    labels: {
                        format: '{value:%Y-%b-%e %l:%M %p }'
                    },
                },
                tooltip: {shared: true},
            },

                document.getElementById('temp-water-toggle').addEventListener('click', () => {
                    const series = chart.get('temp-water');

                    if (series.visible) {
                        series.hide();
                    } else {
                        series.show();
                    }
                }),

                document.getElementById('temp-ambient-toggle').addEventListener('click', () => {
                    const series = chart.get('temp-ambient');

                    if (series.visible) {
                        series.hide();
                    } else {
                        series.show();
                    }
                }),

                document.getElementById('ph-toggle').addEventListener('click', () => {
                    const series = chart.get('ph');

                    if (series.visible) {
                        series.hide();
                    } else {
                        series.show();
                    }
                }),
            )
        }
    });
});