# convert grad cels to fahrengeit
#  Formula	(0°C × 9/5) + 32 = 32°F

# Запрашиваем у пользователя градусы цельсия
try:
  grad_cels_to_convert = float(input("Введите градусы цельсия: "))
except ValueError:
  print("Ошибка: Введите корректное число.")
  exit()

# производим перевод в градусы фаренгейта
grad_fahrengeit = (grad_cels_to_convert * 9/5) + 32

# выводим результат
print ("Градусы фаренгейта", grad_fahrengeit)