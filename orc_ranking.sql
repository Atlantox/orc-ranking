-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-08-2024 a las 22:26:23
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
(2, 'Ertai Resurrected'),
(5, 'Horde of Notions'),
(3, 'Purphoros, Bronze-Blooded'),
(6, 'Sliver Overlord'),
(4, 'Thalia and The Gitrog Monster'),
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
(29, 4, 'Verde');

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
(3, 'Boros'),
(2, 'Roberto'),
(1, 'Yanez'),
(4, 'Yeshirler');

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
(1, '1', '2024-07-27', 0),
(2, '2', '2024-07-31', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tournament`
--

CREATE TABLE `tournament` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `format` varchar(50) NOT NULL,
  `season` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tournament`
--

INSERT INTO `tournament` (`id`, `date`, `format`, `season`, `active`) VALUES
(6, '2024-07-31', 'Pauper', 2, 1),
(7, '2024-07-31', 'Pauper', 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tournament_result`
--

CREATE TABLE `tournament_result` (
  `id` int(11) NOT NULL,
  `tournament` int(11) NOT NULL,
  `player` int(11) NOT NULL,
  `deck` int(11) NOT NULL,
  `wins` tinyint(4) NOT NULL,
  `winner` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tournament_result`
--

INSERT INTO `tournament_result` (`id`, `tournament`, `player`, `deck`, `wins`, `winner`) VALUES
(1, 6, 1, 1, 2, 0),
(2, 6, 2, 2, 4, 1),
(3, 6, 3, 3, 1, 0),
(4, 6, 4, 4, 2, 0),
(5, 7, 1, 1, 1, 0),
(6, 7, 2, 2, 2, 0),
(7, 7, 3, 3, 3, 0),
(8, 7, 4, 4, 5, 1);

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
(1, 'Atlantox7', 'Admin', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$3AS4idk0Vww0t4Sb01WeTA$jGz2iJeNl6gDxT2fMeWDqSoxQFQDGMiKysTEl77zrtE', '$argon2id$v=19$m=65536,t=3,p=4$ZdHbxL0d8wcfNPlDgenj+A$fl4pfvgOkUwHLCjxIAP5d794CGpc13YWcDrOWgrvtak', 'd4239cd0-77e5-4d73-bb73-7ba3e9ecbc00-b4828893-f47d-47fe-a5f0-128b13e8a786', 1),
(2, 'KingPepito', 'Editor', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$8UZyhH7/YQKpgg2BSLWMKQ$JZdATk50aVy3c65APOFXkySRzQhodo6cW/zICTsxINQ', '$argon2id$v=19$m=65536,t=3,p=4$l/9fkk5EhOwo+1EpOkKihg$srAta6y+0YKv1ev70s8lfqFaKLzj4b0CHcxW4BrnBeg', '9559e961-3d82-4013-ac43-1071ae4bbea9-48f22212-d27f-439d-a32e-9c7facdc62c2', 0),
(3, 'El pepito2', 'Admin', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$sC68eq03u8/8VvWIlE7V2w$8zFKttxeLrzFfxzoCv38GzAnNGEdln7SamRwOV+1GRY', '$argon2id$v=19$m=65536,t=3,p=4$bHwiNX9DS0r6cPzgUELkUA$XBm8tql9z9n6rvaSX1YAcbyI5ht97u8lLTnFczr4uak', '73361c62-9340-4c9e-9dd3-33a73547d761-029002f7-f5a7-4c99-bdd4-2d179f024977', 1),
(4, 'El pepito3', 'Editor', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$LpxdH78OEo+g1pjBUaK04Q$HqgbgCdtTM4GaXFZ2ZqLmQv6gMs46Ot5c3Y5Am9LMsY', '$argon2id$v=19$m=65536,t=3,p=4$pkySPKBSNnOnewqZdy67Ww$gUgbBU6aqv5xEtiSdWYRDqoYcBVxCVafxysh4vvxnaY', '08bc0ff1-132b-40b4-ad58-c196890dee56-2ded1689-f8da-4534-9abe-67247860d3ab', 0),
(5, 'El pepito4', 'Editor', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$cpWY38BOtU9Obhe3DR3bhA$XLJGqZHPj1WwsM9OL6JMR2yxTWkzjXwPO1Mw6KP1t2I', '$argon2id$v=19$m=65536,t=3,p=4$Wlmnwt6OoPS40ziRz3qwAQ$yFOrGDhX1sE5VjMiOzZgPz+fbwDBGGIwRWl/DkgL8vY', '876bbab3-5890-457b-888b-69c2acfc8a00-c0938fd2-a87d-4451-a865-fe8405df6122', 1),
(6, 'El pepito5', 'Editor', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$jXGc7XJH4hQT3EOUnaG1uA$1x+TERIFqhg2mZshTx2l+mju0tkap4gSoJ1wFnu7j20', '$argon2id$v=19$m=65536,t=3,p=4$3ibE1pMM3ILiSFWS0bvLYg$Xq6xfDW7TdzXaGCd7KGQcMTclfiR6djZ0kZey/iKmsI', 'c6d08108-8771-46b0-adac-f5ce0c03f8ba-3972822d-3b25-4f54-9f43-c9f134eb266a', 1),
(7, 'El pepito6', 'Editor', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$NqtGczl0CGAQlsjt55K79g$NdQWA4SWVJ/h+I14AA6CWZOJ0sBs6asyrNzPJpK8N0U', '$argon2id$v=19$m=65536,t=3,p=4$TMNXWRrkjSqdYirkW/q7DQ$1JXU038KTPR6PX0LBZuf9FtEbJ9P7J6a79NKi5tSoco', '1ccd1e8a-8272-49a9-a93b-af486ec03a8b-e33f60bc-38b5-4811-a889-04fec04acc4a', 1),
(8, 'El pepito7', 'Editor', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$wkHf2sGs7rzpZr8NnxVpCg$qEP5Xdq2Ug2woLQZGgsVYr/ZcO7rm5jaP3SR0P37UGE', '$argon2id$v=19$m=65536,t=3,p=4$0oU/JC3TILOLMY8MHLgQbg$fa5pLqaom4IjiaL6In8wM0BTCYcBEW3yiN5JuKJ1ny0', 'bc7b23dd-63e4-4624-83d4-e2deeb0f3b05-ec23053e-925d-4e4f-ba67-6eff9ea464b3', 1),
(9, 'El pepito8', 'Editor', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$vQfLmfv2+sGfhhFgruSzfA$PgYiH9XFyggzKsZA4P7tZozj32u8NXi0pPhpvd/RLtY', '$argon2id$v=19$m=65536,t=3,p=4$8vf2Q2qT5OoGFfOpMcCC1A$D9CvCFc2PBJI51YAW4uW8ZswGEgJZWVmCzy7VlLGi68', '45ec7c08-aca4-4c1a-9cdf-cbb9c54ff128-27f6b3b2-50c9-48ac-ba63-3103b995561c', 0),
(10, 'Atlantox', 'Admin', '2024-06-25 19:49:47', '$argon2id$v=19$m=65536,t=3,p=4$am1VC7JJtJEwA6YHympJfA$g7uf84pTXJKeq5QsUGqDacFoj54gR35J9uwf9KFsX7M', '$argon2id$v=19$m=65536,t=3,p=4$ISIMPRqNxz8MHYV3iuBYWg$tiPy3KFUbTTRqoormbEbXOcPnVogoDvwppMvGtUYjO8', 'dcd78902-70b4-40a2-9c17-b7a0486e9980-5f031834-7798-4cb4-a77b-114b3a7b8d6f', 1),
(11, 'DonPancho', 'Editor', '2024-06-26 20:34:27', '$argon2id$v=19$m=65536,t=3,p=4$7y5aQNLihofWYQnkBfP7AQ$iLx1BHVf91i4+xygJ8ik7ktrSKDe7FbjqfCO0H9lyP4', '$argon2id$v=19$m=65536,t=3,p=4$Sj06V0NS178Nr1Y77e80Jg$js0aCrjiL6BIyCpwAXWmaUwqRtJVTrsbu2gqQ1GSSBw', '7a04b361-00b1-4f61-98eb-0799e9728f42-a24a222f-099d-4763-b8e4-1433ad347a58', 1),
(12, 'Atlantox2', 'Editor', '2024-07-02 20:35:53', '$argon2id$v=19$m=65536,t=3,p=4$8c1HJ2Rwl9qPc5tf5q4pDQ$F/MJnarJgP24d/x1NfKLMgs75kLZbPVczmMetI+aJvQ', '$argon2id$v=19$m=65536,t=3,p=4$jakjClp3Hl6lVxsGu4/i1w$jRd5Tg6sMRVVqNkY0bX+Hp/U/TvdVm9e2CUooL2GLrg', '439265b4-72b7-4ffe-9223-ae309e09a1aa-a65a350b-8eca-4370-a0c9-8f2d958cc177', 1);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=207;

--
-- AUTO_INCREMENT de la tabla `deck`
--
ALTER TABLE `deck`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `deck_color`
--
ALTER TABLE `deck_color`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `game_format`
--
ALTER TABLE `game_format`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `permisson`
--
ALTER TABLE `permisson`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT de la tabla `player`
--
ALTER TABLE `player`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `season`
--
ALTER TABLE `season`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tournament`
--
ALTER TABLE `tournament`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tournament_result`
--
ALTER TABLE `tournament_result`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

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
