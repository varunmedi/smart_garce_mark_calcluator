from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Faculty,Student,Subjects
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logouts

# Create your views here.

def home(request):
    return render(request,'home.html')
def login(request):

    if request.method=="POST" :
        
        u,p=request.POST.get('email'),request.POST.get('password')
        fac=Faculty.objects.filter(email=u)
        if fac.exists():
            request.session['email']=u
            if fac.get().password==p:
                
                return render(request,'index.html')
            else:
                
                messages.info(request,'Invalid Credentials')
                return render(request,'login.html')
                
        else:
            messages.error(request, 'No such User exists')
            return redirect('login')
    else:
        
       
        return render(request,'login.html')
def index(request):
    if request.session.has_key('email') :
        print("...................",request.session['email'])
        return render(request,'index.html')
    else:
        messages.error(request, 'You must login first')
        return render(request,'login.html')
def sindex(request):
    if  request.session.has_key('roll'):
        
        return render(request,'sindex.html')
        
    else:
        messages.error(request, 'You must login first')
        return render(request,'slogin.html')
  
def password(request):
    
    if request.method=="POST":
        u=request.POST.get('email')
        email=u
        fac=Faculty.objects.filter(email=u)
        if fac.exists():
            subject="Your accounts need to be verified"
            
            msg=f'Hi use this link to reset your password http://127.0.0.1:8000/{email}'
            email_from='suryaram1592@gmail.com'
            recipient_list=[u]
            send_mail(subject,msg,email_from,recipient_list)
            return render(request,'password_reset_done.html')
        else:
            messages.info(request, 'No such User exists')
            return redirect('password')
    else:
        
        return render(request,'password.html')

def verify(request,email):
    if request.method=="POST":
            fac=Faculty.objects.filter(email=email)
            
            if fac.exists() :
                if(request.POST.get('p1')==request.POST.get('p2')):
                    facu=Faculty.objects.get(email=email)
                    facu.password=request.POST.get('p1')
                    facu.save()
                    return render(request,'password_reset_complete.html')
                else:
                    messages.info(request,'Passwords aint matching')
                    return render(request,'password_reset_confirm.html')
            else:
                messages.info(request, 'No such User exists')
                return render(request,'login.html')
        
    else:
        return render(request,'password_reset_confirm.html',{"email":email})

def profile(request):
    print('Updating...........................')
    if request.session.has_key('email'):
        email=request.session['email']
        fac=Faculty.objects.filter(email=email)
        if request.method=="POST":
            print('its post...........................')
            facu=Faculty.objects.get(email=email)
            if request.POST.get('name')!="":
                facu.name=request.POST.get('name')
            if request.POST.get('phone')!="":
                facu.phone=request.POST.get('phone')
            if request.POST.get('street')!="":
                facu.street=request.POST.get('street')
            if  request.POST.get('city')!="":
                facu.city=request.POST.get('city')
            if  request.POST.get('state')!="":
                facu.state=request.POST.get('state')
            if request.POST.get('zipcode')!="":
                facu.zipcode=request.POST.get('zipcode')
            if request.POST.get('email')!="":
                fac=Faculty.objects.filter(email=request.POST.get('email'))
                if fac.exists():
                    messages.info(request, 'There is an account with this mail')
                    return render(request,'profile.html')
                else:
                    facu.email=request.POST.get('email')
            facu.save()
            
            messages.info(request, 'Details updated')
            return redirect('profile')
            
        else:
            
            return render(request,'profile.html',{"fac":fac.get()})
    else:
        messages.error(request, 'You must login first')
        return render(request,'login.html')

def sprofile(request):
    print('Updating...........................')
    if request.session.has_key('roll'):
        roll=request.session['roll']
        fac=Student.objects.filter(roll=roll)
        if request.method=="POST":
            print('its post...........................')
            facu=Student.objects.get(roll=roll)
            if request.POST.get('name')!="":
                facu.name=request.POST.get('name')
            if request.POST.get('branch')!="":
                facu.branch=request.POST.get('branch')
            
            if request.POST.get('roll')!="":
                fac=Student.objects.filter(roll=request.POST.get('roll'))
                if fac.exists():
                    messages.info(request, 'There is an account with this mail')
                    return render(request,'sprofile.html')
                else:
                    facu.roll=request.POST.get('roll')
            if request.POST.get('pass')!="":
                facu.password=request.POST.get('pass')
            facu.save()
            
            messages.info(request, 'Details updated')
            return redirect('sprofile')
            
        else:
            
            return render(request,'sprofile.html',{"fac":fac.get()})
    else:
        messages.error(request, 'You must login first')
        return render(request,'slogin.html')

def marks(request):
    print('i am in marks')
    if request.session.has_key('email'):
        if request.method=="POST":
            print("in post")
            roll=request.POST.get('roll')
            request.session['roll']=roll
            print(roll)
            fac=Student.objects.filter(roll=roll)
            print(fac.exists(),"...............................")
            if fac.exists():
                facu=Student.objects.get(roll=roll)
                sub=Subjects.objects.get(branch=facu.branch,year=facu.year)
                subjects=(sub.subj).split(",")
                print("..................",subjects)
               
                return render(request,'marks.html',{'l':subjects,'fac':facu})
            else:
                messages.error(request, 'No such student exists')
                return render(request,'details.html')
        
    else:
        messages.error(request, 'You must login first')
        return render(request,'login.html')

