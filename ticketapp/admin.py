from django.contrib import admin
from .models import Movie, Showing, Ticket, Review
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Showing)
class ShowingAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass