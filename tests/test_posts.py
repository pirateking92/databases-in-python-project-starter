from lib.posts import Posts

def test_posts_constructs():
    posts = Posts(1, "Makers", "Studying a lot", 123, 1)
    assert posts.id == 1
    assert posts.title == "Makers"
    assert posts.content == "Studying a lot"
    assert posts.views == 123
    assert posts.user_account_id == 1
    

def test_posts_format_nicely():
    posts = Posts(1, "Makers", "Studying a lot", 123, 1)
    assert str(posts) == "Posts(1, Makers, Studying a lot, 123, 1)"

def test_posts_are_equal():
    posts1 = Posts(1, "Makers", "Studying a lot", 123, 1)
    posts2 = Posts(1, "Makers", "Studying a lot", 123, 1)
    assert posts1 == posts2