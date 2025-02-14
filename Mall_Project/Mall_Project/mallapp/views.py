from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import shopdetails,manageoffers,categoryfloor

# Create your views here.
def index(self):
    return render(self,'mallapp/index.html')

def adminsignup(self):
    return render(self,'mallapp/adminsignup.html')

def adminlogin(self):
    return render(self,'mallapp/adminlogin.html')




# Admin Manage Shop

def adminmanageshop(self):
    shop = shopdetails.objects.all()
    return render(self,'mallapp/admin-manage-shop.html',{'shop':shop})

def delete_shop(request,id):
    shop = shopdetails.objects.get(id = id)
    shop.delete()
    return redirect('/adminmanageshop')

from mallapp.forms import newshopdetailsupdate
def update_shop(request,id):
    shop = shopdetails.objects.get(id = id)
    form = newshopdetailsupdate(instance = shop)
    return render(request,'mallapp/update.html',{'form':form})

def update_shop(request,id):
    shop = shopdetails.objects.get(id = id)
    form = newshopdetailsupdate(instance = shop)
    if request.method == 'POST':
        form = newshopdetailsupdate(request.POST,instance = shop)
        if form.is_valid():
            form.save()
        return redirect('/adminmanageshop')
    return render(request,'mallapp/update.html',{'form':form})


# Admin Manage Offers

def adminmanageoffers(self):
    if self.method=='POST':
        offershopname=self.POST.get('offershopname')
        offershoplocation=self.POST.get('offershoplocation')
        offercategory=self.POST.get('offercategory')
        offertitle=self.POST.get('offertitle')
        offerdescription=self.POST.get('offerdescription')
        offerstartdate=self.POST.get('offerstartdate')
        offerenddate=self.POST.get('offerenddate')

        offer=manageoffers(offershopname=offershopname, offershoplocation=offershoplocation, offercategory= offercategory, 
                           offertitle=offertitle, offerdescription= offerdescription, offerstartdate=offerstartdate, offerenddate=offerenddate)
        offer.save() 
        messages.success(self,"Offer Shop Details Created Successfully!") 
        # return redirect("/adminmanageoffers")
        offers = manageoffers.objects.all()
        return render(self,'mallapp/admin-manage-offers.html',{'offer' : offers})    
    else:
        # return render(self,'mallapp/admin-manage-offers.html')
            offer = manageoffers.objects.all()
            return render(self,'mallapp/admin-manage-offers.html',{'offer' : offer})

def delete_offer(request,id):
        offerdelete = manageoffers.objects.get(id = id)
        offerdelete.delete()
        return redirect('/adminmanageoffers')

from mallapp.forms import newmanageoffersupdate
def update_offer(request,id):
    offer = manageoffers.objects.get(id = id)
    form = newmanageoffersupdate(instance = offer)
    return render(request,'mallapp/offerupdate.html',{'form':form})

def update_offer(request,id):
    offer = manageoffers.objects.get(id = id)
    form = newmanageoffersupdate(instance = offer)
    if request.method == 'POST':
        form = newmanageoffersupdate(request.POST,instance = offer)
        if form.is_valid():
            form.save()
        return redirect('/adminmanageoffers')
    return render(request,'mallapp/offerupdate.html',{'form':form})




# Admin Manage Category & Floor

def adminmanagecategoryfloor(self):
    if self.method=='POST':
        category=self.POST.get('category')
        floor=self.POST.get('floor')
        cf=categoryfloor(category=category, floor=floor)
        cf.save()
        messages.success(self,"Category & Floor Details Created Successfully!")
        # return redirect("/adminmanagecategoryfloor")
        insert=categoryfloor.objects.all()
        return render(self,'mallapp/admin-manage-category & floor.html',{'insert':insert})

    else:
        insert=categoryfloor.objects.all()
        return render(self,'mallapp/admin-manage-category & floor.html',{'insert':insert})    
        
def delete_cf(request,id):
        cfdelete = categoryfloor.objects.get(id = id)
        cfdelete.delete()
        return redirect('/adminmanagecategoryfloor')




# Admin Create Shop

def admincreateshop(self):
    if self.method=='POST':
        shopname=self.POST.get('shopname')
        shoplocation=self.POST.get('shoplocation')
        shopcategory=self.POST.get('category')
        shopdescription=self.POST.get('shopdescription')

        shop=shopdetails(shopname=shopname,shoplocation=shoplocation,shopcategory=shopcategory,shopdescription=shopdescription)
        shop.save() 
        messages.success(self,"Shop Details Created Successfully!") 
        return redirect("/admincreateshop")
        
    else:    
        return render(self,'mallapp/admin-create-shop.html')



def admincategorywisedetails(self):
    return render(self,'mallapp/admin category wise details.html')

def user(self):
    return render(self,'mallapp/user.html')




# User View Shop

def userviewshop(self):
    usershop = shopdetails.objects.all()
    return render(self,'mallapp/user-view-shop.html',{'usershop':usershop}  )




# User Shop Wise Offers

def usershopwiseoffers(self):
    offer=manageoffers.objects.all()
    return render(self,'mallapp/user-shop-wise-offers.html',{'offer':offer})



# user list of shop

def userlistofshop(self):
    usershop = shopdetails.objects.all()
    return render(self,'mallapp/user-list-of-shop.html',{'usershop':usershop})




# User Floor Wise

def userfloorwise(self):
    floors = categoryfloor.objects.all().order_by("floor") 
    return render(self,'mallapp/user-floor-wise.html',{'floors':floors})




#  Sigup
def sigup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('/adminsignup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('/adminsignup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('/adminsignup')

        user = User.objects.create_user(username=username, password=password1,email=email)
        user.save()
        messages.success(request, "User registered successfully!")
        return redirect('/adminlogin')

    else:
        return render(request, 'mallapp/adminsignup.html')


# Login

def login(self):
    if self.method== 'POST':
        username = self.POST.get('username')
        password = self.POST.get('password')
        secretkey = self.POST.get('secretkey')

        if secretkey != '31052000':
            messages.info(self, "Secret key is incorrect!")
            return redirect("/adminlogin")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(self, user)
            return redirect("/admincategorywisedetails")
        else:
            messages.info(self,'Invalid credentials!')
            return redirect('/adminlogin')

    else:    
        return render(self,'mallapp/adminlogin.html')