from django.db import models


class Category(models.Model):
    title = models.CharField('título', max_length=100, unique=True)
    type = models.CharField('tipo', max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField('título', max_length=100, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='categoria',
        related_name='categories',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return f'{self.title}'
