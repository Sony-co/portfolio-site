from django.shortcuts import render

# Create your views here.

#hero section
Hero={"name":"Siddhanth Das",
    "work":"Django Web Developer | Clean & Fast Websites",
    "about":"I build simple, responsive portfolio and small-business websites \n using Django and modern CSS.Focused on clarity, performance,\n and reliable delivery.",
}

def home(request):
    return render(request,"home.html",{"name":Hero.get("name"),
                                                            "work":Hero.get("work"),
                                                            "about":Hero.get("about")})
def about(request):
    return render(request,"about.html",)

def projects(request):
    return render(request,"projects.html",)

def services(request):
    return render(request,"services.html",)

def contact(request):
    return render(request,"contacts.html",)