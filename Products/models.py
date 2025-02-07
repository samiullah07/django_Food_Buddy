from django.db import models
import uuid
import datetime
# Create your models here.



class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        abstract = True

class Category(BaseModel):
    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cat_name}"

class Customer(BaseModel):  # You could extend AbstractBaseUser if you want custom user models
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Increased length to handle hashed passwords
    profile_image = models.ImageField(upload_to="upload/profile", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class ProductDetail(BaseModel):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    product_des = models.TextField()
    prduct_price = models.IntegerField()
    product_image = models.ImageField(upload_to="upload/products")

    is_deal = models.BooleanField(default=False)
    deal_price = models.PositiveIntegerField(default=0)
  


    def __str__(self):
        return f"{self.product_name}"
    


class Order(BaseModel):
    productDetail = models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    quanitiy = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.productDetail.product_name



    



