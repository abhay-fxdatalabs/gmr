<template>
  <div>
    <h1 class="font-weight-light">Sales Report</h1>
    <v-card>
      <v-data-table :headers="headers" :items="reportItems" item-key="id" dark>
        <template v-slot:item="{ item }">
          <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.sales }}</td>
            <td>{{ item.customers }}</td>
            <td>{{ item.items }}</td>
          </tr>
        </template>
        <template slot="body.append">
          <tr class="primary--text">
            <th class="title">Totals</th>
            <th class="title">{{ sumField("sales") }}</th>
            <th class="title">{{ sumField("customers") }}</th>
            <th class="title">{{ sumField("items") }}</th>
          </tr>
        </template>
      </v-data-table>
    </v-card>
    <SideBar />
  </div>
</template>

<script>
import SideBar from "@/components/SideBar";

export default {
  name: " SideBar",

  components: {
    SideBar,
  },
  data: () => ({
    headers: [
      {
        text: "Product",
        align: "left",
        sortable: false,
        value: "name",
      },
      { text: "Sales", value: "sales" },
      { text: "Customers", value: "customers" },
      { text: "Items", value: "items" },
    ],
    reportItems: [
      {
        id: 1,
        name: "N95 Mask",
        sales: 2062,
        customers: 102,
        items: 8029,
        available: null,
      },
      {
        id: 2,
        name: "Safety gloves",
        sales: 62,
        customers: 12,
        items: 70,
        available: null,
      },
      {
        id: 3,
        name: "Widget 2",
        sales: 262,
        customers: 32,
        items: 1020,
        available: null,
      },
      {
        id: 4,
        name: "Widget 4",
        sales: 362,
        customers: 12,
        items: 190,
        available: null,
      },
      {
        id: 4,
        name: "Widget 4",
        sales: 362,
        customers: 12,
        items: 190,
        available: null,
      },
      {
        id: 19,
        name: "Widget ABC",
        sales: 62,
        customers: 5,
        items: 17,
        available: null,
      },
      {
        id: 12,
        name: "Widget 12",
        sales: 262,
        customers: 22,
        items: 199,
        available: null,
      },
    ],
  }),
  methods: {
    sumField(key) {
      // sum data in give key (property)
      return this.reportItems.reduce((a, b) => a + (b[key] || 0), 0);
    },
  },
};
</script>
