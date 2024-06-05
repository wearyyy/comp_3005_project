import psycopg2

conn = psycopg2.connect (
    database = "Gym",
    host = "localhost",
    user = "postgres",
    password = "password",
    port = "5432"
)

conn.autocommit = True

cursor = conn.cursor()

##################################################USER FUNCTIONS##################################################
#Creates a user with the specified name and password
def createUser(username, password, fname, lname, email, address):
    cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))

    cursor.execute("SELECT user_id FROM Users WHERE username = %s", (username,))

    id = cursor.fetchone()

    createProfile(id, fname, lname, email, address)
    createDashboard(id)

#Searches for the specified user
def loginUser(username, password):
    cursor.execute("SELECT user_id FROM Users WHERE username = %s AND password = %s", (username, password))
    id = cursor.fetchone()
    if id:
        return id
    else:
        return False

##################################################TRAINER FUNCTIONS##################################################
#Create a Trainer
def createTrainer(username, password):
    cursor.execute("INSERT INTO Trainers (username, password) VALUES (%s, %s)", (username, password))

#Searches for the specified trainer
def loginTrainer(username, password):
    cursor.execute("SELECT trainer_id FROM Trainers WHERE username = %s AND password = %s", (username, password))
    id = cursor.fetchone()
    if id:
        return id
    else:
        return False

##################################################ADMIN FUNCTIONS##################################################
#Searches for the specified admin
def loginAdmin(username, password):
    cursor.execute("SELECT admin_id FROM Admins WHERE username = %s AND password = %s", (username, password))
    id = cursor.fetchone()
    if id:
        return id
    else:
        return False

##################################################BILL FUNCTIONS##################################################
#Creates a bill
def createBill(id, amount, date):
    cursor.execute("INSERT INTO Bills (user_id, amount, date_created, is_payed) VALUES (%s, %s, %s, %s)", (id, amount, date, False))

#Updates everything for a bill
def updateBill(bid, uid, amount, date, payed):
    updateBillUser(bid, uid)
    updateBillAmount(bid, amount)
    updateBillDate(bid, date)
    updateBillPayed(bid, payed)

#Updates a bill's user_id
def updateBillUser(bid, uid):
    cursor.execute("UPDATE Bills SET user_id = %s WHERE bill_id = %s", (uid, bid))

#Updates a bill's amount
def updateBillAmount(id, amount):
    cursor.execute("UPDATE Bills SET amount = %s WHERE bill_id = %s", (amount, id))

#Updates a bill's date
def updateBillDate(id, date):
    cursor.execute("UPDATE Bills SET date = %s WHERE bill_id = %s", (date, id))

#Updates if a bill is payed
def updateBillPayed(id, payed):
    cursor.execute("UPDATE Bills SET is_payed = %s WHERE bill_id = %s", (payed, id))

#Deletes a bill
def deleteBill(id):
    cursor.execute("DELETE FROM Bills WHERE bill_id = %s", (id))

#Pays a bill
def payBill(id):
    cursor.execute("SELECT is_payed FROM Bills WHERE bill_id = %s", (id))
    if cursor.fetchone()[0]:
        print("Bill is already payed \n")
        return
    else:
        cursor.execute("UPDATE Bills SET is_payed = %s WHERE bill_id = %s", (True, id))

#Prints all bills
def printBills():
    cursor.execute("SELECT * FROM Bills")
    data = cursor.fetchall()

    print("Bill ID | User ID | Is Payed |      Date      | Amount")
    for i in data:
        if i[4]:
            print("    %s   |    %s    |   %s   |   %s   |  %s" % (i[0], i[1], i[4], i[3], i[2]))
        else:
            print("    %s   |    %s    |   %s  |   %s   |  %s" % (i[0], i[1], i[4], i[3], i[2]))

#Prints bills for the specified user
def printUserBills(id):
    cursor.execute("SELECT * FROM Bills WHERE user_id = %s", (id,))
    data = cursor.fetchall()
    print("Bill ID | Is Payed |      Date      | Amount")
    for i in data:
        if i[4]:
            print("    %s   |   %s   |   %s   | %s" % (i[0], i[4], i[3], i[2]))
        else:
            print("    %s   |   %s  |   %s   | %s" % (i[0], i[4], i[3], i[2]))

