<template>
  <div id="wrapper">
    <div class="card">
      <div class="card-header border-0">
        <div class="row align-items-center">
          <div class="col">
            <h3 class="mb-0">Dam RegionWise Grid</h3>
          </div>
        </div>
        <div class="row align-items-center">
          <table class="awesome-table">
            <tr>
              <td style="{background:#f2f2f2}"></td>
              <th>North</th>
              <th>south</th>
              <th>East</th>
              <th>West</th>
            </tr>
            <tr>
              <th>Outage</th>
              <td>550/2%</td>
              <td>200/-4%</td>
              <td>500/-5%</td>
              <td>805/8%</td>
            </tr>

            <tr>
              <th>Power Supply Position</th>
              <td>90/-3%</td>
              <td>300/3%</td>
              <td>50/-5%</td>
              <td>700/7%</td>
            </tr>
          </table>
        </div>
        <Table v-if="tableData" :theData="tableData" :config="config"> </Table>
      </div>
    </div>
  </div>
</template>
<style scoped>
.wrapper {
  flex: 1;
}
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 0.375rem;
}
.card-header:first-child {
  border-radius: calc(0.375rem - 1px) calc(0.375rem - 1px) 0 0;
}

.border-0 {
  border: 0 !important;
}
.card-header {
  padding: 1.25rem 1.5rem;
  margin-bottom: 0;
  background-color: #fff;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}
.align-items-center {
  align-items: center !important;
}
.row {
  display: flex;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
}
.text-right {
  text-align: right !important;
}
.mb-0,
.my-0 {
  margin-bottom: 0 !important;
}
h3,
.h3 {
  text-align: left;
  font: normal normal normal 28px/34px Roboto;
  letter-spacing: 0px;
  color: #4d4f5c;
  opacity: 1;
  font-weight: 600;
}
.awesome-table {
  border: 1px solid #999;
  border-radius: 4px;
  /* color: #858585 0% 0% no-repeat padding-box; */
  overflow: scroll;
  border-collapse: collapse;
  width: 100%;
  padding: 1.25rem 1.5rem;
}

.awesome-table th {
  position: sticky;
  top: 0;
  background: #f2f2f2;
  padding: 10px 5px;
  text-align: center;
  border-bottom: 1px solid #999;
}
.awesome-table td {
  padding: 10px 5px;
  text-align: center;
}
.awesome-table span {
  text-align: center;
}
</style>
