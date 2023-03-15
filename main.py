from business.serivice_apartemante import ServiceApartamente
from infrastructura.file_repo_apartamente import FileRepoApartamanete
from infrastructura.repo_apartamente import RepoApartamente
from prezentare.consola import UI
from validare.validare_apartament import ValidatorApartament
from teste.teste import Teste

if __name__ == '__main__':
    calea_catre_fisier = "apartamente.txt"
    validator_apartamente = ValidatorApartament()
    repo_apartamente = FileRepoApartamanete(calea_catre_fisier)
    service_apartamente = ServiceApartamente(validator_apartamente, repo_apartamente)
    Teste = Teste()
    Teste.run_all_tests()
    Consola = UI(service_apartamente)
    Consola.run()