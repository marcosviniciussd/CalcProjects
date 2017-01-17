
segundos_str = input("Entre com o numero de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = 0
horas = 0;
minutos = 0
segundos_restantes = 0
segundos_restantes_final = 0

dias = total_segs // 86400
horas = segundos_restantes % 3600
segundos_restantes = total_segs % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(dias, " dias", horas, "horas, ", minutos, "minutos e", segundos_restantes_final, "segundos.")
