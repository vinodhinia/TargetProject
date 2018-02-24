# TargetProject
##Project Host URL ##
[Host](http://ec2-52-41-196-53.us-west-2.compute.amazonaws.com/orders)

## API Documentation ##
[Documentation](https://documenter.getpostman.com/view/1637657/shipttakehomeproject/7LkgPTD)

#### Folders ####
- seed
- src
  - models
  - app.py
- tests

**seed**
- Contains the sample data to populate the database

**src**
- src contains the actual logic for the project

**app.py**
- Contains the methods to handle the GET, POST, PUT requests.

  - Products
      - GET - http://localhost/ - Retrieves all the products in the database
      - GET - http://localhost/products/<id> - Retrieves the product by id.
      - GET - http://localhost/extproduct/<id> - Gets the product name from an external API and combines it with the product information in local database.

