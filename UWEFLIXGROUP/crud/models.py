from django.db import models
import uuid

# Account Manager Models - Samuel

class Customer(models.Model):
    cid = models.CharField(max_length=4)
    ctitle = models.CharField(max_length=4)
    cname = models.CharField(max_length=255)
    cclub = models.CharField(max_length=255)
    # ccno = models.CharField(max_length=255)
    # ccexp = models.CharField(max_length=255)
    cdiscount = models.BooleanField(default=False)

def __str__(self):
        return self.cname

# Club Rep Models - Owain

# class Club(models.Model):
#     club_number = models.IntegerField()
#     name = models.CharField(max_length=4)
#     street = models.CharField(max_length = 50)
#     street_num = models.IntegerField()
#     city = models.CharField(max_length=50)
#     post_code = models.CharField(max_length=8)
#     landline_no = models.CharField(max_length=15)
#     mobile_no = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name
    
# class Representative(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     dob = models.DateField()

# Movie Models - Anushka

# class Movie(models.Model):
#     movie_title = models.CharField(max_length=150)
#     movie_duration = models.PositiveIntegerField()
#     movie_age_rating = models.PositiveIntegerField()
#     movie_description = models.TextField()
#     ##Something for image here maybe
    
# class MovieShowings(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     movie_date = models.DateField()
#     movie_time = models.TimeField()
#     movie_screen = models.PositiveIntegerField() 
#     movie_seats = models.PositiveIntegerField() 

# class Ticket(models.Model):
#     ticket_name = models.CharField(max_length=100)
#     ticket_price = models.DecimalField(max_digits=6)

# class NoOfTickets(models.Model):
#     movie_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     ticket_quantity = models.PositiveIntegerField()

# class MovieBooking(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField() 
#     showing = models.ForeignKey(MovieShowings, on_delete=models.CASCADE)
#     no_of_tickets = models.ManyToManyField(NoOfTickets) 
    
# Film Models - Anushka

# class Film(models.Model):

#     RATINGS = (('U', 'U'), ('PG', 'PG'), ('12A', '12A'), ('12', '12'), ('15', '15'), ('18', '18'))

#     title = models.CharField(max_length=32)
#     age_rating = models.CharField(max_length=5, choices=RATINGS)
#     duration = models.IntegerField()
#     description = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title
    
# class Screen(models.Model):
#     screen_id = models.AutoField(primary_key=True)
#     capacity = models.IntegerField()

#     def __str__(self):
#         return "Screen " + str(self.screen_id) + " (Capacity: " + str(self.capacity) + ")"
    
# class Showing(models.Model):
#     film = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
#     screen = models.ForeignKey(Screen, null=True, on_delete=models.SET_NULL)
#     time = models.DateTimeField(default=timezone.now)