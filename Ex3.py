segundos_str = input("Entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)
dias = 0
horas = 0
minutos = 0
segundos_restantes = 0
segundos_restantes_final = 0
dias = total_segs // 86400
horas = (total_segs % 86400) // 3600
minutos = (total_segs % 3600) // 60
segundos_restantes_final = (total_segs % 60) // 1
print(dias," dias,", horas,"horas, ",minutos,"minutos e",segundos_restantes_final,"segundos.")