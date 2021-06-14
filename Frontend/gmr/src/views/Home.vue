<template>
  <div>
    <v-row>
      <v-col>
        <v-card class="mx-auto text-center">
          <v-card-title class="primary--text">
            Sales
          </v-card-title>
          <v-sparkline
            :value="sparklineData"
            padding="18"
            label-size="4"
            color="cyan"
            :gradient="['#007bff', 'cyan']"
            :line-width="2"
            :stroke-linecap="'round'"
            smooth
          >
            <template v-slot:label="item"> ${{ item.value }} </template>
          </v-sparkline>
        </v-card>
      </v-col>
    </v-row>
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
  data: () => ({
    sparklineData: [423, 446, 675, 510, 590, 610, 423],
  }),
};
</script>
