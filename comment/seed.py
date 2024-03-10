from faker import Faker
from comment.models import Comment
from products.models import Product
from django.core.files import File

import random

fake = Faker()
# seeder = Seed.seeder()

# Lấy tất cả sản phẩm hiện có
existing_products = list(Product.objects.all())

for _ in range(15):  # Đây là số lượng Comment bạn muốn tạo
    product = random.choice(existing_products)  # Chọn một sản phẩm ngẫu nhiên
    choice_image = random.randint(1,3)
    image_file = open(f'upload_images/product_{choice_image}.png', 'rb')
    comment = Comment(
        product=product,
        name=fake.name(),
        title=fake.sentence(),
        rating=fake.random_int(min=1, max=5),
        image = File(image_file)
    )
    comment.save()
    image_file.close()

for comment in Comment.objects.filter(image__isnull=True):
    choice_image = random.randint(1,3)
    image_file = open(f'upload_images/product_{choice_image}.png', 'rb')
    comment.image = File(image_file)
    comment.save()
    image_file.close()

# seeder.execute()
