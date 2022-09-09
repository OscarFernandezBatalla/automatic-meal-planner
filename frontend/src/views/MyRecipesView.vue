<template>
  <div class="home">
    <h1>MY RECIPES</h1>

	

	<div class="grid-cards">



    <div class="default_card" @click="modal_visible = !modal_visible"> <!-- todo: add @click to create the modal -->
		+
    </div>

	<ModalRecipe v-if="modal_visible" @close="modal_visible = !modal_visible"/>

	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>

	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>
	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>
	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>
	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>
	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>
	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>
	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>
	<div class="card">
		
        <div class="card-container" >
			<div class="card-info" @click="goRecipeDetails">
				<div class="card-title">
					
					Arroz con limon 
				</div>
				
				<div class="card-dificulty">
					30 minutes
					
				</div>
			</div>

			<div class="card-pic" >
				
				<img src="../assets/arroz.jpg" @click="goRecipeDetails">
				
				<div  class="fav-container" >
					<i class="fav-icon"><font-awesome-icon icon="star" /></i>
                    <i class="edit-icon"><font-awesome-icon icon="edit" /></i>
                    <i class="delete-icon"><font-awesome-icon icon="ban" /></i>
				</div>
				
				
			</div>
        </div>
		
    </div>

	</div>
   



  </div>
</template>

<script>

import ModalRecipe from "../components/ModalRecipe.vue"

export default {
  name: 'HomeView',
  components: {
	ModalRecipe
  },
  data(){
	return{
		clicked: false,
		modal_visible: false
	}
  },
  methods:{
	changeFav(){
		
	},
	goRecipeDetails(){
		this.$router.push( { name: 'recipe-details' })
	}
  }
}
</script>
