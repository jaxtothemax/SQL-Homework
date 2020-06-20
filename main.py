from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

# Print the number of albums in the table
db.pretty_print("SELECT AlbumId FROM Album WHERE AlbumId=(SELECT max(AlbumId) FROM Album)")

# Print all the artist names in the table
db.pretty_print("SELECT Name FROM Artist")

# Print all the invoices where BillingCountry is Germany
db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")

# Print how many customers are from France
db.pretty_print("SELECT COUNT(Country) FROM Customer WHERE Country = 'France'")

