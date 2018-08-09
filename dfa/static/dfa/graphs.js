var urls = [];


function getData(graph_type) {
    // $.ajax({
    //     url: urls[graph_type],
    //     dataType: 'json',
    //     async: true
    // }).done(function(data) {
    $('#' + graph_type).html('');

    am4core.useTheme(am4themes_animated);
    var chart = am4core.create(graph_type, am4charts.XYChart);

    // var data = [];
    // var price1 = 1000;
    // // var price2 = 1200;
    // // var quantity = 30000;
    //
    // for (var i = 0; i < 360; i++) {
    //   price1 += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 100);
    //   data.push({ date1: new Date(2015, 0, i), price1: price1 });
    // }

    // chart.data = data.data;
    chart.dataSource.url = urls[graph_type];
    console.log(urls[graph_type]);
    console.log(chart.data);
    var XValueAxis = chart.xAxes.push(new am4charts.ValueAxis());
    XValueAxis.baseValue = 0;
    XValueAxis.renderer.grid.template.location = 0;
    XValueAxis.renderer.labels.template.fill = am4core.color("#e5262f");


    // var dateAxis2 = chart.xAxes.push(new am4charts.DateAxis());
    // dateAxis2.renderer.grid.template.location = 0;
    // dateAxis2.renderer.labels.template.fill = am4core.color("#dfcc64");

    var YValueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    YValueAxis.renderer.labels.template.fill = am4core.color("#e5262f");
    YValueAxis.renderer.minWidth = 60;

    // var valueAxis2 = chart.yAxes.push(new am4charts.ValueAxis());
    // valueAxis2.tooltip.disabled = true;
    // valueAxis2.renderer.grid.template.strokeDasharray = "2,3";
    // valueAxis2.renderer.labels.template.fill = am4core.color("#dfcc64");
    // valueAxis2.renderer.minWidth = 60;

    var series = chart.series.push(new am4charts.LineSeries());
    series.name = "Nile River Minima";
    series.dataFields.valueX = "year";
    series.dataFields.valueY = "level";
    series.tooltipText = "{valueY.level}";
    series.fill = am4core.color("#e5262f");
    series.stroke = am4core.color("#e5262f");
    // series.strokeWidth = 3;

    // var series2 = chart.series.push(new am4charts.LineSeries());
    // series2.name = "2017";
    // series2.dataFields.dateX = "date2";
    // series2.dataFields.valueY = "price2";
    // series2.yAxis = valueAxis2;
    // series2.xAxis = dateAxis2;
    // series2.tooltipText = "{valueY.value}";
    // series2.fill = am4core.color("#dfcc64");
    // series2.stroke = am4core.color("#dfcc64");
    // //series2.strokeWidth = 3;

    chart.cursor = new am4charts.XYCursor();

    var axisTooltip = XValueAxis.tooltip;
    axisTooltip.background.fill = am4core.color("#07BEB8");
    axisTooltip.background.strokeWidth = 0;
    axisTooltip.background.cornerRadius = 3;
    axisTooltip.background.pointerLength = 0;
    axisTooltip.dy = 5;

    var dropShadow = new am4core.DropShadowFilter();
    dropShadow.dy = 1;
    dropShadow.dx = 1;
    dropShadow.opacity = 0.5;
    axisTooltip.filters.push(dropShadow);

    var scrollbarX = new am4charts.XYChartScrollbar();
    scrollbarX.series.push(series);
    chart.scrollbarX = scrollbarX;

    chart.legend = new am4charts.Legend();
    chart.legend.parent = chart.plotContainer;
    chart.legend.zIndex = 100;

    // valueAxis2.renderer.grid.template.strokeOpacity = 0.07;
    // dateAxis2.renderer.grid.template.strokeOpacity = 0.07;
    XValueAxis.renderer.grid.template.strokeOpacity = 0.1;
    YValueAxis.renderer.grid.template.strokeOpacity = 0.1;
    // setTimeout(moveLinks, 2000);

    // chart.addListener("drawn", moveLinks);
    // charts.push(chart);
    // });
}
