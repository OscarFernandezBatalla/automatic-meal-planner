import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RecipeDetailView from '../views/RecipeDetailView.vue'
import MyRecipesView from '../views/MyRecipesView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/recipe',
    name: 'recipe-details',
    component: RecipeDetailView
  },

  {
    path: '/my-recipes',
    name: 'my-recipes',
    component: MyRecipesView
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
