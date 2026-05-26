-- Migracion: empleados y responsable_id para modificaciones/reparaciones
-- Objetivo:
-- 1. Crear catalogo de empleados.
-- 2. Agregar responsable_id sin eliminar el campo legacy responsable.
-- 3. Agregar baja logica a catalogo_mod_rep.
--
-- Esta migracion usa information_schema para evitar errores si se ejecuta mas de una vez.

CREATE TABLE IF NOT EXISTS empleados (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  puesto VARCHAR(100) DEFAULT NULL,
  departamento VARCHAR(100) DEFAULT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_empleados_nombre (nombre),
  KEY idx_empleados_activo (activo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DELIMITER //

DROP PROCEDURE IF EXISTS add_responsable_id_if_missing//
DROP PROCEDURE IF EXISTS add_idx_mod_rep_responsable_id_if_missing//
DROP PROCEDURE IF EXISTS add_fk_mod_rep_responsable_if_missing//
DROP PROCEDURE IF EXISTS add_catalogo_mod_rep_activo_if_missing//
DROP PROCEDURE IF EXISTS add_idx_catalogo_mod_rep_activo_if_missing//

CREATE PROCEDURE add_responsable_id_if_missing()
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM information_schema.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME = 'modificaciones_reparaciones'
      AND COLUMN_NAME = 'responsable_id'
  ) THEN
    ALTER TABLE modificaciones_reparaciones
      ADD COLUMN responsable_id INT NULL AFTER responsable;
  END IF;
END//

CREATE PROCEDURE add_idx_mod_rep_responsable_id_if_missing()
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM information_schema.STATISTICS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME = 'modificaciones_reparaciones'
      AND INDEX_NAME = 'idx_mod_rep_responsable_id'
  ) THEN
    ALTER TABLE modificaciones_reparaciones
      ADD INDEX idx_mod_rep_responsable_id (responsable_id);
  END IF;
END//

CREATE PROCEDURE add_fk_mod_rep_responsable_if_missing()
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM information_schema.TABLE_CONSTRAINTS
    WHERE CONSTRAINT_SCHEMA = DATABASE()
      AND TABLE_NAME = 'modificaciones_reparaciones'
      AND CONSTRAINT_NAME = 'fk_mod_rep_responsable'
      AND CONSTRAINT_TYPE = 'FOREIGN KEY'
  ) THEN
    ALTER TABLE modificaciones_reparaciones
      ADD CONSTRAINT fk_mod_rep_responsable
      FOREIGN KEY (responsable_id)
      REFERENCES empleados(id)
      ON DELETE SET NULL;
  END IF;
END//

CREATE PROCEDURE add_catalogo_mod_rep_activo_if_missing()
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM information_schema.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME = 'catalogo_mod_rep'
      AND COLUMN_NAME = 'activo'
  ) THEN
    ALTER TABLE catalogo_mod_rep
      ADD COLUMN activo TINYINT(1) NOT NULL DEFAULT 1 AFTER descripcion;
  END IF;
END//

CREATE PROCEDURE add_idx_catalogo_mod_rep_activo_if_missing()
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM information_schema.STATISTICS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME = 'catalogo_mod_rep'
      AND INDEX_NAME = 'idx_catalogo_mod_rep_activo'
  ) THEN
    ALTER TABLE catalogo_mod_rep
      ADD INDEX idx_catalogo_mod_rep_activo (activo);
  END IF;
END//

DELIMITER ;

CALL add_responsable_id_if_missing();
CALL add_idx_mod_rep_responsable_id_if_missing();
CALL add_fk_mod_rep_responsable_if_missing();
CALL add_catalogo_mod_rep_activo_if_missing();
CALL add_idx_catalogo_mod_rep_activo_if_missing();

DROP PROCEDURE add_responsable_id_if_missing;
DROP PROCEDURE add_idx_mod_rep_responsable_id_if_missing;
DROP PROCEDURE add_fk_mod_rep_responsable_if_missing;
DROP PROCEDURE add_catalogo_mod_rep_activo_if_missing;
DROP PROCEDURE add_idx_catalogo_mod_rep_activo_if_missing;
