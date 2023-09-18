#std
import uuid
# 3rd-party
from django.db import models
from UserProfile.models import CustomUser


class Ticket(models.Model):
    STATUS = (
        ('open', 'Open'),
        ('doing', 'Doing'),
        ('closed', 'Closed'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='open')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tickets')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='assigned_tickets')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='Comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='TicketComments')
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}'


class AFile(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='AFiles')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='TicketFiles')
    file = models.FileField(upload_to='project_files/')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}'