##################################################PROFILE FUNCTIONS##################################################

#Create a profile for a user
def createProfile(id, fname, lname, email, address):
    cursor.execute("INSERT INTO Profiles (user_id, first_name, last_name, email, address) VALUES (%s, %s, %s, %s, %s)",
                   (id, fname, lname, email, address))

#Updates the entire profile
def updateProfile(id, fname, lname, email, address, weight, height, BMI):
    updateFname(id, fname)
    updateLname(id, lname)
    updateEmail(id, email)
    updateAddress(id, address)
    updateWeight(id, weight)
    updateHeight(id, height)
    updateBMI(id, BMI)

#Updates first name of the specified id on the Profiles table
def updateFname(id, fname):
    cursor.execute("UPDATE Profiles SET first_name = %s WHERE user_id = %s", (fname, id))

#Updates last name of the specified id on the Profiles table
def updateLname(id, lname):
    cursor.execute("UPDATE Profiles SET last_name = %s WHERE user_id = %s", (lname, id))

#Updates email of the specified id on the Profiles table
def updateEmail(id, email):
    cursor.execute("UPDATE Profiles SET email = %s WHERE user_id = %s", (email, id))

#Updates address of the specified id on the Profiles table
def updateAddress(id, address):
    cursor.execute("UPDATE Profiles SET address = %s WHERE user_id = %s", (address, id))

#Updates weight of the specified id on the Profiles table
def updateWeight(id, weight):
    cursor.execute("UPDATE Profiles SET weight = %s WHERE user_id = %s", (weight, id))

#Updates height of the specified id on the Profiles table
def updateHeight(id, height):
    cursor.execute("UPDATE Profiles SET height = %s WHERE user_id = %s", (height, id))

#Updates BMI of the specified id on the Profiles table
def updateBMI(id, bmi):
    cursor.execute("UPDATE Profiles SET BMI = %s WHERE user_id = %s", (bmi, id))

#Search for a user's profile based on their id
def searchUserID(id):
    cursor.execute("SELECT * FROM Profiles WHERE user_id = %s", (id,))
    data = cursor.fetchone()
    fname = data[1]
    lname = data[2]
    email = data[3]
    address = data[4]
    weight = data[5]
    height = data[6]
    bmi = data[7]
    print("First name: %s \nLast name: %s \nEmail: %s \nAddress: %s \nWeight: %s \nHeight: %s \nBMI: %s" %
          (fname, lname, email, address, weight, height, bmi))

#Search for a user's profile based on their first name
def searchUserF(fname):
    cursor.execute("SELECT user_id FROM Profiles WHERE first_name = %s", (fname,))
    tempData = cursor.fetchone()
    if tempData:
        data = tempData[0]
        printProfile(data)
    else:
        print("User not found \n")

#Search for a user's profile based on their last name
def searchUserL(lname):
    cursor.execute("SELECT user_id FROM Profiles WHERE last_name = %s", (lname,))
    tempData = cursor.fetchone()
    if tempData:
        data = tempData[0]
        printProfile(data)
    else:
        print("User not found \n")

#Prints a user's profile
def printProfile(id):
    cursor.execute("SELECT * FROM Profiles WHERE user_id = %s", (id,))
    data = cursor.fetchone()
    print("First name: %s \nLast name: %s \nEmail: %s \nAddress: %s \nWeight: %s \nHeight: %s \nBMI: %s" %
          (data[1], data[2], data[3], data[4], data[5], data[6], data[7]))


##################################################DASHBOARD FUNCTIONS##################################################

#Create a dashhboard for a user
def createDashboard(id):
    cursor.execute("INSERT INTO Dashboards (user_id, achievements, routine, weight_lost) VALUES (%s, %s, %s, %s)", (id, [], [], 0))

#Prints the user's achievements
def printAchievements(id):
    cursor.execute("SELECT achievements FROM Dashboards WHERE user_id = %s", (id,))
    data = cursor.fetchone()[0]
    for i in range(len(data)):
        print("Achievement %s: %s" % (i + 1, data[i]))

#Appends a string to the achievement array in the Dashboards table
def addAchievement(id, achievement):
    cursor.execute("UPDATE Dashboards SET achievements = ARRAY_APPEND(achievements, %s) WHERE user_id = %s", (achievement, id))

