const line_data = {
    labels: years,
    datasets: [{
        label: 'Number of movies of each year available on Netflix',
        backgroundColor: 'rgb(235, 35, 21,0.4)',
        borderColor: 'rgb(235, 35, 21)',
        data: years_data,
        fill: true
    }]
};

const pie_data = {
    labels: genres,
    datasets: [{
        label: 'My First dataset',
        backgroundColor: [
            'rgba(255, 99, 132)',
            'rgba(255, 159, 64)',
            'rgba(255, 205, 86)',
            'rgba(75, 192, 192)',
            'rgba(54, 162, 235)',
            'rgba(153, 102, 255)',
            'rgba(201, 203, 207)'],
        borderColor: 'rgb(235, 35, 21,0)',
        data: genres_data,
        fill: {
            target: 'My First dataset',
            above: 'rgb(255, 0, 0)',   // Area will be red above the origin
            below: 'rgb(0, 0, 255)'
        }
    }]
};

const pie_age_data = {
    labels: ages,
    datasets: [{
        label: 'My First dataset',
        backgroundColor: [
            'rgba(255, 99, 132)',
            'rgba(255, 159, 64)',
            'rgba(255, 205, 86)',
            'rgba(75, 192, 192)',
            'rgba(54, 162, 235)',
            'rgba(153, 102, 255)',
            'rgba(201, 203, 207)'],
        borderColor: 'rgb(235, 35, 21,0)',
        data: ages_data,
        fill: {
            target: 'My First dataset',
            above: 'rgb(255, 0, 0)',   // Area will be red above the origin
            below: 'rgb(0, 0, 255)'
        }
    }]
};
const pie_language_data = {
    labels: languages,
    datasets: [{
        label: 'My First dataset',
        backgroundColor: [
            'rgba(255, 99, 132)',
            'rgba(255, 159, 64)',
            'rgba(255, 205, 86)',
            'rgba(75, 192, 192)',
            'rgba(54, 162, 235)',
            'rgba(153, 102, 255)',
            'rgba(201, 203, 207)'],
        borderColor: 'rgb(235, 35, 21,0)',
        data: languages_data,
        fill: {
            target: 'My First dataset',
            above: 'rgb(255, 0, 0)',   // Area will be red above the origin
            below: 'rgb(0, 0, 255)'
        }
    }]
};

const configLine = {
    type: 'line',
    data: line_data,
    options: {}
};

const configPie = {
    type: 'pie',
    data: pie_data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            }
        }
    },
};

const bar_data = {
    labels: directors,
    datasets: [{
        label: 'Number of movies for each director',
        data: directors_data,
        backgroundColor: [
            'rgba(255, 99, 132)',
            'rgba(255, 159, 64)',
            'rgba(255, 205, 86)',
            'rgba(75, 192, 192)',
            'rgba(54, 162, 235)',
            'rgba(153, 102, 255)',
            'rgba(201, 203, 207)'
        ],
        borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
            'rgb(153, 102, 255)',
            'rgb(201, 203, 207)'
        ],
        borderWidth: 1
    }]
};

const configBar = {
    type: 'bar',
    data: bar_data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    },
};

const configPieAge = {
    type: 'doughnut',
    data: pie_age_data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text:"Age categories",
                font:{
                    size:20,

                },
                padding: {
                    top: 5,
                    bottom: 5
                },
                color:'rgb(235, 35, 21)'
            }
        }
    },
};

const configPieLanguage = {
    type: 'doughnut',
    data: pie_language_data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                display:false,
            },
            title: {
                display: true,
                text:"Available languages",
                font:{
                    size:20,
                },
                padding: {
                    top: 5,
                    bottom: 5
                },
                color:'rgb(235, 35, 21)'
            }
        }
    },
};
const PieChart = new Chart(
    document.getElementById('PieChart'),
    configPie
);

const LineChart = new Chart(
    document.getElementById('LineChart'),
    configLine
);

const BarChart = new Chart(
    document.getElementById('BarChart'),
    configBar
);

const PieChartAge = new Chart(
    document.getElementById('PieChartAge'),
    configPieAge
);

const PieChartLanguage = new Chart(
    document.getElementById('PieChartLanguage'),
    configPieLanguage
);