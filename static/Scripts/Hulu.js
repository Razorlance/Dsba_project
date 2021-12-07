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
    "Comedy",
    "Drama",
    "Thriller"
]


const line_data = {
    labels: month_labels,
    datasets: [{
        label: 'My First dataset',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [0, 10, 5, 2, 20, 30, 45],
    }]
};
const pie_data = {
    labels: movie_labels,
    datasets: [{
        label: 'My First dataset',
        backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(19, 92, 43)',
            'rgb(91, 217, 133)',
            'rgb(66, 122, 98)',
            'rgb(3, 107, 62)'
        ],

        borderColor: 'rgb(0,0,0,0)',
        data: [0, 10, 5, 2, 20, 30, 45],
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
