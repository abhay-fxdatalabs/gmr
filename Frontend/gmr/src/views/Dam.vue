<template>
  <div>
    <div class="wrapper">
      <LineChart />
      <BarChart />
    </div>
    <div class="grid">
      <DataGrid />
      <RegionWiseGrid />
    </div>

    <SideBar />
  </div>
</template>

<script>
import SideBar from "@/components/SideBar";
import LineChart from "@/components/Charts/LineChart";
import BarChart from "@/components/Charts/BarChart";
import DataGrid from "@/components/Charts/DataGrid";
import RegionWiseGrid from "@/components/Charts/RegionWiseGrid";

export default {
  name: "App",

  components: {
    SideBar,
    LineChart,
    BarChart,
    DataGrid,
    RegionWiseGrid,
  },
  data: () => ({
    //
  }),
};
</script>
<style>
.wrapper {
  display: flex;
}
.grid {
  display: flex;
}
</style>
