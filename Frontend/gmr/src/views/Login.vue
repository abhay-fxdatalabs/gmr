<template>
<div class="vue-tempalte">
  <div class="row justify-content-md-center">
    <div class="col-md-5 p-3 login justify-content-md-center">
      <div class="login-form">
        <div class="lg">
          <h2 v-if="wrongCred">Wrong credentials entered!. Please enter your correct details.</h2>
            <form v-on:submit.prevent="loginUser">
              <div class="form-group">
                <label for="user">Username</label>
                <input type="text" name="username" id="user" v-model="username">
              </div>
              <div class="form-group">
                <label for="pass">Password</label>
                <input type="password" name="password" id="pass" v-model="password">
              </div>
              <button type="submit">Login</button>
            </form>
        </div>
        </div>
      </div>
  </div>
</div>
</template>

<script>
  export default {
    name: 'Login',
    data () {
      return {
        username: '',
        password: '',
        wrongCred: false // activates appropriate message if set to true
      }
    },
    methods: {
      loginUser () { // call loginUSer action
        this.$store.dispatch('loginUser', {
          username: this.username,
          password: this.password
        })
            .then(() => {
              this.wrongCred = false
              this.$router.push({ name: 'Home' })
            })
          .catch(err => {
            console.log(err)
            this.wrongCred = true // if the credentials were wrong set wrongCred to true
          })
        }
      }
  }
</script>

<style scoped>
  body,
  html,
  .App,
  .vue-tempalte,
  .vertical-center {
    width: 100%;
    height: 100%;
  }
</style>