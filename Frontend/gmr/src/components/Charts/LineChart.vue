<template>
  <div id="line">
    <apexchart
      type="line"
      height="450"
      width="600"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
export default {
  name: "App",

  data: function() {
    return {
      chartOptions: {
        chart: {
          height: 350,
          width: "20vw",
          type: "line",
          zoom: {
            enabled: false,
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          width: [2, 3, 5],
          curve: "straight",
          dashArray: [0, 0, 7],
        },
        title: {
          text: "DAM MCP Prediction",
          align: "left",
          offsetX: 20,
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
        legend: {
          tooltipHoverFormatter: function(val, opts) {
            return (
              val +
              " - " +
              opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex] +
              ""
            );
          },
          horizontalAlign: "right",
          offsetX: 350,

          position: "top",
        },
        markers: {
          size: 0,
          hover: {
            sizeOffset: 6,
          },
        },
        xaxis: {
          categories: [
            "01 am",
            "02 am",
            "03 am",
            "04 am",
            "05 am",
            "06 am",
            "07 am",
            "08 am",
            "09 am",
            "10 am",
            "11 am",
            "12 pm",
            "01 pm",
            "02 pm",
            "03 pm",
            "04 pm",
            "05 pm",
            "06 pm",
            "07 pm",
            "08 pm",
            "09 pm",
            "10 pm",
            "11 pm",
            "12 am",
          ],
        },
        yaxis: {
          min: 0,
          max: 3000,
          stepSize: 100,
          reverse: false,
          beginAtZero: true,
        },

        tooltip: {
          y: [
            {
              title: {
                formatter: function(val) {
                  return val + " (mins)";
                },
              },
            },
            {
              title: {
                formatter: function(val) {
                  return val + " per session";
                },
              },
            },
            {
              title: {
                formatter: function(val) {
                  return val;
                },
              },
            },
          ],
        },
        colors: ["#013976", "#E1604B", "#007BFF"],
        grid: {
          borderColor: "#f1f1f1",
        },
      },
      series: [
        {
          name: "Present Prediction (15/06/2021)",
          data: [
            450,
            520,
            380,
            240,
            330,
            260,
            210,
            200,
            60,
            80,
            150,
            100,
            450,
            520,
            380,
            240,
            330,
            260,
            210,
            200,
            60,
            80,
            150,
            100,
          ],
        },
        {
          name: "Past Prediction(14/06/2021)",
          data: [
            350,
            410,
            620,
            420,
            1300,
            1800,
            2900,
            370,
            360,
            510,
            320,
            350,
            350,
            410,
            620,
            420,
            1300,
            1800,
            2900,
            370,
            3000,
            510,
            320,
            350,
          ],
        },
        {
          name: "Future Prediction(16/06/2021)",
          data: [
            870,
            570,
            740,
            990,
            750,
            380,
            620,
            470,
            820,
            560,
            450,
            470,
            870,
            570,
            740,
            990,
            750,
            380,
            620,
            470,
            820,
            560,
            450,
            470,
          ],
        },
      ],
    };
  },
};
</script>
<style scoped>
.line {
  flex: 0 0 65%;
}
</style>
