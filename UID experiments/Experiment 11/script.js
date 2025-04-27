// script.js

// Data for the Pie Chart (Product Category Distribution)
const pieData = {
  labels: ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"],
  datasets: [
    {
      label: "Product Category Distribution",
      data: [15, 30, 25, 10, 20], // Percentage of products in each category
      backgroundColor: ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FFFB33"],
      hoverOffset: 4,
    },
  ],
};

// Pie Chart Configuration
const pieConfig = {
  type: "pie",
  data: pieData,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      tooltip: {
        callbacks: {
          label: function (tooltipItem) {
            return tooltipItem.label + ": " + tooltipItem.raw + "%";
          },
        },
      },
    },
  },
};

// Data for the Bar Chart (Stock Quantity per Item)
const barData = {
  labels: ["Laptop", "Shirt", "Apple", "Sofa", "Doll"],
  datasets: [
    {
      label: "Stock Quantity",
      data: [50, 120, 200, 30, 100], // Quantity of each item in stock
      backgroundColor: "#4CAF50",
      borderColor: "#388E3C",
      borderWidth: 1,
    },
  ],
};

// Bar Chart Configuration
const barConfig = {
  type: "bar",
  data: barData,
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        callbacks: {
          label: function (tooltipItem) {
            return tooltipItem.raw + " units";
          },
        },
      },
    },
  },
};

// Render the Pie Chart
const pieChartCtx = document.getElementById("pieChart").getContext("2d");
new Chart(pieChartCtx, pieConfig);

// Render the Bar Chart
const barChartCtx = document.getElementById("barChart").getContext("2d");
new Chart(barChartCtx, barConfig);
