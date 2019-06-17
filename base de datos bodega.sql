-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `Rut` VARCHAR(13) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Rut`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Bodega`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Bodega` (
  `idBodega` VARCHAR(5) NOT NULL,
  `Usuario_Rut` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idBodega`, `Usuario_Rut`),
  INDEX `fk_Bodega_Usuario_idx` (`Usuario_Rut` ASC),
  CONSTRAINT `fk_Bodega_Usuario`
    FOREIGN KEY (`Usuario_Rut`)
    REFERENCES `mydb`.`Usuario` (`Rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Despunte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Despunte` (
  `idDespunte` VARCHAR(5) NOT NULL,
  `Largo` VARCHAR(45) NULL,
  `Ancho` VARCHAR(45) NULL,
  `Espesor` VARCHAR(45) NULL,
  `Tipo` VARCHAR(45) NULL,
  `Cantidad` VARCHAR(45) NULL,
  `Bodega_idBodega` VARCHAR(5) NOT NULL,
  `Bodega_Usuario_Rut` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idDespunte`, `Bodega_idBodega`, `Bodega_Usuario_Rut`),
  INDEX `fk_Despunte_Bodega1_idx` (`Bodega_idBodega` ASC, `Bodega_Usuario_Rut` ASC),
  CONSTRAINT `fk_Despunte_Bodega1`
    FOREIGN KEY (`Bodega_idBodega` , `Bodega_Usuario_Rut`)
    REFERENCES `mydb`.`Bodega` (`idBodega` , `Usuario_Rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Herramientas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Herramientas` (
  `idHerramientas` INT NOT NULL,
  `Cantidad` VARCHAR(45) NULL,
  `Nombre` VARCHAR(45) NULL,
  `Bodega_idBodega` VARCHAR(5) NOT NULL,
  `Bodega_Usuario_Rut` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idHerramientas`, `Bodega_idBodega`, `Bodega_Usuario_Rut`),
  INDEX `fk_Herramientas_Bodega1_idx` (`Bodega_idBodega` ASC, `Bodega_Usuario_Rut` ASC),
  CONSTRAINT `fk_Herramientas_Bodega1`
    FOREIGN KEY (`Bodega_idBodega` , `Bodega_Usuario_Rut`)
    REFERENCES `mydb`.`Bodega` (`idBodega` , `Usuario_Rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Material` (
  `idMaterial` VARCHAR(5) NOT NULL,
  `Largo` VARCHAR(45) NULL,
  `Ancho` VARCHAR(45) NULL,
  `Espesor` VARCHAR(45) NULL,
  `Tipo` VARCHAR(45) NULL,
  `Cantidad` VARCHAR(45) NULL,
  `Bodega_idBodega` VARCHAR(5) NOT NULL,
  `Bodega_Usuario_Rut` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idMaterial`, `Bodega_idBodega`, `Bodega_Usuario_Rut`),
  INDEX `fk_Material_Bodega1_idx` (`Bodega_idBodega` ASC, `Bodega_Usuario_Rut` ASC),
  CONSTRAINT `fk_Material_Bodega1`
    FOREIGN KEY (`Bodega_idBodega` , `Bodega_Usuario_Rut`)
    REFERENCES `mydb`.`Bodega` (`idBodega` , `Usuario_Rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`EPP`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`EPP` (
  `idEPP` VARCHAR(5) NOT NULL,
  `Antiparras` VARCHAR(45) NULL,
  `Guantes` VARCHAR(45) NULL,
  `Botas de seguridad` VARCHAR(45) NULL,
  `Tapones para oido` VARCHAR(45) NULL,
  `Casco` VARCHAR(45) NULL,
  `Bodega_idBodega` VARCHAR(5) NOT NULL,
  `Bodega_Usuario_Rut` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idEPP`, `Bodega_idBodega`, `Bodega_Usuario_Rut`),
  INDEX `fk_EPP_Bodega1_idx` (`Bodega_idBodega` ASC, `Bodega_Usuario_Rut` ASC),
  CONSTRAINT `fk_EPP_Bodega1`
    FOREIGN KEY (`Bodega_idBodega` , `Bodega_Usuario_Rut`)
    REFERENCES `mydb`.`Bodega` (`idBodega` , `Usuario_Rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
