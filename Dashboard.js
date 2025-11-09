// Bar Chart: Examination Results
new Chart(document.getElementById("examChart"), {
  type: "bar",
  data: {
    labels: ["English", "Math", "Arts", "Science", "Physical Education"],
    datasets: [{
      label: "Performance",
      data: [75, 65, 80, 60, 85],
      backgroundColor: ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"]
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true }
    }
  }
});

// Pie Chart: Avg Subject Score
new Chart(document.getElementById("avgScoreChart"), {
  type: "pie",
  data: {
    labels: ["English", "Math", "Arts", "Science", "Physical Education"],
    datasets: [{
      data: [21.43, 17.86, 14.29, 25.00, 21.43],
      backgroundColor: ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"]
    }]
  }
});

// Doughnut Chart: Student by Gender
new Chart(document.getElementById("genderChart"), {
  type: "doughnut",
  data: {
    labels: ["Male", "Female"],
    datasets: [{
      data: [180, 120],
      backgroundColor: ["#4e79a7", "#f28e2b"]
    }]
  }
});

// Horizontal Bar Chart: Participation Rate
new Chart(document.getElementById("participationChart"), {
  type: "bar",
  data: {
    labels: ["English", "Arts", "Math", "Physical Education", "Science"],
    datasets: [{
      label: "Participation (%)",
      data: [85, 80, 75, 65, 60],
      backgroundColor: "#76b7b2"
    }]
  },
  options: {
    indexAxis: 'y',
    scales: {
      x: { beginAtZero: true }
    }
  }
});
