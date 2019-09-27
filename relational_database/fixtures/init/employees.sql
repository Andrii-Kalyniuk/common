CREATE TABLE Employees (
	EmployeeID SERIAL PRIMARY KEY,
	LastName VARCHAR(255),
	FirstName VARCHAR(255),
	BirthDate DATE,
	Photo VARCHAR(255),
	Notes TEXT
	);