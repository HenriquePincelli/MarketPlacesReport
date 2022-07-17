import re
import jaro


# Validation of E-mail
def validate_domain(email_1, email_2):
    valid_domains = ["gmail.com", "gmail.com.br", "hotmail.com", "hotmail.com.br"]

    # Check if the two e-mails have domains
    try:
        domain_1 = email_1.split("@")[1]
    except IndexError:
        return "Por gentileza, digite um domínio para o primeiro e-mail."
    try:
        domain_2 = email_2.split("@")[1]
    except IndexError:
        return "Por gentileza, digite um domínio para o segundo e-mail."

    # Check if the domains are in the valid_domains list
    if domain_1 in valid_domains:
        domain_in_list = True
    else:
        return """O domínio do primeiro e-mail é inválido.
Observação: Só serão aceitos e-mails com domínio de """ + "'gmail' ou 'hotmail'." 

    if domain_2 in valid_domains:
        domain_in_list = True
    else:
        return """O domínio do segundo e-mail é inválido.
Observação: Só serão aceitos e-mails com domínio de """ + "'gmail' ou 'hotmail'."


    # Check if the two domains are the same
    domains_validation = jaro.jaro_winkler_metric(email_1, email_2)
    if domains_validation == 1:
        return True
    else:
        return """Os endereços não correspondem.
Observação: Os endereços devem ser exatamente os mesmos."""

# Validation of password
def validate_password(password_1, password_2):
    password_validation = jaro.jaro_winkler_metric(password_1, password_2)
    if password_validation == 1:
        return True
    else:
        return False