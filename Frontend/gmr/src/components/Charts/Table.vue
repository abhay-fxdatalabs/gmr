<template>
  <table class="awesome-table">
    <thead>
      <tr>
        <th v-for="(obj, ind) in config" :key="ind">{{ obj.title }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(row, index) in theData" :key="index">
        <td v-for="(obj, ind) in config" :key="ind">
          <span v-if="obj.type === 'date'">{{
            row[obj.key].toLocaleString()
          }}</span>
          <span v-if="obj.type === 'text'">{{ row[obj.key] }}</span>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script>
export default {
  props: ["theData", "config"],
};
</script>

<style lang="scss">
.awesome-table {
  border: 1px solid #999;
  border-radius: 4px;
  color: #858585 0% 0% no-repeat padding-box;
  overflow: scroll;
  border-collapse: collapse;
  width: 100%;
  padding: 1.25rem 1.5rem;
}

.awesome-table th {
  position: sticky;
  top: 0;
  background: #ccc;
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
tr:nth-child(even) {
  background: #f2f2f2 0% 0% no-repeat padding-box;
}
</style>
