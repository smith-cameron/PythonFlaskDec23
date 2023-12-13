SELECT * FROM users;

SELECT * FROM users ORDER BY id DESC LIMIT 1;

SELECT * FROM users WHERE id = 7 ;
SELECT * FROM users WHERE id < 7 ;
SELECT * FROM users WHERE id > 1 AND id <= 6;
SELECT * FROM users WHERE id = 7 OR id = 4;
SELECT first_name, last_name FROM users;
SELECT first_name, last_name FROM users where id = 4;

INSERT INTO users(first_name, last_name,email,password,age) 
VALUES 
("Timmy", "Jimmy-Jam", "tjj@email.com", 1234567890, 35),
("Billy", "BoB", "bb@email.com", 1234567890, 35),
("Jimmy", "Timmy-Jam", "tjj@email.com", 1234567890, 35),
("Timmy", "Jimmy-Jam", "tjj@email.com", 1234567890, 35);

UPDATE users SET 
-- first_name = "Cameron",
-- last_name = "Smith",
email = "cs@email.com" WHERE id = 3;

DELETE FROM users WHERE id = 2;

INSERT INTO users(first_name, last_name,email,password,age) 
VALUES 
("Mr", "Ed", "ed@email.com", 1234567890, 35);

SELECT * FROM flaskdec23.cars;

INSERT INTO cars (make, model, year, color, creator_id) VALUES ("Mitsubishi", "Endeavor", 2014, "red", 1),
("Ford", "Mustang", 2001, "yellow", 6),("Mitsubishi", "Mirage", 2006, "blue", 7), ("Mitsubishi", "Endeavor", 2014, "blue", 7);

SELECT * FROM cars
JOIN users ON cars.creator_id = users.id;

SELECT * FROM cars
LEFT JOIN users ON cars.creator_id = users.id;

SELECT * FROM cars
JOIN users ON cars.creator_id = users.id
WHERE users.id = 7;
