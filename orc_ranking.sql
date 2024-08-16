-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-08-2024 a las 17:12:42
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `orc_ranking`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `binnacle`
--

CREATE TABLE `binnacle` (
  `id` int(11) NOT NULL,
  `user` int(11) NOT NULL,
  `action` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `ip_address` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `color`
--

CREATE TABLE `color` (
  `name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `color`
--

INSERT INTO `color` (`name`) VALUES
('Azul'),
('Blanco'),
('Incoloro'),
('Negro'),
('Rojo'),
('Verde');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deck`
--

CREATE TABLE `deck` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `deck`
--

INSERT INTO `deck` (`id`, `name`) VALUES
(12, 'Ellivere of the Wild Court'),
(2, 'Ertai Resurrected'),
(5, 'Horde of Notions -Midrange'),
(9, 'Mogis, God of Slaugther -Tax Life'),
(8, 'Octavia, Living thesis'),
(11, 'Okinec -Aggro'),
(3, 'Purphoros, Bronze-Blooded'),
(6, 'Sliver Overlord'),
(4, 'Thalia and The Gitrog Monster -Midrange'),
(10, 'The necrobloom -Midrange'),
(1, 'Umbris, fear manifest');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deck_color`
--

CREATE TABLE `deck_color` (
  `id` int(11) NOT NULL,
  `deck` int(11) NOT NULL,
  `color` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `deck_color`
--

INSERT INTO `deck_color` (`id`, `deck`, `color`) VALUES
(1, 1, 'Azul'),
(2, 1, 'Negro'),
(3, 2, 'Azul'),
(5, 2, 'Negro'),
(6, 5, 'Azul'),
(7, 5, 'Blanco'),
(8, 5, 'Negro'),
(9, 5, 'Rojo'),
(10, 5, 'Verde'),
(16, 6, 'Blanco'),
(17, 6, 'Verde'),
(18, 6, 'Azul'),
(19, 6, 'Rojo'),
(20, 6, 'Negro'),
(26, 3, 'Rojo'),
(27, 4, 'Blanco'),
(28, 4, 'Negro'),
(29, 4, 'Verde'),
(33, 8, 'Azul'),
(34, 9, 'Negro'),
(35, 9, 'Rojo'),
(36, 10, 'Blanco'),
(37, 10, 'Verde'),
(38, 10, 'Negro'),
(39, 11, 'Blanco'),
(40, 11, 'Verde'),
(41, 12, 'Verde'),
(42, 12, 'Blanco');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `game_format`
--

CREATE TABLE `game_format` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `game_format`
--

INSERT INTO `game_format` (`id`, `name`) VALUES
(3, 'Coliseo'),
(5, 'Coliseo Duel'),
(2, 'EDH'),
(1, 'Pauper');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisson`
--

CREATE TABLE `permisson` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `level` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `permisson`
--

INSERT INTO `permisson` (`id`, `name`, `level`) VALUES
(29, 'Admin', 'Super'),
(30, 'Editor', 'Super'),
(31, 'Estadísticas', 'Super'),
(32, 'Jugadores', 'Super'),
(33, 'Mazos', 'Super'),
(34, 'Formatos', 'Super'),
(35, 'Temporadas', 'Super'),
(36, 'Torneos', 'Super'),
(37, 'Editor', 'Admin'),
(38, 'Jugadores', 'Admin'),
(39, 'Mazos', 'Admin'),
(40, 'Estadísticas', 'Admin'),
(41, 'Temporadas', 'Admin'),
(42, 'Formatos', 'Admin'),
(43, 'Torneos', 'Admin'),
(44, 'Mazos', 'Editor'),
(45, 'Jugadores', 'Editor'),
(46, 'Estadísticas', 'Editor'),
(47, 'Formatos', 'Editor'),
(48, 'Bitácora', 'Super'),
(49, 'Bitácora', 'Admin');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `player`
--

CREATE TABLE `player` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `player`
--

INSERT INTO `player` (`id`, `name`) VALUES
(6, 'Antoanel'),
(9, 'Atlantox'),
(3, 'Boros'),
(7, 'Danny'),
(11, 'Luis Lugo'),
(8, 'Manstrac'),
(10, 'Marcelo'),
(2, 'Roberto Suárez'),
(1, 'Yanez'),
(4, 'Yeshirler Rodríguez');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `season`
--

CREATE TABLE `season` (
  `id` int(11) NOT NULL,
  `name` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `season`
--

INSERT INTO `season` (`id`, `name`, `date`, `active`) VALUES
(1, '1', '2024-08-16', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tournament`
--

CREATE TABLE `tournament` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `format` varchar(50) NOT NULL,
  `observation` varchar(200) NOT NULL,
  `season` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tournament_result`
--

CREATE TABLE `tournament_result` (
  `id` int(11) NOT NULL,
  `tournament` int(11) NOT NULL,
  `player` int(11) NOT NULL,
  `deck` int(11) NOT NULL,
  `wins` decimal(4,2) NOT NULL,
  `winner` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `level` varchar(20) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `token` varchar(200) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `nickname`, `level`, `created_at`, `username`, `password`, `token`, `active`) VALUES
(10, 'Atlantox', 'Super', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$am1VC7JJtJEwA6YHympJfA$g7uf84pTXJKeq5QsUGqDacFoj54gR35J9uwf9KFsX7M', '$argon2id$v=19$m=65536,t=3,p=4$cb6WD/wlSRf4MIxzlJn/hA$0NKlEYkLPgRvStyq1NSLdJZtTaOMKLjizEdhJ9mrONU', 'dcd78902-70b4-40a2-9c17-b7a0486e9980-5f031834-7798-4cb4-a77b-114b3a7b8d6f', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_level`
--

CREATE TABLE `user_level` (
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user_level`
--

INSERT INTO `user_level` (`name`) VALUES
('Admin'),
('Editor'),
('Super');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `binnacle`
--
ALTER TABLE `binnacle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `binnacle_user` (`user`);

--
-- Indices de la tabla `color`
--
ALTER TABLE `color`
  ADD PRIMARY KEY (`name`);

--
-- Indices de la tabla `deck`
--
ALTER TABLE `deck`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `deck_color`
--
ALTER TABLE `deck_color`
  ADD PRIMARY KEY (`id`),
  ADD KEY `deck_color_deck` (`deck`),
  ADD KEY `deck_color_color` (`color`);

--
-- Indices de la tabla `game_format`
--
ALTER TABLE `game_format`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `permisson`
--
ALTER TABLE `permisson`
  ADD PRIMARY KEY (`id`),
  ADD KEY `permisson_user_level` (`level`);

--
-- Indices de la tabla `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `season`
--
ALTER TABLE `season`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tournament`
--
ALTER TABLE `tournament`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tournament_season` (`season`),
  ADD KEY `tournament_format` (`format`);

--
-- Indices de la tabla `tournament_result`
--
ALTER TABLE `tournament_result`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tournament_result_player` (`player`),
  ADD KEY `tournament_result_deck` (`deck`),
  ADD KEY `tournament_result_tournament` (`tournament`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nickname` (`nickname`),
  ADD UNIQUE KEY `token` (`token`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `user_user_level` (`level`);

--
-- Indices de la tabla `user_level`
--
ALTER TABLE `user_level`
  ADD UNIQUE KEY `name` (`name`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `binnacle`
--
ALTER TABLE `binnacle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=218;

--
-- AUTO_INCREMENT de la tabla `deck`
--
ALTER TABLE `deck`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `deck_color`
--
ALTER TABLE `deck_color`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `game_format`
--
ALTER TABLE `game_format`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `permisson`
--
ALTER TABLE `permisson`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT de la tabla `player`
--
ALTER TABLE `player`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `season`
--
ALTER TABLE `season`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tournament`
--
ALTER TABLE `tournament`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tournament_result`
--
ALTER TABLE `tournament_result`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `binnacle`
--
ALTER TABLE `binnacle`
  ADD CONSTRAINT `binnacle_user` FOREIGN KEY (`user`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `deck_color`
--
ALTER TABLE `deck_color`
  ADD CONSTRAINT `deck_color_color` FOREIGN KEY (`color`) REFERENCES `color` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `deck_color_deck` FOREIGN KEY (`deck`) REFERENCES `deck` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `permisson`
--
ALTER TABLE `permisson`
  ADD CONSTRAINT `permisson_user_level` FOREIGN KEY (`level`) REFERENCES `user_level` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tournament`
--
ALTER TABLE `tournament`
  ADD CONSTRAINT `tournament_format` FOREIGN KEY (`format`) REFERENCES `game_format` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tournament_season` FOREIGN KEY (`season`) REFERENCES `season` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tournament_result`
--
ALTER TABLE `tournament_result`
  ADD CONSTRAINT `tournament_result_deck` FOREIGN KEY (`deck`) REFERENCES `deck` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tournament_result_player` FOREIGN KEY (`player`) REFERENCES `player` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tournament_result_tournament` FOREIGN KEY (`tournament`) REFERENCES `tournament` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_user_level` FOREIGN KEY (`level`) REFERENCES `user_level` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
