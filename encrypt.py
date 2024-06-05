import bcrypt

passwd = "b’P@ssw0rd#321’"
bytes= passwd.encode("utf-16")
salt = bcrypt.gensalt()
salted = bcrypt.hashpw(bytes,salt)
password="b’P@ssw0rd#321’"
pass_bytes=password.encode("utf-16")
print(salt)
print(salted, "This one is salted")
checkd= bcrypt.checkpw(pass_bytes,salted)
print(checkd)
