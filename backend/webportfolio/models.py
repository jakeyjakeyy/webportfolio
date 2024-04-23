from django.db import models


class GithubInfoCache(models.Model):
    repo = models.CharField(max_length=100)
    language_percentages = models.JSONField()
    last_active = models.DateTimeField(null=True)
    cache_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.repo} - {self.cache_time}"
