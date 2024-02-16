from lib.user_accounts import UserAccounts
from lib.user_accounts_repository import UserAccountsRepository

"""
when we call UserAccountsRepository #all
return a list of all user accounts
"""
def test_get_all_user_accounts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserAccountsRepository(db_connection)

    useraccs = repo.all()

    assert useraccs == [
        UserAccounts(1, 'doyle9214@gmail.com', 'doyle9214'),
        UserAccounts(2, 'test@gmail.com', 'test1234')
    ]