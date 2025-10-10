email = input("email: ")
tld = email[email.rfind(".") + 1 :]
valid_tlds = ["com", "info", "org", "net", "edu"]
if tld in valid_tlds:
    print("tls is valid")
