from service import article_service

def get_article_by_id(article_id):
    return article_service.get_article_by_id(article_id)

def get_articles_by_params(params):
    return article_service.get_articles_by_params(params)
