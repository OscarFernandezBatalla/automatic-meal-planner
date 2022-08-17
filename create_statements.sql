CREATE TABLE `cuisine_styles` (
  `cuisine_style_id` int NOT NULL,
  `cuisine_style_name` varchar(45) NOT NULL,
  PRIMARY KEY (`cuisine_style_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `difficulty` (
  `difficulty_id` int NOT NULL,
  `difficulty_name` varchar(45) NOT NULL,
  `difficulty_value` int NOT NULL,
  PRIMARY KEY (`difficulty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `ingredients` (
  `ingredient_id` int NOT NULL,
  `ingredient_name` varchar(45) NOT NULL,
  PRIMARY KEY (`ingredient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `quantities` (
  `quantity_id` int NOT NULL,
  `quantity_name` varchar(45) NOT NULL,
  PRIMARY KEY (`quantity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `recipes` (
  `recipe_id` int NOT NULL,
  `recipe_name` varchar(45) NOT NULL,
  `difficulty_id` int NOT NULL,
  `cuisine_style_id` int NOT NULL,
  `diners` int NOT NULL,
  PRIMARY KEY (`recipe_id`),
  KEY `difficulty_id_idx` (`difficulty_id`),
  KEY `cuisine_style_id_idx` (`cuisine_style_id`),
  CONSTRAINT `cuisine_style_id` FOREIGN KEY (`cuisine_style_id`) REFERENCES `cuisine_styles` (`cuisine_style_id`),
  CONSTRAINT `difficulty_id` FOREIGN KEY (`difficulty_id`) REFERENCES `difficulty` (`difficulty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `recipes_ingredients` (
  `recipe_id` int NOT NULL,
  `ingredient_id` int NOT NULL,
  `quantity_id` int NOT NULL,
  PRIMARY KEY (`ingredient_id`,`recipe_id`),
  KEY `recipe_id_idx` (`recipe_id`),
  KEY `quantity_id_idx` (`quantity_id`),
  CONSTRAINT `ingredient_id` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`),
  CONSTRAINT `quantity_id` FOREIGN KEY (`quantity_id`) REFERENCES `quantities` (`quantity_id`),
  CONSTRAINT `recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
