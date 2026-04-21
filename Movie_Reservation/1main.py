from users import signup, login, get_user_city
from movies import movies
from theatres import theatres
from booking import book_ticket, show_seats, bookings
from payment import process_payment

while True:
    print("\n1. SignUp")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

# ------------------- SIGNUP ----------------- #
    if choice == 1:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        city = input("Enter City: ")

        print(signup(username, password, city))

# ------------------- LOGIN ------------------- #
    elif choice == 2:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if login(username, password):
            print("Login Successful.")

# ------------------ MOVIES ------------------ #
            city = get_user_city(username)

            print("\nAvailable Movies:\n")
            movie_list = list(movies.keys())

            i = 1
            for m in movie_list:
                print(f"{i}. {m}")
                i += 1

            m_choice = int(input("Select movie: ")) - 1
            movie = movie_list[m_choice]

# ------------------ DATES ------------------ #
            dates = list(movies[movie].keys())

            print("\nAvailable Dates:\n")
            i = 1
            for d in dates:
                print(f"{i}. {d}")
                i += 1

            d_choice = int(input("Select date: ")) - 1
            date = dates[d_choice]

# ------------------ TIMES ------------------ #
            times = movies[movie][date]

            print("\nShow Timings:\n")
            i = 1
            for t in times:
                print(f"{i}. {t}")
                i += 1

            time_choice = int(input("Select time: ")) - 1
            time = times[time_choice]

# ------------------ THEATRES ------------------ #
            print("\nAvailable Theatres:\n")
            theatre_list = theatres.get(city.title(), [])

            i = 1
            for th in theatre_list:
                print(f"{i}. {th}")
                i += 1

            theatre_choice = int(input("Select theatre: ")) - 1
            theatre = theatre_list[theatre_choice]

# ------------------ SEAT BOOKING ------------------ #
            key = f"{movie}-{date}-{time}-{theatre}"
            booked_seats = bookings.get(key, [])

            show_seats(booked_seats)

            seat = input("\nEnter seat: ").upper()

# ------------------ PRICE ------------------ #
            row = seat[0]

            if row in ["I", "J"]:
                price = 560
            elif row in ["E", "F", "G", "H"]:
                price = 380
            elif row in ["C", "D"]:
                price = 290
            else:
                price = 270

# ------------------ PAYMENT ------------------ #
            if process_payment(price):
                result = book_ticket(username, movie, date, time, theatre, seat)
                print("\n" + result)
            else:
                print("Payment Failed ")

        else:
            print("Invalid login ")

# ------------------- EXIT ------------------- #
    else:
        print("Thank you!")
        break