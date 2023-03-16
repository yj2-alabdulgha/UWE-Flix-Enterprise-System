from django.db import models
import uuid

# Account Manager Models - Samuel

class Customer(models.Model):
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ctitle = models.CharField(max_length=4)
    cname = models.CharField(max_length=100)
    cclub = models.CharField(max_length=100)
    ccno = models.CharField(max_length=30)
    ccexp = models.CharField(max_length=6)
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


### Anushka Models Update -->


## There is two ways to do abstract user so need to decide which is the bse for us the first one is the one down below:
#class User(AbstractUser):
#  USER_TYPE_CHOICES = (
#      (1, 'customer'),
#      (2, 'accountmanager'),
#      (3, 'clubrepresentative'),
#      (4, 'cinemamanager'),
#    ) 

#  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

#  The second one is here:
#class User(AbstractUser):
#    is_customer = models.BooleanField('student status', default=False)
#    is_accountmanager = models.BooleanField('teacher status', default=False)
#    is_cinemamanager = models.BooleanField('teacher status', default=False)
#    is_clubrepresentative = models.BooleanField('teacher status', default=False)


#class Customer(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#    first_name = models.CharField(max_length=20)
#    last_name = models.CharField(max_length=20)
#    dob = models.DateField()
#    email = models.EmailField() 
#    creditdetails = models.FloatField(default=0.00)

#class CustomerMoneyTransactions(models.Model): 
#   customer = models.ForeignKey(Customer, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT)  
#   date = models.DateField()  
#   cost = models.FloatField()  
#   payment_done = models.BooleanField()  
#   cancel_booking = models.BooleanField(default=False)

#class Club(models.Model):
#     club_number = models.IntegerField()
#     name = models.CharField(max_length=4)
#     street = models.CharField(max_length = 50)
#     street_num = models.IntegerField()
#     city = models.CharField(max_length=50)
#     post_code = models.CharField(max_length=8)
#     landline_no = models.CharField(max_length=15)
#     mobile_no = models.CharField(max_length=15)


#class adminUser(models.Model):
#    adminuser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#    email = models.EmailField() 
#    password = models.CharField(max_length = 15)

#class Film(models.Model):
#    title = models.CharField(max_length=100)
#    age_rating = models.CharField(max_length=3)
#    """Age Ratings:
#        - U
#        - PG
#        - 12
#        - 12A
#        - 15
#        - 18"""
#    duration = models.CharField(max_length=3)
#    discription = models.CharField(max_length=500)
#    filmimage = models.ImageField()

#class Screen(models.Model):
#    roomcapacity = models.IntegerField()
#    something for covid restriction here maybe??

#class FilmShowings(models.Model)
#    movie = models.ForeignKey(Film, on_delete=models.CASCADE)
#    moviescreen = models.ForeignKey(Screen, default=1, on_delete=models.CASCADE)
#    film_date = movie_date = models.DateField()
#    maybe a time field as well??
#    ticketsremaining = models.IntegerField(default=150) ??

#class BookingInformation(models.Model):  
#    payment = models.ForeignKey(Transaction, default=1, on_delete=models.SET_DEFAULT)
#    filmshowings = models.ForeignKey(FilmShowing, default=1, on_delete=models.SET_DEFAULT)  
#    type = models.CharField(max_length=10)
#    ticket_quantity = models.PositiveIntegerField()

## Maybe a model for prices for diiferent groups of people. 

