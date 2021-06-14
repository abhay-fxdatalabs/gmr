<template>
  <div>
    <div id="chart">
      <apexchart
        type="line"
        height="350"
        width="500"
        :options="chartOptions"
        :series="series"
      ></apexchart>
    </div>

    <SideBar />
  </div>
</template>

<script>
import SideBar from "@/components/SideBar";
export default {
  name: "App",

  components: {
    SideBar,
  },
  data: function() {
    return {
      chartOptions: {
        chart: {
          height: 350,
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
          font: "20px",
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
        grid: {
          borderColor: "#f1f1f1",
        },
      },
      series: [
        {
          name: "Present Prediction",
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
          name: "Past Prediction",
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
          name: "Future Prediction",
          data: [
            87,
            57,
            74,
            99,
            75,
            38,
            62,
            47,
            82,
            56,
            45,
            47,
            87,
            57,
            74,
            99,
            75,
            38,
            62,
            47,
            82,
            56,
            45,
            47,
          ],
        },
      ],
    };
  },
};
</script>
