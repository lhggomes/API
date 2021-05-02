def cpf_valid(cpf):
    return len(cpf) == 11


def name_valid(name):
    return name.isalpha()


def rg_valid(rg):
    return len(rg) != 9
