class Apartament:
    def __init__(self, nr_apartament, tip_apartament, pret_total, pret_inch):
        self.__nr_apartament = nr_apartament
        self.__tip_apartament = tip_apartament
        self.__pret_total = pret_total
        self.__pret_inch = pret_inch

    def get_nr_apartament(self):
        """
        functia obtine numarul apartamentului
        :return:numarul apartamentului
        """
        return self.__nr_apartament

    def get_tip_apartament(self):
        """
        functia obtine tipul apartamentului
        :return: tipul apartamentului
        """
        return self.__tip_apartament

    def get_pret_total(self):
        """
        functia obtine pretul total al apartamentului
        :return: pretul total al apartamentului
        """
        return self.__pret_total

    def get_pret_inch(self):
        """
        functia obtine pretul inchirierii apartamentului
        :return: pretul inchirierii apartamentului
        """
        return self.__pret_inch

    def __eq__(self, other):
        """
        functia verifica daca doua obiecte de tipul Apartement sunt egale
        :param other: obiect de tipul Apartament
        :return: True - obiectele sunt egale
                 False - altfel
        """
        return self.__nr_apartament == other.get_nr_apartament()

    def __str__(self):
        """
        functia converteste la string atributele obiectului de tipul Apartament
        :return: string
        """
        return f"{self.__nr_apartament},{self.__tip_apartament},{self.__pret_total},{self.__pret_inch}"
