from django.db import models

class Comments(models.Model):

    comment_writer = models.CharField(max_length=30)
    comment_text = models.TextField(max_length=500,verbose_name="댓글내용")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    class Meta:
        db_table = 'comments'
