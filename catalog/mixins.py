class ProductFormMixin:
    def __init__(self, *args, **kwargs):
        super(ProductFormMixin, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
