<template>
    <v-app id="inspire">
        <v-navigation-drawer v-model="drawer" app>
            <!--  -->
            <h1>Logout</h1>
        </v-navigation-drawer>

        <v-app-bar app>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

            <v-toolbar-title>Chatbot</v-toolbar-title>
        </v-app-bar>

        <v-main>
            <v-container fluid>

                <!-- If using vue-router -->

                <slot></slot>
            </v-container>
            <!--  -->
        </v-main>
    </v-app>
</template>

<script>
export default {
    data: () => ({ drawer: null }),

}
</script>
