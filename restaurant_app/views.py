from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from . import models
from django.templatetags.static import static
from .models import Order
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')
        user = User.objects.create(
            username=username,
            password=make_password(password)
        )
        messages.success(request, "Account created successfully! Please log in.")
        return render(request, 'signup.html')
    return render(request, 'signup.html')
   

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')



def main(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            messages.error(request,'User not exist!')
            return render(request, 'main.html')
    return render(request, 'main.html')



def home(request):
    if request.user.is_anonymous:
        return redirect('/main')
    return render(request, 'base.html')

@login_required
def contact(request):
   if request.method=="POST":
       print('post')
       name=request.POST.get('name')
       email=request.POST.get('email')
       number=request.POST.get('number')
       content=request.POST.get('content')
       if name and email and number and content:
            contact_entry = Contact(name=name, email=email, number=number, content=content)
            contact_entry.save()
            messages.success(request, "Thank You for contacting me!! Your message has been saved")
       else:
            messages.error(request, "Please fill in all fields.")
       return redirect('contact')  
   return render(request, 'contact.html')

@login_required
def gallery(request):
    return render(request, 'gallery.html')

@login_required
def menu(request):
    menu_items = [
        {"name": "Margherita Pizza", "description": "Classic cheese & tomato pizza", "price": 8.99,
         "image_url": static('images/Margherita pizza.jpeg')},
        {"name": "Veggie Burger", "description": "Grilled veggie patty with toppings", "price": 7.49,
         "image_url": static('images/Veggie burger.jpg')},
        {"name": "Grilled Chicken", "description": "Served with sautéed vegetables", "price": 10.99,
         "image_url":  static('images/Grilled chicken.jpg')},
        {"name": "Spaghetti Bolognese", "description": "Pasta in beef tomato sauce", "price": 9.50,
         "image_url": static('images/Spaghetti Bolognese.jpg')},
        {"name": "Paneer Tikka", "description": "Grilled cottage cheese chunks", "price": 8.25,
         "image_url": static('images/Paneer Tikka.jpg')},
        {"name": "Sushi Platter", "description": "Assorted fresh sushi rolls", "price": 13.95,
         "image_url": static('images/Sushi Platter.jpg')},
        {"name": "Caesar Salad", "description": "Crisp romaine with creamy dressing", "price": 6.99,
         "image_url": static('images/Caesar Salad.jpg')},
        {"name": "Fish & Chips", "description": "Classic crispy fried fish", "price": 9.99,
         "image_url": static('images/Fish & Chips.jpg')},
        {"name": "Tacos", "description": "Mexican style soft tacos", "price": 8.00,
         "image_url": static('images/Tacos.jpg')},
        {"name": "Cappuccino", "description": "Rich espresso with steamed milk", "price": 3.50,
         "image_url": static('images/Cappuccino.jpg')},
        {"name": "Iced Latte", "description": "Chilled espresso with milk", "price": 3.75,
         "image_url": static('images/Iced Latte.jpg')},
        {"name": "Mango Smoothie", "description": "Fresh mango blended drink", "price": 4.50,
         "image_url": static('images/Mango Smoothie.jpg')},
        {"name": "Lemonade", "description": "Refreshing lemon drink", "price": 2.50,
         "image_url": static('images/Lemonade.jpg')},
        {"name": "Masala Chai", "description": "Spiced Indian tea", "price": 2.25,
         "image_url": static('images/Masala Chai.jpg')},
        {"name": "Hot Chocolate", "description": "Creamy and rich cocoa drink", "price": 3.00,
         "image_url":static('images/Hot Chocolate.jpg')},
        {"name": "Orange Juice", "description": "Freshly squeezed orange juice", "price": 3.25,
         "image_url": static('images/Orange Juice.jpg')},
        {"name": "Cold Coffee", "description": "Chilled coffee with cream", "price": 3.60,
         "image_url": static('images/Cold Coffee.jpg')},
        {"name": "Mint Mojito", "description": "Mocktail with mint & lime", "price": 3.75,
         "image_url": static('images/Mint Mojito.jpg')},
        {"name": "Fruit Salad", "description": "Mixed seasonal fruit bowl", "price": 4.99,
         "image_url": static('images/Fruit Salad.jpg')},
        {"name": "Bottled Water", "description": "500ml purified water", "price": 1.00,
         "image_url": static('images/Bottled Water.jpg')},
    ]
    return render(request, 'menu.html', {'menu_items': menu_items})

@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your table has been reserved!")
            return redirect('reserve')
    else:
        form = ReservationForm()

    return render(request, 'reserve.html', {'form': form})

@login_required
def place_order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        Order.objects.create(name=name, price=price)
        messages.success(request, f"Order placed for {name}!")
        return redirect('/menu') 

    return redirect('/menu')





