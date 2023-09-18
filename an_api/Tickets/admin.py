from django.contrib import admin
# local
from Tickets.models import Ticket, AFile, Comment


admin.site.register(Ticket)
admin.site.register(AFile)
admin.site.register(Comment)
