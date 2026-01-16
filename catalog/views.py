from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"<h2>Спасибо, {name}!</h2>"
            f"<h3>Ваше сообщение получено.</h3>"
            f'<p>"{message}"</p>'
            f"<p>С вами свяжутся по этому <b>{phone}</b> номеру.</p>"
        )


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