#Prints the user's current routine
def printRoutine(id):
    cursor.execute("SELECT routine FROM Dashboards WHERE user_id = %s", (id,))
    data= cursor.fetchone()[0]
    for i in range(len(data)):
        print("Exercise %s: %s" % (i + 1, data[i]))
    
#Changes the routine array in the Dashboards table
def updateRoutine(id, routine):
    cursor.execute("UPDATE Dashboards SET routine = %s WHERE user_id = %s", (routine, id))

#Adds to the weight lost in the Dashboards table
def updateWeightLost(id, weight):
    cursor.execute("UPDATE Dashboards SET weight_lost = weight_lost + %s WHERE user_id = %s", (weight, id))

##################################################GOAL FUNCTIONS##################################################

#Creates a goal for the specified user
def createGoal(id, goal):
    cursor.execute("INSERT INTO Goals (user_id, goal) VALUES (%s, %s)", (id, goal))

#Deletes a goal
def deleteGoal(id):
    cursor.execute("DELETE FROM Goals WHERE goal_id = %s", (id,))

#Update a goal
def updateGoal(id, goal):
    cursor.execute("UPDATE Goals SET goal = %s WHERE goal_id = %s", (goal, id))

##################################################AVAILABILITY FUNCTIONS##################################################

#Create an available time slot on the Schedule table
def createAvailability(id, date, time, duration):
    cursor.execute("INSERT INTO Schedule (trainer_id, available_date, available_time, duration) VALUES (%s, %s, %s, %s)", (id, date, time , duration))

#Creates an appointment and deletes the availability
def scheduleAppointment(aid, uid):
    cursor.execute("SELECT * FROM Schedule WHERE availability_id = %s", (aid, ))
    data = cursor.fetchone()
    createAppointment(data[1], uid, data[2], data[3], data[4])
    deleteAvailability(aid)
    
#Delete a time slot on the Schedule table
def deleteAvailability(id):
    cursor.execute("DELETE FROM Schedule WHERE availability_id = %s", (id,))

#Changes the entire availability
def updateAvailability(id, date, time, duration):
    updateAvailabilityDate(id, date)
    updateAvailabilityTime(id, time)
    updateAvailabilityDuration(id, duration)

#Changes the date of an availability
def updateAvailabilityDate(id, date):
    cursor.execute("UPDATE Schedule SET available_date = %s WHERE availability_id = %s", (date, id))

#Changes the time of an availability
def updateAvailabilityTime(id, time):
    cursor.execute("UPDATE Schedule SET available_time = %s WHERE availability_id = %s", (time, id))

#Changes the duration of an availability
def updateAvailabilityDuration(id, duration):
    cursor.execute("UPDATE Schedule SET duration = %s WHERE availability_id = %s", (duration, id))

#Prints all availabilities
def printAvailabilities():
    cursor.execute("SELECT * FROM Schedule")
    data = cursor.fetchall()
    print("Available Times \n")
    print("Availability ID | Trainer ID |     Date     |    Time    | Duration (Hours)")
    for i in data:
        print("        %s       |     %s      |  %s  |  %s  |    %s" % (i[0], i[1],i[2],i[3],i[4]))

#Prints the availabilities for the specified trainer
def printSchedule(id):
    cursor.execute("SELECT * FROM Schedule WHERE trainer_id = %s", (id,))
    data = cursor.fetchall()
    print("Available Times \n")
    print("Availability ID | Trainer ID |     Date     |    Time    | Duration (Hours)")
    for i in data:
        print("        %s       |     %s      |  %s  |  %s  |    %s" % (i[0], i[1],i[2],i[3],i[4]))


##################################################APPOINTMENT FUNCTIONS##################################################

#Creates an appointment
def createAppointment(tid, uid, date, time, duration):
    cursor.execute("INSERT INTO Appointments (trainer_id, user_id, appointment_date, appointment_time, duration) VALUES (%s, %s, %s, %s, %s)", (tid, uid, date, time, duration))

#Changes the appointment's trainer
def updateAppointmentTrainer(tid, aid):
    cursor.execute("UPDATE Appointments SET trainer_id = %s WHERE appointment_id = %s", (tid, aid))

