from django.db import models


class ProductsInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=20)
    store = models.CharField(max_length=50)
    brief_introduction = models.CharField(max_length=400)
    price = models.FloatField(blank=True, null=True)
    variety = models.CharField(max_length=100)
    product_id = models.BigIntegerField()
    authenticate_moder = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    crawl_time_stamp = models.IntegerField()
    crawl_time = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.brand

    class Meta:
        managed = False
        db_table = 'products_info'
        verbose_name = 'Scrapy爬取的京东商品信息'
        verbose_name_plural = verbose_name


class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=100)
    passwd_encode = models.Field()
    email = models.Field(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        managed = False
        db_table = 'users_info'
        verbose_name = 'Django用户账号信息'
        verbose_name_plural = verbose_name



