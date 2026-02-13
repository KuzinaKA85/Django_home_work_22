from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_product_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"

    def get_queryset(self):
        return get_product_from_cache()


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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = ("catalog.delete_product",)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not (
            self.object.owner == request.user
            or request.user.has_perm("catalog.delete_product")
        ):
            return HttpResponseForbidden("Нет прав на удаление")
        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs["pk"])
        if request.user.has_perm("catalog.can_unpublish_product"):
            product.is_published = False
            product.save()
            return redirect("catalog:product_list")
        else:
            return HttpResponseForbidden("У вас нет прав на выполнение этого действия.")


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = get_products_by_category(category_id)

    context = {"category": category, "products": products}
    return render(request, "catalog/category_products.html", context)
