from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.
@csrf_exempt
def books(request):
  if request.method == 'GET':
    books = Book.objects.all().values()
    return JsonResponse({'book': list(books)})

  elif request.method == 'POST':
    title = request.POST.get('title')
    author = request.POST.get('author')
    price = request.POST.get('price')
    inventory = request.POST.get('inventory')
  
    book = Book(
      title=title,
      author=author,
      price=price,
      inventory=inventory,
      )
    
    try: 
      book.save()
    except IntegrityError:
      return JsonResponse({
        'error': 'true',
        'message': 'required filed missing'
      },
      status = 400)
    
    return JsonResponse(model_to_dict(book), status=201)
  
      
    

