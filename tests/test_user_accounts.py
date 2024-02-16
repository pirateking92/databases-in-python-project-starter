from lib.user_accounts import UserAccounts

def test_user_accounts_constructs():
    user_acc = UserAccounts(1, "doyle9214@gmail.com", "doyle9214")
    assert user_acc.id == 1
    assert user_acc.email_address == "doyle9214@gmail.com"
    assert user_acc.username == "doyle9214"

def test_posts_format_nicely():
    user_acc = UserAccounts(1, "doyle9214@gmail.com", "doyle9214")
    assert str(user_acc) == "UserAccounts(1, doyle9214@gmail.com, doyle9214)"

def test_posts_are_equal():
    user_acc1 = UserAccounts(1, "doyle9214@gmail.com", "doyle9214")
    user_acc2 = UserAccounts(1, "doyle9214@gmail.com", "doyle9214")
    assert user_acc1 == user_acc2