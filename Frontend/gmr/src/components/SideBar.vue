<template>
   <nav>
    <v-navigation-drawer
      v-model="sidebarMenu"
      dark
      app
      mini-variant
      mini-variant-width="200"
      width="50%"
      class="white"
      style="  border: 2px solid black !important"
    >
      <v-list dense>
        <v-list-item class="mb-12">
          <v-list-item-content>
            <v-img class="mr-3" src="@/assets/img/GMR_Logo.webp"> </v-img>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list flat>
        <v-list-item router to="/home" active-class="bg-active">
          <v-list-item-content>
            <v-icon size="40" class="mb-2" style="color:#575757 "
              >fas fa-home
            </v-icon>
            <v-list-item-subtitle style="color:#575757 " align="center"
              >Home</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
        <v-list-item router to="/dam" active-class="bg-active">
          <v-list-item-content>
            <v-icon class="mb-2" size="40" style="color:#575757 "
              >fas fa-chart-line</v-icon
            >
            <v-list-item-subtitle align="center" style="color:#575757 "
              >DAM</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
        <v-list-item router to="/rtm" active-class="bg-active">
          <v-list-item-content>
            <v-icon class="mb-2" size="40" style="color:#575757"
              >fas fa-chart-bar</v-icon
            >
            <v-list-item-subtitle align="center" style="color:#575757 "
              >RTM</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>

        <v-list-item router to="/model" active-class="bg-active">
          <v-list-item-content>
            <v-icon class="mb-2" size="40" style="color:#575757 "
              >fas fa-home</v-icon
            >
            <v-list-item-subtitle align="center" style="color:#575757 "
              >Model</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
        <v-list-item router to="/users" active-class="bg-active">
          <!-- <v-badge color="pink" dot overlap> -->
          <v-list-item-content>
            <v-icon class="mb-2" size="40" style="color:#575757 "
              >fas fa-user</v-icon
            >
            <v-list-item-subtitle align="center" style="color:#575757 "
              >Users</v-list-item-subtitle
            >
          </v-list-item-content>
          <!-- </v-badge> -->
        </v-list-item>
        <v-list-item router to="/logout" active-class="bg-active">
          <v-list-item-content>
            <v-icon class="mb-2" size="40" style="color:#575757 "
              >fas fa-sign-out-alt</v-icon
            >
            <v-list-item-subtitle align="center" style="color:#575757 "
              >Logout</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>
<script>
export default {
  data: () => ({
    sidebarMenu: true,
  }),
};
</script>
<style scoped>
.bg-active {
  background-color: #bfbfbf !important;
  /* color: black !important; */
}
.bgWhite {
  background-color: darkgrey !important;
}
</style>
