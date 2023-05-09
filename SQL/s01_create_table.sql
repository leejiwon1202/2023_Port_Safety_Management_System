CREATE TABLE `prj_db`.`info_port2` (
  `id` MEDIUMINT(0) UNSIGNED NOT NULL AUTO_INCREMENT,
  `camera_no` TINYINT(0) UNSIGNED NOT NULL,
  `situation_type` TINYTEXT NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  `link_storage` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`)
);