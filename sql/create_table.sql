create table amazon_data(
	Index int primary key,
	OrderID varchar(50),
	Date date,
	Status varchar(50),
	Sales_channel varchar(50),
	Amount float
);

select * from amazon_data;

copy amazon_data
from '/Users/aady/Desktop/Ayush Vats/ETL Pipeline Project/data/cleaned/amazon_main.csv'
delimiter ','
csv header;