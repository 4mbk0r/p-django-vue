<template>

    <v-container fluid>
        <div>
            <v-alert v-if="type === 'info'" dense type="info">
                I'm a dense alert with a <strong>type</strong> of info
            </v-alert>
            <v-alert v-if="type === 'success'" dense text type="success">
                Welcome
            </v-alert>
            <v-alert dense v-if="type === 'warning'" border="left" type="warning">
                Nombre de usurio o contraseña incorrectos
            </v-alert>
            <v-alert dense v-if="type === 'error'" outlined type="error">
                I'm a dense alert with the <strong>outlined</strong> prop and a <strong>type</strong> of error
            </v-alert>
        </div>
        <v-tabs v-model="tab" show-arrows background-color="deep-purple accent-4" icons-and-text dark grow>
            <v-tabs-slider color="purple darken-4"></v-tabs-slider>
            <v-tab v-for="(tab, i) in tabs" :key="i">
                <v-icon large>{{ tab.icon }}</v-icon>
                <div class="caption py-1">{{ tab.name }}</div>
            </v-tab>
            <v-tab-item>
                <v-card class="px-4">
                    <v-card-text>
                        <v-form ref="loginForm" lazy-validation @action="validate">
                            <v-row>
                                <v-col cols="12">
                                    <v-text-field v-model="user.username" :rules="loginEmailRules"
                                        label="Nombre de Usuario" required>
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field v-model="user.password" :append-icon="show1 ? 'eye' : 'eye-off'"
                                        :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'"
                                        name="input-10-1" label="Constaseña" hint="Minimo 8 caracteres" counter
                                        @click:append="show1 = !show1">
                                    </v-text-field>
                                </v-col>
                                <v-col class="d-flex" cols="12" sm="6" xsm="12">
                                </v-col>
                                <v-spacer></v-spacer>
                                <v-col class="d-flex" cols="12" sm="3" xsm="12" align-end>
                                    <v-btn x-large block :disabled="!valid" color="success" @click="validate"> Iniciar
                                        Sesion </v-btn>
                                </v-col>
                            </v-row>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-tab-item>
            <v-tab-item>
                <v-card class="px-4">
                    <v-card-text>
                        <v-form ref="registerForm" lazy-validation>
                            <v-row>
                                <v-col cols="12">
                                    <v-text-field v-model="user.username" :rules="[rules.required]" label="Nick"
                                        :error-messages="error.username" maxlength="20" required>
                                    </v-text-field>
                                </v-col>

                                <v-col cols="12">
                                    <v-text-field v-model="user.name" label="Nombre Completo" maxlength="20">
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-menu ref="menu" v-model="menu" :close-on-content-click="false"
                                        transition="scale-transition" offset-y min-width="auto">
                                        <template v-slot:activator="{ on, attrs }">
                                            <v-text-field v-model="user.bith_date" :rules="[rules.required]"
                                                label="Fecha de Nacimineto" prepend-icon="mdi-calendar" readonly
                                                v-bind="attrs" v-on="on">
                                            </v-text-field>
                                        </template>
                                        <v-date-picker v-model="user.bith_date" :active-picker.sync="activePicker"
                                            locale="es-ES"
                                            :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
                                            min="1950-01-01" @change="save(user.bith_date)"></v-date-picker>
                                    </v-menu>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field v-model="user.email" :error-messages="error.email" label="E-mail">
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field v-model="user.password"
                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'"
                                        name="input-10-1" label="Password" hint="At least 8 characters" counter
                                        @click:append="show1 = !show1">
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field block v-model="verify"
                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :rules="[rules.required, passwordConfirmationRule]"
                                        :type="show1 ? 'text' : 'password'" name="input-10-1" label="Confirm Password"
                                        counter @click:append="show1 = !show1"></v-text-field>
                                </v-col>
                                <v-spacer></v-spacer>
                                <v-col class="d-flex ml-auto" cols="12" sm="3" xsm="12">
                                    <v-btn x-large block :disabled="!valid" color="success" @click="register">Registro
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-tab-item>
        </v-tabs>
    </v-container>
</template>
  
  <script>
  import axios from 'axios';
  import App from '../App.vue';
  const Cookies = require('js-cookie');
  export default {
      name: 'HelloWorld',
      components: {
          App,
      },
      data: () => ({
          type: '',
          dialog: true,
          tab: 0,
          tabs: [
              { name: "Inicio de Sesion", icon: "mdi-account" },
              { name: "Registro", icon: "mdi-account-outline" }
          ],
          valid: true,
          user: {
          },
          error: {
          },
          loginEmailRules: [
              v => !!v || "Se requiere completar",
          ],
          emailRules: [
              v => !!v || "Se requiere completar",
          ],
  
          show1: false,
          rules: {
              required: value => !!value || "Se requiere completar",
              min: v => (v && v.length >= 4) || "Minimo 4 Caracteres",
  
          },
          verify: null,
          activePicker: null,
          date: null,
          menu: false,
  
      }),
  
      mounted() {
          if (localStorage.getItem('token') && localStorage.getItem('refresh-token')
              && localStorage.getItem('user')) {
              this.$router.push('/inicio')
          }
      },
      watch: {
          menu(val) {
              val && setTimeout(() => (this.activePicker = 'YEAR'))
          },
      },
      computed: {
          passwordConfirmationRule() {
              return () => (this.verify === this.user.password) || 'Contraseña no coincide'
          }
      },
      methods: {
          validate() {
              if (this.$refs.loginForm.validate()) {
                  const path = process.env.API_URL + "/login/"
                  console.log(path)
                  //this.user.token=null
                  axios({
                      method: "post",
                      url: path,
                      data: this.user,
                      headers: {
                          'Content-Type': 'application/json',
                          "X-CSRFToken": Cookies.get('csrftoken')
                      },
  
                  }).then((response) => {
                      console.log(response.data)
                      if (response.status == 200) {
                          this.type = 'success'
                          localStorage.setItem('token', response.data.token)
                          localStorage.setItem('refresh-token', response.data['refresh-token'])
                          localStorage.setItem('user', JSON.stringify(response.data.user))
                          this.$router.push('/inicio')
                      }
                  })
                      .catch((error) => {
                          this.type = 'warning'
                          console.log(error);
                      })
              }
  
          },
          save(date) {
              this.$refs.menu.save(date)
          },
          register() {
              if (this.$refs.registerForm.validate()) {
                  const path = process.env.API_URL + "/users/"
                  axios({
                      method: "post",
                      url: path,
                      data: this.user,
                      headers: {
                          'Content-Type': 'application/json',
                          "X-CSRFToken": Cookies.get('csrftoken')
                      },
  
                  }).then((response) => {
                      console.log(response.data)
                      if (response.status == 200) {
                          this.type = 'success'
                          localStorage.setItem('token', response.data.token)
                          localStorage.setItem('refresh-token', response.data['refresh-token'])
                          localStorage.setItem('user', JSON.stringify(response.data.user))
                          this.$router.push('/inicio')
                          return
                      }
                      if (response.status == 400) {
                          console.log(response.data)
                      }
                  })
                      .catch((error) => {
                          this.type = 'warning'
                          console.log(error.response.data.errors);
                          this.error = error.response.data.errors
                          this.valid = true
                      })
              }
              return false
          },
  
  
      }
  }
  </script>
  








