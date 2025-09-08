async function fetchData() {
    const res = await fetch('/traffic-data');
    return await res.json();
}

const packetCtx = document.getElementById('packetChart').getContext('2d');
const speedCtx = document.getElementById('speedChart').getContext('2d');

let packetChart = new Chart(packetCtx, {
    type: 'line',
    data: { labels: [], datasets: [{ label: 'Packets', data: [] }] }
});

let speedChart = new Chart(speedCtx, {
    type: 'line',
    data: { 
        labels: [], 
        datasets: [
            { label: 'Upload (MB)', data: [] },
            { label: 'Download (MB)', data: [] }
        ]
    }
});

setInterval(async () => {
    let data = await fetchData();
    let time = new Date().toLocaleTimeString();

    packetChart.data.labels.push(time);
    packetChart.data.datasets[0].data.push(data.packets);
    packetChart.update();

    speedChart.data.labels.push(time);
    speedChart.data.datasets[0].data.push(data.upload_speed);
    speedChart.data.datasets[1].data.push(data.download_speed);
    speedChart.update();
}, 2000);
