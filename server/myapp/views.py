from django.shortcuts import render
def home(request):
    return render(request,"file.html")
def calculate_power(request):
    if request.method=="POST":
        intensity=int(request.POST.get("intensity"))
        resistance=int(request.POST.get("resistance"))
        power=(intensity**2)*resistance
        print(f"Intensity:{intensity},Resistance:{resistance},Power:{power}")
        return render(request,"file.html",{"Power":power})
        return render(request,"file.html")
# Create your views here.
