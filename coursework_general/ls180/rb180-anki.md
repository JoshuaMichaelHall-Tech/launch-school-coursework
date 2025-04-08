## What is a relational database?
A relational database is a type of database that organizes data into relations (tables) based on the relational model of data. It uses relationships between tables to establish connections between the data.

## What is SQL?
SQL (Structured Query Language) is a standardized programming language specifically designed for managing and manipulating relational databases. It is used to create, retrieve, update, and delete data, as well as to define and modify the database structure.

## What is PostgreSQL?
PostgreSQL is an open-source, advanced object-relational database management system (RDBMS) that emphasizes extensibility and SQL compliance. It offers features like complex queries, foreign keys, triggers, updatable views, and transactional integrity.

## What is a table in a database?
A table is a collection of related data organized in rows and columns. It represents a set of entities of the same type. Each table has a defined structure that specifies the attributes (columns) that the entities have.

## What is a schema in a database?
A schema is a blueprint that defines the organization of data in a database. It includes tables, views, indexes, relationships, constraints, and other database objects. Schemas help organize database objects into logical groups and control permissions.

## What are the basic components of a table?
The basic components of a table include:
- Columns (fields): Define the data types and constraints
- Rows (records or tuples): Contain the actual data
- Primary key: Uniquely identifies each row
- Foreign keys: Create relationships with other tables
- Constraints: Rules enforced on data in the table

## What is a data type in SQL?
A data type defines the kind of data that can be stored in a column. Common SQL data types include:
- VARCHAR: Variable-length character strings
- INTEGER: Whole numbers
- DECIMAL/NUMERIC: Exact numeric values with fixed precision
- DATE/TIME/TIMESTAMP: Date and time values
- BOOLEAN: True/false values
- TEXT: Variable unlimited length strings

## What is a primary key?
A primary key is a column or set of columns that uniquely identifies each row in a table. It must contain unique values and cannot have NULL values. Primary keys are used to establish relationships between tables and ensure data integrity.

## What is a foreign key?
A foreign key is a column or set of columns in one table that references the primary key of another table. It creates a link between tables and enforces referential integrity, ensuring that values in the foreign key column match values in the referenced primary key.

## What are database constraints?
Constraints are rules enforced on data columns to maintain accuracy and reliability. Common constraints include:
- NOT NULL: Column cannot have NULL values
- UNIQUE: All values in the column must be different
- PRIMARY KEY: Uniquely identifies each row
- FOREIGN KEY: Links to a primary key in another table
- CHECK: Values must satisfy a specific condition
- DEFAULT: Provides a default value for a column

## What are the different types of JOINs in SQL?
SQL supports several types of joins:
- INNER JOIN: Returns rows when there is a match in both tables
- LEFT JOIN: Returns all rows from the left table and matched rows from the right table
- RIGHT JOIN: Returns all rows from the right table and matched rows from the left table
- FULL OUTER JOIN: Returns rows when there is a match in either table
- CROSS JOIN: Returns the Cartesian product of both tables

## What is normalization in database design?
Normalization is the process of organizing database tables to minimize redundancy and dependency. It involves dividing large tables into smaller ones and defining relationships between them. The goal is to reduce data duplication, prevent update anomalies, and improve database integrity.

## What are the first three normal forms (1NF, 2NF, 3NF)?
1. First Normal Form (1NF): Each table cell should contain a single value, and each record needs to be unique.
2. Second Normal Form (2NF): The table is in 1NF and all non-key attributes are fully functionally dependent on the primary key.
3. Third Normal Form (3NF): The table is in 2NF and all attributes are directly dependent on the primary key, not on other non-key attributes.

## What is an entity-relationship diagram (ERD)?
An Entity-Relationship Diagram (ERD) is a visual representation of a database's structure showing entities (tables), attributes (columns), and relationships between entities. ERDs help database designers plan the database schema and communicate its structure to stakeholders.

