from lib.user_accounts import UserAccounts
class UserAccountsRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from user_accounts')
        user_accounts = []
        for row in rows:
            item = UserAccounts(
                row["id"], row["email_address"], row["username"]
            )
            user_accounts.append(item)
        return user_accounts