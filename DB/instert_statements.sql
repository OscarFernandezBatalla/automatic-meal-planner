-- INGREDIENTS
INSERT INTO `meals`.`ingredients` (`ingredient_id`, `ingredient_name`) VALUES ('0', 'Patata');
INSERT INTO `meals`.`ingredients` (`ingredient_id`, `ingredient_name`) VALUES ('1', 'Cebolla');
INSERT INTO `meals`.`ingredients` (`ingredient_id`, `ingredient_name`) VALUES ('2', 'Huevo');
INSERT INTO `meals`.`ingredients` (`ingredient_id`, `ingredient_name`) VALUES ('3', 'Aceite');
INSERT INTO `meals`.`ingredients` (`ingredient_id`, `ingredient_name`) VALUES ('4', 'Sal');



-- Quantities
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('0', '1/2');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('1', '1');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('2', '2');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('3', '3');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('4', '4');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('5', '5');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('6', '6');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('7', '7');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('8', '8');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('9', '9');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('10', '10');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('11', 'Chorrito');
INSERT INTO `meals`.`quantities` (`quantity_id`, `quantity_name`) VALUES ('12', 'Pizca');




-- Levels
INSERT INTO `meals`.`difficulty` (`difficulty_id`, `difficulty_name`, `difficulty_value`) VALUES ('0', 'Muy fácil', '0');
INSERT INTO `meals`.`difficulty` (`difficulty_id`, `difficulty_name`, `difficulty_value`) VALUES ('1', 'Fácil', '1');
INSERT INTO `meals`.`difficulty` (`difficulty_id`, `difficulty_name`, `difficulty_value`) VALUES ('2', 'Media', '2');
INSERT INTO `meals`.`difficulty` (`difficulty_id`, `difficulty_name`, `difficulty_value`) VALUES ('3', 'Difícil', '3');
INSERT INTO `meals`.`difficulty` (`difficulty_id`, `difficulty_name`, `difficulty_value`) VALUES ('4', 'Muy difícil', '4');


-- Cuisine style
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('0', 'Asiática');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('1', 'Mediterránea');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('2', 'Francesa');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('3', 'India');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('4', 'Italiana');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('5', 'Vegetariana');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('6', 'Mejicana');
INSERT INTO `meals`.`cuisine_styles` (`cuisine_style_id`, `cuisine_style_name`) VALUES ('7', 'Americana');


-- Recipes
INSERT INTO `meals`.`recipes` (`recipe_id`, `recipe_name`, `difficulty_id`, `cuisine_style_id`, `diners`) VALUES ('0', 'Trotilla de Patatas', 1, 1, 2);
INSERT INTO `meals`.`recipes` (`recipe_id`, `recipe_name`, `difficulty_id`, `cuisine_style_id`, `diners`) VALUES ('1', 'Tortilla Francesa', 0, 2, 1);


-- Recipes - Ingredients
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES ('0', '0', '2');
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES ('0', '1', '1');
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES ('0', '2', '4');
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES ('0', '3', '11');
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES ('0', '4', '12');
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES ('1', '2', '2');
INSERT INTO `meals`.`recipes_ingredients` (`recipe_id`, `ingredient_id`, `quantity_id`) VALUES ('1', '3', '11');
