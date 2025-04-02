<template>
  <v-container>
    <MenuComponent></MenuComponent>
    <BusquedaComponent></BusquedaComponent>
    <TableComponent></TableComponent>
    <AppFooter></AppFooter>
  </v-container>
</template>

<script>
import AppFooter from '@/components/AppFooter.vue';
import BusquedaComponent from '@/components/BusquedaComponent.vue';

import MenuComponent from '@/components/MenuComponent.vue';
import TableComponent from '@/components/TableComponent.vue';

export default {
    name:'HomeView',
    components:{
        AppFooter,
        MenuComponent,
        BusquedaComponent,
        TableComponent
    },
}
</script>

<style>

</style>