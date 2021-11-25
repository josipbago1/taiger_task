from models.article import Article
from util import data_access
from view import *

from datetime import datetime

db_content = {
    'article': [
        Article(1, 'Title_1', 'Author_1', 'Topic_1', datetime.now()),
        Article(2, 'Title_2', 'Author_1', 'Topic_2', datetime.now()),
        Article(3, 'Title_3', 'Author_3', 'Topic_3', datetime.now()),
        Article(4, 'Title_4', 'Author_4', 'Topic_4', datetime.now()),
    ]
}
data_access.write_db_content(db_content)

print(get_article_by_id(1))
print(get_articles_by_params({
    'author': 'Author_1'
}))
