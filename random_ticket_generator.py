import random
import mysql.connector
from datetime import datetime, timedelta

db_config = {
    'host': 'localhost',
    'user': 'demoaccount',
    'password': 'ensf607PA$$',
    'database': 'service_tickets'
}

priority_dic = {
    'H': 1, 
    'M': 2, 
    'L': 3,
}



#User inputs for number of tickets, and time window
while (True):
    try:
        num_tickets = int(input("Please enter the number of tickets to generate: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while(True):
    try:
        start_date = input("please enter the time window start date (YYYY-MM-DD): ")
        # Attempt to parse the input string into a datetime object
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid input. Please enter a date in the format YYYY-MM-DD.")

while(True):
    try:
        end_date = input("please enter the time window end date (YYYY-MM-DD): ")
        # Attempt to parse the input string into a datetime object
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        break  # Exit the loop if the input is a valid date
    except ValueError:
        print("Invalid input. Please enter a date in the format YYYY-MM-DD.")

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

id_range = list(range(1, num_tickets + 1))

for _ in range(num_tickets):

    case_id = f'CS_{id_range.pop(0)}'
    activity = random.choice(['Design', 'Construction', 'Test', 'Password Reset'])

    urgency = random.choice(['H', 'M', 'L'])
    impact = random.choice(['H', 'M', 'L'])
    priority = priority_dic.get(urgency) + priority_dic.get(impact) - 1

    generated_start_date = start_date + timedelta(days=random.randint(0, (end_date - timedelta(days=14) - start_date).days))                         
    generated_end_date = generated_start_date + timedelta(days=random.randint(1,14))                 
    ticket_status = random.choice(['Open', 'On Hold', 'In Process', 'Deployed', 'Deployed Failed'])                                                                                                                                                
    update_datetime = generated_start_date + timedelta(days=random.randint(0, (generated_end_date - generated_start_date).days))                                            
    duration = (generated_end_date - generated_start_date).days
    origin = random.choice(['Joe S.', 'Bill B.', 'George E.', 'Achmed M.', 'Rona E.'])
    ticket_class = random.choice(['Change', 'Incident', 'Problem', 'SR'])

    # Insert the generated ticket into the database

    insert_query = """
    INSERT INTO EventLog (Caseid, Activity, Urgency, Impact, Priority, StartDate, EndDate, TicketStatus, UpdateDateTime, Duration, Origin, Class)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (case_id, activity, urgency, impact, priority, generated_start_date, generated_end_date, ticket_status, update_datetime, duration, origin, ticket_class)

    cursor.execute(insert_query, values)
    conn.commit()

cursor.close()
conn.close()