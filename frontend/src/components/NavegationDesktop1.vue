<template>
    <nav>
        
        <div class="logo">
            <a href="/">AMP</a>
        </div>
        <ul class="nav-links" :class="{'nav-active':showNav}">
            <li>
                <a href="/my-recipes" >My Recipes</a>
            </li>
            <li>
                <a href="/">Storage</a>
            </li>
            <li>
                <a href="/">Calendar</a>
            </li>
            <li>
                <a href="/">Login</a>
            </li>
       
        </ul>


        
        <div class="burger" @click="showNav= !showNav" :class="{'toggle':showNav}">
            <div class="line1"></div>
            <div class="line2"></div>
            <div class="line3"></div>
        </div>

        
    </nav>
</template>

<script>
export default {
    data() {
        return {
            showNav: false
        }
    },
    methods: {
        
    }
}
</script>