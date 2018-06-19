from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.urls import reverse
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.schema_name

class Domain(DomainMixin):
    pass


class Task(models.Model):
    name = models.TextField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return "%s (done)" % self.name
        else:
            return self.name
    def get_absolute_url(self):
        return reverse('list')
