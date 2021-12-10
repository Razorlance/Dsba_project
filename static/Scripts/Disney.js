const line_data = {
    labels: years,
    datasets: [{
        label: 'Number of movies of each year available on Netflix',
        backgroundColor: 'rgb(116, 72, 167,0.4)',
        borderColor: 'rgb(116, 72, 167)',
        data: years_data,
        fill: true
    }]
};

const pie_data = {
    labels: genres,
    datasets: [{
        label: 'My First dataset',
        backgroundColor: [
            'rgb(116, 72, 167, 1)',
            'rgb(116, 72, 167, 0.9)',
            'rgb(116, 72, 167, 0.8)',
            'rgb(116, 72, 167, 0.7)',
            'rgb(116, 72, 167, 0.6)',
            'rgb(116, 72, 167, 0.5)',
            'rgb(116, 72, 167, 0.4)',
            'rgb(116, 72, 167, 0.3)',
            'rgb(116, 72, 167, 0.2)',
            'rgb(116, 72, 167, 0.1)',
            'rgb(116, 72, 167, 0.05)'],
        borderColor: 'rgb(255,255, 255,0)',
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
            'rgb(116, 72, 167, 1)',
            'rgb(116, 72, 167, 0.8)',
            'rgb(116, 72, 167, 0.6)',
            'rgb(116, 72, 167, 0.4)',
            'rgb(116, 72, 167, 0.2)',
            'rgb(116, 72, 167, 0.5)',
            'rgb(116, 72, 167, 0.4)',
            'rgb(116, 72, 167, 0.3)',
            'rgb(116, 72, 167, 0.2)',
            'rgb(116, 72, 167, 0.1)'],
        borderColor: 'rgb(116, 72, 167,0)',
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
            'rgb(116, 72, 167, 1)',
            'rgb(116, 72, 167, 0.9)',
            'rgb(116, 72, 167, 0.8)',
            'rgb(116, 72, 167, 0.7)',
            'rgb(116, 72, 167, 0.6)',
            'rgb(116, 72, 167, 0.5)',
            'rgb(116, 72, 167, 0.4)',
            'rgb(116, 72, 167, 0.3)',
            'rgb(116, 72, 167, 0.2)',
            'rgb(116, 72, 167, 0.1)'],
        borderColor: 'rgb(116, 72, 167,0)',
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
            'rgb(116, 72, 167,1)',
            'rgb(116, 72, 167,0.7)',
            'rgb(116, 72, 167,0.5)'
        ],
        borderWidth: 0
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
                text: "Age categories",
                font: {
                    size: 20,

                },
                padding: {
                    top: 5,
                    bottom: 5
                },
                color: 'rgb(116, 72, 167)'
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
                display: false,
            },
            title: {
                display: true,
                text: "Available languages",
                font: {
                    size: 20,
                },
                padding: {
                    top: 5,
                    bottom: 5
                },
                color: 'rgb(116, 72, 167)'
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