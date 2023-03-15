from domeniu.apartament import Apartament


class ServiceApartamente:
    def __init__(self, validator_ap, repo_ap):
        self.__validator_ap = validator_ap
        self.__repo_ap = repo_ap

    def adauga_apartament(self, nr_ap, tip, pret_total, pret_inch):
        apartament = Apartament(nr_ap, tip, pret_total, pret_inch)
        self.__validator_ap.valideaza(apartament)
        self.__repo_ap.adauga_apartament(apartament)

    def get_all(self):
        return self.__repo_ap.get_all()

    def cauta_ap_de_tipul(self, tip):
        return self.__repo_ap.cauta_apartament_dupa_tip(tip)
