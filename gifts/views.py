from django.shortcuts import render
from .models import Destination,firstvalue,RegisteredForms,OrderForm
from .forms import FormRegisterForm
from django.core.mail import send_mail


# Create your views here.

def detail():
    fir = firstvalue()
    fir.title='Ancient statue'
    fir.img='5'
    fir.price='₹699'
    fir.oldprice='₹799'
    fir.href='simple11'

    fir1 = firstvalue()
    fir1.title='Baby statue'
    fir1.img='2a'
    fir1.price='₹899'
    fir1.oldprice='₹1099'
    fir1.href='simple12'

    fir2 = firstvalue()
    fir2.title='Buddha statue'
    fir2.img='2'
    fir2.price='₹1299'
    fir2.oldprice='₹1349'
    fir2.href='simple13'

    fir3 = firstvalue()
    fir3.title='baby buddha'
    fir3.img='3a'
    fir3.price='₹799'
    fir3.oldprice='₹899'
    fir3.href='simple14'


    first = [fir,fir1,fir2,fir3]
    return first

def detail2():
    fir = firstvalue()
    fir.title='Steel toys'
    fir.img='27'
    fir.price='₹299'
    fir.oldprice='₹399'
    fir.href='simple21'

    fir1 = firstvalue()
    fir1.title='Alloy toys'
    fir1.img='18'
    fir1.price='₹999'
    fir1.oldprice='₹1099'
    fir1.href='simple22'

    fir2 = firstvalue()
    fir2.title='wooden toys'
    fir2.img='21'
    fir2.price='₹499'
    fir2.oldprice='₹649'
    fir2.href='simple23'

    fir3 = firstvalue()
    fir3.title='cycle lampstand'
    fir3.img='15'
    fir3.price='₹399'
    fir3.oldprice='₹499'
    fir3.href='simple24'


    second = [fir,fir1,fir2,fir3]
    return second

    
def detail3():
    fir = firstvalue()
    fir.title='Guitar statue'
    fir.img='25'
    fir.price='₹2799'
    fir.oldprice='₹3000'
    fir.href='simple31'

    fir1 = firstvalue()
    fir1.title='Couple statue'
    fir1.img='23'
    fir1.price='₹599'
    fir1.oldprice='₹699'
    fir1.href='simple32'

    fir2 = firstvalue()
    fir2.title='Friends toys'
    fir2.img='11'
    fir2.price='₹499'
    fir2.oldprice='₹699'
    fir2.href='simple33'

    fir3 = firstvalue()
    fir3.title='golden camel'
    fir3.img='12'
    fir3.price='₹799'
    fir3.oldprice='₹899'
    fir3.href='simple34'

    third = [fir,fir1,fir2,fir3]
    return third

    
def detail4():
    fir = firstvalue()
    fir.title='Wooden wolf'
    fir.img='1a'
    fir.price='₹499'
    fir.oldprice='₹649'
    fir.href='simple41'

    fir1 = firstvalue()
    fir1.title='Tabla ganesh'
    fir1.img='17'
    fir1.price='₹999'
    fir1.oldprice='₹1099'
    fir1.href='simple42'

    fir2 = firstvalue()
    fir2.title='Baby toys'
    fir2.img='19'
    fir2.price='₹499'
    fir2.oldprice='₹599'
    fir2.href='simple43'

    fir3 = firstvalue()
    fir3.title='Baby toys'
    fir3.img='20'
    fir3.price='₹499'
    fir3.oldprice='₹599'
    fir3.href='simple44'


    fourth = [fir,fir1,fir2,fir3]
    return fourth

    
def detail5():
    fir = firstvalue()
    fir.title='Teddy(pink)'
    fir.img='35'
    fir.price='₹499'
    fir.oldprice='₹699'
    fir.href='simple51'

    fir1 = firstvalue()
    fir1.title='Teddy(Brown)'
    fir1.img='33'
    fir1.price='₹799'
    fir1.oldprice='₹899'
    fir1.href='simple52'

    fir2 = firstvalue()
    fir2.title='Teddy(Sandal)'
    fir2.img='31'
    fir2.price='₹999'
    fir2.oldprice='₹1099'
    fir2.href='simple53'

    fir3 = firstvalue()
    fir3.title='Teddy(Red)'
    fir3.img='32'
    fir3.price='₹699'
    fir3.oldprice='₹799'
    fir3.href='simple54'


    fifth = [fir,fir1,fir2,fir3]
    return fifth

