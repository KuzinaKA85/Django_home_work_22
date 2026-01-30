from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name_category", "description_category"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name_product",
            "description_product",
            "category_product",
            "price_product",
            "image_product",
        ]

    def clean(self):
        ban_words = [
            "казино",
            "биржа",
            "обман",
            "криптовалюта",
            "дешево",
            "полиция",
            "крипта",
            "бесплатно",
            "радар",
        ]
        cleaned_date = super().clean()
        name = cleaned_date.get("name_product")
        description = cleaned_date.get("description_product")

        if any(word in name.lower() for word in ban_words):
            self.add_error("name_product", "Использованны запрещённые слова")

        if any(word in description.lower() for word in ban_words):
            self.add_error("description_product", "Использованны запрещённые слова")
