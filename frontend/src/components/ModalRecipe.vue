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
                    <input type="text" id="difficulty">
                    <!-- <input id="room_name" name="room_name" type="text" placeholder="E.g. Mastering Python + Django" /> -->
                </div>

                <div class="form_group">
                    <label for="time">Time:</label>
                    <input v-model="time" type="text" id="time" style="margin-right:10px;"> <!--TODO STYLE... -->
                    minutes
                </div>


                <div class="form_group">
                    <label for="time">Cuisine Style:</label>
                    <select type="text" id="cuisine_style"> <!--TODO STYLE... -->
                    <option value="traditional">Traditional</option>
                    <option value="italian">Italian</option>
                    <option value="greek">Greek</option>
                    <option value="american">American</option>
                    </select>
                </div>
                
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
                    <div id="step-1" class="step-container">
                     

                            <div class="box-step-number">
                                1
                            </div>


                            <textarea wrap="hard" name = "step1"></textarea>

                           
                            <button class="delete-step" @click="removeStep">X</button>

                    </div>

                    <div class="step-container">
                     

                            <div class="box-step-number">
                                2
                            </div>

                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo ab ipsa commodi ratione obcaecati illum temporibus maiores iusto aperiam dignissimos voluptatem omnis magni quos blanditiis soluta maxime facere in minima excepturi culpa at, corporis nam reprehenderit aspernatur. Dolor, id? Impedit.</p>
                            <button class="delete-step">X</button>

                    </div>

                    <div class="step-container">
                     

                            <div class="box-step-number">
                                3
                            </div>

                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo ab ipsa commodi ratione obcaecati illum temporibus maiores iusto aperiam dignissimos voluptatem omnis magni quos blanditiis soluta maxime facere in minima excepturi culpa at, corporis nam reprehenderit aspernatur. Dolor, id? Impedit.</p>
                            <button class="delete-step">X</button>

                    </div>

                    <div class="step-container">
                     

                            <div class="box-step-number">
                                4
                            </div>

                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo ab ipsa commodi ratione obcaecati illum temporibus maiores iusto aperiam dignissimos voluptatem omnis magni quos blanditiis soluta maxime facere in minima excepturi culpa at, corporis nam reprehenderit aspernatur. Dolor, id? Impedit.</p>
                            <button class="delete-step">X</button>

                    </div>

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
            cuisine_style: 'traditional',
            ingredinets: null,
            fav: true,
            time: 30,
            num_steps: 0,
        }
    },

    methods:{
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
            bodyFormData.append('ingredinets', this.ingredinets)
            bodyFormData.append('fav', this.fav)
            bodyFormData.append('time', this.time)
        
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
            const step_list = document.getElementById("step-list");

            const divFormGroup = document.createElement("div");
            divFormGroup.classList.add('form_group')

            divFormGroup.innerHTML += 'hola'



            step_list.appendChild(divFormGroup);

        },

        addIngredient(){
            const ingredient_list = document.getElementById("ingredient-list");
            
            //li.appendChild(document.createTextNode("Element 4"));
            //ul.appendChild(li);
            var arrayIngredients = ["Patata","Aceite","Mayonesa","Pollo"];
            var arrayUnities = ["Gramos","Pizca","Cucharada","Cucharadita"];

            const newLabel = document.createElement("label");
            newLabel.setAttribute("for", 'checkbox');
          

            const divFormGroup = document.createElement("div");
            divFormGroup.classList.add('form_group')
            
            const ingredientSelect = document.createElement("select");
            //newCheckbox.setAttribute("type", 'text');
            ingredientSelect.setAttribute("id", 'ingredient1');

            const unitySelect = document.createElement("select");
            //newCheckbox.setAttribute("type", 'text');
            unitySelect.setAttribute("id", 'unity1');



            const quantity = document.createElement("input");
            quantity.setAttribute("type", 'text');





            //Create and append the options
            for (var i = 0; i < arrayIngredients.length; i++) {
                var option = document.createElement("option");
                option.value = arrayIngredients[i];
                option.text = arrayIngredients[i];
                ingredientSelect.appendChild(option);
            }

            for (var i = 0; i < arrayUnities.length; i++) {
                var option = document.createElement("option");
                option.value = arrayUnities[i];
                option.text = arrayUnities[i];
                unitySelect.appendChild(option);
            }
            
            

            divFormGroup.appendChild(newLabel);
            divFormGroup.appendChild(ingredientSelect);

            divFormGroup.appendChild(quantity)
            divFormGroup.appendChild(unitySelect)


            ingredient_list.appendChild(divFormGroup);
            //Todo: Create Ingredient with autocomplete (name ingredient) + quantity + unity
        },

        closeModal(){
            this.$emit('close')
        }
    }
    
}
</script>