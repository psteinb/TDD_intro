google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Category', 'Landmark Publications'],
        ['Reproducible',     6],
        ['Irreproducible',      47]
    ]);

    var options = {
        title: '53 Selected Studies',
        pieHole: 0.4,
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
}
