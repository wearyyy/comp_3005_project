---Populate User Table
INSERT INTO Users (username, password)
VALUES
('john', 'jerryword'),
('bobbybob2003', 'bobbobby'),
('toughguy', 'strongguy'),
('bigman', 'smallman');

---Populate Profiles Table
INSERT INTO Profiles(user_id, first_name, last_name, email, address, weight, height, BMI)
VALUES
(1, 'Jerry','Jenkins','jerryjenkins@example.com','46 jerrySt', 84.6, 177.7, 27.2),
(2, 'Bobby','Bob','bobbybob@example.com','12 bobbySt', 60.4, 163.4, 24),
(3, 'Larry','Lobster','larrylobster@example.com','1 shellSt', 100, 221.2, 40),
(4, 'Saxton','Hale','saxtonhale@mannco.com','99 gravelRd', 120, 250, 50);

---Populate Dasboards Table
INSERT INTO Dashboards(user_id, achievements, routine, weight_lost)
VALUES
(1, ARRAY ['Lost 10 pounds', 'Consistently went to the gym for a year'], ARRAY ['20 pushups', '20 situps', '1.6 kilometere run'], 13.2),
(2, ARRAY ['Went to the gym once'], ARRAY ['5 pushups'], 2),
(3, ARRAY ['Benched 130 kg', 'Squated 110 kg'], ARRAY ['7 reps of bench press', '7 reps of squats', '2 km run'], 56),
(4, ARRAY ['Benched 160 kg', 'Squated 140 kg'], ARRAY ['20 reps of bench presses', '20 reps of squats', '10 reps deadlifts'], 70);

---Popualte Goals Table
INSERT INTO Goals(user_id, goal)
VALUES
(1, 'Keep going to the gym'),
(1, 'Lose 5 kg'),
(1, 'Stay healthy'),
(2, 'Go to the gym'),
(3, 'Bench 135 kg'),
(3, 'Squat 115 kg'),
(4, 'Bench 180 by the end of the year'),
(4, 'Squat 150 by the end of the year');

---Populate Trainer Table
INSERT INTO Trainers (username, password)
VALUES
('lifecoach', 'hearthstone'),
('muscleInspector', 'pecs');

---Populate Schedule Table
INSERT INTO Schedule (trainer_id, available_date, available_time, duration)
VALUES
(1, '2024-04-01', '11:00', 2),
(1, '2024-04-01', '14:00', 3),
(1, '2024-04-01', '16:00', 1),
(1, '2024-04-02', '11:00', 3),
(1, '2024-04-02', '16:00', 2),
(2, '2024-04-01', '11:00', 3),
(2, '2024-04-01', '14:00', 3),
(2, '2024-04-02', '11:00', 3);

--Populate Appointments Table
INSERT INTO Appointments (trainer_id, user_id, appointment_date, appointment_time, duration)
VALUES
(1, 1, '2024-03-30', '11:00', 2),
(2, 3, '2024-03-30', '14:00', 3),
(1, 4, '2024-03-31', '11:00', 2);

---Populate Admin Table
INSERT INTO Admins (username, password)
VALUES
('paperPusher', 'thumbtacks');

---Populate Rooms Table
INSERT INTO Rooms (capacity)
VALUES
(4),
(5),
(7),
(10),
(10);

---Populate Reservations Table
INSERT INTO Reservations (room_id, class_id, user_id, reserved_date, reserved_time, duration)
VALUES
(1, NULL, 1, '2024-04-01', '11:00', 2),
(2, NULL, 4, '2024-04-01', '12:00', 4),
(4, 1, NULL, '2024-04-04', '13:00', 2),
(5, 2, NULL, '2024-04-05', '11:00', 2);

---Populate Classes Table
INSERT INTO Classes(class_date, class_time, duration, trainer_id, room_id)
VALUES
('2024-04-04', '13:00', 2, 1, 4),
('2024-04-05', '11:00', 2, 2, 4);

---Populate Participants Table
INSERT INTO Participants(class_id, user_id)
VALUES
(1, 1),
(1, 3),
(2, 4);

--Populate Bills Table
INSERT INTO Bills (user_id, amount, date_created, is_payed)
VALUES
(1, 20, '2024-03-25', TRUE),
(4, 40, '2024-03-25', FALSE),
(1,  9.99, '2024-03-26', FALSE),
(3, 9.99, '2024-03-26', FALSE),
(4, 14.99, '2024-03-27', FALSE);

---Populate Equipment Table
INSERT INTO Equipment (equipment_type, last_maintained)
VALUES
('Treadmill', '2024-03-01'),
('Treadmill', '2024-03-01'),
('Chest Press Machine', '2024-03-15'),
('Chest Press Machine', '2024-03-15'),
('Exercise Bike', '2024-03-23'),
('Exercise Bike', '2024-03-23'),
('Power Rack', '2024-03-20');

