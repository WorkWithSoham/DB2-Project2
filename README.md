# MONGO DB

-----------------------------------------------------
### Version
Python ~ 3.8

-----------------------------------------------------
### Execution

1. To create mongo db and collections execute following command

    
    python3 scripts/mongo_db_creation.py mongodb://localhost:5000


    python3 scripts/mongo_db_creation.py {localhost url}


2. To retrieve data from mongo db schema execute following query. Query result will be stored in output files directory.


    python3 ./scripts/get_db_data.py mongodb://localhost:5000

    python3 ./scripts/get_db_data.py {localhost url}

3. If url is not provided then the code will use cloud mongo db server for schema.

-----------------------------------------------------------
