var urls = [];


function makeAmCharts4Graphs(data, graph_type) {
    $('#' + graph_type).html('');
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create(graph_type, am4charts.XYChart);

    chart.data = data.data;
    console.log(data.data);

    var XValueAxis = chart.xAxes.push(new am4charts.ValueAxis());
    XValueAxis.baseValue = 0;
    XValueAxis.renderer.grid.template.location = 0;
    XValueAxis.renderer.labels.template.fill = am4core.color("#e5262f");

    var XValueAxis2 = chart.xAxes.push(new am4charts.ValueAxis());
    XValueAxis2.renderer.grid.template.location = 0;
    XValueAxis2.renderer.labels.template.fill = am4core.color("#2c65df");

    var YValueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    YValueAxis.renderer.labels.template.fill = am4core.color("#e5262f");
    YValueAxis.renderer.minWidth = 60;

    var YValueAxis2 = chart.yAxes.push(new am4charts.ValueAxis());
    YValueAxis2.tooltip.disabled = true;
    YValueAxis2.renderer.grid.template.strokeDasharray = "2,3";
    YValueAxis2.renderer.labels.template.fill = am4core.color("#2c65df");
    YValueAxis2.renderer.minWidth = 60;

    var series = chart.series.push(new am4charts.LineSeries());
    series.name = "Nile River Minima";
    series.dataFields.valueX = "year";
    series.dataFields.valueY = "level";
    series.tooltipText = "{valueY.value}";
    series.fill = am4core.color("#e5262f");
    series.stroke = am4core.color("#e5262f");
    // series.strokeWidth = 3;

    var series2 = chart.series.push(new am4charts.LineSeries());
    series2.name = "Fitted line";
    series2.dataFields.valueX = "year1";
    series2.dataFields.valueY = "level1";
    series2.yAxis = YValueAxis2;
    series2.xAxis = XValueAxis2;
    series2.tooltipText = "{valueY.value}";
    series2.fill = am4core.color("#2c65df");
    series2.stroke = am4core.color("#2c65df");
    series2.strokeWidth = 2;

    chart.cursor = new am4charts.XYCursor();
    chart.cursor.yAxis = YValueAxis;

    var scrollbarX = new am4charts.XYChartScrollbar();
    scrollbarX.series.push(series);
    chart.scrollbarX = scrollbarX;

    chart.legend = new am4charts.Legend();
    chart.legend.parent = chart.plotContainer;
    chart.legend.zIndex = 100;

    XValueAxis2.renderer.grid.template.strokeOpacity = 0.07;
    YValueAxis2.renderer.grid.template.strokeOpacity = 0.07;
    XValueAxis.renderer.grid.template.strokeOpacity = 0.07;
    YValueAxis.renderer.grid.template.strokeOpacity = 0.07;
}


function getData(graph_type) {
    $.ajax({
        url: urls[graph_type],
        dataType: 'json',
        async: true
    }).done(function(data) {
        makeAmCharts4Graphs(data, graph_type);
    });
}
