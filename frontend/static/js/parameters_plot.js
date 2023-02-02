$(document).ready(function () {

    $.ajax({
        dataType: "json",
        url: "http://localhost:8090/data",
        success: function (data) {

            $("#plot_spinner").remove()

            // Highcharts
            $("#parameters").append('<div id="parameters_plot" style="height: 400px; min-width: 310px"></div>')

            Highcharts.stockChart('parameters_plot', {
                rangeSelector: {selected: 2},
                title: {text: 'Water Parameters'},
                chart: {displayErrors: true},
                xAxis: {
                    tickInterval: 24 * 3600 * 1000,
                    type: 'datetime',
                },
                series: [
                    {
                        name: 'pH',
                        data: data['ph'],
                        lineWidth: 1,
                        tooltip: {valueDecimals: 1},
                    },
                ],
            });
        }
    });
});