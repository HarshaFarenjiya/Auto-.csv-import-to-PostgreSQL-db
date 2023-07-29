![importpostgres](https://github.com/HarshaFarenjiya/Auto-.csv-import-to-PostgreSQL-db/assets/117337376/8fd28807-d9fb-4308-9413-bbe1a7661065)

# Auto-.csv-import-to-PostgreSQL-db

<div align="justify">
  
## Introduction

File import is an essential aspect in the field of data as it enables professionals to efficiently load and analyze large datasets stored in external files. This process is particularly important when dealing with real-world datasets that can be vast and complex.

While file import is essential in PostgreSQL, it can be considered more difficult as compared to other server platforms for a few reasons:

* <b> Data Types and Formatting </b>: PostgreSQL is stricter in terms of data types and formatting. If the file's data type and format do not align with the target table's schema, it may lead to errors during the import process.
  
  In PostgreSQL, it is necessary to specify the data types of columns before importing data. This can be more cumbersome, especially when dealing with tables with a large number of columns. The requirement to define the data types in advance can make the import process more time-consuming and error-prone, as it involves accurately specifying the data types for each column.

* <b> Transactions and Rollback </b>: PostgreSQL is transactional, meaning that each data import is treated as a transaction. In case of errors or issues during import, the whole transaction may be rolled back. Handling transaction management properly can be tricky, especially when dealing with large datasets.


## Objective

PostgreSQL's approach of explicitly defining data types offers the advantage of data integrity enforcement and stricter control over the data being imported. It ensures that the imported data aligns with the defined table schema, reducing the risk of data inconsistencies or integrity violations.

Hence, The goal of this project is to automate the process of importing .csv files into PostgreSQL.


## Prerequisites

* Install PostgreSQL and pgAdmin (Note: While setting up the both applications, set password = '1111')
* Check whether the .csv file is encoded in UTF-8 format or not using Notepad++. If your file is not in csv format convert it using Notepad++        
* Make sure your .csv file has not any columns without header or with header ontaining special characters, such as colons (":"). Column names must start with a letter or an underscore ( _ ).


## How to use?

1. Download and install PostgreSQL and pgAdmin as instructed above.
2. Download .exe file and place it in a new folder.
3. Place any .csv file in that new folder also.
4. Execute the .exe file and get your desired data in PostgreSQL database.

</div>
