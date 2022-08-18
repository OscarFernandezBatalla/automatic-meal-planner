import mysql.connector
import DB.config as config

class Database:

    def __init__(self):
        self.db_instance = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_DATABASE,
        )

        self.cursor = self.db_instance.cursor()

    def get_all_recipes(self):
        self.cursor.execute("SELECT * FROM recipes")
        result = self.cursor.fetchall()

        for x in result:
            print(x)

    def get_ingredient_names_of_recipe(self, recipe_id):
        self.cursor.execute("SELECT recipes_ingredients.ingredient_id, ingredient_name "
                            "FROM recipes_ingredients "
                            "INNER JOIN ingredients "
                            "ON recipes_ingredients.ingredient_id = ingredients.ingredient_id "
                            "WHERE recipes_ingredients.recipe_id = %s;", (recipe_id,))
        result = self.cursor.fetchall()

        for x in result:
            print(x)
