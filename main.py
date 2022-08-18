from DB.db import Database


def main():
    db = Database()
    db.get_ingredient_names_of_recipe(0)


if __name__ == "__main__":
    main()
