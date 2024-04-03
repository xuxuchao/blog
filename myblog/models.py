from django.db import models

# Create your models here.

class DocumentContent(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='文章标题', unique=True)
    author = models.CharField(max_length=20, verbose_name='作者', blank=True)
    summary = models.TextField(max_length=500, verbose_name='内容摘要', blank=True)
    add_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', blank=True)
    update_timestamp = models.DateTimeField(auto_now=True, verbose_name='修改时间', blank=True)

    class Meta:
        db_table = 'blog_document_content'
        verbose_name = '博客'
        verbose_name_plural = '博客'