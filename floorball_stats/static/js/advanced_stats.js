document.addEventListener("DOMContentLoaded", () => {
  // Set the default font sizes...
  Chart.defaults.font.size = 14;
  Chart.defaults.font.weight = "bold";

  Chart.defaults.plugins.legend.labels.font = {
    size: 18,
    weight: "bold",
  };

  Chart.defaults.plugins.tooltip.titleFont = {
    size: 14,
    weight: "bold",
  };

  Chart.defaults.plugins.tooltip.bodyFont = {
    size: 13,
  };

  Chart.defaults.scale.ticks.font = {
    size: 14,
    weight: "bold",
  };

  const modal = document.getElementById("chartModal");
  const modalCtx = document.getElementById("modalChart");
  const gameLabels = JSON.parse(
    document.getElementById("game-labels").textContent,
  );
  const gameDetails = JSON.parse(
    document.getElementById("game-details").textContent,
  );
  const rollingGoals = JSON.parse(
    document.getElementById("our-rolling-goals").textContent,
  );
  const rollingGoalsP1 = JSON.parse(
    document.getElementById("our-rolling-goals-p1").textContent,
  );
  const rollingGoalsP2 = JSON.parse(
    document.getElementById("our-rolling-goals-p2").textContent,
  );
  const rollingGoalsP3 = JSON.parse(
    document.getElementById("our-rolling-goals-p3").textContent,
  );
  const opprollingGoals = JSON.parse(
    document.getElementById("opp-rolling-goals").textContent,
  );
  const opprollingGoalsP1 = JSON.parse(
    document.getElementById("opp-rolling-goals-p1").textContent,
  );
  const opprollingGoalsP2 = JSON.parse(
    document.getElementById("opp-rolling-goals-p2").textContent,
  );
  const opprollingGoalsP3 = JSON.parse(
    document.getElementById("opp-rolling-goals-p3").textContent,
  );
  const rollingShots = JSON.parse(
    document.getElementById("our-rolling-shots").textContent,
  );

  let modalChartInstance = null;

  // Helper function for tooltip showing opponent team name
  function createTooltipCallbacks(gameDetails) {
    return {
      plugins: {
        tooltip: {
          callbacks: {
            title: function (context) {
              const index = context[0].dataIndex;
              return gameDetails[index]; // custom label
            },
          },
        },
      },
    };
  }

  // Store chart configs so we can reuse them
  const chartConfigs = {
    goalsChart: {
      type: "line",
      data: {
        labels: gameLabels,
        datasets: [
          {
            label: "Gjorda Mål",
            data: rollingGoals,
            borderWidth: 4,
            borderColor: "#1f77b4", // blue
            fill: false,
            tension: 0.3,
            pointRadius: 4,
          },
        ],
      },

      // For tooltip showing opponent team name
      options: {
        ...createTooltipCallbacks(gameDetails),
      },
    },
    goalsChart_full: {
      type: "line",
      data: {
        labels: gameLabels,
        datasets: [
          {
            label: "Totalt",
            data: rollingGoals,
            borderWidth: 4,
            borderColor: "#1f77b4", // blue
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
          {
            label: "Period 1",
            data: rollingGoalsP1,
            borderColor: "#2ca02c", // green
            borderDash: [5, 5],
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
          {
            label: "Period 2",
            data: rollingGoalsP2,
            borderColor: "#ff7f0e", // orange
            borderDash: [10, 5],
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
          {
            label: "Period 3",
            data: rollingGoalsP3,
            borderColor: "#d62728", // red
            borderDash: [2, 2],
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
        ],
      },

      // For tooltip showing opponent team name
      options: {
        ...createTooltipCallbacks(gameDetails),
      },
    },

    oppgoalsChart: {
      type: "line",
      data: {
        labels: gameLabels,
        datasets: [
          {
            label: "Insläppta Mål",
            data: opprollingGoals,
            borderWidth: 4,
            borderColor: "#1f77b4", // blue
            fill: false,
            tension: 0.3,
            pointRadius: 4,
          },
        ],
      },

      // For tooltip showing opponent team name
      options: {
        ...createTooltipCallbacks(gameDetails),
      },
    },
    oppgoalsChart_full: {
      type: "line",
      data: {
        labels: gameLabels,
        datasets: [
          {
            label: "Totalt",
            data: opprollingGoals,
            borderWidth: 4,
            borderColor: "#1f77b4", // blue
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
          {
            label: "Period 1",
            data: opprollingGoalsP1,
            borderColor: "#2ca02c", // green
            borderDash: [5, 5],
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
          {
            label: "Period 2",
            data: opprollingGoalsP2,
            borderColor: "#ff7f0e", // orange
            borderDash: [10, 5],
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
          {
            label: "Period 3",
            data: opprollingGoalsP3,
            borderColor: "#d62728", // red
            borderDash: [2, 2],
            fill: false,
            tension: 0.3,
            pointRadius: 5,
          },
        ],
      },

      // For tooltip showing opponent team name
      options: {
        ...createTooltipCallbacks(gameDetails),
      },
    },

    shotsChart: {
      type: "line",
      data: {
        labels: gameLabels,
        datasets: [
          {
            label: "Skott",
            data: rollingShots,
          },
        ],
      },
    },
  };

  // Attach click to each chart card
  document.querySelectorAll(".chart-card").forEach((card) => {
    card.addEventListener("click", () => {
      const canvas = card.querySelector("canvas");
      const id = canvas.id;

      modal.style.display = "block";

      // Destroy previous chart
      if (modalChartInstance) {
        modalChartInstance.destroy();
      }

      // Use FULL version if available for fullscreen
      const fullConfig = chartConfigs[id + "_full"] || chartConfigs[id];

      modalChartInstance = new Chart(modalCtx, fullConfig);
    });
  });

  // Helper function to close model
  function closeModal() {
    modal.style.display = "none";

    if (modalChartInstance) {
      modalChartInstance.destroy();
      modalChartInstance = null;
    }
  }

  // Close modal on click
  modal.addEventListener("click", closeModal);

  // Close modal on esc key
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeModal();
    }
  });

  Object.keys(chartConfigs).forEach((chartId) => {
    const ctx = document.getElementById(chartId);

    if (ctx) {
      new Chart(ctx, chartConfigs[chartId]);
    }
  });
});
