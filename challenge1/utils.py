def extract_numbers(s):
    return ''.join([n for n in s if n.isdigit()])

def format_cpf(cpf):
    return '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

def format_cnpj(cnpj):
    return '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
