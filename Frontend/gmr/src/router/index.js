import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Dam from "../views/Dam";
import Rtm from "../views/Rtm";
import WeakAhead from "../views/WeakAhead";
import Model from "../views/Model";
import Users from "../views/Users";
import Login from "../views/Login";
import Logout from "../views/Logout";

Vue.use(VueRouter);

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/dam",
    name: "Dam",
    component: Dam,
  },
  {
    path: "/rtm",
    name: "Rtm",
    component: Rtm,
  },
  {
    path: "/weakahead",
    name: "WeakAhead",
    component: WeakAhead,
  },
  {
    path: "/model",
    name: "Model",
    component: Model,
  },
  {
    path: "/users",
    name: "Users",
    component: Users,
  },
  {
    path: '/',
    name: 'Login',
    component: Login,
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout,
    meta: {
      requiresAuth: true
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