def detail6():
    fir = firstvalue()
    fir.title='Flowervase frame'
    fir.img='38'
    fir.price='₹499'
    fir.oldprice='₹699'
    fir.href='simple61'

    fir1 = firstvalue()
    fir1.title='buddha frame'
    fir1.img='36'
    fir1.price='₹599'
    fir1.oldprice='₹749'
    fir1.href='simple62'

    fir2 = firstvalue()
    fir2.title='Oilpaint frame'
    fir2.img='37'
    fir2.price='₹1199'
    fir2.oldprice='₹1399'
    fir2.href='simple63'

    fir3 = firstvalue()
    fir3.title='Flowervase frame'
    fir3.img='40'
    fir3.price='₹499'
    fir3.oldprice='₹699'
    fir3.href='simple64'


    sixth = [fir,fir1,fir2,fir3]
    return sixth

def simplesection1():
    first=detail()
    return first

def simplesection2():
    first=detail2()
    return first

def simplesection3():
    first=detail3()
    return first

def simplesection4():
    first=detail4()
    return first

def simplesection5():
    first=detail5()
    return first

def simplesection6():
    first=detail6()
    return first
def index(request):
    first=detail()
    second=detail2()
    return render(request,'index.html',{'first':first,'second':second})

def dest(title,image,order,price,oldprice):
    dests = Destination()
    dests.title=title
    dests.image=image
    dests.order=order
    dests.price=price
    dests.oldprice=oldprice
    return dests

def simple11(request):
    simplesection=simplesection1()
    dests = dest('Ancient statue','5','order11','₹699','₹799')
    
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple12(request):
    simplesection=simplesection1()
    
    dests=dest('Baby statue','2a','order12','₹899','₹1099')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple13(request):
    simplesection=simplesection1()
    dests=dest('Buddha statue','2','order13','₹1299','₹1349')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple14(request):
    simplesection=simplesection1()
    dests=dest('Baby statue','3a','order14','₹799','₹899')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple21(request):
    simplesection=simplesection2()
    dests=dest('Steel toys','27','order21','₹299','₹399')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple22(request):
    simplesection=simplesection2()
    dests=dest('Alloy toys','18','order22','₹999','₹1099')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple23(request):
    simplesection=simplesection2()
    dests=dest('Wooden toys','21','order23','₹599','₹649')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple24(request):
    simplesection=simplesection2()
    dests=dest('cycle lampstand','15','order24','₹399','₹499')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple31(request):
    simplesection=simplesection3()
    dests=dest('Guitar statue','25','order31','₹2799','₹3000')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple32(request):
    simplesection=simplesection3()
    dests=dest('Couple statue','23','order32','₹599','₹699')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple33(request):
    simplesection=simplesection3()
    dests=dest('Friends toys','11','order33','₹499','₹699')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple34(request):
    simplesection=simplesection3()
    dests=dest('golden camel','12','order34','₹799','₹899')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})



def simple41(request):
    simplesection=simplesection4()
    dests=dest('Wooden Wolf','1a','order41','₹499','₹649')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple42(request):
    simplesection=simplesection4()
    dests=dest('Tabla Ganesh','17','order42','999','₹1099')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple43(request):
    simplesection=simplesection4()
    dests=dest('Baby toys','19','order43','₹499','₹599')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple44(request):
    simplesection=simplesection4()
    dests=dest('Baby toys','20','order44','₹499','₹599')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple51(request):
    simplesection=simplesection5()
    dests=dest('Teddy(pink)','35','order51','₹499','₹699')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple52(request):
    simplesection=simplesection5()
    dests=dest('Teddy(brown)','33','order52','₹799','₹899')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple53(request):
    simplesection=simplesection5()
    dests=dest('Teddy(Sandal)','31','order53','₹999','₹1099')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple54(request):
    simplesection=simplesection5()
    dests=dest('Teddy(red)','32','order54','₹699','₹799')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple61(request):
    simplesection=simplesection6()
    dests=dest('Flowervase frame','38','order61','₹499','₹699')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple62(request):
    simplesection=simplesection6()
    dests=dest('Buddha Frame','36','order62','₹599','₹749')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple63(request):
    simplesection=simplesection6()
    dests=dest('OilPainting Frame','37','order63','₹1199','₹1399')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def simple64(request):
    simplesection=simplesection6()
    dests=dest('Flowervase Frame','40','order64','₹499','₹699')
    return render(request,'simple.html',{'dests':dests,'simplesection':simplesection})

