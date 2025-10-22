from routes.app import login


def test_login():
    assert test_login("email, password") == ""
