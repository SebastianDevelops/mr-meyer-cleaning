from re import template
from django.shortcuts import render
from .models import ExternalSite, Product, Litre, ProductPage

# Create your views here.
def index(request):
    externalwebsite = ExternalSite.objects.get(name="Business Name")
    
    # products being called individually one at a time
    allpurposecleaner1l = Litre.objects.get(product="1", amount_of_litres="1L")
    
    dishwashsuper1l = Litre.objects.get(product=4)
    
    fatdegreaser1l = Litre.objects.get(product=7)
    
    handyclean5l = Litre.objects.get(product=11)
    
    pinegel1l = Litre.objects.get(product=13)
    
    heavydutycleaner1l = Litre.objects.get(product=16)
    
    liquidfloorwax1l = Litre.objects.get(product=33)
    
    tilebrite5l = Litre.objects.get(product=37)
    
    tilecleaner1l = Litre.objects.get(product=39)
    
    tilecleaner5l = Litre.objects.get(product=40)
    
    tilecleaner25l = Litre.objects.get(product=41)
    
    liquidfloorwax5l = Litre.objects.get(product=34)
    
    blackfluid1l = Litre.objects.get(product=42)
    
    thickbleach1l = Litre.objects.get(product=45)
    
    savtol750ml = Litre.objects.get(product=48)
    
    toiletbowelcleaner1l = Litre.objects.get(product=51)
    
    foodsanatizer1l = Litre.objects.get(product=54)
    
    draincleaner500g = Litre.objects.get(product=56)
    
    carwashandwax1l = Litre.objects.get(product=57)
    
    tyreandbumpershine1l = Litre.objects.get(product=60)
    
    carpolish500ml = Litre.objects.get(product=63)
    
    dashprotector500ml = Litre.objects.get(product=65)
    
    handsanatizer500ml = Litre.objects.get(product=67)
    
    tyreandbumpershine5l = Litre.objects.get(product=62)
    
    context = {
        "externalwebsite":externalwebsite,
        "allpurposecleaner1l": allpurposecleaner1l,
        "dishwashsuper1l":dishwashsuper1l,
        "fatdegreaser1l": fatdegreaser1l,
        "handyclean5l": handyclean5l,
        "pinegel1l": pinegel1l,
        "heavydutycleaner1l": heavydutycleaner1l,
        "liquidfloorwax1l": liquidfloorwax1l,
        "tilebrite5l":tilebrite5l,
        "tilecleaner1l":tilecleaner1l,
        "tilecleaner5l":tilecleaner5l,
        "tilecleaner25l":tilecleaner25l,
        "liquidfloorwax5l":liquidfloorwax5l,
        "blackfluid1l":blackfluid1l,
        "thickbleach1l":thickbleach1l,
        "savtol750ml":savtol750ml,
        "toiletbowelcleaner1l":toiletbowelcleaner1l,
        "foodsanatizer1l":foodsanatizer1l,
        "draincleaner500g": draincleaner500g,
        "carwashandwax1l":carwashandwax1l,
        "tyreandbumpershine1l":tyreandbumpershine1l,
        "carpolish500ml":carpolish500ml,
        "dashprotector500ml":dashprotector500ml,
        "handsanatizer500ml":handsanatizer500ml,
        "tyreandbumpershine5l":tyreandbumpershine5l,
    }
    return render(request, "index.html", context)

def detergents(request):
    one_litre = ProductPage.objects.filter(group=1, productliters=1)
    five_litre = ProductPage.objects.filter(group=1, productliters=2)
    twentyfive_litre = ProductPage.objects.filter(group=1, productliters=3)
    other = ProductPage.objects.filter(group=1, productliters=4)
    context ={
        "one": one_litre,
        "five": five_litre,
        "twentyfive": twentyfive_litre,
        "other": other,
    }
    return render(request, "detergents.html", context)

def floor_care(request):
    one_litre = ProductPage.objects.filter(group=2, productliters=1)
    five_litre = ProductPage.objects.filter(group=2, productliters=2)
    twentyfive_litre = ProductPage.objects.filter(group=2, productliters=3)
    other = ProductPage.objects.filter(group=2, productliters=4)
    context = {
        "one": one_litre,
        "five": five_litre,
        "twentyfive": twentyfive_litre,
        "other": other,
    }
    return render(request, "floor-care.html", context)

def car_care(request):
    one_litre = ProductPage.objects.filter(group=4, productliters=1)
    five_litre = ProductPage.objects.filter(group=4, productliters=2)
    twentyfive_litre = ProductPage.objects.filter(group=4, productliters=3)
    other = ProductPage.objects.filter(group=4, productliters=4)
    context = {
        "one": one_litre,
        "five": five_litre,
        "twentyfive": twentyfive_litre,
        "other": other,
    }
    return render(request, "car-care.html", context)

def disinfect(request):
    one_litre = ProductPage.objects.filter(group=3, productliters=1)
    five_litre = ProductPage.objects.filter(group=3, productliters=2)
    twentyfive_litre = ProductPage.objects.filter(group=3, productliters=3)
    other = ProductPage.objects.filter(group=3, productliters=4)
    context = {
        "one": one_litre,
        "five": five_litre,
        "twentyfive": twentyfive_litre,
        "other": other,
    }
    return render(request, "s-and-disinfect.html", context)