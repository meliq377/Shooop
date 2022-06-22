from django.db import models
from django.urls import reverse


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('slug', 'parent',)
        ordering = ['id']
        verbose_name ='Категория'
        verbose_name_plural = 'Категотии'

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Brand(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Product(models.Model):
    title = models.CharField(max_length=100,)
    slug = models.SlugField(max_length=100, verbose_name='url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Products')
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='Products')
    brand = models.ForeignKey(Brand, related_name='Products', on_delete=models.CASCADE)
    availability = models.CharField(max_length=100)
    condition = models.CharField(max_length=100, blank=True)
    web_id = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'), )


class Library_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Library_Image')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.image
