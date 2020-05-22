from django.conf import settings
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=150, blank=True, null=True)
    text = MarkdownxField()
    tags = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def tags_as_list(self):
        if self.tags is not None:
            return self.tags.split(',')
        else:
            return []
    
    def formatted_markdown(self):
        return markdownify(self.text)
