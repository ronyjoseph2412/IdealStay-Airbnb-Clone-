from django.shortcuts import redirect, render,HttpResponse
from datetime import datetime
from home.models import contactus,hostus1,AryanHomestay,CosyRoom,BakshiHeritage,paradise,RiversedgeNest,EdenHomestay,Packiavilla,RestelStudio,UrbanNest,WalnutCottage,Shambhal,Bellevue,BirTerraces,ThinlayHomestay,ShumbukHomes,OrchidGlade,HeavotCaves,VillaC
from home.models import booktr,bookdb,booknz,bookp,bookgr,booksw
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import random
from django.contrib.auth import authenticate, logout
# "All the forms used in the functions use the POST Method"
def index(request):
    return render(request,'index.html')

""" The function(stay) defined below is used to render the HTML page for experience page which 
consists of the basic layout for Places to Stay Homepage.
 """

def stay(request):
    return render(request,'stay.html')

""" The function(exp) defined below is used to render the HTML page for experience page which 
consists of the basic layout for Experiences Homepage.
 """

def exp(request):
    return render(request,'exp.html')

""" The function(login) defined below is used to render the HTML page for login page which 
consists of the basic layout for Login page. The function also authenticates the user to login into the portal.
The Login is authenticated by using authenticate function which takes arguements such as username and password.
"If user is true then redirected to the homepage". 
 """

def login(request):
    if request.method=='POST':
        userlogin=request.POST.get('userlogin')
        passlogin=request.POST.get('passlogin')
        user = authenticate(username=userlogin, password=passlogin)
        if user is not None:
            # A backend authenticated the credentials
            return redirect("/")
        else:
            return render(request,'login.html')
            # No backend authenticated the credentials

    return render(request,'login.html')
def logout(request):
    logout(request)
    return redirect("/")
""" The function(sign) defined below is used to render the HTML page for Sign up page where a new user can 
create their account by entering  basic details such as "EMAIL-ID" AND "PASSWORD" AND "CONFIRM PASSWORD" 
Error message is shown if "Some error occurs". On successful signup --- Success message is shown. Direct button to redirect to 
"""
def sign(request):
    if request.method=='POST':
        usersign=request.POST.get('usersign')
        passsign=request.POST.get('passsign')
        repasssign=request.POST.get('repasssign')
        try:
            if(passsign==repasssign):
                user = User.objects.create_user(usersign,usersign,passsign)
                user.save()
                messages.success(request, 'Account Created Succesfully.Please Login to continue.')
                return redirect('/sign')
            if(passsign!=repasssign):
                messages.warning(request, 'Some error Occured!Please try again later!')
                return redirect('/sign')
        except:
            print('Error Occured!')
        finally:
            pass
            


    return render(request,'sign.html')
def host(request):
    return render(request,'host.html')
def covid(request):
    return render(request,'covid.html')
