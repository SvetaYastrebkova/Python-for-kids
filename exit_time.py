# Input flight departure time
try:
    flight_time = input("Введите время рейса (HH:MM): ")
    flight_time_h, flight_time_m = map(int, flight_time.split(":"))
except ValueError:
  print("Ошибка: Введите часы и минуты в формате HH:MM.")
  exit()
  
# Input travel time to the airport
try:
    travel_time = int(input("Введите время пути до аэропорта в минутах: "))
except ValueError:
    print("Ошибка: Введите время пути в минутах.")
    exit()

# Security check time (3 hours = 180 minutes)
security_check_time = 180

# Convert flight time to total minutes

flight_total_minutes = flight_time_h * 60 + flight_time_m


# Calculate home exit time
home_exit_minutes = flight_total_minutes - (travel_time + security_check_time)

# Convert back to HH:MM format
home_exit_h = (home_exit_minutes // 60) % 24
home_exit_m = home_exit_minutes % 60

print(f"Выходите в: {home_exit_h:02d}:{home_exit_m:02d}")
