from domeniu.apartament import Apartament
from infrastructura.file_repo_apartamente import FileRepoApartamanete


class Teste:
    def run_all_tests(self):
        self.__run_file_repo_tests()

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def __run_file_repo_tests(self):
        cale_test_file = "teste/apartamente_test.txt"
        self.__goleste_fisier(cale_test_file)
        file_repo = FileRepoApartamanete(cale_test_file)
        assert file_repo.size() == 0
        ap = Apartament(12, 2, 50000, 300)
        file_repo.adauga_apartament(ap)
        assert file_repo.size() == 1
        print("teste file repo rulate cu succes!")