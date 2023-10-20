import random
import mysql.connector
from datetime import datetime, timedelta

#database configuration, used to sign into the MySQL server
db_config = {
    'host': 'localhost', 
    'user': 'demoaccount',     # Edit this to your own account
    'password': 'ensf607PA$$', # Edit this to your own account password
    'database': 'service_tickets'
}

#dictionary used to calculate priority. 
#provides a numeric reference for urgency and impact values

priority_dic = {
    'H': 1, #high priority
    'M': 2, #medium 
    'L': 3, #low priotity
}

#Accepts user inputs for number of tickets
while (True):
    try: #user must enter an integer
        num_tickets = int(input("Please enter the number of tickets to generate: "))
        break
    except ValueError: #throw exception if invalid input is entered
        print("Invalid input. Please enter an integer.")

#Accepts user inputs for start date of the ticket
while(True):
    try: #user must enter a vlid date in the correct format
        start_date = input("please enter the time window start date (YYYY-MM-DD): ")
        # Attempt to parse the input string into a datetime object
        start_date = datetime.strptime(start_date, "%Y-%m-%d") #strip the input into a valid format
        break
    except ValueError: #throw exception if invalid format was entered, or invalid date
        print("Invalid input. Please enter a date in the format YYYY-MM-DD.")

#Accepts user inputs for end date of the ticket
while(True):
    try:#user must enter a valid date in the correct format
        end_date = input("please enter the time window end date (YYYY-MM-DD): ")
        # Attempt to parse the input string into a datetime object
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        break  # Exit the loop if the input is a valid date
    except ValueError:
        print("Invalid input. Please enter a date in the format YYYY-MM-DD.")

#establishes a connection with the SQL server
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

#creates a range of possible id numbers, to be randomly selected from.
id_range = list(range(1, num_tickets + 1))

#loop through all tickets
for _ in range(num_tickets):

    case_id = f'CS_{id_range.pop(0)}'
    #randomly selects category of ticket
    activity = random.choice(['Design', 'Construction', 'Test', 'Password Reset'])

    #creates lists of possible urgency and impact markers.
    urgency = random.choice(['H', 'M', 'L'])
    impact = random.choice(['H', 'M', 'L'])

    #calculates the priority by using the urgency and impact
    priority = priority_dic.get(urgency) + priority_dic.get(impact) - 1

    #randomly generates the start and end dates, but applies a condition that they can only be 14 days apart maximally
    generated_start_date = start_date + timedelta(days=random.randint(0, (end_date - timedelta(days=14) - start_date).days))                         
    generated_end_date = generated_start_date + timedelta(days=random.randint(1,14))   

    # randomly pick between acceptable ticket statue codes
    ticket_status = random.choice(['Open', 'On Hold', 'In Process', 'Deployed', 'Deployed Failed'])   

    #randomly select a time that the ticket was updated in between the start and end date                                                                                                                                             
    update_datetime = generated_start_date + timedelta(days=random.randint(0, (generated_end_date - generated_start_date).days))                                            
    
    #calculate duration of days the ticket was open for
    duration = (generated_end_date - generated_start_date).days

    #randomly assign the ticket to one employee
    origin = random.choice(['Joe S.', 'Bill B.', 'George E.', 'Achmed M.', 'Rona E.'])

    #randomly assign the ticket class
    ticket_class = random.choice(['Change', 'Incident', 'Problem', 'SR'])

    # Insert the generated ticket into the database SQL Query
    insert_query = """
    INSERT INTO EventLog (Caseid, Activity, Urgency, Impact, Priority, StartDate, EndDate, TicketStatus, UpdateDateTime, Duration, Origin, Class)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (case_id, activity, urgency, impact, priority, generated_start_date, generated_end_date, ticket_status, update_datetime, duration, origin, ticket_class)

    cursor.execute(insert_query, values)
    conn.commit()

#close connections
cursor.close()
conn.close()