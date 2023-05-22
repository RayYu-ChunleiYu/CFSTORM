# CFSTORM
Python ORM database scripts that record experiments and simulation data for concrete filled steel tube.
A database class is developed to connect postgre database and add/delete record in it. 

## Environment 
Environment to used those stripts is records in pyproject.toml
Poetry package can be used to create virtual environment 

## Models design 
Detail can be seen in Models.py 

## Database class 
A Database that implement 
- Database connection 
- table create 
- record add (Duplication check)
- record remove 
