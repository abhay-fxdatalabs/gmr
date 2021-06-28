<template>
  <div id="wrapper">
    <div class="card">
      <div class="card-header border-0">
        <div class="row align-items-center">
          <div class="col">
            <h3 class="mb-0">Prediction Data Grid for DAM</h3>
          </div>
        </div>
        <div class="row align-items-center">
          <v-col class="d-flex" cols="4" sm="4">
            <v-select
              v-model="select"
              :items="items"
              prepend-icon="mdi-calendar"
              label="Select"
            ></v-select>
          </v-col>
          <v-col class="d-flex" cols="8" sm="8">
            <v-radio-group v-model="row" row>
              <v-radio label="BlockWise" value="BlockWise"></v-radio>
              <v-radio label="Hourly" value="Hourly"></v-radio>
              <v-radio label="TimeSegmented" value="TimeSegmented"></v-radio>
            </v-radio-group>
          </v-col>
        </div>
        <Table v-if="tableData" :theData="tableData" :config="config"> </Table>
      </div>
    </div>
  </div>
</template>

<script>
import Table from "./Table.vue";
export default {
  components: {
    Table,
  },
  data: () => ({
    tableData: undefined,
    config: [
      {
        key: "time",
        title: "Time",
        type: "text",
      },
      {
        key: "PredictedMcp",
        title: "Predicted Mcp value",
        type: "date",
      },
    ],

    items: ["Yesterday", "Today", "Tomorrow"],
  }),
  mounted() {
    this.$axios
      .get("https://60cc2c8b71b73400171f72c3.mockapi.io/something123/data")
      .then(({ data }) => {
        this.tableData = data;
      });
  },
};
</script>
<style>
.wrapper {
  flex: 0 0 65%;
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
/* .v-input {
  background: #575757 0% 0% no-repeat padding-box;
} */
</style>
