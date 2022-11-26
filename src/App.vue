<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app>
      <!--  -->
      <v-list v-if="login()">
        <v-list-item class="px-2">
          <v-list-item-avatar>
            <v-img src="https://randomuser.me/api/portraits/women/85.jpg"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="text-h6">
              {{ user.email }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ user.username }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list nav dense>
        <v-list-item @click="logout" link>
          <v-list-item-icon>
            <v-icon>mdi-folder</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Cerrar seccion</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Chatbot</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    drawer: null,
    user: ""

  }),
  mounted() {
    if (localStorage.getItem('token') && localStorage.getItem('refresh-token')
      && localStorage.getItem('user')) {
      this.user = JSON.parse(structuredClone(localStorage.getItem('user')))
      console.log(typeof this.user)
    }
  },
  computed: {

  },
  methods: {
    login() {
      if (localStorage.getItem('token') && localStorage.getItem('refresh-token')
        && localStorage.getItem('user')) {
        return true
      }
      return false
    },
    logout() {
      localStorage.removeItem('user');
      localStorage.removeItem('token');
      localStorage.removeItem('refresh-token')
      this.$router.push('/')

    }
  }
};
</script>
