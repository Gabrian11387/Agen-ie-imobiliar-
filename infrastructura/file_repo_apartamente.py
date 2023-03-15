from domeniu.apartament import Apartament
from infrastructura.repo_apartamente import RepoApartamente


class FileRepoApartamanete(RepoApartamente):
    def __init__(self, calea_catre_fisier):
        RepoApartamente.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._apartamente.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    nr_ap = int(parts[0])
                    tip = int(parts[1])
                    pret_total = int(parts[2])
                    pret_inch = int(parts[3])
                    ap = Apartament(nr_ap, tip, pret_total, pret_inch)
                    self._apartamente.append(ap)

    def write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for ap in self._apartamente:
                f.write(str(ap) + "\n")

    def adauga_apartament(self, apartament):
        self.read_all_from_file()
        RepoApartamente.adauga_apartament(self, apartament)
        self.write_all_to_file()

    def get_all(self):
        self.read_all_from_file()
        return RepoApartamente.get_all(self)

    def size(self):
        self.write_all_to_file()
        return RepoApartamente.size(self)