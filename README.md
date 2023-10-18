# Incident-Management-Dashboard

## Introduction
This a sample Incident Mangagement Dashboard that provides information on randomly generated service tickets. A Python script was used to generate the service tickets randomly, which was stored in a MySQL database and then connected to Power BI for visualization purposes.

## How to set up
1. In your own MySQL database on your machine, run the script named 'create_tables.sql' to generate the necessary tables.
2. Set up a user with DBManager Priviliges (CREATE, INSERT, UPDATE, DELETE, GRANT OPTION, etc.). Remember to note down the username and password you have set.
   - If you want to avoid making any adjustments to the Python code in Step 3, use username=demoaccount and password=ensf607PA$$ when setting up the account on your database.
3. Open the Python code named random_ticket_generator.py and input your username into the 'user' field and password into the 'password' field in the variable 'db_config'.
4. Run the Python program to generate random service tickets.
5. You can then use Power BI to connect and generate dashboards and business insights.
