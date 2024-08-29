----
Estructura SQL software -----

CREATE TABLE `db_inventario_ur`.`software` (`id` INT NOT NULL AUTO_INCREMENT , `nombre` INT(15) NOT NULL , `version` INT(15) NOT NULL , `instalationKey` INT(15) NOT NULL , `cantLincencias` INT(15) NOT NULL , `vigencias` INT(10) NOT NULL , `id_equipo` INT(15) NOT NULL , `id_proveedor` INT(15) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;