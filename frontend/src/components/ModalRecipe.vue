<template>
    
    <div class="backdrop" @click.self="closeModal">

        <div class="modal">
            <div class="title">
                <i @click="closeModal"><font-awesome-icon icon="arrow-left" /></i> 
                Create a Recipe!
            </div>
            

            <form class="form" method='POST' @submit.prevent="createRecipe" enctype='multipart/form-data'>
                <div class="form_group">
                    <label for="room_name">Recipe name:</label>
                    <input v-model="name" type="text">
                    <!-- <input id="room_name" name="room_name" type="text" placeholder="E.g. Mastering Python + Django" /> -->
                </div>
                


                <div class="form_group" style="">
                    <label for="dinners">Dinners:</label>
                    <input v-model="dinners" id="dinners" readonly>
                    <button type="button" class="button" @click="addDinners(1)">+</button>
                    <button type="button" class="button" @click="addDinners(-1)">-</button>
                    <!-- <input id="room_name" name="room_name" type="text" placeholder="E.g. Mastering Python + Django" /> -->
                </div>


                <div class="form_group">
                    <label for="image">Image:</label>
                    <input type="file" id="image" @change="onChangeFile">

                    <!-- <input id="room_name" name="room_name" type="text" placeholder="E.g. Mastering Python + Django" /> -->
                </div>


                <div class="form_group">
                    <label for="difficulty">Difficulty:</label>
                    <select v-model="difficulty" id="difficulty"> <!--TODO STYLE... -->
                    <option v-for="dif in difficulty_list" v-bind:key="dif">{{dif.name}}</option>
                    
                    
                    </select>
                    <!-- <input id="room_name" name="room_name" type="text" placeholder="E.g. Mastering Python + Django" /> -->
                </div>

                <div class="form_group">
                    <label for="time">Time:</label>
                    <input v-model="time" type="text" id="time" style="margin-right:10px;"> <!--TODO STYLE... -->
                    minutes
                </div>


                <div class="form_group">
                    <label for="time">Cuisine Style:</label>
                    <select v-model="cuisine_style" id="cuisine_style"> <!--TODO STYLE... -->
                    <option v-for="cuisine in cuisine_styles" v-bind:key="cuisine">{{cuisine.name}}</option>
                    
                    </select>
                </div>


                <!-- <div class="form_group">
                    <label for="Cuisine">Ingredients:</label>
                    <input type="text" v-model="cuisine_style" id="cuisine_style" required list="cuisine_list">
                    <datalist id="cuisine_list">
                        <select id="recipe_style">
                            <option v-for="cuisine in cuisine_styles" v-bind:key="cuisine.name">{{cuisine.name}}</option>
                        </select>
                    </datalist>
                    
                    
                    
                  
                </div> -->




                
                <div class="ingredients-button-container">
                    <h1>Ingredients</h1>
                    <button type="button" @click="addIngredient">Add Ingredient</button>
                </div>

                <div id="ingredient-list">
                    
                </div>


                <div class="step-button-container">
                    <h1>Steps</h1>
                    <button type="button" @click="addStep">Add Step</button>
                </div>

                <div id="step-list">
       


                </div>

            






                 <div class="form_action">
                    <button id="button_cancel">Cancel</button>
                    <button type="submit" id="button_submit">Submit</button>
                </div>

            </form>

        </div>

    </div>

</template>

