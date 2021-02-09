from django.shortcuts import render
from . models import user_register
from . models import purchase_details
from . models import battery_details
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"index.html")
def gallerypage(request):
    data = battery_details.objects.filter(status=0)
    
    return render(request,"main_gallery.html",{'r':data})
def pinputpage(request):
    return render(request,"purchase deatails input.html")
def homepage(request):
    return render(request,"index.html")
def gotohome(request):
    return render(request,"index.html")
def galleryin(request):
    data = battery_details.objects.all()
    return render(request,"gallery.html",{'r':data})
def tables(request):
    data = purchase_details.objects.all()
    return render(request,"tables.html",{'r': data})
def bupload(request):
    return render(request,"batteryupload.html")
def contactpage(request):
      return render(request,"contact.html")
def register_details(request):
    fullname=request.POST['fullname']
    email=request.POST['email']
    mobileno=request.POST['mobileno']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['pswd']

    data= user_register(fullname=fullname,email=email,mobileno=mobileno,address=address,username=username,password=password,status=0)
    data.save()
    data = user_register.objects.all()
    return render(request,"index.html")
def login(request):
    m = user_register.objects.get(username=request.POST['usrname'],password = request.POST['password'])
    
    if m.status == '0':
        request.session['user_id'] = m.username
        data = battery_details.objects.all()
        return render(request, "gallery.html",{'r':data})
    elif m.status == '2':
        request.session['admin_id']=m.username
        return render(request,"tables.html")

    else:
        return render(request, "index.html")
def pdetailsinput(request):
    battery_type=request.POST['btype']
    serial_no=request.POST['serialno']
    buyer_name=request.POST['bname']
    mobno=request.POST['bmobile']
    address=request.POST['address']
    purchase_date=request.POST['pdate']
    maintenance_date=request.POST['mdatef']
    expiry_date=request.POST['wdatef']
    billno=request.POST['billno']
    pincode=request.POST['pincode']
    price=request.POST['price']
    data=purchase_details( battery_type= battery_type,serial_no=serial_no,buyer_name=buyer_name,mobno=mobno,address=address,purchase_date=purchase_date,maintenance_date=maintenance_date,
                           expiry_date=expiry_date, billno= billno,pincode=pincode, price= price,status=0)
    data.save()
    return render(request, "purchase deatails input.html")



def serialno(request):
   
    try:
        serialno=request.POST['srno']
        m = purchase_details.objects.get(serial_no=serialno)    
        if serialno == m.serial_no:        
            data = battery_details.objects.all()
            return render(request,"gallery.html",{'z':m,'r':data},)
        
           
    except:
         data = battery_details.objects.all()
         return render(request,"gallery.html",{'t': "your battery is not registered",'r':data})
        



def galleryup(request):
    
      bimage=request.FILES['bimg']
      bname=request.POST['banme']
      bdesc=request.POST['bdesc']
      vtype=request.POST['btype']
      ftype=request.POST['ftype']
      bvoltage=request.POST['bvolt']
      bprice=request.POST['bprize']

      data=battery_details( bimage=bimage,bname=bname, bdesc= bdesc,vtype=vtype,ftype=ftype, bvoltage= bvoltage,bprice=bprice,status=0)
      data.save()
      return render(request,"batteryupload.html")



def gotohome(request):
    return render(request,"index.html")

def gallerymanage(request):
    data = battery_details.objects.all()
    return render(request, "gallery table.html",{'x':data})
def retrievebdeatils(request):
    return render(request,"retrievebdetails.html")    

def retrieve(request):
    mob_no=request.POST['bdetin']
    m = purchase_details.objects.get(mobno=mob_no)
    data = battery_details.objects.all()
    return render(request,"retrievebdetails.html",{'y':m})
def stupdate(request):
    st=request.POST['stts']
    serialno=request.POST['serial']
    m=purchase_details.objects.filter(serial_no= serialno).update(status=st)
    data = purchase_details.objects.all()
    return render(request,"tables.html",{'r': data})   
def gmupdate(request):
     st1=request.POST['st']
     bname=request.POST['bname']
     m=battery_details.objects.filter(bname=bname).update(status=st1)
     data = battery_details.objects.all()
     return render(request, "gallery table.html",{'x':data})
    

def logoutuser(request):
    try:
        del request.session['user_id']
        return render(request,"index.html")
    except KeyError:
        pass
    return render(request,"gallery.html")

def userdetails(request):
    data = user_register.objects.all()
    

    return render(request,"userlist.html",{'q':data})

def usermanage(request):
     st1=request.POST['stts']
     mobno=request.POST['mobino']
     m=user_register.objects.filter(mobileno=mobno).update(status=st1)
     data = user_register.objects.all()
     return render(request, "userlist.html",{'q':data})

def logoutadmin(request):
    try:
        del request.session['admin_id']
        return render(request,"index.html")
    except KeyError:
        pass
    return render(request,"index.html")