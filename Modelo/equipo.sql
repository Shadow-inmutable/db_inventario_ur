-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-08-2024 a las 06:14:42
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pureba_in`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo`
--

CREATE TABLE `equipo` (
  `id` int(11) NOT NULL,
  `serial` varchar(20) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `modelo` varchar(15) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `fecha_compra` date NOT NULL,
  `garantia` int(11) NOT NULL,
  `clasificacion` varchar(12) NOT NULL,
  `cuentadante_id` int(11) NOT NULL,
  `ubicacion_id` int(11) NOT NULL,
  `proveedor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipo`
--

INSERT INTO `equipo` (`id`, `serial`, `marca`, `modelo`, `tipo`, `fecha_compra`, `garantia`, `clasificacion`, `cuentadante_id`, `ubicacion_id`, `proveedor_id`) VALUES
(5, '123-BC', 'Dell', 'model 1', 'Todo en un', '2024-08-01', 12, 'Administrati', 6, 1, 2),
(6, '123456987', 'Dell', 'One touch', 'Laptop', '2024-08-15', 12, 'Administraci', 6, 1, 4),
(7, '1111111', 'hp', 'hp 2', 'All in one', '2020-12-24', 5, 'Formación', 6, 1, 5);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `serial` (`serial`),
  ADD KEY `equ_cue` (`cuentadante_id`),
  ADD KEY `equ_ubi` (`ubicacion_id`),
  ADD KEY `equ_pro` (`proveedor_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipo`
--
ALTER TABLE `equipo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD CONSTRAINT `equ_cue` FOREIGN KEY (`cuentadante_id`) REFERENCES `cuentadante` (`id`),
  ADD CONSTRAINT `equ_pro` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`),
  ADD CONSTRAINT `equ_ubi` FOREIGN KEY (`ubicacion_id`) REFERENCES `ubicacion` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
