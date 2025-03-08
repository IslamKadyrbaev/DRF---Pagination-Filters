import os

def get_product_upload_path(instance, filename):
    return os.path.join(
        'products', 
        str(instance.product_id),
        filename
    )