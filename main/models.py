from django.db import models
from django.urls import reverse

class Memory(models.Model):

    class Context(models.TextChoices):
        MARYAMA = 'M', 'Maryama'
        ARYA = 'A', 'Arya'
        TOGETHER = 'T', 'Together'
        FAMILY = 'F', 'Family'

    # Fields
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/'
                              , default=None)
    video = models.FileField(upload_to='videos/',
                             default=None,
                             blank=True)
    context = models.CharField(max_length=2,
                               choices=Context.choices,
                               default=Context.TOGETHER,
                               blank=True)

    class Meta:
        verbose_name = 'Memory ✨'
        verbose_name_plural = 'Memories ✨'
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} on {self.date}"

    def get_absolute_url(self):
       return reverse("main:memory-detail",
                      args=[self.slug])
