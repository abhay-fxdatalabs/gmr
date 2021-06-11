<template>
  <div id="app">
    <v-app-bar app color="blue darken-4" dark>
      <v-app-bar-nav-icon
        @click.stop="sidebarMenu = !sidebarMenu"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>Dashboard</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-icon>mdi-account</v-icon>
    </v-app-bar>
    <v-navigation-drawer
      v-model="sidebarMenu"
      app
      floating
      :permanent="sidebarMenu"
      :mini-variant.sync="mini"
      color="white darken-4"
    >
      <v-list dense>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list-item class="px-2" @click="toggleMini = !toggleMini">
        <v-list-item-avatar>
          <v-icon>mdi-account-outline</v-icon>
        </v-list-item-avatar>
        <v-list-item-content class="text-truncate">
          Carol Skelly
        </v-list-item-content>
        <v-btn icon small>
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>
      <v-divider></v-divider>
      <v-list>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.href"
        >
          <v-list-item-icon>
            <v-icon color="primary">{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="primary--text">{{
              item.title
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <v-container class="px-4 py-0 fill-height" fluid>
        <v-row class="fill-height">
          <v-col>
            <transition name="fade">
              <router-view></router-view>
            </transition>
          </v-col>
        </v-row>
      </v-container>
      <v-footer app color="blue darken-4" class="py-3">
        <span class="ml-auto overline" style="color:white">GMR &copy;2021</span>
      </v-footer>
    </v-content>
  </div>
</template>
<script>
export default {
  data: () => ({
    sidebarMenu: true,
    toggleMini: false,
    items: [
      { title: "Home", href: "/home", icon: "mdi-home-outline" },
      {
        title: "DAM",
        href: "/dam",
        icon: "mdi-chart-line",
      },
      { title: "RTM", href: "/rtm", icon: "mdi-chart-bar" },
      { title: "Model", href: "/model", icon: "mdi-alarm-light-outline" },

      {
        title: "Users",
        href: "/users",
        icon: "mdi-account-search-outline",
      },
      {
        title: "Logout",
        href: "/logout",
        icon: "mdi-logout",
      },
    ],
  }),
  computed: {
    mini() {
      return this.$vuetify.breakpoint.smAndDown || this.toggleMini;
    },
  },
};
</script>
<style>
.theme--dark.v-list-item:not(.v-list-item--active):not(.v-list-item--disabled) {
  color: #fff !important;
}
</style>