## What are database indexes?
Indexes are data structures that improve the speed of data retrieval operations on database tables. They act like the index in a book, allowing the database to find data without scanning the entire table. While indexes speed up read operations, they can slow down write operations.

## What is the difference between DDL, DML, DCL, and TCL in SQL?
- DDL (Data Definition Language): Commands that define database structure (CREATE, ALTER, DROP)
- DML (Data Manipulation Language): Commands that manipulate data (SELECT, INSERT, UPDATE, DELETE)
- DCL (Data Control Language): Commands that control access (GRANT, REVOKE)
- TCL (Transaction Control Language): Commands that manage transactions (COMMIT, ROLLBACK)

## What is a subquery in SQL?
A subquery (or nested query) is a query nested inside another query. Subqueries can be used in SELECT, INSERT, UPDATE, or DELETE statements, typically in WHERE clauses. They allow complex operations that would otherwise require multiple queries or temporary tables.

## What are aggregate functions in SQL?
Aggregate functions perform calculations on a set of values and return a single value. Common aggregate functions include:
- COUNT(): Counts the number of rows
- SUM(): Calculates the sum of values
- AVG(): Calculates the average of values
- MIN(): Finds the minimum value
- MAX(): Finds the maximum value

## What is a database transaction?
A transaction is a sequence of operations performed as a single logical unit of work. Transactions have ACID properties:
- Atomicity: All operations complete successfully or none do
- Consistency: The database remains in a consistent state
- Isolation: Transactions operate independently
- Durability: Once committed, changes are permanent

## How do you create a table in SQL?
```sql
CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  department VARCHAR(50),
  salary NUMERIC(10,2),
  hire_date DATE DEFAULT CURRENT_DATE
);
```

## How do you insert data into a table?
```sql
-- Insert a single row
INSERT INTO employees (name, email, department, salary)
VALUES ('John Doe', 'john@example.com', 'Marketing', 60000.00);

-- Insert multiple rows
INSERT INTO employees (name, email, department, salary)
VALUES 
  ('Jane Smith', 'jane@example.com', 'Engineering', 75000.00),
  ('Bob Johnson', 'bob@example.com', 'Finance', 65000.00);
```

## How do you update data in a table?
```sql
-- Update a single row
UPDATE employees
SET salary = 70000.00
WHERE id = 1;

-- Update multiple rows
UPDATE employees
SET department = 'Sales', salary = salary * 1.1
WHERE department = 'Marketing';
```

## How do you delete data from a table?
```sql
-- Delete a single row
DELETE FROM employees
WHERE id = 3;

-- Delete multiple rows
DELETE FROM employees
WHERE department = 'Finance';

-- Delete all rows
DELETE FROM employees;
```

## How do you perform a basic SELECT query?
```sql
-- Select all columns
SELECT * FROM employees;

-- Select specific columns
SELECT id, name, department FROM employees;

-- Select with WHERE clause
SELECT name, salary FROM employees
WHERE department = 'Engineering';

-- Order results
SELECT name, salary FROM employees
ORDER BY salary DESC;

-- Limit results
SELECT name, salary FROM employees
ORDER BY salary DESC
LIMIT 5;
```

## How do you perform a JOIN operation?
```sql
-- Inner join
SELECT employees.name, departments.name AS department_name
FROM employees
JOIN departments ON employees.department_id = departments.id;

-- Left join
SELECT employees.name, departments.name AS department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id;

-- Join with aliases
SELECT e.name, d.name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.id;
```

## How do you use GROUP BY and HAVING?
```sql
-- Group by department and count employees
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

-- Group by department and calculate average salary
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- Group by with HAVING (filter on aggregated data)
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

## How do you create and use a view?
```sql
-- Create a view
CREATE VIEW employee_summary AS
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- Use the view
SELECT * FROM employee_summary;

-- Drop the view
DROP VIEW employee_summary;
```
