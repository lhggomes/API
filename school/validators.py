import re


def cpf_valid(cpf):
    """
    Return if the CPF is valid or not
    :param cpf: cpf in a string
    :return: True or False
    """
    return len(cpf) == 11


def name_valid(name):
    """
    Check if the name if valid
    :param name: in a string
    :return: True or False
    """
    return name.isalpha()


def rg_valid(rg):
    """
    Check if the RG provided if valid or not
    :param rg: Check if the RG is valid
    :return: True or False
    """
    return len(rg) != 9


def phone_valid(number):
    """
    Check if the phone number is valid
    :param number: phone number in a string type
    :return: True or False
    """
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'

    return re.findall(model, number)
