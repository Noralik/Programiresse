class Room:
  def __init__(self, room_number, room_type):
      self.room_number = room_number
      self.room_type = room_type
      self.bookings = []

  def is_available(self, check_in_date, check_out_date):
      for booking in self.bookings:
          if check_in_date <= booking['check_out'] and check_out_date >= booking['check_in']:
              print(f"Room {self.room_number} is not available")
              return False
      print(f"Room {self.room_number} is available")
      return True

  def add_booking(self, check_in_date, check_out_date):
      if self.is_available(check_in_date, check_out_date):
          self.bookings.append({'check_in': check_in_date, 'check_out': check_out_date})
          print(f"Booking added for room {self.room_number} from {check_in_date} to {check_out_date}")
      else:
          print(f"Cannot add booking for room {self.room_number} from {check_in_date} to {check_out_date}, the room is not available")


class Booking:
  def __init__(self, booking_id, room, guest_name, check_in_date, check_out_date):
      self.booking_id = booking_id
      self.room = room
      self.guest_name = guest_name
      self.check_in_date = check_in_date
      self.check_out_date = check_out_date

  def display_details(self):
      print(f"Booking ID: {self.booking_id}")
      print(f"Room Number: {self.room.room_number}")
      print(f"Guest Name: {self.guest_name}")
      print(f"Check-in Date: {self.check_in_date}")
      print(f"Check-out Date: {self.check_out_date}")


class Hotel:
  def __init__(self, name):
      self.name = name
      self.rooms = []
      self.bookings = []

  def add_room(self, room_number, room_type):
      room = Room(room_number, room_type)
      self.rooms.append(room)
      print(f"Room {room_number} added to {self.name}")

  def get_available_rooms(self, check_in_date, check_out_date):
      available_rooms = []
      for room in self.rooms:
          if room.is_available(check_in_date, check_out_date):
              available_rooms.append(room)
      return available_rooms

  def book_room(self, room_number, guest_name, check_in_date, check_out_date):
      for room in self.rooms:
          if room.room_number == room_number:
              if room.is_available(check_in_date, check_out_date):
                  room.add_booking(check_in_date, check_out_date)
                  booking_id = len(self.bookings) + 1
                  new_booking = Booking(booking_id, room, guest_name, check_in_date, check_out_date)
                  self.bookings.append(new_booking)
                  print(f"Booking for room {room_number} added successfully.")
                  return new_booking
              else:
                  print(f"Room {room_number} is not available for the given dates.")
                  return None
      print(f"Room {room_number} not found.")
      return None


class HotelManagementSystem:
  def __init__(self):
      self.hotels = []

  def add_hotel(self, hotel):
      self.hotels.append(hotel)
      print(f"Hotel {hotel.name} added to the management system.")

  def find_available_rooms(self, check_in_date, check_out_date):
      available_rooms = []
      for hotel in self.hotels:
          available_rooms.extend(hotel.get_available_rooms(check_in_date, check_out_date))
      return available_rooms

  def book_room(self, hotel_name, room_number, guest_name, check_in_date, check_out_date):
      for hotel in self.hotels:
          if hotel.name == hotel_name:
              return hotel.book_room(room_number, guest_name, check_in_date, check_out_date)
      print(f"Hotel {hotel_name} not found in the management system.")
      return None


def main():
  management_system = HotelManagementSystem()

  hotel1 = Hotel("The Grand Budapest")
  hotel2 = Hotel("Luxury Inn")
  hotel3 = Hotel("Cozy Retreat")

  management_system.add_hotel(hotel1)
  management_system.add_hotel(hotel2)
  management_system.add_hotel(hotel3)

  hotel1.add_room("101", "Single")
  hotel1.add_room("102", "Double")
  hotel2.add_room("201", "Single")
  hotel2.add_room("202", "Double")
  hotel3.add_room("301", "Single")
  hotel3.add_room("302", "Double")

  while True:
      print("1. Show available rooms")
      print("2. Book a room")
      print("3. Exit")
      choice = input("Enter your choice: ")

      if choice == "1":
          check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
          check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
          available_rooms = management_system.find_available_rooms(check_in_date, check_out_date)
          if available_rooms:
              print("Available rooms:")
              for room in available_rooms:
                  print(f"Room Number: {room.room_number} - Room Type: {room.room_type}")
          else:
              print("No available rooms for the specified dates.")

      elif choice == "2":
          hotel_name = input("Enter hotel name: ")
          room_number = input("Enter room number: ")
          guest_name = input("Enter guest name: ")
          check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
          check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
          management_system.book_room(hotel_name, room_number, guest_name, check_in_date, check_out_date)

      elif choice == "3":
          print("Exiting...")
          break

      else:
          print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
  main()
