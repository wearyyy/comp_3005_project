CREATE TABLE IF NOT EXISTS Users (
	user_id			SERIAL			PRIMARY KEY,
	username		VARCHAR(255)	UNIQUE NOT NULL,
	password		VARCHAR(255)	NOT NULL
);

CREATE TABLE IF NOT EXISTS Dashboards(
	user_id			INT				PRIMARY KEY,
	achievements	VARCHAR(255)	ARRAY,
	routine			VARCHAR(255)	ARRAY,
	weight_lost		FLOAT,
	
	FOREIGN KEY (user_id)
		REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Profiles(
	user_id			INT				PRIMARY KEY,
	first_name		VARCHAR(255),
	last_name		VARCHAR(255),
	email			VARCHAR(255),
	address			VARCHAR(255),
	weight			FLOAT,
	height			FLOAT,
	BMI				FLOAT,
	
	FOREIGN KEY(user_id)
		REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Goals(
	goal_id			SERIAL			PRIMARY KEY,
	user_id			INT,
	goal			VARCHAR(255),

	FOREIGN KEY(user_id)
		REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Trainers(
	trainer_id		SERIAL			PRIMARY KEY,
	username		VARCHAR(255)	UNIQUE NOT NULL,
	password		VARCHAR(255)	NOT NULL
);

CREATE TABLE IF NOT EXISTS Schedule(
	availability_id	SERIAL			PRIMARY KEY,
	trainer_id		INT,	
	available_date	DATE,
	available_time	TIME,
	duration		INT,
	
	FOREIGN KEY(trainer_id)
		REFERENCES Trainers(trainer_id)
);

CREATE TABLE IF NOT EXISTS Appointments(
	appointment_id		SERIAL		PRIMARY KEY,
	trainer_id			INT,
	user_id				INT,
	appointment_date	DATE,
	appointment_time	TIME,
	duration			INT,
	
	FOREIGN KEY(trainer_id)
		REFERENCES Trainers(trainer_id),
	FOREIGN KEY(user_id)
		REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Admins(
	admin_id		SERIAL			PRIMARY KEY,
	username		VARCHAR(255)	UNIQUE NOT NULL, 
	password		VARCHAR(255)	NOT NULL
);

CREATE TABLE IF NOT EXISTS Rooms(
	room_id			SERIAL			PRIMARY KEY,
	capacity		INT
);

CREATE TABLE IF NOT EXISTS Reservations(
	reservation_id	SERIAL			PRIMARY KEY,
	room_id			INT,
	class_id		INT,
	user_id			INT,
	reserved_date	DATE,
	reserved_time	TIME,
	duration		INT,
	
	FOREIGN KEY(room_id)
		REFERENCES Rooms(room_id),
	FOREIGN KEY(user_id)
		REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Classes(
	class_id		SERIAL			PRIMARY KEY,
	class_date		DATE,
	class_time		TIME,
	duration		INT,
	trainer_id		INT,
	room_id			INT,
	
	FOREIGN KEY(trainer_id)
		REFERENCES Trainers(trainer_id),
	FOREIGN KEY(room_id)
		REFERENCES Rooms(room_id)
);

CREATE TABLE IF NOT EXISTS Participants(
	participant_id 	SERIAL			PRIMARY KEY,
	class_id		INT,
	user_id			INT,
	
	FOREIGN KEY(user_id)
		REFERENCES Users(user_id),
	FOREIGN KEY(class_id)
		REFERENCES Classes(class_id)
);

CREATE TABLE IF NOT EXISTS Bills(
	bill_id			SERIAL			PRIMARY KEY,
	user_id			INT,
	amount			FLOAT,
	date_created	DATE,
	is_payed		BOOLEAN,
	FOREIGN KEY(user_id)
		REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Equipment(
	equipment_id	SERIAL			PRIMARY KEY,
	equipment_type	VARCHAR(255),
	last_maintained DATE
);