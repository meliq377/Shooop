from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        index_together = (('id', 'slug'), )

