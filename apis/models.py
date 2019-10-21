from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=300)
    self_describe = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

class Articles(models.Model):
    article_writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='모임작성자')
    article_title = models.CharField(max_length=50)
    article_content = models.TextField(max_length=500)
    article_updated_at = models.DateTimeField(auto_now=True)
    article_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'articles'

class Comments(models.Model):

    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='댓글작성자')
    comment_text = models.TextField(verbose_name="댓글내용")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    class Meta:
        db_table = 'comments'



