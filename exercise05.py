from get_input import Input_and_Casting, Input_only

def main():

header()
people_object_list = []
new_people_object_list = process_counter(people_object_list,5)
for x in new_people_object_list:
        print(f"\n{x}")

def header():
print("\n")
print("      @                           @@@")
print("     @ @          Centro          @@@")
print("    @   @                     @@@@@@@@@@@")
print("   @  @@@@          de        @@@@@@@@@@@")
print("   @@@@@@@                        @@@")
print("    @@@@@       Hematologia       @@@")
print("\n")

class Person:
def __init__(self, name, cpf, password,can_be_donor):
self.name = name
self.cpf = cpf
self.password = password
self.can_be_donor = can_be_donor

def __str__(self):
description = f"Nome completo: {self.name}\n"
description += f"CPF: {self.cpf}\n"
description += f"Senha: {self.password}\n"
description += f"Pode ser doador?: {self.can_be_donor}"
return description

def verified(x):
if True in x:
return x[1]

def verification(age,weight,sleep_time):
    
def age_verification(age):
return age<16 or age>69, "Idade"

def weight_verification(weight):
return weight<50, "Peso"
        

def sleep_time_verification(sleep_time):
return sleep_time=="n", "Não dormiu mais de 6 horas na últimas 24 horas"

return  age_verification(age), weight_verification(weight), sleep_time_verification(sleep_time)

def register(can_be_donor):
full_name = input("Qual seu nome completo: ")
cpf = input("Qual seu CPF: ")
password = input("Qual será sua senha: ")
return Person(full_name,cpf,password,can_be_donor)
 
def process():
age = Input_and_Casting("\nQual a sua idade: ",int).casting() 
weight = Input_and_Casting("Qual o seu peso: ",int).casting()
sleep_time = Input_only("Você dormiu pelo menos 6 horas nas últimas 24 horas: s/n ").only("s", "n")

verified_age, verified_weight, verified_sleep_time = verification(age,weight,sleep_time)
list_of_verified = [verified_age, verified_weight, verified_sleep_time]
unmet_requirements = list(map(verified, list_of_verified))

if unmet_requirements.count(None) != 3:
can_be_donor = "Não"
print("\nOs requisitos que não foram atendidos são:")
for x in unmet_requirements: 
            if x != None: print(x)
else:
can_be_donor = "Sim"
print("Você pode ser um doador")

want_to_register = Input_only("\nVocê gostaria de se cadastrar no laboratório: s/n ").only("s", "n")

if want_to_register=="s":
person = register(can_be_donor)
return person
else:
return False

def process_counter(people_object_list, number_obligatory_registers):
return_receiver = process()
if return_receiver:
people_object_list.append(return_receiver)
if len(people_object_list)<number_obligatory_registers:
return process_counter(people_object_list,number_obligatory_registers) 
else:
return people_object_list

if __name__ == "__main__":
main()
