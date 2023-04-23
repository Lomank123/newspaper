class GetArticleService:
    """Fetch article(s) from outer service."""

    def filter_by(self, **kwargs):
        return {'data': {'id': 1, 'title': 'default'}}

    def get_list(self, **kwargs):
        articles = [
            {'id': 1, 'title': 'default'},
            {'id': 2, 'title': 'default 2'},
        ]
        return {'data': articles}


# TODO: Perhaps you should move it to the above service
class CreateArticleService:
    """Create article using outer service."""

    def create(self, **kwargs):
        return {'data': {'id': 3, 'title': 'new default 3'}}
