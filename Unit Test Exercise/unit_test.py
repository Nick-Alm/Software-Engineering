from user import user
def test_user(firstName, lastName, email, user):
    print("testing user")
    assert(user.first == firstName)
    assert(user.last == lastName)
    assert(user.email == email)
def test_create(firstName, lastName, email):
    print("testing create")
    user1 = user(firstName, lastName, email)
    test_user(firstName, lastName, email, user1)
def test_userlist(list):
    pass

# print("hello world")

first = "Nick"
last = "Alm"
email = "alm.nicholas.2013@gmail.com"

test_create(first, last, email)
# test_user()

userlist = {
    {"john", "smith", "john.smith@unco.edu"}
    {"jane", "doe", "jane.doe@unco.edu"}
    {"david", "pumpkins", "david.pumpkins@unco.edu"}
    }

# for i in
