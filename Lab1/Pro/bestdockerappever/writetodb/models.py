from django.db import models


class BootRecord(models.Model):
    """
    мы запустили джангу!
    """

    copy_paste = models.CharField(max_length=1100, verbose_name='Копипаста на вставку', blank=True, null=True)
    date_add = models.DateField(auto_now=True)

    def __str__(self):
        return self.copy_paste
