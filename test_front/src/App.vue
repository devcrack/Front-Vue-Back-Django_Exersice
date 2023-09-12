<template>
<!--  This the header-->
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          src="https://www.zentric.mx/wp-content/uploads/2023/05/Logo-Zentric.svg"
          transition="scale-transition"
          width="100"
        />
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
