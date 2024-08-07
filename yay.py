import time

tempo = 5

nome =input ("What's your name?")

time.sleep(tempo)
print("How can i help you?")
print("1 - exams")
print("2 - consult")
print("3 - Medic Prescription")

opcao = int(input("Choose a number"))
if opcao == 1:
    print ("Write your CPF")

elif opcao == 2:
    print ("Write your CPF")

else:
    print("Try another number")