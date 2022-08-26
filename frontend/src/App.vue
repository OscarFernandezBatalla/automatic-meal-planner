<template>

    <div>
        <NavegationDesktop1/> <!-- v-if="!mobileView" /> -->
    </div>
    <router-view/>
</template>

<script>
import NavegationDesktop1 from "./components/NavegationDesktop1.vue"


export default {
  data(){
    return {
        //mobileView: false,
        //showNav: false
    }
  },
  methods:{
    //handleView(){
    //  this.mobileView = window.innerWidth <= 768;
    //}
  },
  components: {
    NavegationDesktop1,
  },
  created(){
    //this.handleView();
    //window.addEventListener('resize', this.handleView);
  }
}

</script>


