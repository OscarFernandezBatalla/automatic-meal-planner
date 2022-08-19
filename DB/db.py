import mysql.connector
import DB.config as config
import pandas as pd

class Database:

    def __init__(self):
        self.db_instance = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_DATABASE,
        )

        self.cursor = self.db_instance.cursor()

    def query_res_to_df(self, result_sql, column_names):
        return pd.DataFrame(result_sql, columns=column_names)

    """
    GETTER FUNCTIONS
    """
    def get_all_recipes(self):
        self.cursor.execute("SELECT * FROM recipes")
        result = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]
        return self.query_res_to_df(result, column_names)

    def get_all_ingredients(self):
        self.cursor.execute("SELECT * FROM ingredients")
        result = self.cursor.fetchall()

        for x in result:
            print(x)

    def get_all_quantities(self):
        self.cursor.execute("SELECT * FROM quantities")
        result = self.cursor.fetchall()

        for x in result:
            print(x)

    def get_all_difficulty_levels(self):
        self.cursor.execute("SELECT * FROM difficulty")
        result = self.cursor.fetchall()

        for x in result:
            print(x)

    def get_all_cuisine_styles(self):
        self.cursor.execute("SELECT * FROM cuisine_styles")
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

    """
    INSERT FUNCTIONS
    """

    def insert_ingredient(self, quantity_name):

        sql = "INSERT INTO meals.quantities (quantity_id, quantity_name) VALUES (%s, %s);"
        val = ("John", "Highway 21")
        self.cursor.execute(sql, val)

        self.db_instance.commit()

        print(self.cursor.rowcount, "records inserted.")