def first(request):

   
    first=detail()
    second=detail2()
    third=detail3()
    fourth=detail4()
    fifth=detail5()
    sixth=detail6()
    val='0'
    check='0'
    

    if request.method == 'POST':
        username= request.POST['uname']
        emailid = request.POST['Email']
        password = request.POST['psw']
        
    
        

        
        form=RegisteredForms(uname=username,Email=emailid,psw=password)

        all_data= RegisteredForms.objects.all()
            
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            if (RegisteredForms.objects.filter(psw=password)).exists():
                send_mail(
                    'GIFTS SHOP',
                    'Dear {name} \nthanks for Login our shop website '.format(name=username),
                    'harimukesh821@gmail.com',
                    [emailid],
                    fail_silently=False)
                val='1'
                check='1'
                return render(request,'first.html',{'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth,'sixth':sixth,'val':val,'check':check})
            else:
                check='2'
            print("user not created")
            return render(request,'first.html',{'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth,'sixth':sixth,'val':val,'check':check})

                
        else:
                
            check='3'
            print("user not created")
            return render(request,'first.html',{'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth,'sixth':sixth,'val':val,'check':check})
               
    else:
        return render(request,'first.html',{'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth,'sixth':sixth,'val':val,'check':check})
    
        

  
    
def mail(name,product,emailid,phoneno,address):
    send_mail(
                'GIFTS SHOP',
                'Dear {name}, \nThanks for ordering the product {product} in our shop \nConfirmation of your order \nYour phone: {phoneno} \nYour address: {address} \nPlease verify it \nYour order will deliver in within 12 days '
                .format(name=name,product=product,phoneno=phoneno,address=address),
                'harimukesh821@gmail.com',
                [emailid],
                fail_silently=False)




def signup(request):

    first=detail()
    second=detail2()
    third=detail3()
    fourth=detail4()
    fifth=detail5()
    sixth=detail6()
    val='0'
    check='0'
    if request.method == 'POST':
        username= request.POST['uname']
        phone=request.POST['phonenum']
        emailid = request.POST['Email']
        password = request.POST['psw']
        confirmpassword = request.POST['psw2']
        
        url='127.0.0.1:8000/simple'
        

        
        form=RegisteredForms(uname=username,phone=phone,Email=emailid,psw=password,psw2=confirmpassword)
    
        if password == confirmpassword:
            if (RegisteredForms.objects.filter(Email=emailid)).exists():
                check='2'
                print("Email already exists")
                return render(request,'signup.html',{'val':val,'check':check})
                
            else:

                form.save()
                print('user created')
                send_mail(
                    'GIFTS SHOP',
                    'Dear {name} \nthanks for Login our shop website '.format(name=username),
                    'harimukesh821@gmail.com',
                    [emailid],
                    fail_silently=False)
                val='1'
                check='1'
                return render(request,'first.html',{'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth,'sixth':sixth,'val':val,'check':check})
                
        
        else:
                
            check='3'
            print("Email already exits")
            return render(request,'signup.html',{'val':val,'check':check})
               
    else:
        return render(request,'signup.html')
        
def login2(request):

    first=detail()
    second=detail2()
    third=detail3()
    fourth=detail4()
    fifth=detail5()
    sixth=detail6()


    val='0'
    check='0'
    

    if request.method == 'POST':
        username= request.POST['uname']
        emailid = request.POST['Email']
        password = request.POST['psw']
        
        
        form=RegisteredForms(uname=username,Email=emailid,psw=password)
            
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            if (RegisteredForms.objects.filter(psw=password)).exists():
                send_mail(
                    'GIFTS SHOP',
                    'Dear {name} \nthanks for Login our shop website '.format(name=username),
                    'harimukesh821@gmail.com',
                    [emailid],
                    fail_silently=False)
                val='1'
                check='1'
                return render(request,'first.html',{'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth,'sixth':sixth,'val':val,'check':check})
            else:
                check='2'
            print("user not created")
            return render(request,'login.html',{'val':val,'check':check})

                
        else:
                
            check='3'
            print("user not created")
            return render(request,'login.html',{'val':val,'check':check})
               
    else:
        return render(request,'login.html',{'val':val,'check':check})


#---------------order pages---------------------------
def destsorder(title,image,price,oldprice):
    dests = Destination()
    dests.title=title
    dests.image=image
    dests.price=price
    dests.oldprice=oldprice
    return dests

def order11(request):
    first=detail()
    second=detail2()
    dests=destsorder('Ancient statue','5','₹699','₹799')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})




def order12(request):
    first=detail()
    second=detail2()
    dests=destsorder('Baby statue','2a','₹899','₹1099')
    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order13(request):
    first=detail()
    second=detail2()
    dests=destsorder('Buddha Statue','2','₹1299','₹1349')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order14(request):
    first=detail()
    second=detail2()
    dests=destsorder('Baby Buddha','3a','₹799','₹899')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order21(request):
    first=detail()
    second=detail2()
    dests=destsorder('Steel toys','27','₹299','₹399')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order22(request):
    first=detail()
    second=detail2()
    dests=destsorder('Alloy toys','18','₹999','₹1099')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order23(request):
    first=detail()
    second=detail2()
    dests=destsorder('Wooden toys','21','₹499','₹649')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order24(request):
    first=detail()
    second=detail2()
    dests=destsorder('Cycle lampstand','15','₹399','₹499')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order31(request):
    first=detail()
    second=detail2()
    dests=destsorder('Guitar statue','25','₹2799','₹3000')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order32(request):
    first=detail()
    second=detail2()
    dests=destsorder('Couple Statue','23','₹599','₹699')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order33(request):
    first=detail()
    second=detail2()
    dests=destsorder('Friends Toys','11','₹499','₹699')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order34(request):
    first=detail()
    second=detail2()
    dests=destsorder('Golden Camel','12','₹799','₹899')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order41(request):
    first=detail()
    second=detail2()
    dests=destsorder('Wooden Wolf','1a','₹499','₹649')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order42(request):
    first=detail()
    second=detail2()
    dests=destsorder('tabla Ganesh','17','₹999','₹1099')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order43(request):
    first=detail()
    second=detail2()
    dests=destsorder('Baby toys','19','₹499','₹599')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order44(request):
    first=detail()
    second=detail2()
    dests=destsorder('Baby Toys','20','₹499','₹599')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order51(request):
    first=detail()
    second=detail2()
    dests=destsorder('Teddy(pink)','35','₹499','₹699')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order52(request):
    first=detail()
    second=detail2()
    dests=destsorder('Teddy(Brown)','33','₹799','₹899')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order53(request):
    first=detail()
    second=detail2()
    dests=destsorder('Teddy(Sandal)','31','₹999','₹1099')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order54(request):
    first=detail()
    second=detail2()
    dests=destsorder('Teddy(Red)','32','₹699','₹799')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order61(request):
    first=detail()
    second=detail2()
    dests=destsorder('Flowervase Frame','38','₹499','₹699')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order62(request):
    first=detail()
    second=detail2()
    dests=destsorder('Buddha Frame','36','₹599','₹749')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order63(request):
    first=detail()
    second=detail2()
    dests=destsorder('Oilpainting Frame','37','₹1199','₹1399')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})

def order64(request):
    first=detail()
    second=detail2()
    dests=destsorder('Flowervase Frame','40','₹599','₹699')

    if request.method == 'POST':
        product=request.POST['productname']
        username= request.POST['uname']
        phonenum= request.POST['phonenum']
        emailid = request.POST['Email']
        address = request.POST['comment']
        print(username)
    
        if (RegisteredForms.objects.filter(Email=emailid)).exists():
            mail(username,product,emailid,phonenum,address)
            form=OrderForm(product=product,uname=username,phone=phonenum,Email=emailid,address=address)
            form.save()
            return render(request,'index.html',{'first':first,'second':second})
        else:
            return render(request,'order.html',{'dests':dests})
    else:
        return render(request,'order.html',{'dests':dests})
