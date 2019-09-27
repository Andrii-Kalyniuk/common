CREATE TABLE Products (
	ProductID SERIAL PRIMARY KEY,
	ProductName VARCHAR(255),
	SupplierID INT,
	CategoryID INT,
	Unit VARCHAR(255),
	Price MONEY
);