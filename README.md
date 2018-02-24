# TargetProject
##Project Host URL ##
[Host](http://ec2-52-41-196-53.us-west-2.compute.amazonaws.com/target/products)

## API Documentation ##
[Documentation](https://documenter.getpostman.com/view/1637657/targetapi/RVg2B9EX)

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
      - GET  - http://127.0.0.1:5000/target/product/{id} - Gets the product name from an external API and combines it with the product information in local database and displays it.
      - PUT  - http://127.0.0.1:5000/target/product/{id} - Takes JSON request body similar to the GET response as input, and updates the product’s price in the data store
      - POST - http://127.0.0.1:5000/target/products - Create a product in the database
      - GET  - http://127.0.0.1:5000/target/products - Retrieves all the products in the database.