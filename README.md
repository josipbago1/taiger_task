# taiger_task

The whole project is divided into 3 layers, controller, service and data access. For the database I pickled the dictionary where keys indicate different tables and each table is a list of objects. Article is represented by the class Article in the models module. Starting point of the program is main.py where by running there is a simulation of populating the data and fetching the data used by two methods. I didn't use any dependencies so controllers are only the methods. DataAccess class simulates ORM and database with some functionality and is used by repository.