<script>
import axios from 'axios'
export default {



    data(){
        return{
            name: "",
            image: null,
            dinners: 1,
            difficulty: 1,
            cuisine_style: null,
            ingredinets: null,
            fav: true,
            time: 0,
            num_steps: 0,
            cuisine_styles: null,
            num_ingredient: 0,
            units: null,
            difficulty_list: null,
            ingredients_list: null,
            ingredients_recipe: {},
       
        }
    },
    created(){
        this.getStyles()
        this.getUnits()
        this.getIngredients()
        this.getDifficulty()
    },

    methods:{

        getDifficulty(){
            axios
            .get('/api/difficulty/')
            .then(response => {
            this.difficulty_list = response.data
            console.log("dificulty")
            console.log(response.data)
            })
            .catch(error => {
            console.log(error)
            })   
        },

         getIngredients(){
            axios
            .get('/api/food_items/')
            .then(response => {
            this.ingredients_list = response.data
            console.log(response.data)
            })
            .catch(error => {
            console.log(error)
            })
        },

        getUnits(){
            axios
            .get('/api/units/')
            .then(response => {
            this.units = response.data
            })
            .catch(error => {
            console.log(error)
            })
        },

        getStyles(){
            axios
            .get('/api/cuisine_styles/')
            .then(response => {
            this.cuisine_styles = response.data
            this.cuisine_style = this.cuisine_styles[0].name		  
            })
            .catch(error => {
            console.log(error)
            })
        },
        onChangeFile(event){
            this.image = event.target.files[0]
            console.log(this.image)
        },

        async createRecipe(){
            
            let bodyFormData = new FormData()
            bodyFormData.append('name', this.name)
            bodyFormData.append('image', this.image)
            bodyFormData.append('dinners', this.dinners)
            bodyFormData.append('difficulty', this.difficulty)
            bodyFormData.append('cuisine_style', this.cuisine_style)
            // bodyFormData.append('ingredinets', this.ingredinets)
            bodyFormData.append('fav', this.fav)
            bodyFormData.append('time', this.time)
            
            var food_items_ingredient = document.getElementsByClassName('food_item_ingredient')
            var quantities_ingredient = document.getElementsByClassName('quantity_ingredient')
            var units_ingredients = document.getElementsByClassName('unity_ingredient')

            for (var i = 1; i <= this.num_ingredient; i++) {
                
                this.ingredients_recipe['ingredient' + String(i)] = JSON.stringify({
                    "food_item" : food_items_ingredient[i-1].value,
                    "quantity" : quantities_ingredient[i-1].value,
                    "unit" : units_ingredients[i-1].value
                })
            }

            bodyFormData.append('ingredients',  JSON.stringify(this.ingredients_recipe))

            console.log(this.ingredients_recipe)

            
        
            await axios
            .post('/api/create-recipe/', bodyFormData, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
            .then(response => {
                 console.log(response)
            })

            // axios
            // .post('/api/create-recipe/', {
            // name: this.name,
            // image: this.image,
            // dinners: this.dinners,
            // difficulty: this.difficulty,
            // cuisine_style: this.cuisine_style,
            // ingredinets: this.ingredinets,
            // fav: this.fav,
            // time: this.time,
            // })
            // .then(response => {
                // console.log(response)
            // })
            // .catch(error => {
                // console.log(error.response)
            // })
        },

        removeStep(){
            let delete_div = document.getElementById('step-1')
            delete_div.remove()

        },

        addDinners(num){
            let dinners = document.getElementById('dinners')
            console.log(num)
            dinners.value = Number(dinners.value) + num
            if(dinners.value <= 0){
                dinners.value = 1
            }

        },
        addStep(){

            // <div id="step-list">
            //         <div id="step-1" class="step-container">
                     

            //                 <div class="box-step-number">
            //                     1
            //                 </div>


            //                 <textarea wrap="hard" name = "step1"></textarea>

                           
            //                 <button class="delete-step" @click="removeStep">X</button>

            //         </div>
            // </div>

            this.num_steps += 1

            const step_list = document.getElementById("step-list");

            const divFormGroup = document.createElement("div");
            divFormGroup.classList.add('step-container')
            divFormGroup.setAttribute('id', 'step'+String(this.num_steps))

            const box_number = document.createElement("div")
            box_number.innerHTML += String(this.num_steps)
            box_number.classList.add('box-step-number')

            const text_step = document.createElement("textarea")
            text_step.setAttribute('wrap','hard')
            text_step.id = "text_step"+String(this.num_steps)

            const delete_step = document.createElement("button")
            delete_step.classList.add('delete-step')
            delete_step.innerHTML += 'x'
            
            delete_step.onclick = function (){
                let delete_div = document.getElementById(divFormGroup.id)
                delete_div.remove()
                console.log(this.num_steps)
                num_steps = this.num_steps - 1
                console.log(this.num_steps)
            }
            


            divFormGroup.appendChild(box_number)
            divFormGroup.appendChild(text_step)
            divFormGroup.appendChild(delete_step)

            step_list.appendChild(divFormGroup);

            if(step_list.childElementCount>1){
                let delete_buttons = document.getElementsByClassName('delete-step')
               
                for(var i=0; i<delete_buttons.length - 1; i++ ){
                    delete_buttons[i].disabled = true;
                }
        
            }


        },

        addIngredient(){

            console.log(this.num_ingredient)
            this.num_ingredient += 1
            // div class="form_group">
            //         <label for="Cuisine">Ingredients:</label>
            //         <input type="text" v-model="cuisine_style" id="cuisine_style" required list="cuisine_list"> <!--TODO STYLE... -->
            //         <datalist id="cuisine_list">
            //             <select id="recipe_style">
            //                 <option v-for="cuisine in cuisine_styles" v-bind:key="cuisine.name">{{cuisine.name}}</option>
            //             </select>
            //         </datalist>
            // div
            






            const ingredient_list_div = document.getElementById("ingredient-list");
            
            //li.appendChild(document.createTextNode("Element 4"));
            //ul.appendChild(li);
           
 

        
          

            const divFormGroup = document.createElement("div");
            divFormGroup.classList.add('form_group_ingredients')


            const numIngredientDiv = document.createElement("div")
            numIngredientDiv.classList.add('ingredient_num')
            numIngredientDiv.innerHTML += this.num_ingredient
            divFormGroup.appendChild(numIngredientDiv)

            const ingredient_delete = document.createElement("div")
            ingredient_delete.classList.add('ingredient_delete')
            ingredient_delete.innerHTML += "x"
            

               
            
            
           

            const unitySelect = document.createElement("select");
            //newCheckbox.setAttribute("type", 'text');
            unitySelect.setAttribute("id", 'unity1');
            unitySelect.classList.add('ingredient-select')
            unitySelect.classList.add('unity_ingredient')
            



            const quantity = document.createElement("input");
            quantity.setAttribute("type", 'text');
            quantity.setAttribute("placeholder", 'Quantity')
            quantity.classList.add('quantity_ingredient')


            for (var i = 0; i < this.units.length; i++) {
                var option = document.createElement("option");
                option.value = this.units[i].name;
                option.text = this.units[i].name;
                unitySelect.appendChild(option);
            }
            


            
            const ingredient_input = document.createElement("input");
            ingredient_input.type = "text"
            ingredient_input.id="ingredient"+String(this.num_ingredient)
            ingredient_input.setAttribute("placeholder", 'Food')
            ingredient_input.required = true
            ingredient_input.classList.add('food_item_ingredient')
         
            ingredient_input.setAttribute("list", 'ingredient_list');

            const ingredient_list = document.createElement("datalist");
            ingredient_list.id = "ingredient_list"
            const ingredient_select = document.createElement("select")
            
            for (var i = 0; i < this.ingredients_list.length; i++) {
                var option = document.createElement("option");
                option.value = this.ingredients_list[i].name;
                option.text = this.ingredients_list[i].name;
                ingredient_select.appendChild(option);
            }

            ingredient_list.appendChild(ingredient_select)
            ingredient_input.appendChild(ingredient_list)

            


            divFormGroup.appendChild(quantity)
            divFormGroup.appendChild(unitySelect)
            divFormGroup.appendChild(ingredient_input)
            divFormGroup.appendChild(ingredient_delete)
            



            ingredient_list_div.appendChild(divFormGroup);
            //Todo: Create Ingredient with autocomplete (name ingredient) + quantity + unity
        },

        closeModal(){
            this.$emit('close')
        }
    }
    
}
</script>