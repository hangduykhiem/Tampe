# Tempo

Tempo is a project to connect the NodeMCU module to a Python Flask backend, primarily to read and store room temperature and humidity.

### How it will work

The project is divided to 3 parts: 

1. Python Flask project to provide a RESTful interface to perform CRUD operations on a SQLite database.
2. NodeMCU with DHT11 temperature and humidity sensors. This will send data periodically to the Flask backend to store in the database.
3. A client of some sort, to display the data. This is to be decided.

Each of the components' source code is stored in their own individual folder. There is also documentation specific to each component in the respective folder.

### License

The project is MIT licensed. Check out the license [here](https://github.com/hangduykhiem/Tampe/blob/master/LICENSE).
