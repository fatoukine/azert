special_characters = "\"!@#$%^&*()-+?_=,<>/'"
blocked = ["qwertyuiop", "azertyuiop", "123456789", "password", "abcdefg"]


def checkPwd(pwd):
    res = [True]

    if not(10 <= len(pwd) <= 25):
        res.append({"type": "len", "message": "Length must be between 10 and 25"})
        res[0] = False

    if not(any(c for c in pwd if c.isdigit())):
        res.append({"type": "digit", "message": "Must contains digits"})
        res[0] = False

    if not(any(c in special_characters for c in pwd)):
        res.append({"type": "special", "message": "Must contains special characters"})
        res[0] = False

    if not(any(c for c in pwd if c.isupper())):
        res.append({"type": "upper", "message": "Must contains one uppercase"})
        res[0] = False

    if not(any(c for c in pwd if c.islower())):
        res.append({"type": "lower", "message": "Must contains one uppercase"})
        res[0] = False

    if any(word for word in blocked if word.lower() in pwd.lower()):
        res.append({"type": "common", "message": "Too common"})
        res[0] = False

    return res


if __name__ == '__main__':
    mdp = input(f"Saisir un mot de passe : ")
    print(checkPwd(mdp))
