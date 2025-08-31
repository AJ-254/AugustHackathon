async function fetchData() {
    const res = await fetch('/get_data');
    const data = await res.json();

    const labels = data.map((_, index) => `Entry ${index + 1}`);
    const scores = data.map(item => item[1]); // mood_score
    const colors = data.map(item => item[0] === "POSITIVE" ? 'green' : 'red');

    const ctx = document.getElementById('moodChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Mood Score',
                data: scores,
                borderColor: 'blue',
                fill: false,
                pointBackgroundColor: colors, // color the points
                pointRadius: 6
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

window.onload = fetchData;
