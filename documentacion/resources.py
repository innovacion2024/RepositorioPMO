from import_export import resources
from .models import Product

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')  # List of your model fields

    # Explicit mapping between column titles in the Excel file and field names in the model
    def get_import_id_fields(self):
        return ['name']

    def before_import_row(self, row, **kwargs):
        row['name'] = row.pop('Product Name', None)