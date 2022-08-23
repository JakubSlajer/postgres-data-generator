# Python-Data-Generator
### Prerequisites:

- Python version from 3.6 to 3,9
- PostgreSQL version from 7.4 to 13
- Python IDE (Visual Studio Code, PyCharm)
- Instaled Python modules

### Installation:

<div style="padding-left:20px;">
At first, if you don't have python installed on your device, it's the rigth time to do so. You should also have PIP installed with the python installation.
<p></p>
After the python installation, install python modules by typing these pip commands into your command line.
<p></p>

```pip install psycopg2```

```pip install term_color```

```pip install fruit_stand```

```pip install psycopg2```


If you're using VSCode, restart your IDE after the installation. You sould be able to import those modules into your scripts with no errors. 
</div>

### PostgreSQL database schema:
<div style="padding-left:20px;">

See [schema.drawio](src/schema.drawio) entity relationship diagram. 

You will need to install Draw.[]()io Integration extension plugin into your VS Code 

or Diagrams[]().net Integration plugin, if you're working in PyCharm.


Create the database by running schema.psql in PgAdmin query editor

Pass your postgres login credentials as arguments in the [connectors/my_connector.py](connectors/my_connector.py)
</div>

### Running:
<div style="padding-left:20px;">
Run each script in your terminal

You can test your connection by running connection_test.py
</div>

### Goals:

- Generate 10 app users with random data
- Generate fruit products
- Generate 100 orders
- Generate 1000 order lines
