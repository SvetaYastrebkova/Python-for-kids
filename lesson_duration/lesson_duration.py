# input start time
try:
    start_time = input("Введите время начала (HH:MM): ")
    start_h, start_m = map(int, start_time.split(":"))
except ValueError:
  print("Ошибка: Введите часы и минуты в формате HH:MM.")
  exit()
# input end time
try:
    end_time = input("Введите время окончания (HH:MM): ")
    end_h, end_m = map(int, end_time.split(":"))
except ValueError:
  print("Ошибка: Введите часы и минуты в формате HH:MM.")
  exit()  
    
# calc lesson duration, min

start_total_minutes = start_h * 60 + start_m
end_total_minutes = end_h * 60 + end_m

# chek 24:00 
if end_total_minutes < start_total_minutes:
    duration_minutes = (24 * 60 - start_total_minutes) + end_total_minutes
else:
    duration_minutes = end_total_minutes - start_total_minutes


# calc lesson duration, academic hours
academic_hours = duration_minutes / 45

# output

print(f"Продолжительность занятия: {academic_hours:.2f} академ. часов")
