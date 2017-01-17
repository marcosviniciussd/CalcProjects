
segundos_str = input("Entre com o numero de segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = 0;
minutos = 0
segundos_restantes = 0
segundos_restantes_final = 0

horas = total_segs // 3600
segundos_restantes = total_segs % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(horas, "horas, ", minutos, "minutos e", segundos_restantes_final, "segundos.")
