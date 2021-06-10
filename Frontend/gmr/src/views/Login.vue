<template>
  <v-content>
    <h2 class="headertekst" v-if="wrongCred">
      Wrong credentials entered!. Please enter your correct details.
    </h2>
    <v-card width="500" class="mx-auto justify-center" style="margin-top:10rem">
      <form v-on:submit.prevent="loginUser">
        <v-card-title>Sign In </v-card-title>

        <div class="form-group">
          <v-card-text>
            <v-text-field
              label="Username"
              prepend-icon="mdi-account-circle"
              v-model="username"
            />
            <v-text-field
              label="Password"
              :type="showPassword ? 'text' : 'password'"
              prepend-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword = !showPassword"
              v-model="password"
            />
          </v-card-text>
        </div>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="#858585" type="submit"> Sign In </v-btn>
          <v-btn color="#858585" onclick="this.form.reset()"> Clear </v-btn>
        </v-card-actions>
      </form>
    </v-card>
  </v-content>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      showPassword: false,
      username: "",
      password: "",
      wrongCred: false, // activates appropriate message if set to true
    };
  },
  methods: {
    loginUser() {
      // call loginUSer action
      this.$store
        .dispatch("loginUser", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.wrongCred = false;
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err);
          this.wrongCred = true; // if the credentials were wrong set wrongCred to true
        });
    },
  },
};
</script>

<style scoped>
h2.headertekst {
  text-align: center;
  color: red;
  font-size: 20px;
  margin-top: 5rem;
}
</style>
