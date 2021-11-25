from util import data_access

class ArticleRepository:

    @staticmethod
    def find_article_by_id(article_id):
        return data_access.find_object_by_id(article_id, 'article')

    @staticmethod
    def get_all_articles():
        return data_access.get_all_objects('article')
