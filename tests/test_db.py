import email
from re import T
import unittest

from pymysql import Time
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='jd@example.com', content='Hello World, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jd2@example.com', content='Hello World :3!')
        assert second_post.id ==2
        first_post = TimelinePost.select().where(id=1)
        assert first_post.name == 'John Doe'
        second_post = TimelinePost.select().where(id=2)
        assert first_post.name == 'Jane Doe'