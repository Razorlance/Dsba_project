const month_labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
];

const movie_labels = [
    "Horror",
    "Action",
    "Comedy"
]

const line_data = {
    labels: years,
    datasets: [{
        label: 'Number of movies during each year available on Netflix',
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
            },
            title: {
                display: true,
            }
        }
    },
};

const bar_data = {
    labels: month_labels,
    datasets: [{
        label: 'My First Dataset',
        data: [65, 59, 80, 81, 56, 55, 40],
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
