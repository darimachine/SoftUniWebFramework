from django.shortcuts import render

# Create your views here.
class ProductListView(APIView):
    queryset = Product.objects.all()