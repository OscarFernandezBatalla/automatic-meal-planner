-- INGREDIENTS
INSERT INTO `meals`.`ingredients` (`ingredient_name`) VALUES ('Patata');
INSERT INTO `meals`.`ingredients` (`ingredient_name`) VALUES ('Cebolla');
INSERT INTO `meals`.`ingredients` (`ingredient_name`) VALUES ('Huevo');
INSERT INTO `meals`.`ingredients` (`ingredient_name`) VALUES ('Aceite');
INSERT INTO `meals`.`ingredients` (`ingredient_name`) VALUES ('Sal');

-- Quantities
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('1/2');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('1');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('2');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('3');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('4');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('5');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('6');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('7');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('8');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ('9');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ( '10');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ( 'Chorrito');
INSERT INTO `meals`.`quantities` (`quantity_name`) VALUES ( 'Pizca');

-- Levels
INSERT INTO `meals`.`difficulty` (`difficulty_name`, `difficulty_value`) VALUES ('Muy fácil', 0);
INSERT INTO `meals`.`difficulty` (`difficulty_name`, `difficulty_value`) VALUES ('Fácil', 1);
INSERT INTO `meals`.`difficulty` (`difficulty_name`, `difficulty_value`) VALUES ('Media', 2);
INSERT INTO `meals`.`difficulty` (`difficulty_name`, `difficulty_value`) VALUES ('Difícil', 3);
INSERT INTO `meals`.`difficulty` (`difficulty_name`, `difficulty_value`) VALUES ('Muy difícil', 4);

-- Cuisine style
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('Asiática');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('Mediterránea');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('Francesa');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('India');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('Italiana');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('Vegetariana');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('Mejicana');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_name`) VALUES ('Americana');

-- Recipes
INSERT INTO `meals`.`recipes` (`recipe_name`, `difficulty_id`, `cuisine_style_id`, `diners`) VALUES ('Tortilla de Patatas', 2, 2, 2);
INSERT INTO `meals`.`recipes` (`recipe_name`, `difficulty_id`, `cuisine_style_id`, `diners`) VALUES ('Tortilla Francesa', 1, 3, 1);

-- -- Recipes - Ingredients
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES (1, 1, 3);
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES (1, 2, 2);
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES (1, 3, 5);
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES (1, 4, 12);
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES (1, 5, 13);
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES (2, 3, 3);
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES (2, 4, 12);
