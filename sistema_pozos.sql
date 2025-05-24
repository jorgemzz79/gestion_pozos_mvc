-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2025 at 10:19 PM
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

--
-- Dumping data for table `archivos`
--

INSERT INTO `archivos` (`id`, `nombre_archivo`, `tipo_archivo`, `ruta_archivo`, `categoria`, `descripcion`, `fecha_subida`) VALUES
(1, 'factura_enero.pdf', 'pdf', '/archivos/factura_enero.pdf', 'recibo_luz', 'Factura de luz de enero', '2025-03-06 18:28:47'),
(2, 'FOTO MOTOR', 'JPEG', '/RECURSOS/FOTOS/', 'FOTOS', 'ESTA ES LA FOTO DEL MOTOR INSTALADA EN EL POZO #1', '2025-05-20 23:18:18'),
(3, 'RECIBO DE LUZ ENERO-FEBRERO', 'JPEG', '/RECURSOS/FOTOS/', 'FOTOS', 'ESTA ES LA FOTO DEL RECIBO DE LUZ DEL POZO #1', '2025-05-20 23:18:18');

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

--
-- Dumping data for table `archivos_relaciones`
--

INSERT INTO `archivos_relaciones` (`id`, `archivo_id`, `pozo_id`, `recibo_luz_id`, `medicion_id`, `modificacion_reparacion_id`) VALUES
(5, 2, 3, NULL, NULL, NULL),
(6, 3, 3, 3, NULL, NULL);

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
  `gasto` float DEFAULT NULL,
  `acumulado` float DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mediciones`
--

INSERT INTO `mediciones` (`id`, `pozo_id`, `fecha`, `gasto`, `acumulado`, `created_at`) VALUES
(1, 3, '2025-05-20 17:40:33', 50, 5000, '2025-05-20 17:40:52');

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

--
-- Dumping data for table `modificaciones_reparaciones`
--

INSERT INTO `modificaciones_reparaciones` (`id`, `pozo_id`, `tipo_modificacion`, `descripcion_modificacion_reparacion`, `fecha`, `responsable`) VALUES
(3, 3, 1, 'SE METIERON 2 CABLES DE USO RUDO CON CALIBRE 16 PARA LOS SENSORES DE EL TREN DE DESCARGA', '2025-05-20 23:41:37', 'MECATRONICA');

-- --------------------------------------------------------

--
-- Table structure for table `motores`
--

CREATE TABLE `motores` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `motor` varchar(255) DEFAULT NULL,
  `velocidad` varchar(255) DEFAULT NULL,
  `voltaje` varchar(255) DEFAULT NULL,
  `corriente` varchar(255) DEFAULT NULL,
  `marca` varchar(255) DEFAULT NULL,
  `modelo` varchar(255) DEFAULT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  `diametro_descarga` varchar(255) DEFAULT NULL,
  `estado` enum('activo','inactivo','mantenimiento') NOT NULL DEFAULT 'activo',
  `fotos` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `motores`
--

INSERT INTO `motores` (`id`, `pozo_id`, `motor`, `velocidad`, `voltaje`, `corriente`, `marca`, `modelo`, `tipo`, `diametro_descarga`, `estado`, `fotos`, `descripcion`) VALUES
(1, 3, 'SIEMENS 50 HP', '3500 RPM', '440 V', '40 A', 'SIMENS', '3F ARM 286JM', 'TRIFASICO', '4 PULGADAS', 'activo', '5', 'MOTOR RECIENTEMENTE ADQUIRIDO E INSTALADO');

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
  `diametro_ademe` varchar(255) DEFAULT NULL,
  `longitud_ademe_ciego` varchar(255) DEFAULT NULL,
  `longitud_ademe_ranurado` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `tren_descarga` varchar(255) DEFAULT NULL,
  `concesion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pozos`
--

INSERT INTO `pozos` (`id`, `nombre_pozo`, `comunidad`, `fecha_perforacion`, `domicilio`, `latitud`, `longitud`, `altitud`, `profundidad`, `gasto_actual_id`, `diametro_ademe`, `longitud_ademe_ciego`, `longitud_ademe_ranurado`, `created_at`, `updated_at`, `tren_descarga`, `concesion`) VALUES
(1, 'POZO EL GUARDAGANADO', 'EL VERANO', '2025-03-05', 'valle del verano chihuahua, mexico', 560.256454, 86.324154, 950, 200.00, 150, '30', '200', '100', '2025-03-06 18:27:25', '0000-00-00 00:00:00', NULL, 'CONAGUA-151228-MX'),
(2, 'Pozo El Roble', 'La Estanzuela', '2020-05-10', 'Calle Ejido #123', 27.234567, -105.987654, 1245, 85.50, NULL, '10 pulgadas', '20 m', '65.5 m', '2025-05-06 16:34:55', '2025-05-06 16:34:55', 'Tramo PVC cédula 40', 'CONAGUA-POZ-CH-245'),
(3, 'Pozo #1', 'EL VERANO', '2020-08-15', 'Calle Ejido 45', 27.123456, -105.987654, 1250, 85.50, NULL, '12 pulgadas', '30 m', '55.5 m', '2025-05-20 16:51:50', '2025-05-20 16:51:50', 'Tubo de acero galvanizado', 'CONAGUA-CHH-90210');

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

--
-- Dumping data for table `recibos_luz`
--

INSERT INTO `recibos_luz` (`id`, `pozo_id`, `bimestre`, `consumo_kwh`, `costo_total`, `fecha_pago`, `created_at`) VALUES
(2, 1, 'Enero-Febrero', 1200.5, 3500.00, '2025-03-01', '2025-03-06 18:27:48'),
(3, 3, 'ENERO-FEBRERO', 2850, 25200.00, '2025-05-20', '2025-05-20 17:36:09');

-- --------------------------------------------------------

--
-- Table structure for table `transformadores`
--

CREATE TABLE `transformadores` (
  `id` int(11) NOT NULL,
  `pozo_id` int(11) NOT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `kva` int(11) DEFAULT NULL,
  `voltage_primario` decimal(10,2) DEFAULT NULL,
  `voltage_secundario` varchar(20) DEFAULT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `serie` varchar(50) DEFAULT NULL,
  `bomba` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `serie_bomba` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transformadores`
