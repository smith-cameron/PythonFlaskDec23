
--< https://www.sql-practice.com/
--< [Queries - Slideshow](https://docs.google.com/presentation/d/1STD18JBWbJ4Uf4sKs29n3LDYNiOqqdj81YsHd6_bBJc/edit#slide=id.g181e2dc7e50_0_21)

--? Most Queries (all basic) follow a specific structure with similarities
--? What ACTION
--? What TABLE
--? What COLUMNS
--? What VALUES
--? Where CONDITION

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

-- single line comments
/* multi line
comments */

-- CONDITIONALS
SELECT * FROM users WHERE id = 5;
/* OR */
SELECT * FROM users WHERE id = 1 OR 4;
/* RANGE */
SELECT * FROM users WHERE id > 5;
SELECT * FROM users WHERE id > 5 AND id <= 10;
/* FIELD VALUE */
SELECT * FROM users WHERE email = %(email)s;
/* VARIABE DATA */
/*Note: Percentage signs (%) in the query represent zero or more characters.*/
SELECT * FROM users WHERE first_name LIKE "%e";
SELECT * FROM users WHERE first_name LIKE "C%";
SELECT * FROM users WHERE first_name NOT LIKE "K%";
SELECT * FROM users WHERE last_name LIKE '%Mc%';
-- SORTING
SELECT * FROM users ORDER BY first_name;
SELECT * FROM users ORDER BY <column/fieldName > DESC;
SELECT * FROM users ORDER BY <column/fieldName > ASC;
/* SORTED CONDITION */
SELECT * FROM users WHERE id > 5 AND id <= 10 ORDER BY first_name ASC;
-- LIMIT & OFFSET
/* get the first 3 users */
SELECT * FROM users LIMIT 3;
/* get user records 3-7 */
SELECT * FROM users LIMIT 3 OFFSET 4;
/* Same as above */
SELECT * FROM users LIMIT 2,3;

-- JOINS
-- The JOIN operation (or INNER JOIN), is meant to pull rows that have a match in both tables. 
-- __SELECT 1:1 JOIN__
SELECT * FROM users JOIN addresses ON users.id = addresses.user_id;

-- __SELECT JOIN 1:M__
SELECT * from posts JOIN users on posts.user_id = users.id;

-- Returns only posts with a users association
-- Use with WHERE for specific users comments

SELECT * from posts JOIN users on posts.user_id = users.id WHERE posts.user_id = 4;

-- _Table aliases with 1:M
-- WHY?
-- - field specificity
-- - Easier to read queries as they get longer
-- - No need for AS (though recommended for tables with similar columns)

SELECT p.*, u.first_name, u.last_name from posts p JOIN users u on p.user_id = u.id WHERE u.id = 12

-- _Left Join
/* The LEFT JOIN, on the other hand, is meant to pull all rows from the left table, and only matching rows from the right table.
null values will be returned for empty columns in right hand table*/
-- __SELECT LEFT JOIN 1:M__
-- Returns ALL users with null if there is no associated post

SELECT * FROM users LEFT JOIN posts ON posts.user_id = users.id;

SELECT * FROM users JOIN posts ON posts.user_id = users.id;

-- _ SELECT M:N  
-- - Returns all posts a user has liked with their info
-- - This will be useful for display and conditional rendering

SELECT * from liked_posts f JOIN posts p ON f.post_id = p.id JOIN users u ON f.user_id = u.id  WHERE u.id = 12;

-- - Same as above with new column names

SELECT f.*, u.first_name AS firstName, u.last_name AS lastName from liked_posts f JOIN posts p ON f.post_id = p.id JOIN users u ON f.user_id = u.id  WHERE u.id = 12;

-- - All the posts data and their likers data

SELECT * from liked_posts f JOIN posts p ON f.post_id = p.id JOIN users u ON f.user_id = u.id Order BY p.id;

SELECT * from posts p JOIN liked_posts f ON f.post_id = p.id;

--  VS. 

SELECT * from posts p LEFT JOIN liked_posts f ON f.post_id = p.id;

-- _Functions

--< https://www.w3schools.com/mysql/mysql_ref_functions.asp 
-- Functions can be applied to the SELECTed columns
-- When calling a function on a column, make sure that column is the appropriate Data Type for that function.

-- | Function Type | Data Type |
-- | ------------ | ---------- |
-- | Text  | VARCHAR, TEXT, CHAR etc. |
-- | Numeric  | INT, BIGINT, FLOAT etc. |
-- | Date and Time | DATETIME |

SELECT FUNCTION (column) FROM table_name

SELECT COUNT(*) FROM admissions;

SELECT CONCAT(p.first_name," ", p.last_name) 
FROM patients p;

SELECT COUNT(*) FROM patients 
WHERE patients.birth_date LIKE "2010%"

SELECT
    SUM(gender = 'M') AS total_male_patients,
    SUM(gender = 'F') AS total_female_patients
FROM patients;

SELECT city, COUNT(*) AS total_patients
FROM patients
GROUP BY city
ORDER BY total_patients DESC, city ASC;

SELECT CONCAT(p.first_name, ' ', p.last_name) 
AS patient_name, a.diagnosis,
CONCAT(d.first_name, ' ', d.last_name) 
AS doctor_name
FROM admissions a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.attending_doctor_id = d.doctor_id;