import os

class Passenger:
    def __init__(self, name, seat, flight_code):
        self.name = name
        self.seat = seat
        self.flight_code = flight_code

    def __str__(self):
        return f"{self.name},{self.seat},{self.flight_code}"


ROWS = 5
COLS = 6
seats = [[0 for _ in range(COLS)] for _ in range(ROWS)]
passengers = []
FILE_NAME = "bookings.txt"


def load_data():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, seat, flight = line.strip().split(",")
            passengers.append(Passenger(name, seat, flight))
            row = int(seat[1]) - 1
            col = ord(seat[0]) - 65
            seats[row][col] = 1


def save_data():
    with open(FILE_NAME, "w") as file:
        for p in passengers:
            file.write(str(p) + "\n")


def display_seats():
    print("\nSeat Layout (0 = Available, 1 = Booked)")
    print("   A B C D E F")
    for i in range(ROWS):
        print(f"{i+1}  ", end="")
        for j in range(COLS):
            print(seats[i][j], end=" ")
        print()


def book_ticket():
    name = input("Enter passenger name: ").strip()
    flight = input("Enter flight code: ").strip()
    seat = input("Choose seat (e.g. A1): ").upper().strip()

    try:
        row = int(seat[1]) - 1
        col = ord(seat[0]) - 65
    except:
        print("Invalid seat format")
        return

    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print("Seat does not exist")
        return

    if seats[row][col] == 1:
        print("Seat already booked")
        return

    seats[row][col] = 1
    passengers.append(Passenger(name, seat, flight))
    print("Ticket booked successfully")

def cancel_booking():
    name = input("Enter passenger name to cancel: ").strip()

    for p in passengers:
        if p.name.lower() == name.lower():
            row = int(p.seat[1]) - 1
            col = ord(p.seat[0]) - 65
            seats[row][col] = 0
            passengers.remove(p)
            print("Booking cancelled")
            return

    print("Passenger not found")


def search_passenger():
    name = input("Enter name to search: ").strip()
    found = False

    for p in passengers:
        if name.lower() in p.name.lower():
            print(f"Name: {p.name}, Seat: {p.seat}, Flight: {p.flight_code}")
            found = True

    if not found:
        print("No passenger found")


def main():
    load_data()

    while True:
        print("\n--- Airline Ticket Reservation System ---")
        print("1. Book Ticket")
        print("2. View Seats")
        print("3. Cancel Booking")
        print("4. Search Passenger")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            display_seats()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            search_passenger()
        elif choice == "5":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()