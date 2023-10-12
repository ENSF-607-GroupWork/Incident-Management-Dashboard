CREATE TABLE EventActivity (
	ID INT AUTO_INCREMENT PRIMARY KEY,  
    Activityname VARCHAR(20)	/* Activity Name */
);

CREATE TABLE EventOrigin (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Activityname VARCHAR(20)	/* Activity Name */
);

CREATE TABLE EventStatus (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Status VARCHAR(20)    		/* Status Description */
);

CREATE TABLE EventClass (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Class VARCHAR(20)			/* Class Description */
);

CREATE TABLE EventLog (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Caseid VARCHAR(20),			/* Unique Case ID. Prefixed with CS_<number> */
    Activity VARCHAR(20),		/* Activity from EventActivity Table */
    Urgency VARCHAR(1),			/* Urgency value from table */
	Impact VARCHAR(1),			/* Impact from table */
    Priority VARCHAR(1),		/* Calculated Priority from urgency and impact */
    StartDate DATE,				/* Date ticket was created */
    EndDate DATE,				/* Date ticket was closed */
    TicketStatus VARCHAR(20),	/* Ticket status */
    UpdateDateTime DATETIME,	/* Date/ Timestamp of ticket record */
    Duration INT,				/* Length of ticket time. Calculated between start date and end date */
    Origin VARCHAR(20),			/* Person/Owner of ticket */
    Class VARCHAR(20)			/* Ticket class from the class table */
);


