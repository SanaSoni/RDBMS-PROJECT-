// Bar chart: Time spent
new Chart(document.getElementById("barChart"), {
  type: "bar",
  data: {
    labels: ["DSA", "COA", "RDBMS", "MOT", "OOP"],
    datasets: [{
      label: "Hours Spent",
      data: [15, 10, 12, 14, 5],
      backgroundColor: "#3f51b5"
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true }
    }
  }
});

// Circular progress chart
new Chart(document.getElementById("progressChart"), {
  type: "doughnut",
  data: {
    labels: ["Completed", "Remaining"],
    datasets: [{
      data: [100, 0],
      backgroundColor: ["#4caf50", "#e0e0e0"]
    }]
  },
  options: {
    cutout: "70%",
    plugins: {
      tooltip: { enabled: false },
      legend: { display: false }
    }
  }
});

const courseCompletion = [90, 60, 80, 30, 68];

const gpas = courseCompletion.map(p => (p / 100 * 4));

const totalGPA = gpas.reduce((sum, val) => sum + val, 0);
const averageGPA = (totalGPA / gpas.length).toFixed(2);

document.getElementById("gpaScore").textContent = averageGPA;

