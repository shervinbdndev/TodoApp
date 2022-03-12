from django.db import models


class TodoDatabase(models.Model):
    title = models.CharField(max_length = 100)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        super(TodoDatabase , self).__str__()
        return self.title
    
    class Meta:
        verbose_name = 'Todo Table'
        verbose_name_plural = 'List Of Todos'