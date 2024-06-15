from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(max_length=100)
    parent_category = models.ForeignKey('self', default=None, related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    is_sub = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
