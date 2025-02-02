import json # importing the Java Script Object Notation
import Pandas as pd # importing the pandas librraries
import boto3 # Boto3 is the AWS SDK (Software Development Kit) for Python, which allows you to interact with Amazon Web Services (AWS) such as S3, EC2, Lambda, DynamoDB, and many others.
import os # Get the current working directory (The os module allows you to interact with environment variables, such as retrieving or modifying the system's environment variables.)
import Numpy as np # numpy module is a powerful library in Python used for numerical computations, especially when dealing with arrays, matrices, and large datasets. It provides a high-performance multidimensional array object
import sys as sys # importing the sys module and import the library
import sqlachemy # import SQLAlchemy, which is a popular SQL toolkit and Object-Relational Mapping (ORM) library for Python.
import pyodbc #  Python library used to connect to databases via ODBC (Open Database Connectivity). It allows you to connect to a wide variety of database management systems (DBMS) such as Microsoft SQL Server, MySQL, PostgreSQL, SQLite, and many others, provided you have the appropriate ODBC driver installed.

 # NOW WE WANT TO START THE CONNECTION OF THE CLOUD DATABASE, WE SHALL BE CONNECTING AWS CLOUD DATABASE S3
 
 # creatint the low level functional client
 client = boto3.client('s3',
          aws_access_key_id = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          aws_secret_access_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          region_name = 'ap-south-1'
          )
 # creating the high level functional oriented interface
 resource = boto3.resource('s3',
            aws_access_key_id = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            aws_secret_access_key ='ABCDIFGHIJKLMNPOQRSTUVWXYZ'
            region_name = 'ap-south-1'
            )
 # Fetch the list of existing buckets for confirmation if correctly coded
 
 clientResponse = client.list_buckets()
 
 # Now print the buckets name one by one
 print('printing bucket names...')
 for bucket in clientResponse['Buckets']:
     print(f'Bucket Name: {bucket["Name"]}')
     
# debugging variable statement.
number = 100
print(f'Number is {number}')

number = 500
print(f'number is {number}')


# debugging for loop
userList = ['Bob', 'Dave', 'Tom', 'Paul']
for user in userList:
    print(user)
    
# NOW LET EXPLORE THE CLOUD BASE
# creating a new database in the online database (a new bucket in the AWS s3) by locating LOCATION = {'LocationConstraint': 'ap-south-1'}
#client.create_bucket ( Bucket = 'THE NEW NAME YOU WANT IN THE DATABASE', CreateBucketConstraint=location )

# create the s3 object
obj = client.get_object(
Bucket = 'THE NEW NAME YOU WANT IN THE DATABASE',
KEY = 'ABCD_EFGHIJKL_CSV'
)

# let check what we have added
# Read data from the s3 object
data = pd.head_csv(obj['Body'])
print(data.head())

# print the data frame
print('printing the data frame...')
print(data)
data

# review some interesting columns you will like to see

columns_to_be_selected = ["CustomerID", "TransactionTime", "CustLocation", "CustGender", "CustomerDOB", "CustAccountBalance"]
df[columns_to_be_selected]




