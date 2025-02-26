-- -----------------------------------------------------
-- Table `osmotrDB`.`Driver`
-- -----------------------------------------------------
CREATE TABLE drivers (
driver_id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(256) NOT NULL, -- электронная почта
first_name VARCHAR(256) NOT NULL, -- имя
last_name VARCHAR(256) NOT NULL, -- фамилия
phone_number VARCHAR(20), -- номер телефона
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (driver_id)
);
-- -----------------------------------------------------
-- Table `osmotrDB`.`doctor`
-- -----------------------------------------------------
CREATE TABLE doctors (
doctor_id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(256) NOT NULL, -- электронная почта
first_name VARCHAR(256) NOT NULL, -- имя
last_name VARCHAR(256) NOT NULL, -- фамилия
phone_number VARCHAR(20), -- номер телефона
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (doctor_id)
);
-- -----------------------------------------------------
-- Table `smartphoneShopDb`.`examination`
-- -----------------------------------------------------
CREATE TABLE examinations(
examination_id INT NOT NULL AUTO_INCREMENT,
driver_id INT, -- id покупателя
doctor_id INT,
status TINYINT UNSIGNED NOT NULL, -- статус заказа
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (examination_id),
CONSTRAINT fk_Driver_Examination FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
CONSTRAINT fk_Doctor_Examination FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);