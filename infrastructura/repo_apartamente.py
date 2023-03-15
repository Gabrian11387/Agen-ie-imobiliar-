from erori.Repo_Error import RepoError

class RepoApartamente:
    def __init__(self):
        self._apartamente = []

    def adauga_apartament(self, apartament):
        for ap in self._apartamente:
            if ap.get_nr_apartament() == apartament.get_nr_apartament():
                raise RepoError("Apartament existent")
        self._apartamente.append(apartament)

    def cauta_apartament_dupa_tip(self, tip):
        ap_bune = []
        for ap in self._apartamente:
            if ap.get_tip_apartament() == tip:
                ap_bune.append(ap)
        return ap_bune[:]

    def sterge_apartament_dupa_nr_ap(self, nr_ap):
        for ap in self._apartamente:
            if ap.get_nr_apartament() == nr_ap:
                self._apartamente.remove(ap)
                return
        raise RepoError("Apartament inexistent")

    def get_all(self):
        return self._apartamente[:]

    def size(self):
        return len(self._apartamente)