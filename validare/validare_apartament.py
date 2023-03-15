from erori.Validation_Error import ValidationError


class ValidatorApartament:
    def __init__(self):
        pass

    def valideaza(self, apartament):
        erori = ""
        if apartament.get_nr_apartament() < 0:
            erori += "Numar apartament invalid!\n"
        if apartament.get_tip_apartament() < 0:
            erori += "Tip apartament invalid!\n"
        if apartament.get_pret_total() < 0:
            erori += "Pret total apartament invalid!\n"
        if apartament.get_pret_inch() < 0:
            erori += "Pret inchiriere apartament invalid!\n"
        if len(erori) > 0:
            raise ValidationError(erori)