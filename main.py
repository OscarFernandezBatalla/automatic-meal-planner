from DB.db import Database


def main():
    db = Database()
    df = db.get_all_recipes()
    print()


if __name__ == "__main__":
    main()
