from django.db import models


class Comment(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    text = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    photo = models.ImageField('Фото', blank=True, upload_to="photos/%Y/%m/%d/")
    likes = models.IntegerField('Лайки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
