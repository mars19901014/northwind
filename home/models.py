from django.db import models
# import pymysql
# import MySQLdb
from django.db import connection

# Create your models here.

class Categories(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', unique=True, max_length=15)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    ############## 新增 ##############
    def create(self,usercomment):
        with connection.cursor() as cursor:
            sql = """insert into categories(categoryid,categoryname,description,picture) values(%s,%s,%s,%s)"""
            cursor.execute(sql,usercomment)
    ############## 刪除 ##############
    ### 依照一種敘述(where)刪除資料 
    # def delete(self,usercomment):
    #     with connection.cursor() as cursor:
    #         sql = "delete from categories where categoryid = %s"
    #         cursor.execute(sql,usercomment)
    ### 依照多種敘述(where)刪除資料 
    def delete(self,usercomment):
        with connection.cursor() as cursor:
            sql = "delete from categories where (categoryid = %s and categoryname = %s)"
            # cursor.execute(sql,(usercomment,))
            cursor.execute(sql,usercomment)
    ############## 修改 ##############
    def update(self,usercomment):
        with connection.cursor() as cursor:
            sql = """update categories set categoryname = %s, description = %s, picture = %s  where categoryid = %s"""
            cursor.execute(sql,usercomment)
    ############## 查詢 ##############
    def read(self,usercomment):
        with connection.cursor() as cursor:
            # sql = """update categories set categoryname = %s, description = %s, picture = %s  where categoryid = %s"""
            # cursor.execute(sql,usercomment)
            cursor.execute("select * from categories where description = %s",usercomment)
            rows = cursor.fetchall()
            print(rows)

# ((45, 'uuuu', 'dddd', b'dddd'), (50, 'ffvvxx', 'dddd', b'dddd'), (68, 'pppklkj', 'dddd', b'dddd'))



    class Meta:
        managed = False
        db_table = 'categories'


class Customercustomerdemo(models.Model):
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    customertypeid = models.ForeignKey('Customerdemographics', models.DO_NOTHING, db_column='CustomerTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customercustomerdemo'
        unique_together = (('customerid', 'customertypeid'),)


class Customerdemographics(models.Model):
    customertypeid = models.CharField(db_column='CustomerTypeID', primary_key=True, max_length=10)  # Field name made lowercase.
    customerdesc = models.TextField(db_column='CustomerDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customerdemographics'


class Customers(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=5)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)  # Field name made lowercase.
    titleofcourtesy = models.CharField(db_column='TitleOfCourtesy', max_length=25, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=24, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=4, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    reportsto = models.IntegerField(db_column='ReportsTo', blank=True, null=True)  # Field name made lowercase.
    photopath = models.CharField(db_column='PhotoPath', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'


class Employeeterritories(models.Model):
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    territoryid = models.ForeignKey('Territories', models.DO_NOTHING, db_column='TerritoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employeeterritories'
        unique_together = (('employeeid', 'territoryid'),)


class OrderDetails(models.Model):
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    discount = models.FloatField(db_column='Discount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_details'
        unique_together = (('orderid', 'productid'),)


class Orderhist(models.Model):
    productid = models.IntegerField()
    orderid = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderhist'


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    requireddate = models.DateTimeField(db_column='RequiredDate', blank=True, null=True)  # Field name made lowercase.
    shippeddate = models.DateTimeField(db_column='ShippedDate', blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippers', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    freight = models.DecimalField(db_column='Freight', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    shipname = models.CharField(db_column='ShipName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shipaddress = models.CharField(db_column='ShipAddress', max_length=60, blank=True, null=True)  # Field name made lowercase.
    shipcity = models.CharField(db_column='ShipCity', max_length=15, blank=True, null=True)  # Field name made lowercase.
    shipregion = models.CharField(db_column='ShipRegion', max_length=15, blank=True, null=True)  # Field name made lowercase.
    shippostalcode = models.CharField(db_column='ShipPostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shipcountry = models.CharField(db_column='ShipCountry', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=40)  # Field name made lowercase.
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    quantityperunit = models.CharField(db_column='QuantityPerUnit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitsinstock = models.IntegerField(db_column='UnitsInStock', blank=True, null=True)  # Field name made lowercase.
    unitsonorder = models.IntegerField(db_column='UnitsOnOrder', blank=True, null=True)  # Field name made lowercase.
    reorderlevel = models.IntegerField(db_column='ReorderLevel', blank=True, null=True)  # Field name made lowercase.
    discontinued = models.IntegerField(db_column='Discontinued')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'


class Region(models.Model):
    regionid = models.IntegerField(db_column='RegionID', primary_key=True)  # Field name made lowercase.
    regiondescription = models.CharField(db_column='RegionDescription', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Shippers(models.Model):
    shipperid = models.AutoField(db_column='ShipperID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shippers'


class Suppliers(models.Model):
    supplierid = models.AutoField(db_column='SupplierID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)  # Field name made lowercase.
    homepage = models.TextField(db_column='HomePage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suppliers'


class Territories(models.Model):
    territoryid = models.CharField(db_column='TerritoryID', primary_key=True, max_length=20)  # Field name made lowercase.
    territorydescription = models.CharField(db_column='TerritoryDescription', max_length=50)  # Field name made lowercase.
    regionid = models.ForeignKey(Region, models.DO_NOTHING, db_column='RegionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territories'
