from erori.Repo_Error import RepoError
from erori.Validation_Error import ValidationError


class UI:
    def __init__(self, serice_apartamente):
        self.__service_apartamente = serice_apartamente
        self.__comenzi = {
            "cauta_ap_de_tipul": self.__ui_cauta_apartament_de_tipul,
            "determinare_pret_inch": self.__ui_determinare_pret_inch,
            "adauga_ap": self.__ui_adauga_apartamente,
            "print_ap": self.__ui_print_apartamente
        }

    def run(self):
        while True:
            comanda = input(">>> ")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI: Tip numeric invalid!")
                except ValidationError as ve:
                    print(f"Validation Error:{ve}")
                except RepoError as rp:
                    print(f"Repo Error: {rp}")
            else:
                print("comanda invalida!")

    def __ui_cauta_apartament_de_tipul(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
        tip = int(self.__params[0])
        ap_de_tipul = self.__service_apartamente.cauta_ap_de_tipul(tip)
        if len(ap_de_tipul) == 0:
            print(f"Nu exista niciun apartament de tipul {tip}!")
            return
        for ap in ap_de_tipul:
            print(ap)

    def __ui_determinare_pret_inch(self):
        pass

    def __ui_adauga_apartamente(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
        nr_ap = int(self.__params[0])
        tip = int(self.__params[1])
        pret_total = int(self.__params[2])
        pret_inch = int(self.__params[3])
        self.__service_apartamente.adauga_apartament(nr_ap, tip, pret_total, pret_inch)
        print("Apartament adaugat cu succes!")

    def __ui_print_apartamente(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
        apartamente = self.__service_apartamente.get_all()
        if len(apartamente) == 0:
            print("Nu exista apartamente in aplicatie!")
            return
        for ap in apartamente:
            print(ap)
