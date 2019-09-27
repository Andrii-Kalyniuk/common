CREATE TABLE Orders (
	OrderID SERIAL PRIMARY KEY,
	CustomerID INT,
	EmployeeID INT,
	OrderDate DATE,
	ShipperID INT
);
