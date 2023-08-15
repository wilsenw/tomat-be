from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(
        to=Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