#Changes the appointment's date
def updateAppointmentTrainer(date, id):
    cursor.execute("UPDATE Appointments SET appointment_date = %s WHERE appointment_id = %s", (date, id))

#Changes the appointment's time
def updateAppointmentTrainer(time, id):
    cursor.execute("UPDATE Appointments SET appointment_time = %s WHERE appointment_id = %s", (time, id))

#Prints a user's appointments
def printUserAppointments(id):
    cursor.execute ("SELECT * FROM Appointments WHERE user_id = %s", (id, ))
    data = cursor.fetchall()

    print("Appointments")
    print("Appointment ID | Trainer ID | User ID |     Date     |    Time    | Duration (Hours)")
    for i in data:
        print("       %s       |     %s      |    %s    |  %s  |  %s  |        %s" % (i[0], i[1], i[2], i[3], i[4], i[5]))

##################################################EQUIPMENT FUNCTIONS##################################################

#Creates equipment
def createEquipment(type, maintained):
    cursor.execute("INSERT INTO Equipment (equipment_type, last_maintained) VALUES (%s, %s)", (type, maintained))

#Deletes equipment
def deleteEquipment(id):
    cursor.execute("DELETE FROM Equipment WHERE equipment_id = %s", (id,))

#Update's equipment's last maintained date
def updateEquipment(id, date):
    cursor.execute("UPDATE Equipment SET last_maintained = %s WHERE equipment_id = %s", (date, id))

#Prints all equipment
def printEquipment():
    cursor.execute("SELECT * FROM Equipment")
    data = cursor.fetchall()
    print(" Equipment ID | Last Maintained | Equipment Type \n")
    for i in data:
        print("      %s      |   %s    |   %s " % (i[0], i[1], i[2]))

##################################################CLASS FUNCTIONS##################################################

#Creates a class
def createClass(date, time, duration, tid, rid):
    cursor.execute("INSERT INTO Classes (class_date, class_time, duration, trainer_id, room_id) VALUES (%s, %s, %s, %s ,%s)", (date, time, duration, tid, rid))

#Updates a class
def updateClass(cid, date, time, duration, tid, rid):
    updateClassDate(cid, date)
    updateClassTime(cid, time)
    updateClassDuration(cid, duration)
    updateClassTrainer(cid, tid)
    updateClassRoom(cid, rid)

#Update a class's date
def updateClassDate(id, date):
    cursor.execute("UPDATE Classes SET class_date = %s WHERE class_id = %s", (date, id))

#Update a class's time
def updateClassTime(id, time):
    cursor.execute("UPDATE Classes SET class_time = %s WHERE class_id = %s", (time, id))

#Update a class's duration
def updateClassDuration(id, duration):
    cursor.execute("UPDATE Classes SET duration = %s WHERE class_id = %s", (duration, id))

#Update a class's trainer
def updateClassTrainer(cid, tid):
    cursor.execute("UPDATE Classes SET trainer_id = %s WHERE class_id = %s", (tid, cid))

#Update a class's room
def updateClassRoom(cid, rid):
    cursor.execute("UPDATE Classes SET room_id = %s WHERE class_id = %s", (rid, cid))

#Deletes a class and all participants
def deleteClass(id):
    cursor.execute("DELETE FROM Participants WHERE class_id = %s", (id,))
    cursor.execute("DELETE FROM Classes WHERE class_id = %s", (id,))

#Prints all classes
def printClasses():
    cursor.execute("SELECT * FROM Classes")
    data = cursor.fetchall()
    print("Class ID |    Date    |   Time   | Length | Trainer | Room")
    for i in data:
        print("    %s    | %s | %s |   %s    |    %s    |  %s " % (i[0], i[1], i[2], i[3], i[4], i[5])) 

#Prints all participations for a user
def printUserParticipations(id):
    cursor.execute("SELECT class_id FROM Participants WHERE user_id = %s", (id, ))
    data = cursor.fetchall()
    print("Classes")
    print("Class ID |    Date    |   Time   | Length | Trainer | Room")
    for i in data:
        cursor.execute("SELECT * FROM Classes WHERE class_id = %s", (i))
        tempData = cursor.fetchone()
        print("    %s    | %s | %s |   %s    |    %s    |  %s " % (tempData[0], tempData[1], tempData[2], tempData[3], tempData[4], tempData[5])) 

