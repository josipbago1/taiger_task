from repository import ArticleRepository

class ArticleService:

    @staticmethod
    def get_article_by_id(article_id):
        return ArticleRepository.find_article_by_id(article_id)

    @staticmethod
    def filter_articles_by_param(articles, param, value):
        return [x for x in articles if x.__dict__[param] == value]

    def get_articles_by_params(self, params):
        all_articles = ArticleRepository.get_all_articles()
        for param, value in params.items():
            all_articles = self.filter_articles_by_param(all_articles, param, value)
        return all_articles
