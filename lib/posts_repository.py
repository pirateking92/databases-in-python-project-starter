from lib.posts import Posts

class PostsRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Posts(
                row["id"], row["title"], row["content"], row["views"], row["user_account_id"]
            )
            posts.append(item)
        print(posts)
        return posts