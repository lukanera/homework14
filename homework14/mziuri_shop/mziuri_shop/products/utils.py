def get_filters(request):
    filters = dict()

    product_name = request.GET.get('product_name')
    if product_name:
        filters['name__icontains'] = product_name

    min_price = request.GET.get('min_price')
    if min_price:
        filters['price__gt'] = min_price

    max_price = request.GET.get('max_price')
    if max_price:
        filters['price__lt'] = max_price

    address = request.GET.get('address')
    if address:
        filters['address__icontains'] = address

    category = request.GET.get('category')
    if category:
        filters['category_id'] = category

    return filters