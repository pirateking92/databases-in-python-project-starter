from lib.posts_repository import PostsRepository
from lib.posts import Posts

"""
when we call #all
get a list of all posts
"""

def test_get_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = PostsRepository(db_connection)

    posts = repo.all()

    assert posts == [
        Posts(1, 'Makers', 'Studying a lot', 123, 1),
        Posts(2, 'Test', 'Test to test', 54321, 1)
    ]
