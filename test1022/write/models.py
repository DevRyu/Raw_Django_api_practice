from django.db import models

class WriteTable(models.Model):
    article_writer = models.CharField(max_length=20)
    article_title = models.CharField(max_length=50)
    article_content = models.TextField(max_length=500)
    article_updated_at = models.DateTimeField(auto_now=True)
    article_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'WriteTable'
