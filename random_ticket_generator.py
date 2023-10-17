import random
import mysql.connector
from datetime import datetime, timedelta

db_config = {
    'host': 'localhost',
    'user': 'demoaccount',
    'password': 'ensf607PA$$',
    'database': 'service_tickets'
}

num_tickets = 10000

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 6, 30)

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

for _ in range(num_tickets):
    case_id = f'CS_{random.randint(1, 10000)}'
    activity = random.choice(['Design', 'Construction', 'Test', 'Password Reset'])
    urgency = random.choice(['H', 'M', 'L'])
    impact = random.choice(['H', 'M', 'L'])
    priority_values = 'HML'
    priority = priority_values[min(2, 3 * ('H' in urgency) + ('H' in impact))]
    start_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    end_date = start_date + timedelta(days=random.randint(1, (end_date - start_date).days))
    ticket_status = random.choice(['Open', 'On Hold', 'In Process', 'Deployed', 'Deployed Failed'])
    update_datetime = datetime.now()
    duration = (end_date - start_date).days
    origin = random.choice(['Joe S.', 'Bill B.', 'George E.', 'Achmed M.', 'Rona E.'])
    ticket_class = random.choice(['Change', 'Incident', 'Problem', 'SR'])

    # Insert the generated ticket into the database
    insert_query = """
    INSERT INTO EventLog (Caseid, Activity, Urgency, Impact, Priority, StartDate, EndDate, TicketStatus, UpdateDateTime, Duration, Origin, Class)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (case_id, activity, urgency, impact, priority, start_date, end_date, ticket_status, update_datetime, duration, origin, ticket_class)

    cursor.execute(insert_query, values)
    conn.commit()

cursor.close()
conn.close()