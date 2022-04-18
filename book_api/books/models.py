import uuid

from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Category Name')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Author(BaseModel):
    first_name = models.CharField(max_length=30, verbose_name='Firstname')
    last_name = models.CharField(max_length=30, verbose_name='Lastname')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Bookname')
    description = models.TextField(verbose_name='Description')
    page = models.PositiveIntegerField(verbose_name='Page')
    author = models.ForeignKey(
        "books.Author",
        verbose_name="Author",
        related_name='books',
        on_delete=models.CASCADE
    )
    category = models.ManyToManyField(
        "books.Category",
        verbose_name='Category',
        related_name='books',
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
