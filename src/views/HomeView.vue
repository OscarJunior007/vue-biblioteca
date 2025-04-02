<template>
  <v-container>
    <HelloWorld></HelloWorld>
    <AppFooter></AppFooter>
  </v-container>
</template>

<script>
import AppFooter from '@/components/AppFooter.vue';
import HelloWorld from '@/components/HelloWorld.vue';

export default {
    name:'HomeView',
    components:{
        HelloWorld,
        AppFooter   
    },
}
</script>

<style>

</style>