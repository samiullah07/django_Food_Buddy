from django.db import models
import uuid
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

class ProductDetail(BaseModel):
    product_name = models.ForeignKey(Category,related_name="cat_pro_name",on_delete=models.CASCADE)
    product_des = models.TextField()
    prduct_price = models.IntegerField()
    product_image = models.ImageField(upload_to="media")


    def __str__(self):
        return f"{self.product_name}"
    

    

