-- phpMyAdmin SQL Dump
<<<<<<< HEAD
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2020 at 01:58 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5
=======
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-05-2022 a las 10:36:15
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.1.32
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
<<<<<<< HEAD
-- Database: `listingpage`
=======
-- Base de datos: `listingpage`
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823
--

-- --------------------------------------------------------

--
<<<<<<< HEAD
-- Table structure for table `listings`
=======
-- Estructura de tabla para la tabla `listings`
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823
--

CREATE TABLE `listings` (
  `listing_id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `listing_title` varchar(50) NOT NULL,
  `listing_domain` varchar(50) NOT NULL,
  `listing_description` text NOT NULL,
  `listing_price` decimal(10,0) NOT NULL,
  `listing_expiration` date NOT NULL,
  `listing_start` date NOT NULL,
  `listing_creation` timestamp NOT NULL DEFAULT current_timestamp(),
  `listing_status` varchar(50) NOT NULL,
  `listing_type` varchar(50) NOT NULL,
  `listing_special` varchar(50) NOT NULL,
  `listing_buyer` int(11) DEFAULT NULL,
  `listing_multimedia` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`listing_multimedia`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
<<<<<<< HEAD
-- Dumping data for table `listings`
--

INSERT INTO `listings` (`listing_id`, `uid`, `listing_title`, `listing_domain`, `listing_description`, `listing_price`, `listing_expiration`, `listing_start`, `listing_creation`, `listing_status`, `listing_type`, `listing_special`, `listing_buyer`, `listing_multimedia`) VALUES
(1, 1, 'rreerer', 'reererer', 'ererererer', '44', '2020-05-19', '2020-05-14', '2020-05-28 04:33:11', 'Active', 'Normal', 'None', 1, '{ \"name\":\"John\" }'),
(2, 1, 'tester2 proyect', '34434dfdfdf', 'redffredfdfdfdftrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrfttrtr', '6565', '2020-05-29', '2020-05-29', '2020-05-29 04:30:42', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(3, 2, 'reerer', 'weewwewe', 'weerwerererweereerererererererererrreererer', '322323', '2020-05-29', '2020-05-29', '2020-05-29 04:34:17', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(4, 3, 'teser', 'reererererer', 'reererererererererererererererererererreer', '3434', '2020-05-29', '2020-05-29', '2020-05-29 04:48:09', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(5, 3, 'testeee', 'weewwewe', 'ddsdsdsdsdfddfdffffffffffffffffffffffffffffffffffffdfffddfdfdfdfdfdfdfdf', '34433', '2020-05-30', '2020-05-30', '2020-05-30 05:39:33', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(6, 1, 'Json Test 1', 'wwww.aquati.cl', 'TESTanfrage von der Json API der erste Versuch mit Json', '565', '2020-05-30', '2020-05-30', '2020-05-31 03:32:58', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(7, 1, 'Json Test 1', 'wwww.aquati.cl', 'TESTanfrage von der Json API der erste Versuch mit Json', '565', '2020-05-30', '2020-05-30', '2020-05-31 03:35:04', 'Active', 'Buy', 'Feature1W', NULL, NULL);
=======
-- Volcado de datos para la tabla `listings`
--

INSERT INTO `listings` (`listing_id`, `uid`, `listing_title`, `listing_domain`, `listing_description`, `listing_price`, `listing_expiration`, `listing_start`, `listing_creation`, `listing_status`, `listing_type`, `listing_special`, `listing_buyer`, `listing_multimedia`) VALUES
(1, 1, 'Selling domain1.com', 'domain1.com', 'Quisque a tempor ipsum, vulputate pharetra augue. Fusce ipsum sapien, dignissim in tempus ac, tincidunt eu augue. ', '44', '2021-05-19', '2021-05-14', '2020-05-28 04:33:11', 'Active', 'Normal', 'None', 1, '{ \"name\":\"John\" }'),
(2, 1, 'Selling domain2.com', 'domain2.com', 'Sed ut massa ac massa dignissim tincidunt. ', '6565', '2020-05-29', '2020-05-29', '2020-05-29 04:30:42', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(3, 2, 'Selling domain3.com', 'domain3.com', 'fusce ipsum sapien, dignissim in tempus ac, tincidunt eu augue. Quisque eu faucibus ante.', '322323', '2020-05-29', '2020-05-29', '2020-05-29 04:34:17', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(4, 3, 'Selling domain4.com', 'domain4.com', 'Quisque eu faucibus ante. Vivamus non imperdiet quam, ut pulvinar urna.', '3434', '2020-05-29', '2020-05-29', '2020-05-29 04:48:09', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(5, 3, 'Selling domain5.com ', 'domain5.com', 'Vestibulum non vulputate felis. Mauris eget elit elit. Nunc condimentum diam mi, vitae ullamcorper mauris hendrerit at. ', '34433', '2020-05-30', '2020-05-30', '2020-05-30 05:39:33', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(6, 1, 'Selling domain6.com', 'domain6.com', 'Quisque eu faucibus ante. Vivamus non imperdiet quam, ut pulvinar urna.', '565', '2020-05-30', '2020-05-30', '2020-05-31 03:32:58', 'Active', 'Buy', 'Feature1W', NULL, NULL),
(7, 1, 'Selling domain7.com', 'domain7.com', 'Quisque a tempor ipsum, vulputate pharetra augue. Fusce ipsum sapien, dignissim in tempus ac, tincidunt eu augue. Quisque eu faucibus ante. Vivamus non imperdiet quam, ut pulvinar urna.', '565', '2022-03-30', '2022-03-30', '2022-03-31 02:35:04', 'Active', 'Buy', 'Feature1W', NULL, NULL);
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823

-- --------------------------------------------------------

--
<<<<<<< HEAD
-- Table structure for table `users`
=======
-- Estructura de tabla para la tabla `users`
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823
--

CREATE TABLE `users` (
  `uid` int(11) NOT NULL,
  `username` varchar(64) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(400) NOT NULL,
  `fullname` varchar(64) NOT NULL,
  `roleid` int(11) NOT NULL,
  `userstatus` varchar(64) NOT NULL,
  `usercreation` timestamp NOT NULL DEFAULT current_timestamp(),
  `company` varchar(50) DEFAULT NULL,
  `aproves` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
<<<<<<< HEAD
-- Dumping data for table `users`
--

INSERT INTO `users` (`uid`, `username`, `email`, `password`, `fullname`, `roleid`, `userstatus`, `usercreation`, `company`, `aproves`) VALUES
(1, 'test', 'christian.bader@futurework.cl', '$5$rounds=535000$X4LQ/KFA6lT09YVS$og2ETwS7/sSpUldX.hp8ocKdEg3XpUTGtqyKkydO9Y.', 'test', 1, 'active', '2020-06-01 01:21:13', NULL, NULL),
(2, 'tester2', 'dfdfdfdfd@de.de', '123456', 'tester2', 0, 'active', '2020-05-29 04:21:34', NULL, NULL),
(3, 'tester3', 'jjjj@ddd.de', '123456', 'hermann', 1, 'deactived', '2020-05-29 04:43:25', NULL, NULL),
(24, 'jerome', 'jerome.bader@gmail.com', '$5$rounds=535000$Nn/ym7v4Gi8l7Rdv$fzgIagskuO8PkEwk7sRxnffavCH04KSXigP94z93yCB', 'jerome', 1, 'active', '2020-06-01 01:00:44', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `listings`
=======
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`uid`, `username`, `email`, `password`, `fullname`, `roleid`, `userstatus`, `usercreation`, `company`, `aproves`) VALUES
(1, 'test', 'christian@test.com', '$5$rounds=535000$L1/wYoIxY/5VJsSv$HAvcvr3ymR0.P1MApnfJSNhM.f.Ou.trpfkeSKGQRqD', 'test', 1, 'active', '2021-03-31 00:21:13', NULL, NULL),
(2, 'tester2', 'dfdfdfdfd@de.de', '$5$rounds=535000$L1/wYoIxY/5VJsSv$HAvcvr3ymR0.P1MApnfJSNhM.f.Ou.trpfkeSKGQRqD', 'tester2', 0, 'active', '2022-03-29 03:21:34', NULL, NULL),
(3, 'tester3', 'jjjj@ddd.de', '$5$rounds=535000$L1/wYoIxY/5VJsSv$HAvcvr3ymR0.P1MApnfJSNhM.f.Ou.trpfkeSKGQRqD', 'hermann', 1, 'deactived', '2022-03-29 03:43:25', NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `listings`
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823
--
ALTER TABLE `listings`
  ADD PRIMARY KEY (`listing_id`);

--
<<<<<<< HEAD
-- Indexes for table `users`
=======
-- Indices de la tabla `users`
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uid`);

--
<<<<<<< HEAD
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `listings`
=======
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `listings`
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823
--
ALTER TABLE `listings`
  MODIFY `listing_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
<<<<<<< HEAD
-- AUTO_INCREMENT for table `users`
=======
-- AUTO_INCREMENT de la tabla `users`
>>>>>>> c1a32949eed24d22dd1494acef15df5b7e367823
--
ALTER TABLE `users`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
