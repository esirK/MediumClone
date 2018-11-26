from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404

from .models import Article, Author
from .serializers import ArticleSerializer

class ArticleView(CreateAPIView, ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)
