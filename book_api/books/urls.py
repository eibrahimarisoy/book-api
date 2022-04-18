from books.views import AuthorViewSet, BookViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

app_name = "books"

router = DefaultRouter()
router.register('books', BookViewSet, basename="books")
router.register('authors', AuthorViewSet, basename="authors")
router.register('categories', CategoryViewSet, basename="categories")

urlpatterns = router.urls