#Creates a participant
def createParticipant(uid, cid):
    cursor.execute("INSERT INTO Participants (class_id, user_id) VALUES (%s, %s)", (cid, uid))

#Deletes a participant
def deleteParticipant(uid, cid):
    cursor.execute("DELETE FROM Participants WHERE class_id = %s AND user_id = %s", (cid, uid))

##################################################RESERVATION FUNCTIONS##################################################

#Creates a room reservation
def createReservation(rid, cid, uid, date, time, duration):
    cursor.execute("INSERT INTO Reservations (room_id, class_id, user_id, reserved_date, reserved_time, duration) VALUES (%s, %s, %s, %s, %s, %s)", (rid, cid, uid, date, time, duration))

#Deletes a room reservation
def deleteReservation(id):
    cursor.execute("DELETE FROM Reservations WHERE reservation_id = %s", (id,))

#Update Everything for a reservation
def updateReservation(roid, reid, cid, uid, date, time, duration):
    cursor.execute("UPDATE Reservations SET room_id = %s AND class_id = %s AND user_id = %s AND reserved_date = %s AND reserved_time = %s AND duration = %s WHERE reservation_id = %s",
                   (roid, reid, cid, uid, date, time, duration))

#Update a reservations's room
def updateReservationRoom(roid, reid):
    cursor.execute("UPDATE Reservations SET room_id = %s WHERE reservation_id = %s", (roid, reid))

#Update a reservations's class_id
def updateReservationClass(cid, rid):
    cursor.execute("UPDATE Reservations SET class_id = %s WHERE reservation_id = %s", (cid, rid))

#Update a reservations's user_id
def updateReservationUser(uid, rid):
    cursor.execute("UPDATE Reservations SET user_id = %s WHERE reservation_id = %s", (uid, rid))

#Update a reservations's date
def updateReservationDate(date, id):
    cursor.execute("UPDATE Reservations SET reserved_date = %s WHERE reservation_id = %s", (date, id))

#Update a reservations's time
def updateReservationTime(time, id):
    cursor.execute("UPDATE Reservations SET reserved_time = %s WHERE reservation_id = %s", (time, id))

#Update a reservations's duration
def updateReservationDuration(duration, id):
    cursor.execute("UPDATE Reservations SET duration = %s WHERE reservation_id = %s", (duration, id))