""" 
The function(Contact) defined below is used to render HTML page of contact us and also to store the entered input parameters by the user.
A Object is created to store the details entered by the user. At end of each successful submission, A success message is shown to the user.
"""
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        C=contactus(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        C.save()
        messages.success(request, 'Your Message/Query has been succesfully sent.')
    return render(request,'contact.html')
def hostus(request):
    if request.method=="POST":
        firstnameh=request.POST.get('firstnameh')
        lastnameh=request.POST.get('lastnameh')   
        emailh=request.POST.get('emailh')
        phoneh=request.POST.get('phoneh')
        addressh=request.POST.get('addressh')
        stateh=request.POST.get('stateh')
        pinh=request.POST.get('pinh')
        B=hostus1(firstnameh=firstnameh,lastnameh=lastnameh,emailh=emailh,phoneh=phoneh,addressh=addressh,stateh=stateh,pinh=pinh,date=datetime.today())
        B.save()
        messages.success(request, 'Your request has been succefully registered.Our team will contact you shortly!')
    return render(request,'hostus.html')
def lucknow(request):
    return render(request,'lucknow.html')
def raipur(request):
    return render(request,'raipur.html')
def hyd(request):
    return render(request,'hyderabad.html')
def ntl(request):
    return render(request,'nainital.html')
def shimla(request):
    return render(request,'shimla.html')
def gangtok(request):
    return render(request,'gangtok.html')


'''Codes for Places to Stay'''

'''
In total 18 functions(stay1,stay2,....stay18) are written to render the pages for booking each stay.
The functions also help in creating object for each booking done in respective stay where the information such as Name,Booking Reference ID etc.
Each stay gets it's own Database which makes it easy to sort the booking data.
The reference ID for each stay is generated using Random function by import random. 
The function also displays message on successful booking. It also renders the HTML Page.
All 18 functions are defined in the same manner with changes in their object creation.
'''
def stay1(request):
    import random
    x=random.randint(11111,99999)
    
    if request.method=="POST":
        firstname1=request.POST.get('firstname1')
        lastname1=request.POST.get('lastname1')    
        email1=request.POST.get('email1')
        phone1=request.POST.get('phone1')
        adult1=request.POST.get('adult1')
        child1=request.POST.get('child1')
        start1=request.POST.get('start1')
        end1=request.POST.get('end1')
        address1=request.POST.get('address1')
        state1=request.POST.get('state1')
        pin1=request.POST.get('pin1')
        refid=x
        A=AryanHomestay(firstname1=firstname1,lastname1=lastname1,email1=email1,phone1=phone1,adult1=adult1,child1=child1,start1=start1,end1=end1,address1=address1,state1=state1,pin1=pin1,refid=x)
        A.save()
        messages.success(request, 'Your booking at Aryan’s Homestay is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay1.html')

def stay2(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname2=request.POST.get('firstname2')
        lastname2=request.POST.get('lastname2')    
        email2=request.POST.get('email2')
        phone2=request.POST.get('phone2')
        adult2=request.POST.get('adult2')
        child2=request.POST.get('child2')
        start2=request.POST.get('start2')
        end2=request.POST.get('end2')
        address2=request.POST.get('address2')
        state2=request.POST.get('state2')
        pin2=request.POST.get('pin2')
        D=CosyRoom(firstname2=firstname2,lastname2=lastname2,email2=email2,phone2=phone2,adult2=adult2,child2=child2,start2=start2,end2=end2,address2=address2,state2=state2,pin2=pin2,refid=x)
        D.save()
        messages.success(request, 'Your booking at Cosy Room in City of Nawabs! is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay2.html')

def stay3(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname3=request.POST.get('firstname3')
        lastname3=request.POST.get('lastname3')    
        email3=request.POST.get('email3')
        phone3=request.POST.get('phone3')
        adult3=request.POST.get('adult3')
        child3=request.POST.get('child3')
        start3=request.POST.get('start3')
        end3=request.POST.get('end3')
        address3=request.POST.get('address3')
        state3=request.POST.get('state3')
        pin3=request.POST.get('pin3')
        E=BakshiHeritage(firstname3=firstname3,lastname3=lastname3,email3=email3,phone3=phone3,adult3=adult3,child3=child3,start3=start3,end3=end3,address3=address3,state3=state3,pin3=pin3,refid=x)
        E.save()
        messages.success(request, 'Your booking at The Bakshi Heritage is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay3.html')

def stay4(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname4=request.POST.get('firstname4')
        lastname4=request.POST.get('lastname4')    
        email4=request.POST.get('email4')
        phone4=request.POST.get('phone4')
        adult4=request.POST.get('adult4')
        child4=request.POST.get('child4')
        start4=request.POST.get('start4')
        end4=request.POST.get('end4')
        address4=request.POST.get('address4')
        state4=request.POST.get('state4')
        pin4=request.POST.get('pin4')
        F=paradise(firstname4=firstname4,lastname4=lastname4,email4=email4,phone4=phone4,adult4=adult4,child4=child4,start4=start4,end4=end4,address4=address4,state4=state4,pin4=pin4,refid=x)
        F.save()
        messages.success(request, 'Your booking at The Paradise is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay4.html')

def stay5(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname5=request.POST.get('firstname5')
        lastname5=request.POST.get('lastname5')    
        email5=request.POST.get('email5')
        phone5=request.POST.get('phone5')
        adult5=request.POST.get('adult5')
        child5=request.POST.get('child5')
        start5=request.POST.get('start5')
        end5=request.POST.get('end5')
        address5=request.POST.get('address5')
        state5=request.POST.get('state5')
        pin5=request.POST.get('pin5')
        G=RiversedgeNest(firstname5=firstname5,lastname5=lastname5,email5=email5,phone5=phone5,adult5=adult5,child5=child5,start5=start5,end5=end5,address5=address5,state5=state5,pin5=pin5,refid=x)
        G.save()
        messages.success(request, 'Your booking at Riversedge Nest is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay5.html')

def stay6(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname6=request.POST.get('firstname6')
        lastname6=request.POST.get('lastname6')    
        email6=request.POST.get('email6')
        phone6=request.POST.get('phone6')
        adult6=request.POST.get('adult6')
        child6=request.POST.get('child6')
        start6=request.POST.get('start6')
        end6=request.POST.get('end6')
        address6=request.POST.get('address6')
        state6=request.POST.get('state6')
        pin6=request.POST.get('pin6')
        H=EdenHomestay(firstname6=firstname6,lastname6=lastname6,email6=email6,phone6=phone6,adult6=adult6,child6=child6,start6=start6,end6=end6,address6=address6,state6=state6,pin6=pin6,refid=x)
        H.save()
        messages.success(request, 'Your booking at Eden Homestay is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay6.html')

def stay7(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname7=request.POST.get('firstname7')
        lastname7=request.POST.get('lastname7')    
        email7=request.POST.get('email7')
        phone7=request.POST.get('phone7')
        adult7=request.POST.get('adult7')
        child7=request.POST.get('child7')
        start7=request.POST.get('start7')
        end7=request.POST.get('end7')
        address7=request.POST.get('address7')
        state7=request.POST.get('state7')
        pin7=request.POST.get('pin7')
        I=Packiavilla(firstname7=firstname7,lastname7=lastname7,email7=email7,phone7=phone7,adult7=adult7,child7=child7,start7=start7,end7=end7,address7=address7,state7=state7,pin7=pin7,refid=x)
        I.save()
        messages.success(request, 'Your booking at Packiavilla is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay7.html')

def stay8(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname8=request.POST.get('firstname8')
        lastname8=request.POST.get('lastname8')    
        email8=request.POST.get('email8')
        phone8=request.POST.get('phone8')
        adult8=request.POST.get('adult8')
        child8=request.POST.get('child8')
        start8=request.POST.get('start8')
        end8=request.POST.get('end8')
        address8=request.POST.get('address8')
        state8=request.POST.get('state8')
        pin8=request.POST.get('pin8')
        J=RestelStudio(firstname8=firstname8,lastname8=lastname8,email8=email8,phone8=phone8,adult8=adult8,child8=child8,start8=start8,end8=end8,address8=address8,state8=state8,pin8=pin8,refid=x)
        J.save()
        messages.success(request, 'Your booking at Restel Studio Apartment is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay8.html')

def stay9(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname9=request.POST.get('firstname9')
        lastname9=request.POST.get('lastname9')    
        email9=request.POST.get('email9')
        phone9=request.POST.get('phone9')
        adult9=request.POST.get('adult9')
        child9=request.POST.get('child9')
        start9=request.POST.get('start9')
        end9=request.POST.get('end9')
        address9=request.POST.get('address9')
        state9=request.POST.get('state9')
        pin9=request.POST.get('pin9')
        K=UrbanNest(firstname9=firstname9,lastname9=lastname9,email9=email9,phone9=phone9,adult9=adult9,child9=child9,start9=start9,end9=end9,address9=address9,state9=state9,pin9=pin9,refid=x)
        K.save()
        messages.success(request, 'Your booking at The Urban Nest is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay9.html')

def stay10(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname10=request.POST.get('firstname10')
        lastname10=request.POST.get('lastname10')    
        email10=request.POST.get('email10')
        phone10=request.POST.get('phone10')
        adult10=request.POST.get('adult10')
        child10=request.POST.get('child10')
        start10=request.POST.get('start10')
        end10=request.POST.get('end10')
        address10=request.POST.get('address10')
        state10=request.POST.get('state10')
        pin10=request.POST.get('pin10')
        L=WalnutCottage(firstname10=firstname10,lastname10=lastname10,email10=email10,phone10=phone10,adult10=adult10,child10=child10,start10=start10,end10=end10,address10=address10,state10=state10,pin10=pin10,refid=x)
        L.save()
        messages.success(request, 'Your booking at Walnut Cottage is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay10.html')

def stay11(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname11=request.POST.get('firstname11')
        lastname11=request.POST.get('lastname11')    
        email11=request.POST.get('email11')
        phone11=request.POST.get('phone11')
        adult11=request.POST.get('adult11')
        child11=request.POST.get('child11')
        start11=request.POST.get('start11')
        end11=request.POST.get('end11')
        address11=request.POST.get('address11')
        state11=request.POST.get('state11')
        pin11=request.POST.get('pin11')
        M=Shambhal(firstname11=firstname11,lastname11=lastname11,email11=email11,phone11=phone11,adult11=adult11,child11=child11,start11=start11,end11=end11,address11=address11,state11=state11,pin11=pin11,refid=x)
        M.save()
        messages.success(request, 'Your booking at Shambhal Luxury Villa is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay11.html')

def stay12(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname12=request.POST.get('firstname12')
        lastname12=request.POST.get('lastname12')    
        email12=request.POST.get('email12')
        phone12=request.POST.get('phone12')
        adult12=request.POST.get('adult12')
        child12=request.POST.get('child12')
        start12=request.POST.get('start12')
        end12=request.POST.get('end12')
        address12=request.POST.get('address12')
        state12=request.POST.get('state12')
        pin12=request.POST.get('pin12')
        N=Bellevue(firstname12=firstname12,lastname12=lastname12,email12=email12,phone12=phone12,adult12=adult12,child12=child12,start12=start12,end12=end12,address12=address12,state12=state12,pin12=pin12,refid=x)
        N.save()
        messages.success(request, 'Your booking at Bellevue Retreat is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay12.html')

def stay13(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname13=request.POST.get('firstname13')
        lastname13=request.POST.get('lastname13')    
        email13=request.POST.get('email13')
        phone13=request.POST.get('phone13')
        adult13=request.POST.get('adult13')
        child13=request.POST.get('child13')
        start13=request.POST.get('start13')
        end13=request.POST.get('end13')
        address13=request.POST.get('address13')
        state13=request.POST.get('state13')
        pin13=request.POST.get('pin13')
        O=BirTerraces(firstname13=firstname13,lastname13=lastname13,email13=email13,phone13=phone13,adult13=adult13,child13=child13,start13=start13,end13=end13,address13=address13,state13=state13,pin13=pin13,refid=x)
        O.save()
        messages.success(request, 'Your booking at Bir Terraces:Utopia in the hills is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay13.html')

def stay14(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname14=request.POST.get('firstname14')
        lastname14=request.POST.get('lastname14')    
        email14=request.POST.get('email14')
        phone14=request.POST.get('phone14')
        adult14=request.POST.get('adult14')
        child14=request.POST.get('child14')
        start14=request.POST.get('start14')
        end14=request.POST.get('end14')
        address14=request.POST.get('address14')
        state14=request.POST.get('state14')
        pin14=request.POST.get('pin14')
        P=ThinlayHomestay(firstname14=firstname14,lastname14=lastname14,email14=email14,phone14=phone14,adult14=adult14,child14=child14,start14=start14,end14=end14,address14=address14,state14=state14,pin14=pin14,refid=x)
        P.save()
        messages.success(request, 'Your booking at Thinlay Homestay is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay14.html')

def stay15(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname15=request.POST.get('firstname15')
        lastname15=request.POST.get('lastname15')    
        email15=request.POST.get('email15')
        phone15=request.POST.get('phone15')
        adult15=request.POST.get('adult15')
        child15=request.POST.get('child15')
        start15=request.POST.get('start15')
        end15=request.POST.get('end15')
        address15=request.POST.get('address15')
        state15=request.POST.get('state15')
        pin15=request.POST.get('pin15')
        Q=ShumbukHomes(firstname15=firstname15,lastname15=lastname15,email15=email15,phone15=phone15,adult15=adult15,child15=child15,start15=start15,end15=end15,address15=address15,state15=state15,pin15=pin15,refid=x)
        Q.save()
        messages.success(request, 'Your booking at Shumbuk Homes is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay15.html')

def stay16(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname16=request.POST.get('firstname16')
        lastname16=request.POST.get('lastname16')    
        email16=request.POST.get('email16')
        phone16=request.POST.get('phone16')
        adult16=request.POST.get('adult16')
        child16=request.POST.get('child16')
        start16=request.POST.get('start16')
        end16=request.POST.get('end16')
        address16=request.POST.get('address16')
        state16=request.POST.get('state16')
        pin16=request.POST.get('pin16')
        R=OrchidGlade(firstname16=firstname16,lastname16=lastname16,email16=email16,phone16=phone16,adult16=adult16,child16=child16,start16=start16,end16=end16,address16=address16,state16=state16,pin16=pin16,refid=x)
        R.save()
        messages.success(request, 'Your booking at Orchid Glade is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay16.html')

def stay17(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname17=request.POST.get('firstname17')
        lastname17=request.POST.get('lastname17')    
        email17=request.POST.get('email17')
        phone17=request.POST.get('phone17')
        adult17=request.POST.get('adult17')
        child17=request.POST.get('child17')
        start17=request.POST.get('start17')
        end17=request.POST.get('end17')
        address17=request.POST.get('address17')
        state17=request.POST.get('state17')
        pin17=request.POST.get('pin17')
        S=HeavotCaves(firstname17=firstname17,lastname17=lastname17,email17=email17,phone17=phone17,adult17=adult17,child17=child17,start17=start17,end17=end17,address17=address17,state17=state17,pin17=pin17,refid=x)
        S.save()
        messages.success(request, 'Your booking at Heavot Caves is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay17.html')

def stay18(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname18=request.POST.get('firstname18')
        lastname18=request.POST.get('lastname18')    
        email18=request.POST.get('email18')
        phone18=request.POST.get('phone18')
        adult18=request.POST.get('adult18')
        child18=request.POST.get('child18')
        start18=request.POST.get('start18')
        end18=request.POST.get('end18')
        address18=request.POST.get('address18')
        state18=request.POST.get('state18')
        pin18=request.POST.get('pin18')
        T=VillaC(firstname18=firstname18,lastname18=lastname18,email18=email18,phone18=phone18,adult18=adult18,child18=child18,start18=start18,end18=end18,address18=address18,state18=state18,pin18=pin18,refid=x)
        T.save()
        messages.success(request, 'Your booking at Villa 20C is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay18.html')

'''Similarly 18 functions are defined to render the map pages of all the 18 places.
The map pages are created in HTML format using Google Maps.
'''
def stay1map(request):
    return render(request,"stay1map.html")
def stay2map(request):
    return render(request,"stay2map.html")
def stay3map(request):
    return render(request,"stay3map.html")
def stay4map(request):
    return render(request,"stay4map.html")
def stay5map(request):
    return render(request,"stay5map.html")
def stay6map(request):
    return render(request,"stay6map.html")
def stay7map(request):
    return render(request,"stay7map.html")
def stay8map(request):
    return render(request,"stay8map.html")
def stay9map(request):
    return render(request,"stay9map.html")
def stay10map(request):
    return render(request,"stay10map.html")
def stay11map(request):
    return render(request,"stay11map.html")
def stay12map(request):
    return render(request,"stay12map.html")
def stay13map(request):
    return render(request,"stay13map.html")
def stay14map(request):
    return render(request,"stay14map.html")
def stay15map(request):
    return render(request,"stay15map.html")
def stay16map(request):
    return render(request,"stay16map.html")
def stay17map(request):
    return render(request,"stay17map.html")
def stay18map(request):
    return render(request,"stay18map.html")

""" The functions defined below are used to render the HTML pages used for experiences.
"Each experience has a dedicated HTML page".
"""
def turkey(request):
    return render(request,"turkey.html")

def dubai(request):
    return render(request,"dubai.html")

def grece(request):
    return render(request,"grece.html")

def nz(request):
    return render(request,"nz.html")

def portugal(request):
    return render(request,"portugal.html")

def swis(request):
    return render(request,"swis.html")

"""
The functions defined below are used to render the HTML pages used for experiences for booking each experience.
Each experience booking has it's indiviual function. Each experience booking page has it's own object-creation to maintain indiviual database 
for each experience. Here the object is created with few basic parameters such as name,booking date and number of guests etc.
Each booking has it's own Reference ID for creating a easy redressal forum.
At end each successful booking a success message and reference ID is shown to the user.

"""

def stay20(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname20=request.POST.get('firstname20')
        lastname20=request.POST.get('lastname20')    
        email20=request.POST.get('email20')
        phone20=request.POST.get('phone20')
        adult20=request.POST.get('adult20')
        child20=request.POST.get('child20')
        start20=request.POST.get('start20')
        address20=request.POST.get('address20')
        state20=request.POST.get('state20')
        pin20=request.POST.get('pin20')
        T=bookdb(firstname20=firstname20,lastname20=lastname20,email20=email20,phone20=phone20,adult20=adult20,child20=child20,start20=start20,address20=address20,state20=state20,pin20=pin20,refid=x)
        T.save()
        messages.success(request, 'We are delighted to travel along with you to Dubai! Your booking is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay20.html')

def stay21(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname21=request.POST.get('firstname21')
        lastname21=request.POST.get('lastname21')    
        email21=request.POST.get('email21')
        phone21=request.POST.get('phone21')
        adult21=request.POST.get('adult21')
        child21=request.POST.get('child21')
        start21=request.POST.get('start21')
        address21=request.POST.get('address21')
        state21=request.POST.get('state21')
        pin21=request.POST.get('pin21')
        T=booknz(firstname21=firstname21,lastname21=lastname21,email21=email21,phone21=phone21,adult21=adult21,child21=child21,start21=start21,address21=address21,state21=state21,pin21=pin21,refid=x)
        T.save()
        messages.success(request, 'We are delighted to travel along with you to NewZealand! Your booking is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay21.html')

def stay22(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname22=request.POST.get('firstname22')
        lastname22=request.POST.get('lastname22')    
        email22=request.POST.get('email22')
        phone22=request.POST.get('phone22')
        adult22=request.POST.get('adult22')
        child22=request.POST.get('child22')
        start22=request.POST.get('start22')
        address22=request.POST.get('address22')
        state22=request.POST.get('state22')
        pin22=request.POST.get('pin22')
        T=bookp(firstname22=firstname22,lastname22=lastname22,email22=email22,phone22=phone22,adult22=adult22,child22=child22,start22=start22,address22=address22,state22=state22,pin22=pin22,refid=x)
        T.save()
        messages.success(request, 'We are delighted to travel along with you to Portugal! Your booking is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay22.html')

def stay23(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname23=request.POST.get('firstname23')
        lastname23=request.POST.get('lastname23')    
        email23=request.POST.get('email23')
        phone23=request.POST.get('phone23')
        adult23=request.POST.get('adult23')
        child23=request.POST.get('child23')
        start23=request.POST.get('start23')
        address23=request.POST.get('address23')
        state23=request.POST.get('state23')
        pin23=request.POST.get('pin23')
        T=bookgr(firstname23=firstname23,lastname23=lastname23,email23=email23,phone23=phone23,adult23=adult23,child23=child23,start23=start23,address23=address23,state23=state23,pin23=pin23,refid=x)
        T.save()
        messages.success(request, 'We are delighted to travel along with you to Greece! Your booking is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay23.html')

def stay24(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname24=request.POST.get('firstname24')
        lastname24=request.POST.get('lastname24')    
        email24=request.POST.get('email24')
        phone24=request.POST.get('phone24')
        adult24=request.POST.get('adult24')
        child24=request.POST.get('child24')
        start24=request.POST.get('start24')
        address24=request.POST.get('address24')
        state24=request.POST.get('state24')
        pin24=request.POST.get('pin24')
        T=booksw(firstname24=firstname24,lastname24=lastname24,email24=email24,phone24=phone24,adult24=adult24,child24=child24,start24=start24,address24=address24,state24=state24,pin24=pin24,refid=x)
        T.save()
        messages.success(request, 'We are delighted to travel along with you to Switzerland! Your booking is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay24.html')

def stay19(request):
    import random
    x=random.randint(11111,99999)
    if request.method=="POST":
        firstname19=request.POST.get('firstname19')
        lastname19=request.POST.get('lastname19')    
        email19=request.POST.get('email19')
        phone19=request.POST.get('phone19')
        adult19=request.POST.get('adult19')
        child19=request.POST.get('child19')
        start19=request.POST.get('start19')
        address19=request.POST.get('address19')
        state19=request.POST.get('state19')
        pin19=request.POST.get('pin19')
        T=booktr(firstname19=firstname19,lastname19=lastname19,email19=email19,phone19=phone19,adult19=adult19,child19=child19,start19=start19,address19=address19,state19=state19,pin19=pin19,refid=x)
        T.save()
        messages.success(request, 'We are delighted to travel along with you to Turkey! Your booking is under process with Reference ID:-{}.We will sent you a confirmation mail shortly! '.format(x))
    return render(request,'stay19.html')