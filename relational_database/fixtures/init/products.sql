SET lc_monetary to "en_US.utf8";
CREATE TABLE Products (
	ProductID SERIAL PRIMARY KEY,
	ProductName VARCHAR(255),
	SupplierID INT,
	CategoryID INT,
	Unit VARCHAR(255),
	Price MONEY
);