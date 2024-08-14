import time

tempo = 2

nome =input ("What's your name?")

time.sleep(tempo)
print("How can i help you?")
time.sleep(tempo)
print("1 - exams")
time.sleep(tempo)
print("2 - consult")
time.sleep(tempo)
print("3 - Medic Prescription")

time.sleep(tempo)
opcao = int(input("Choose a number"))

if opcao == 1:
    time.sleep(tempo)
    print ("Write your CPF")

elif opcao == 2:
    time.sleep(tempo)
    print ("Write your CPF")

else:
    time.sleep(tempo)
    print("Try another number")

