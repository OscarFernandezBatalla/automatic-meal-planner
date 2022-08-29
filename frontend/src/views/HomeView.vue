<template>
  <div class="home">
    <h1>RECIPES</h1>

	

	<div class="grid-cards">

	<div class="card">
		
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" 
				v-bind:class="{'white': !clicked, 'yellow': clicked}">
					<i @click="clicked = !clicked" ><font-awesome-icon icon="star" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>

	


	<div class="card" v-for="recipe in recipes" v-bind:key="recipe.id">
		
		
        <div class="card-container">
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					{{ recipe.name }}
				</div>
				
				<div class="card-dificulty">
					{{ recipe.difficulty }}
					
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic" >
				
		
	
				<img v-bind:src="recipe.image_url" @click="goRecipeDetails">

		
				
				
				
				<div  class="fav-container" 
				v-bind:class="{'white': !clicked, 'yellow': clicked}">
					<i @click="clicked = !clicked" ><font-awesome-icon icon="star" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>





	



	</div>
   



  </div>
</template>

<script>

import axios from 'axios'


export default {
  name: 'HomeView',
  components: {
  },
  data(){
	return{
		clicked: false,
		recipes: null,
	}
  },
  created(){
	this.getAllRecipes()
  },
  methods:{
	changeFav(){
		
	},
	goRecipeDetails(){
		this.$router.push( { name: 'recipe-details' })
	},

	getAllRecipes(){
		axios
        .get('/api/recipes/')
        .then(response => {
          this.recipes = response.data
		  console.log(this.recipes)

		  
        })
        .catch(error => {
          console.log(error)
        })
	}
  }
}
</script>