#Print all reservations
def printReservations():
    cursor.execute("SELECT * FROM Reservations")
    data = cursor.fetchall()
    print("Reservation ID | Room ID | Class ID | User ID |    Date    |   Time   | Length (Hours)")
    for i in data:
        if i[2] == None:
            print("      %s        |    %s    |   %s   |    %s    | %s | %s |     %s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        else:
            print("      %s        |    %s    |    %s     |   %s  | %s | %s |     %s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

##################################################VIEW##################################################

loginInput = -1

#main
while loginInput != "0":
    loginInput = input("0. Exit \n1. User Login \n2. User Registration \n3. Trainer Login \n4. Admin Login \n")
    if loginInput == "1":
        username = input("Input your Username: \n")
        password = input("Input your Password: \n")
        tempId = loginUser(username, password)
        if tempId:
            id = tempId[0]
            userInput = -1
            while userInput != "0":
                userInput = input("0. Logout \n1. View Profile \n2. View exercise routines \n3. View achievements \n4. Schedule an appointment/class \n5. View your bills \n")
                
                #Handles the profile view. Allows the user to edit each item individually, or all at once
                if userInput == "1":
                    printProfile(id)
                    profileInput = input("0.Return to dashboard \n1.Edit profile \n")

                    if profileInput == "1":
                        editInput = input("0.Return to dashboard \n1. Edit Everything \n2. Edit Name \n3. Edit email \n4. Edit address \n5. Edit weight \n6. Edit height \n7. Edit BMI \n")

                        if editInput == "1":
                            fname = input("Input a First Name\n")
                            lname = input("Input a Last Name\n")
                            email = input("Input an Email\n")
                            address = input("Input an Address\n")
                            weight = input("Input a Weight\n")
                            height = input("Input a Height\n")
                            bmi = input("Input a BMI\n")
                            updateProfile(id, fname, lname, email, address, weight, height, bmi)
                        elif editInput == "2":
                            fname = input("Input a First Name\n")
                            lname = input("Input a Last Name\n")
                            updateFname(id, fname)
                            updateLname(id, lname)
                        elif editInput == "3":
                            email = input("Input an Email\n")
                            updateEmail(id, email)
                        elif editInput == "4":
                            address = input("Input an Address\n")
                            updateAddress(id, address)
                        elif editInput == "5":
                            weight = input("Input a Weight\n")
                            updateWeight(id, weight)
                        elif editInput == "6":
                            height = input("Input a Height\n")
                            updateHeight(id, height)
                        elif editInput == "7":
                            bmi = input("Input a BMI\n")
                            updateBMI(id, bmi)
                        searchUserID(id)
                #Handles the Routines view, allows the user to create a new routine
                if userInput == "2":
                    printRoutine(id)
                    routineInput = input("0. Return to dashboard \n1.Edit routine \n")
                    if routineInput == "1":
                        routine = []
                        while True:
                            routineInput = input("0. Finish routine \nInput the next exercise: \n")
                            if routineInput == "0":
                                routine.append("Finish workout")
                                break
                            routine.append(routineInput)
                        updateRoutine(id, routine)
                        printRoutine(id)
                if userInput == "3":
                    printAchievements(id)
                    achievementInput = input("0. Return to dashboard \n1. Add achievement \n")
                    if achievementInput == "1":
                        achievement = input("Input your achievement: \n")
                        addAchievement(id,achievement)
                        printAchievements(id)
                if userInput == "4":
                    scheduleInput = input("0. Return to dashboard \n1. Sign up for class \n2. Sign up for private session \n3. View your classes/sessions \n")
                    if scheduleInput == "1":
                        printClasses()
                        registrationInput = input("0. Return to dashboard \n1. Sign up for a class \n")
                        if registrationInput == "1":
                            cid = input("0. Return to dashboard \nInput the class's id: \n")
                            if cid == "0":
                                print("\n")
                            else:
                                createParticipant(id, cid)
                    elif scheduleInput == "2":
                        printAvailabilities()
                        aid = input("0. Return to dashboard \nInput the availability's id: \n")
                        if aid == "0":
                            print("\n")
                        else:
                            scheduleAppointment(aid, id)
                    elif scheduleInput == "3":
                        printUserAppointments(id)
                        printUserParticipations(id)
                elif userInput == "5":
                    printUserBills(id)
                    billInput = input("0. Return to dashboard \n1. Pay bill \n")
                    if billInput == "1":
                        bid = input("Input a bill id: \n")
                        payBill(bid)
        else:
            print("Incorrect username/pasword \n")
    elif loginInput == "2":
            username = input("Input an Username: \n")
            password = input("Input a Password: \n")
            fname = input("Input a First Name\n")
            lname = input("Input a Last Name\n")
            email = input("Input an Email\n")
            address = input("Input an Address \n")

            createUser(username, password, fname, lname, email, address)

    elif loginInput == "3":
            username = input("Input your Username: \n")
            password = input("Input your Password: \n")
            tempId = loginTrainer(username, password)
            
            if tempId:
                id = tempId[0]
                trainerInput = -1
                while trainerInput != "0":
                    trainerInput = input("0. Logout \n1. Manage Schedule \n2. Search Members \n")
                    if trainerInput == "1":
                        printSchedule(1)
                        scheduleInput = input("0. Return to dashboard \n1. Create availability \n2. Edit availability \n3. Delete availability \n")
                        if scheduleInput == "1":
                            date = input("Input a date: \n")
                            time = input("Input a time: \n")
                            duration = input("Input a length: \n")
                            createAvailability(id, date, time, duration)
                        elif scheduleInput == "2":
                            editInput = input("0. Return to dashboard \n1. Edit Everything \n2. Edit date \n3. Edit time \n4. Edit length \n")

                            if editInput == "1":
                                aid = input("Input an availability id \n")
                                date = input("Input a date: \n")
                                time = input("Input a time: \n")
                                duration = input("Input a length(hours): \n")
                                updateAvailability(aid, date, time, duration)
                            elif editInput == "2":
                                aid = input("Input an availability id \n")
                                date = input("Input a date: \n")
                                updateAvailabilityDate(aid, date)
                            elif editInput == "3":
                                aid = input("Input an availability id \n")
                                time = input("Input a time: \n")
                                updateAvailabilityTime(aid, time)
                            elif editInput == "4":
                                aid = input("Input an availability id \n")
                                duration = input("Input a length(hours): \n")
                                updateAvailabilityDuration(aid, duration)
                        elif scheduleInput == "3":
                            aid = input("Input an availability id \n")
                            deleteAvailability(aid)
                    elif trainerInput == "2":
                        nameInput = input("0. Return to dashboard \n1. Search by first name \n2. Search by last name \n")
                        
                        if nameInput == "1":
                            searchInput = input ("0. Return to dashboard \nEnter a name to search: \n")
                            if searchInput == "0":
                                print("\n")
                            else:
                                searchUserF(searchInput)
                        elif nameInput == "2":
                            searchInput = input ("0. Return to dashboard \nEnter a name to search: \n")
                            if searchInput == "0":
                                print("\n")
                            else:
                                searchUserL(searchInput)

            else:
                print("Incorrect username/pasword \n")
    elif loginInput == "4":
            username = input("Input your Username: \n")
            password = input("Input your Password: \n")
            tempId = loginAdmin(username, password)
            if tempId:
                id = tempId[0]
                adminInput = -1
                while adminInput != "0":
                    adminInput = input("0. Logout \n1. Manage Rooms \n2. Manage Equipment \n3. Manage classes \n4. Create trainer \n5. Manage bills \n")
                    if adminInput == "1":
                        printReservations()
                        roomInput = input("0. Return to dashboard \n1. Create a reservation \n2. Edit a reservation \n3. Delete a reservation \n")
                        if roomInput == "1":
                            room = input("Input a room id: \n")
                            cid = input("Input a class id (Input 0 if there is no class): \n")
                            uid = input("Input a user id (Input 0 if there is no user): \n")
                            date = input("Input a date (Format: yyyy-mm-dd): \n")
                            time = input("Input a time (Format: HH:MM): \n")
                            duration = input("Input a length in hours: \n")

                            if cid == "0":
                                createReservation(room, None, uid, date, time, duration)
                            elif uid == "0":
                                createReservation(room, cid, None, date, time, duration)
                        elif roomInput == "2":
                            editInput = input("0. Return to dashboard \n1. Edit Everything \n2. Edit Room \n3. Edit Class \n4. Edit User \n5. Edit Date \n6. Edit Time \n7. Edit Length \n")

                            if editInput == "1":
                                reid = input("Input a reservation ID: \n")
                                roid = input("Input a room ID: \n")
                                cid = input("Input a class ID: \n")
                                uid = input("Input a user ID: \n")
                                date = input("Input a date: \n")
                                time = input("Input a time: \n")
                                duration = input("Input a length(hours): \n")
                                updateReservation(roid, reid, cid, uid, date, time, duration)
                            elif editInput == "2":
                                reid = input("Input a reservation ID: \n")
                                roid = input("Input a room ID: \n")
                                updateReservationRoom(roid, reid)
                            elif editInput == "3":
                                reid = input("Input a reservation ID: \n")
                                cid = input("Input a class ID: \n")
                                updateReservationClass(cid, reid)
                            elif editInput == "4":
                                reid = input("Input a reservation ID: \n")
                                uid = input("Input a user ID: \n")
                                updateReservationUser(uid, reid)
                            elif editInput == "5":
                                reid = input("Input a reservation ID: \n")
                                date = input("Input a date: \n")
                                updateReservationDate(date, reid)
                            elif editInput == "6":
                                reid = input("Input a reservation ID: \n")
                                time = input("Input a time: \n")
                                updateReservationTime(time, reid)
                            elif editInput == "7":
                                reid = input("Input a reservation ID: \n")
                                duration = input("Input a length(hours): \n")
                                updateReservationDuration(duration, reid)
                        elif roomInput == "3":
                            id = input("0. Return to dashboard \nInput a reservation id:\n")
                            if id == "0":
                                print("\n")
                            else:
                                deleteReservation(id)

                    elif adminInput == "2":
                        printEquipment()
                        
                        equipmentInput = input("0. Return to dashboard \n1. Add Equipment \n2. Update Equipment Maintained Date \n3. Delete Equipment \n")
                        
                        if equipmentInput == "1":
                            type = input("Input an equipment type \n")
                            date = input("Input a date \n")
                            createEquipment(type, date)
                        elif equipmentInput == "2":
                            id = input("Input an equipment id \n")
                            date = input("Input a date \n")
                            updateEquipment(id, date)
                        elif equipmentInput == "3":
                            id = input("Input an equipment id \n")
                            deleteEquipment(id)
                    elif adminInput == "3":
                        printClasses()
                        classInput = input("0. Return to dashboard \n1. Create a class \n2. Update a class \n3. Delete a class \n")
                        if classInput == "1":
                            date = input("Input a date \n")
                            time = input("Input a time \n")
                            duration = input("Input a length(hours) \n")
                            tid = input("Input a trainer id \n")
                            rid = input("Input a room id \n")
                            createClass(date, time, duration, tid, rid)
                        elif classInput == "2":
                            editInput = input("0. Return to dashboard \n1. Edit Everything \n2. Edit date \n3. Edit time \n4. Edit length \n5. Edit trainer \n6. Edit room \n")
                            if editInput == "1":
                                cid = input("Input a class id \n")
                                date = input("Input a date \n")
                                time = input("Input a time \n")
                                duration = input("Input a length(hours) \n")
                                tid = input("Input a trainer id \n")
                                rid = input("Input a room id \n")
                                updateClass(cid, date, time, duration, tid, rid)
                            elif editInput == "2":
                                cid = input("Input a class ID: \n")
                                date = input("Input a date \n")
                                updateClassDate(cid, date)
                            elif editInput == "3":
                                cid = input("Input a class ID: \n")
                                time = input("Input a time \n")
                                updateClassTime(cid, time)
                            elif editInput == "4":
                                cid = input("Input a class ID: \n")
                                duration = input("Input a length(hours) \n")
                                updateClassDuration(cid, duration)
                            elif editInput == "5":
                                cid = input("Input a class ID: \n")
                                tid = input("Input a trainer id \n")
                                updateClassTrainer(cid, tid)
                            elif editInput == "6":
                                cid = input("Input a class ID: \n")
                                rid = input("Input a room id \n")
                                updateClassRoom(cid, rid)
                        elif classInput == "3":
                            cid = input("Input a class ID: \n")
                            deleteClass(cid)

                    elif adminInput == "4":
                        usernameT = input("Input a Username \n")
                        passwordT = input("Input a Password \n")
                        createTrainer(usernameT, passwordT)

                    elif adminInput == "5":
                        printBills()
                        billInput = input("0. Return to dashboard \n1. Create a bill \n2. Edit a bill \n3. Delete a bill \n")
                        if billInput == "1":
                            uid = input("Input a user id: \n")
                            amount = input("Input an amount: \n")
                            date = input("Input a date: \n")
                            createBill(uid, amount, date)
                        elif billInput == "2":
                            editInput = input("0. Return to dashboard \n1. Edit Everything \n2. Edit bill's user id \n3. Edit bill's amount \n4. Edit bill's date \n 5. Edit if a bill is payed \n")
                            if editInput == "1":
                                bid = input("Input a bill id: \n")
                                uid = input("Input a user id: \n")
                                amount = input("Input a amount: \n")
                                date = input("Input a date: \n")
                                payed = input("Input if the bill is payed (True/False): \n")
                                updateBill(bid, uid, amount, date, payed)
                            elif editInput == "2":
                                bid = input("Input a bill id: \n")
                                uid = input("Input a user id: \n")
                                updateBillUser(bid, uid)
                            elif editInput == "3":
                                bid = input("Input a bill id: \n")
                                amount = input("Input a amount: \n")
                                updateBillAmount(bid, amount)
                            elif editInput == "4":
                                bid = input("Input a bill id: \n")
                                date = input("Input a date: \n")
                                updateBillDate(bid, date)
                            elif editInput == "5":
                                bid = input("Input a bill id: \n")
                                payed = input("Input if the bill is payed (True/False): \n")
                                updateBillPayed(bid, payed)
                        elif billInput == "3":
                            bid = input("Input a bill id: \n")
                            deleteBill(bid)
                
            else:
                print("Incorrect username/pasword \n")
