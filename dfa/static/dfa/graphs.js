var urls = [];


function showCalculatedData(formula_list, f_l_list, f_l_average, alpha){
    var calculated_data_div = $('#calculated_data_container');
    calculated_data_div.empty();

    var div = "<p style='font-size:120%; font-weight:bold;'>Alpha = " + alpha.toString() + "</p>";
    div += "<p style='font-size:120%; font-weight:bold;'>Average F(L) = " + f_l_average.toString() + "</p>";

    div += "<p style='font-size:120%; font-weight:bold; font-style:italic;'>The fitted functions: </p>";
    calculated_data_div.append(div);
    for (var i = 0; i < formula_list.length; ++i){
        div = "<div>" + formula_list[i] + "</div>";
        calculated_data_div.append(div);
    }
}


function makeDynamicSeries(calculated_data, segments_number) {
    var series;
    var series_list = [{
        id: "s1",
        type: "LineSeries",
        dataFields: {
            valueX: "year",
            valueY: "level"
        },
        name: "Nile River Minima",
        fill: am4core.color("#e5262f"),
        stroke: am4core.color("#e5262f"),
        strokeWidth: 1.5
    }];

    for (var i = 0; i < segments_number; ++i) {
        series = {
            id: "s" + (i + 2).toString(),
            type: "LineSeries",
            dataFields: {
                valueX: "year" + i.toString(),
                valueY: "level" + i.toString()
            },
            fill: am4core.color("#2c65df"),
            stroke: am4core.color("#2c65df"),
            strokeWidth: 3
        };
        if (i === 0) {
            series["name"] = "Fitted line/lines";
        }
        series_list.push(series);
    }
    return series_list;
}


function buildAmCharts4Graphs(data, graph_type) {
    var sample_data = data.sample_data;
    var calculated_data = data.calculated_data;
    var segments_number = data.segments_number;
    var formula_list = data.formula_list;
    var f_l_list = data.f_l_list;
    var f_l_average = data.f_l_average;
    var alpha = data.alpha;

    console.log(formula_list);
    console.log("\nF(L) for each segments = \n", f_l_list);
    console.log("\nF(L) average = ", f_l_average);
    console.log("\nALPHA = ", alpha);

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

    // Creating chart using json config.
    var chart = am4core.createFromConfig({
        data: sample_data.concat(calculated_data),
        // The X axes which will show years.
        xAxes: [
        // The X value axis for original data.
        {
            type: "ValueAxis",
            StrictMinMax: true,
            min: min_x,
            max: max_x
        }],
        // The Y axes which will show levels.
        yAxes: [
        // The Y value axis for original data.
        {
            type: "ValueAxis",
            StrictMinMax: true,
            min: min_y,
            max: max_y
        }],
        series: makeDynamicSeries(calculated_data, segments_number),
        scrollbarX: {
            series: [{
                id: "s1"
            }]
        },
        export: {
            enabled: true
        }

    }, graph_type, am4charts.XYChart);


    chart.cursor = new am4charts.XYCursor();
    chart.cursor.yAxis = chart.yAxes[0];

    // Overriding graphs legend, otherwise it will have (n + 1) segments_number legends.
    chart.legend = new am4charts.Legend();
    chart.legend.data = [{
        name: "Nile River Minima",
        fill: am4core.color("#e5262f")
    },{
        name: "Fitted line/lines",
        fill: am4core.color("#2c65df")
    }];

    showCalculatedData(formula_list, f_l_list, f_l_average, alpha);
}


function getDataThenBuildGraph(graph_type) {
    $.ajax({
        url: 'get_data/classic_dfa/',
        dataType: 'json',
        async: true
    }).done(function(data) {
        buildAmCharts4Graphs(data, graph_type);
    });
}
