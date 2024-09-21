-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-09-2024 a las 03:17:57
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

--
-- Volcado de datos para la tabla `binnacle`
--

INSERT INTO `binnacle` (`id`, `user`, `action`, `date`, `ip_address`) VALUES
(218, 10, 'Atlantox ha ingresado al sistema', '2024-08-16 19:30:38', '10.0.5.105'),
(219, 10, 'Creó al jugador Gwen', '2024-08-16 19:30:49', '10.0.5.105'),
(220, 10, 'Atlantox ha ingresado al sistema', '2024-08-18 02:38:56', '10.0.5.105'),
(221, 10, 'Atlantox ha ingresado al sistema', '2024-08-18 02:51:20', '10.0.5.105'),
(222, 10, 'Creó el torneo del día 2024-08-10', '2024-08-18 02:55:31', '10.0.5.105'),
(223, 10, 'Creó al jugador Gerardo', '2024-08-18 23:14:10', '10.0.5.105'),
(224, 10, 'Creó al jugador Ricardo', '2024-08-18 23:14:20', '10.0.5.105'),
(225, 10, 'Creó al jugador Angel Virgüez', '2024-08-18 23:14:32', '10.0.5.105'),
(226, 10, 'Creó al jugador Leonardo', '2024-08-18 23:14:46', '10.0.5.105'),
(227, 10, 'Creó al jugador Mark', '2024-08-18 23:14:56', '10.0.5.105'),
(228, 10, 'Creó al jugador Alexander', '2024-08-18 23:15:06', '10.0.5.105'),
(229, 10, 'Creó el deck Alela, Cunning Conqueror', '2024-08-18 23:15:39', '10.0.5.105'),
(230, 10, 'Creó el deck Atarka, World Render', '2024-08-18 23:16:10', '10.0.5.105'),
(231, 10, 'Creó el deck Kruphix, God of Horizons', '2024-08-18 23:16:41', '10.0.5.105'),
(232, 10, 'Creó el deck Voja, Jaws Of The Conclave', '2024-08-18 23:17:17', '10.0.5.105'),
(233, 10, 'Creó el deck Jhoira, Ageless Innovator', '2024-08-18 23:17:46', '10.0.5.105'),
(234, 10, 'Creó el deck Astarion, the Decadent', '2024-08-18 23:18:39', '10.0.5.105'),
(235, 10, 'Creó el deck Balmor, Battlemage Captain', '2024-08-18 23:19:20', '10.0.5.105'),
(236, 10, 'Creó el deck Olivia, Opulent Outlaw', '2024-08-18 23:19:45', '10.0.5.105'),
(237, 10, 'Creó el torneo del día 2024-08-18', '2024-08-18 23:24:09', '10.0.5.105'),
(238, 10, 'Creó al jugador Daniel Ganzo', '2024-08-25 23:58:34', '10.0.5.105'),
(239, 10, 'Creó al jugador Nandy', '2024-08-25 23:58:44', '10.0.5.105'),
(240, 10, 'Creó al jugador Miguel', '2024-08-25 23:58:51', '10.0.5.105'),
(241, 10, 'Creó al jugador Gabriel', '2024-08-25 23:59:06', '10.0.5.105'),
(242, 10, 'Creó el deck Kykar, Wind\'s Fury', '2024-08-26 00:00:09', '10.0.5.105'),
(243, 10, 'Creó el deck Leori, Sparktouched Hunter', '2024-08-26 00:01:14', '10.0.5.105'),
(244, 10, 'Creó el deck Keleth + Tevesh', '2024-08-26 00:02:27', '10.0.5.105'),
(245, 10, 'Creó el deck Animar, Soul of Elements', '2024-08-26 00:03:14', '10.0.5.105'),
(246, 10, 'Creó el deck Krenko, Tin Street Kingpin', '2024-08-26 00:03:50', '10.0.5.105'),
(247, 10, 'Creó el deck Minsc & Boo, Timeless Heroes', '2024-08-26 00:04:32', '10.0.5.105'),
(248, 10, 'Modificó el deck \"4\"', '2024-08-26 00:04:59', '10.0.5.105'),
(249, 10, 'Creó el torneo del día 2024-08-25', '2024-08-26 00:10:27', '10.0.5.105'),
(250, 10, 'Modificó el deck \"5\"', '2024-08-26 00:10:50', '10.0.5.105'),
(251, 10, 'Modificó el deck \"10\"', '2024-08-26 00:11:18', '10.0.5.105'),
(252, 10, 'Atlantox ha ingresado al sistema', '2024-09-01 10:12:27', '127.0.0.1'),
(253, 10, 'Creó el torneo del día 2024-08-31', '2024-09-01 10:13:18', '127.0.0.1'),
(254, 10, 'Creó el torneo del día 2024-08-10', '2024-09-20 18:02:41', '127.0.0.1'),
(255, 10, 'Creó el torneo del día 2024-08-10', '2024-09-20 18:11:10', '127.0.0.1');

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
(13, 'Alela, Cunning Conqueror'),
(24, 'Animar, Soul of Elements'),
(18, 'Astarion, the Decadent'),
(14, 'Atarka, World Render'),
(19, 'Balmor, Battlemage Captain'),
(12, 'Ellivere of the Wild Court'),
(2, 'Ertai Resurrected'),
(5, 'Horde of Notions'),
(17, 'Jhoira, Ageless Innovator'),
(23, 'Keleth + Tevesh'),
(25, 'Krenko, Tin Street Kingpin'),
(15, 'Kruphix, God of Horizons'),
(21, 'Kykar, Wind\'s Fury'),
(22, 'Leori, Sparktouched Hunter'),
(26, 'Minsc & Boo, Timeless Heroes'),
(9, 'Mogis, God of Slaugther -Tax Life'),
(8, 'Octavia, Living thesis'),
(11, 'Okinec -Aggro'),
(20, 'Olivia, Opulent Outlaw'),
(3, 'Purphoros, Bronze-Blooded'),
(6, 'Sliver Overlord'),
(4, 'Thalia and The Gitrog Monster'),
(10, 'The necrobloom'),
(1, 'Umbris, fear manifest'),
(16, 'Voja, Jaws Of The Conclave');

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
(42, 12, 'Blanco'),
(43, 13, 'Negro'),
(44, 13, 'Azul'),
(45, 14, 'Verde'),
(46, 14, 'Rojo'),
(47, 15, 'Azul'),
(48, 15, 'Verde'),
(49, 16, 'Verde'),
(50, 16, 'Rojo'),
(51, 16, 'Blanco'),
(52, 17, 'Azul'),
(53, 17, 'Rojo'),
(54, 18, 'Negro'),
(55, 18, 'Blanco'),
(56, 19, 'Azul'),
(57, 19, 'Rojo'),
(58, 20, 'Negro'),
(59, 20, 'Rojo'),
(60, 20, 'Blanco'),
(61, 21, 'Rojo'),
(62, 21, 'Blanco'),
(63, 21, 'Azul'),
(64, 22, 'Rojo'),
(65, 22, 'Blanco'),
(66, 22, 'Azul'),
(67, 23, 'Negro'),
(68, 23, 'Blanco'),
(69, 24, 'Rojo'),
(70, 24, 'Verde'),
(71, 24, 'Azul'),
(72, 25, 'Rojo'),
(73, 26, 'Rojo'),
(74, 26, 'Verde');

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
(18, 'Alexander'),
(15, 'Angel Virgüez'),
(6, 'Antoanel'),
(9, 'Atlantox'),
(3, 'Boros'),
(19, 'Daniel Ganzo'),
(7, 'Danny'),
(22, 'Gabriel'),
(13, 'Gerardo'),
(12, 'Gwen'),
(16, 'Leonardo'),
(11, 'Luis Lugo'),
(8, 'Manstrac'),
(10, 'Marcelo'),
(17, 'Mark'),
(21, 'Miguel'),
(20, 'Nandy'),
(14, 'Ricardo'),
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
  `pot` decimal(10,2) NOT NULL DEFAULT 0.00,
  `season` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tournament`
--

INSERT INTO `tournament` (`id`, `date`, `format`, `observation`, `pot`, `season`, `active`) VALUES
(2, '2024-08-18', 'Coliseo', '', '0.00', 1, 1),
(3, '2024-08-25', 'Coliseo', '', '0.00', 1, 1),
(4, '2024-08-31', 'EDH', 'jsxfykguk', '0.00', 1, 1),
(5, '2024-08-10', 'Coliseo', '', '5.00', 1, 1),
(6, '2024-08-10', 'Coliseo', '', '5.42', 1, 1);

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

--
-- Volcado de datos para la tabla `tournament_result`
--

INSERT INTO `tournament_result` (`id`, `tournament`, `player`, `deck`, `wins`, `winner`) VALUES
(5, 2, 18, 19, '3.25', 0),
(6, 2, 15, 15, '2.33', 0),
(7, 2, 9, 1, '1.25', 0),
(8, 2, 7, 17, '3.91', 0),
(9, 2, 13, 13, '2.33', 0),
(10, 2, 12, 20, '1.33', 0),
(11, 2, 1, 2, '4.58', 0),
(12, 2, 2, 4, '2.33', 0),
(13, 2, 14, 14, '5.33', 0),
(14, 2, 17, 18, '8.33', 0),
(15, 2, 16, 16, '10.00', 1),
(16, 2, 10, 12, '0.00', 0),
(17, 3, 6, 25, '6.00', 0),
(18, 3, 18, 19, '6.33', 0),
(19, 3, 9, 1, '4.00', 0),
(20, 3, 1, 2, '10.00', 0),
(21, 3, 7, 17, '20.00', 1),
(22, 3, 19, 21, '0.00', 0),
(23, 3, 2, 4, '13.00', 0),
(24, 3, 15, 15, '5.00', 0),
(25, 3, 22, 24, '10.00', 0),
(26, 3, 4, 5, '2.00', 0),
(27, 3, 16, 16, '3.33', 0),
(28, 3, 20, 22, '0.00', 0),
(29, 3, 21, 23, '8.00', 0),
(30, 3, 12, 20, '5.00', 0),
(31, 3, 14, 14, '0.00', 0),
(32, 3, 13, 13, '0.00', 0),
(33, 3, 17, 26, '7.33', 0),
(34, 4, 18, 24, '1.00', 0),
(35, 4, 15, 14, '2.00', 0),
(36, 4, 6, 10, '5.00', 1),
(37, 4, 3, 19, '0.00', 0),
(38, 5, 9, 1, '3.50', 0),
(39, 5, 2, 2, '2.10', 0),
(40, 5, 3, 3, '2.00', 0),
(41, 5, 4, 4, '4.80', 1),
(42, 6, 9, 1, '3.50', 0),
(43, 6, 2, 2, '2.10', 0),
(44, 6, 3, 3, '2.00', 0),
(45, 6, 4, 4, '4.80', 1);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=256;

--
-- AUTO_INCREMENT de la tabla `deck`
--
ALTER TABLE `deck`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `deck_color`
--
ALTER TABLE `deck_color`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `season`
--
ALTER TABLE `season`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tournament`
--
ALTER TABLE `tournament`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `tournament_result`
--
ALTER TABLE `tournament_result`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

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