def details(request):
    if request.session.has_key('email'):
        print("...................",request.session['email'])
        return render(request,'details.html')
    else:
        messages.error(request, 'You must login first')
        return render(request,'login.html')


def msubmit(request):
    print('i am in marks')
    if request.session.has_key('email') :
        if request.method=="POST" and request.session.has_key('roll'):
            print("in post")
            roll=request.session['roll']
            print("roll",roll)
            fac=Student.objects.filter(roll=roll)
            if fac.exists():
                facu=Student.objects.get(roll=roll)
                sub=Subjects.objects.get(branch=facu.branch,year=facu.year)
                subjects=(sub.subj).split()
                k=dict(request.POST)
                a=""
                print(type(k['p1']))
                p =  [str(int(0.3 * float(i))) for i in k['p1']]
                q=   [str(int(0.3 * float(i))) for i in k['p2']]
                s=   [str(int(0.5 * float(i))) for i in k['sem']]
                
            
                a=a=" ".join(p)+"#"+" ".join(q)+'#'+" ".join(k['ca'])+'#'+" ".join(s)+'#'+" ".join(k['total'])+"#"+" ".join(k['grace'])
                print(a,"..........................")
                facu.marks=a
                facu.save()
                return render(request,'details.html')
            else:
                messages.error(request, 'No such student exists')
                return render(request,'details.html')
    else:
        messages.error(request, 'You must login first')
        return render(request,'login.html')
def grade(request):
    if request.session.has_key('email') :
        return render(request,'grade.html')
    else:
        messages.error(request, 'You must login first')
        return render(request,'login.html')

def sgrade(request):
    if request.session.has_key('roll') :
        return render(request,'sgrade.html')
    else:
        messages.error(request, 'You must login first')
        return render(request,'slogin.html')


    

def slogin(request):
    if request.method=="POST" :
        
        u,p=request.POST.get('email'),request.POST.get('password')
        print(u,p)
        fac=Student.objects.filter(roll=u)
        if fac.exists():
            request.session['roll']=u
            if fac.get().password==p:
                
                return render(request,'sindex.html')
            else:
                
                messages.info(request,'Invalid Credentials')
                return render(request,'slogin.html')
                
        else:
            messages.error(request, 'No such User exists')
            return redirect('slogin')
    else:
        
       
        return render(request,'slogin.html')

def final(request):
    if request.session.has_key('roll') :
        roll=request.session['roll']
        print(".....",roll)
        facu=Student.objects.get(roll=roll)
        print("...",facu.branch)
        sub=Subjects.objects.get(branch=facu.branch,year=facu.year)
        subjects=(sub.subj).split(",")
        k=(facu.marks).split('#')
        print("..................",k)
        p1=list(map(int,k[0].split(' ')))
        p2=list(map(int,k[1].split(' ')))
        ca=list(map(int,k[2].split(' ')))
        sem=list(map(int,k[3].split(' ')))
        total=list(map(int,k[4].split(' ')))
        grace=int(k[5])
        grade=[]
        for i in range(len(total)):
            if(total[i]<50 and total[i]+grace>=50):
                    total[i]= total[i]+grace
                    grace=0
                    break
        if(grace!=0):
            for i in range(len(total)):
                if(total[i]>=50 and total[i]<=60):
                    total[i]= total[i]+grace
                    grace=0
                    break
        if(grace!=0):
            for i in range(len(total)):
                if(total[i]>=61 and total[i]<=70):
                    total[i]= total[i]+grace
                    grace=0
                    break
        if(grace!=0):
            for i in range(len(total)):
                if(total[i]>=71 and total[i]<=80):
                    total[i]= total[i]+grace
                    grace=0
                    break

                
        
        for i in range(len(total)):
            if(total[i]>=96):
                grade.append('O')
                continue
            elif(total[i]>=91):
                grade.append('A+')
                continue
            elif(total[i]>=86):
                grade.append('A')
                continue
            elif(total[i]>=81):
                grade.append('B+')
                continue
            elif(total[i]>=71):
                grade.append('B')
                continue
            elif(total[i]>=61):
                grade.append('C')
                continue
            elif(total[i]>=50):
                grade.append('P')
                continue
            else:
                grade.append('F')

                         
            

        f=list(zip(subjects,p1,p2,ca,sem,total,grade))
        

        return render(request,'final.html',{'l':f})
    else:
        messages.error(request, 'You must login first')
        return render(request,'slogin.html')


        

def logout(request):
    if request.session.has_key('email'):
            request.session.flush()
            return render(request,'login.html')
    else:
        messages.error(request, 'You must login first')
        return render(request,'login.html')

def slogout(request):
    if  request.session.has_key('roll'):
            request.session.flush()
            return render(request,'slogin.html')
    else:
        messages.error(request, 'You must login first')
        return render(request,'slogin.html')
 

    