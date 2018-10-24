from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        import pdb; pdb.set_trace()
        title = article.get('title')
        description = article.get('description')
        body = article.get('body')
        author_id = article.get('author_id')

        # Create an article from the above data
        Article.objects.create(
            title=title,
            description=description,
            body=body,
            author_id=author_id
        )

        return Response({"success": "Article {} created successfully".format(title)})


