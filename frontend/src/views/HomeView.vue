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


	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Pollo al limón
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
				</div>

				<div class="card-available">
					
					<i class="not_available_icon">
						<font-awesome-icon icon="circle-xmark" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/pollo_limon.jpg" >
				<div class="fav-container" @click="clicked = !clicked" 
				v-bind:class="{'white': !clicked, 'yellow': clicked}">
					<i><font-awesome-icon icon="star" /></i>
				</div>
				
				
			</div>
        </div>
    </div>

	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Pollo al limón
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>	
				</div>

				<div class="card-available">
					
					<i class="not_available_icon">
						<font-awesome-icon icon="circle-xmark" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/pollo_limon.jpg" >
				
				
			</div>
        </div>
    </div>


	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Pollo al limón
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>	
				</div>

				<div class="card-available">
					
					<i class="not_available_icon">
						<font-awesome-icon icon="circle-xmark" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/pollo_limon.jpg" >
				
				
			</div>
        </div>
    </div>


	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Pollo al limón
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>	
				</div>

				<div class="card-available">
					
					<i class="not_available_icon">
						<font-awesome-icon icon="circle-xmark" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/pollo_limon.jpg" >
				
				
			</div>
        </div>
    </div>

	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Arroz
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/arroz.jpg" >
				
				
			</div>
        </div>
    </div>

	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Arroz
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/arroz.jpg" >
				
				
			</div>
        </div>
    </div>

	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Arroz
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/arroz.jpg" >
				
				
			</div>
        </div>
    </div>

	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Arroz
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/arroz.jpg" >
				
				
			</div>
        </div>
    </div>
	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Arroz
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/arroz.jpg" >
				
				
			</div>
        </div>
    </div>

	<div class="card">
        <div class="card-container">
			<div class="card-info">
				<div class="card-title">
					
					Arroz
				</div>
				
				<div class="card-dificulty">
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
					<i><font-awesome-icon icon="star" /></i>
				</div>
				<div class="card-available">
					
					<i class="available_icon">
						<font-awesome-icon icon="circle-check" />
					</i>
				</div>
			</div>

			<div class="card-pic">
				<img src="../assets/arroz.jpg" >
				
				
			</div>
        </div>
    </div>



	



	</div>
   



  </div>
</template>

<script>


export default {
  name: 'HomeView',
  components: {
  },
  data(){
	return{
		clicked: false
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
