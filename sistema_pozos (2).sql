-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2025 at 07:38 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sistema_pozos`
--

-- --------------------------------------------------------

--
-- Table structure for table `almacenamiento`
--

CREATE TABLE `almacenamiento` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `tipo_almacenamiento` varchar(255) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `lon` varchar(255) DEFAULT NULL,
  `capacidad_m3` varchar(255) DEFAULT NULL,
  `diametro_linea` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `archivos`
--

CREATE TABLE `archivos` (
  `id` int(11) NOT NULL,
  `nombre_archivo` varchar(255) NOT NULL,
  `tipo_archivo` varchar(50) DEFAULT NULL,
  `ruta_archivo` varchar(500) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_subida` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `archivos_relaciones`
--

CREATE TABLE `archivos_relaciones` (
  `id` int(11) NOT NULL,
  `archivo_id` int(11) NOT NULL,
  `pozo_id` int(11) DEFAULT NULL,
  `recibo_luz_id` int(11) DEFAULT NULL,
  `medicion_id` int(11) DEFAULT NULL,
  `modificacion_reparacion_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `catalogo_mod_rep`
--

CREATE TABLE `catalogo_mod_rep` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `catalogo_mod_rep`
--

INSERT INTO `catalogo_mod_rep` (`id`, `nombre`, `tipo`, `descripcion`) VALUES
(0, 'MODIFICACION', 'MANTENIMIENTO PREVENTIVO', NULL),
(1, 'REPARACION', 'MANTENIMIENTO CORRECTIVO', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `mediciones`
--

CREATE TABLE `mediciones` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `valor` float NOT NULL,
  `unidad_id` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `modificaciones_reparaciones`
--

CREATE TABLE `modificaciones_reparaciones` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `tipo_modificacion` int(11) DEFAULT NULL,
  `descripcion_modificacion_reparacion` varchar(500) DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp(),
  `responsable` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `motores`
--

CREATE TABLE `motores` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `motor` varchar(255) DEFAULT NULL,
  `velocidad` decimal(10,0) DEFAULT NULL,
  `voltaje` decimal(10,0) DEFAULT NULL,
  `corriente` decimal(10,0) DEFAULT NULL,
  `marca` varchar(255) DEFAULT NULL,
  `modelo` varchar(255) DEFAULT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  `diametro_descarga` decimal(10,0) DEFAULT NULL,
  `estado` enum('activo','inactivo','mantenimiento') NOT NULL DEFAULT 'activo',
  `fotos` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `motores`
--

INSERT INTO `motores` (`id`, `pozo_id`, `motor`, `velocidad`, `voltaje`, `corriente`, `marca`, `modelo`, `tipo`, `diametro_descarga`, `estado`, `fotos`, `descripcion`) VALUES
(6, 7, 'MOTOR AZUL', 3500, NULL, 50, 'SIEMENS', 'AB5515', 'SUMERGIBLE', 5, 'activo', '', 'ESTE ES EL MOTOR DEL POZO 1');

-- --------------------------------------------------------

--
-- Table structure for table `niveles`
--

CREATE TABLE `niveles` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `tipo_nivel` varchar(255) DEFAULT NULL,
  `abatimiento` varchar(255) DEFAULT NULL,
  `fecha_medicion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pozos`
--

CREATE TABLE `pozos` (
  `id` int(11) NOT NULL,
  `nombre_pozo` varchar(100) NOT NULL,
  `comunidad` varchar(100) DEFAULT NULL,
  `fecha_perforacion` date DEFAULT NULL,
  `domicilio` varchar(200) DEFAULT NULL,
  `latitud` decimal(9,6) DEFAULT NULL,
  `longitud` decimal(9,6) DEFAULT NULL,
  `altitud` int(11) DEFAULT NULL,
  `profundidad` decimal(10,2) DEFAULT NULL,
  `gasto_actual_id` int(11) DEFAULT NULL,
  `diametro_ademe` float(10,4) DEFAULT NULL,
  `longitud_ademe_ciego` float(10,4) DEFAULT NULL,
  `longitud_ademe_ranurado` float(10,4) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `tren_descarga` varchar(255) DEFAULT NULL,
  `concesion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pozos`
--

INSERT INTO `pozos` (`id`, `nombre_pozo`, `comunidad`, `fecha_perforacion`, `domicilio`, `latitud`, `longitud`, `altitud`, `profundidad`, `gasto_actual_id`, `diametro_ademe`, `longitud_ademe_ciego`, `longitud_ademe_ranurado`, `created_at`, `updated_at`, `tren_descarga`, `concesion`) VALUES
(7, 'POZO PRUEBA', 'COMUNIDAD DE PRUEBA', '2025-06-29', 'DOMICILIO CONOCIDO', 26.906483, -105.731661, 1500, 200.00, 0, 20.0000, 50.0000, 50.0000, '2025-07-03 18:39:17', '2025-07-03 18:39:17', 'ES UN TREN DE DESCARGA DE ACERO DE 5 METROS 5 PULGADAS', 'MEX-CONAGUA-50');

-- --------------------------------------------------------

--
-- Table structure for table `recibos_luz`
--

CREATE TABLE `recibos_luz` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `bimestre` varchar(20) DEFAULT NULL,
  `consumo_kwh` float DEFAULT NULL CHECK (`consumo_kwh` >= 0),
  `costo_total` decimal(10,2) DEFAULT NULL CHECK (`costo_total` >= 0),
  `fecha_pago` date DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transformadores`
--

CREATE TABLE `transformadores` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `kva` decimal(11,2) DEFAULT NULL,
  `voltage_primario` decimal(11,2) DEFAULT NULL,
  `voltage_secundario` decimal(11,2) DEFAULT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `serie` varchar(50) DEFAULT NULL,
  `bomba` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `serie_bomba` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `unidades`
--

CREATE TABLE `unidades` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `abreviatura` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `unidades`
--

INSERT INTO `unidades` (`id`, `nombre`, `abreviatura`) VALUES
(1, 'METRO CUBICO', 'M3'),
(2, 'LITROS POR SEGUNDO', 'LPS');

-- --------------------------------------------------------

--
-- Table structure for table `unidades_medida`
--

CREATE TABLE `unidades_medida` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `abreviatura` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `unidades_medida`
--

INSERT INTO `unidades_medida` (`id`, `nombre`, `abreviatura`) VALUES
(1, 'METRO CUBICO', 'M3'),
(2, 'LITROS POR SEGUNDO', 'LPS');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `rol` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password_hash`, `rol`) VALUES
(1, 'admin', '$2b$12$e577gNDm5OnyftV6R4PlOu9DzukL8zw8VrW5dyxlwIiDOYJjZNcUK', 'administrador');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `almacenamiento`
--
ALTER TABLE `almacenamiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pozo_id` (`pozo_id`);

--
-- Indexes for table `archivos`
--
ALTER TABLE `archivos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `archivos_relaciones`
--
ALTER TABLE `archivos_relaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pozo_id` (`pozo_id`),
  ADD KEY `recibo_luz_id` (`recibo_luz_id`),
  ADD KEY `medicion_id` (`medicion_id`),
  ADD KEY `modificacion_reparacion_id` (`modificacion_reparacion_id`),
  ADD KEY `idx_archivo_id` (`archivo_id`);

--
-- Indexes for table `catalogo_mod_rep`
--
ALTER TABLE `catalogo_mod_rep`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mediciones`
--
ALTER TABLE `mediciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pozo_id` (`pozo_id`),
  ADD KEY `unidad_id` (`unidad_id`);

--
-- Indexes for table `modificaciones_reparaciones`
--
ALTER TABLE `modificaciones_reparaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pozo_id` (`pozo_id`),
  ADD KEY `fk_modificaciones_catalogo` (`tipo_modificacion`);

--
-- Indexes for table `motores`
--
ALTER TABLE `motores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_pozo_id` (`pozo_id`);

--
-- Indexes for table `niveles`
--
ALTER TABLE `niveles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pozo_id` (`pozo_id`);

--
-- Indexes for table `pozos`
--
ALTER TABLE `pozos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recibos_luz`
--
ALTER TABLE `recibos_luz`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_pozo_id_recibos` (`pozo_id`);

--
-- Indexes for table `transformadores`
--
ALTER TABLE `transformadores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pozo_id` (`pozo_id`);

--
-- Indexes for table `unidades`
--
ALTER TABLE `unidades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_unidades_id` (`id`);

--
-- Indexes for table `unidades_medida`
--
ALTER TABLE `unidades_medida`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_usuarios_username` (`username`),
  ADD KEY `ix_usuarios_id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `almacenamiento`
--
ALTER TABLE `almacenamiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `archivos`
--
ALTER TABLE `archivos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `archivos_relaciones`
--
ALTER TABLE `archivos_relaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `mediciones`
--
ALTER TABLE `mediciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `modificaciones_reparaciones`
--
ALTER TABLE `modificaciones_reparaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `motores`
--
ALTER TABLE `motores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `niveles`
--
ALTER TABLE `niveles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pozos`
--
ALTER TABLE `pozos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `recibos_luz`
--
ALTER TABLE `recibos_luz`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transformadores`
--
ALTER TABLE `transformadores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `unidades`
--
ALTER TABLE `unidades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `unidades_medida`
--
ALTER TABLE `unidades_medida`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `almacenamiento`
--
ALTER TABLE `almacenamiento`
  ADD CONSTRAINT `almacenamiento_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `archivos_relaciones`
--
ALTER TABLE `archivos_relaciones`
  ADD CONSTRAINT `archivos_relaciones_ibfk_1` FOREIGN KEY (`archivo_id`) REFERENCES `archivos` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `archivos_relaciones_ibfk_2` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `archivos_relaciones_ibfk_3` FOREIGN KEY (`recibo_luz_id`) REFERENCES `recibos_luz` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `archivos_relaciones_ibfk_5` FOREIGN KEY (`modificacion_reparacion_id`) REFERENCES `modificaciones_reparaciones` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `mediciones`
--
ALTER TABLE `mediciones`
  ADD CONSTRAINT `mediciones_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `mediciones_ibfk_2` FOREIGN KEY (`unidad_id`) REFERENCES `unidades_medida` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `modificaciones_reparaciones`
--
ALTER TABLE `modificaciones_reparaciones`
  ADD CONSTRAINT `fk_modificaciones_catalogo` FOREIGN KEY (`tipo_modificacion`) REFERENCES `catalogo_mod_rep` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `modificaciones_reparaciones_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `motores`
--
ALTER TABLE `motores`
  ADD CONSTRAINT `motores_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `niveles`
--
ALTER TABLE `niveles`
  ADD CONSTRAINT `niveles_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `recibos_luz`
--
ALTER TABLE `recibos_luz`
  ADD CONSTRAINT `recibos_luz_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `transformadores`
--
ALTER TABLE `transformadores`
  ADD CONSTRAINT `transformadores_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
