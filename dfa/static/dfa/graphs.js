var urls = [];


function buildAmCharts4Graphs(data, graph_type) {
    var sample_data = data.sample_data;
    var calculated_data = data.calculated_data;
    var segments_number = data.segments_number;

    // Used to synchronize all graphs Y axes's minimum and maximum values.
    var min_y = data.min_y;
    var max_y = data.max_y;

    // Used to synchronize all graphs X axes's minimum and maximum values.
    var min_x = data.min_x;
    var max_x = data.max_x;

    // Selecting and clearing the <div> element using its pre-initialized id.
    // e.g.: 'classic_dfa' or 'modified_dfa'.
    $('#' + graph_type).html('');

    // Setting the animated theme for am4core.
    // am4core.useTheme(am4themes_animated);

    // Creating the XYChart using the graphs type (e.g.: 'classic_dfa')
    var chart = am4core.create(graph_type, am4charts.XYChart);
    // Adding the pre-calculated data to newly created chart's data field.
    chart.data = sample_data;

    // console.log("Calculated data = \n", chart.data);

    var XValueAxis = chart.xAxes.push(new am4charts.ValueAxis());
    XValueAxis.min = min_x;
    XValueAxis.max = max_x;
    XValueAxis.baseValue = 0;
    XValueAxis.renderer.grid.template.location = 0;
    XValueAxis.renderer.labels.template.fill = am4core.color("#e5262f");

    var YValueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    YValueAxis.min = min_y;
    YValueAxis.max = max_y;
    YValueAxis.StrictMinMax = true;
    YValueAxis.renderer.labels.template.fill = am4core.color("#e5262f");
    YValueAxis.renderer.minWidth = 60;

    var series = chart.series.push(new am4charts.LineSeries());
    series.name = "Nile River Minima";
    series.dataFields.valueX = "year";
    series.dataFields.valueY = "level";
    series.tooltipText = "{valueY.value}";
    series.fill = am4core.color("#e5262f");
    series.stroke = am4core.color("#e5262f");
    // series.strokeWidth = 3;

    chart.cursor = new am4charts.XYCursor();
    chart.cursor.yAxis = YValueAxis2;

    var scrollbarX = new am4charts.XYChartScrollbar();
    scrollbarX.series.push(series);
    chart.scrollbarX = scrollbarX;

    chart.legend = new am4charts.Legend();
    chart.legend.parent = chart.plotContainer;
    chart.legend.zIndex = 100;

    XValueAxis.renderer.grid.template.strokeOpacity = 0.07;
    YValueAxis.renderer.grid.template.strokeOpacity = 0.07;

    // console.log(chart);

    // for (var i = 0; i < segments_number; ++i) {
    //     eval ("var XValueAxis" + i + "= chart.xAxes.push(new am4charts.ValueAxis());");
    var XValueAxis2 = chart.xAxes.push(new am4charts.ValueAxis());
    XValueAxis2.min = min_x;
    XValueAxis2.max = max_x;
    XValueAxis2.renderer.grid.template.location = 0;
    XValueAxis2.renderer.labels.template.fill = am4core.color("#2c65df");

    var YValueAxis2 = chart.yAxes.push(new am4charts.ValueAxis());
    YValueAxis2.min = min_y;
    YValueAxis2.max = max_y;
    YValueAxis2.tooltip.disabled = true;
    YValueAxis2.renderer.grid.template.strokeDasharray = "2,3";
    YValueAxis2.renderer.labels.template.fill = am4core.color("#2c65df");
    YValueAxis2.renderer.minWidth = 60;

    var series2 = chart.series.push(new am4charts.LineSeries());
    series2.name = "Fitted line/lines";
    series2.dataFields.valueX = "year0";
    series2.dataFields.valueY = "level0";
    series2.yAxis = YValueAxis2;
    series2.xAxis = XValueAxis2;
    series2.tooltipText = "{valueY.value}";
    series2.fill = am4core.color("#2c65df");
    series2.stroke = am4core.color("#2c65df");
    series2.strokeWidth = 2;

    XValueAxis2.renderer.grid.template.strokeOpacity = 0.07;
    YValueAxis2.renderer.grid.template.strokeOpacity = 0.07;

}


function getDataThenBuildGraph(graph_type) {
    console.log(urls[graph_type]);
    $.ajax({
        url: 'get_data/classic_dfa/',
        dataType: 'json',
        async: true
    }).done(function(data) {
        buildAmCharts4Graphs(data, graph_type);
    });
}
