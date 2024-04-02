from django.shortcuts import render
from .forms import EnForm
from.models import EnModel

def home(request):
	if request.method=="POST":
		na=request.POST.get("name")
		em=request.POST.get("email")
		ph=int(request.POST.get("phone"))
		print(na,em,ph)
		d=EnModel(name=na,email=em,phone=ph)
		d.save()
		fm=EnForm()
		return render(request,"home.html",{"fm":fm,"msg":"we will get back to u"})
	else:
		fm=EnForm()
		return render(request,"home.html",{"fm":fm})