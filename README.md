# TargetProject
##Project Host URL ##
[Host](http://ec2-52-41-196-53.us-west-2.compute.amazonaws.com/orders)

## API Documentation ##
[Documentation](https://documenter.getpostman.com/view/1637657/collection/RVg2AogE)

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
      - GET  - http://localhost/products/<id> - Gets the product name from an external API and combines it with the product information in local database.
      - PUT  - http://127.0.0.1:5000/products/<id> - Takes JSON request body similar to the GET response as input, and updates the product’s price in the data store
      - POST - http://localhost/products - Create a product in the database
      - GET  - http://localhost/products - Retrieves all the products in the database.