--

INSERT INTO `transformadores` (`id`, `pozo_id`, `ubicacion`, `kva`, `voltage_primario`, `voltage_secundario`, `marca`, `serie`, `bomba`, `modelo`, `serie_bomba`) VALUES
(1, 3, 'POZO 3', 70, 440.00, '220', 'SIMENS', '12121S2SD45F4FG', 'SIMENS 200 HP', 'SIMENS 5000', '33225544');

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
  ADD KEY `idx_pozo_id_mediciones` (`pozo_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `archivos_relaciones`
--
ALTER TABLE `archivos_relaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `mediciones`
--
ALTER TABLE `mediciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `modificaciones_reparaciones`
--
ALTER TABLE `modificaciones_reparaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `motores`
--
ALTER TABLE `motores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `niveles`
--
ALTER TABLE `niveles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pozos`
--
ALTER TABLE `pozos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `recibos_luz`
--
ALTER TABLE `recibos_luz`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transformadores`
--
ALTER TABLE `transformadores`
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
  ADD CONSTRAINT `archivos_relaciones_ibfk_4` FOREIGN KEY (`medicion_id`) REFERENCES `mediciones` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `archivos_relaciones_ibfk_5` FOREIGN KEY (`modificacion_reparacion_id`) REFERENCES `modificaciones_reparaciones` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `mediciones`
--
ALTER TABLE `mediciones`
  ADD CONSTRAINT `mediciones_ibfk_1` FOREIGN KEY (`pozo_id`) REFERENCES `pozos` (`id`) ON DELETE CASCADE;

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
