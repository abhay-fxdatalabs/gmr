<template>
  <div class="bar">
    <apexchart
      type="line"
      height="450"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      series: [
        {
          name: "MCP",
          type: "column",
          data: [1.4, 2, 2.5, 1.5, 2.5, 2.8, 3.8, 4.6],
        },

        {
          name: "MCV",
          type: "column",
          data: [1.1, 3, 3.1, 4, 4.1, 4.9, 6.5, 8.5],
        },
      ],
      chartOptions: {
        chart: {
          height: 350,
          width: "20vw",
          type: "line",
          stacked: false,
        },

        dataLabels: {
          enabled: false,
        },
        stroke: {
          width: [1, 1, 4],
        },
        title: {
          text: "MCV vs MCP",
          align: "left",
          offsetX: 50,
          offsetY: 20,

          style: {
            color: "#4d4f5c",
            fontSize: "28px",
            fontFamily: "Roboto",
            fontWeight: 600,
            font: "normal normal normal 28px/34px ",
            letterSpacing: "0px",
            opacity: 1,
          },
        },
        xaxis: {
          colors: "#858585",
          categories: [
            "20May",
            "21May",
            "22May",
            "23May",
            "24May",
            "25May",
            "26May",
            "27May",
          ],
        },
        yaxis: [
          {
            axisTicks: {
              show: true,
            },
            axisBorder: {
              show: true,
              color: "#858585",
            },
            labels: {
              style: {
                colors: "#858585",
              },
            },
            title: {
              text: "MCV",
              style: {
                color: "#858585",
              },
            },
            tooltip: {
              enabled: true,
            },
          },
          {
            seriesName: "MCP",
            opposite: true,
            axisTicks: {
              show: true,
            },
            axisBorder: {
              show: true,
              color: "#858585",
            },
            labels: {
              style: {
                colors: "#858585",
              },
            },
            title: {
              text: "MCP",
              style: {
                color: "#858585",
              },
            },
          },
        ],
        tooltip: {
          fixed: {
            enabled: true,
            position: "topLeft", // topRight, topLeft, bottomRight, bottomLeft
            offsetY: 30,
            offsetX: 60,
          },
        },
        legend: {
          horizontalAlign: "right",
          offsetX: 470,
          position: "top",
        },
        colors: ["#F9A61A", "#E1604B"],
      },
    };
  },
};
</script>
<style scoped>
.bar {
  flex: 1;
}
</style>
