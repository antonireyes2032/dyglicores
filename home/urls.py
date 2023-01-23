from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^GetInventory/$',GetInventory,name="GetInventory"),
		url(r'^SetInventory/$',SetInventory,name="SetInventory"),
		url(r'^Update_Product/$',Update_Product,name="Update_Product"),
		url(r'^Delete_Product/$',Delete_Product,name="Delete_Product"),
		url(r'^all_true/$',all_true,name="all_true"),
		url(r'^Update_Product_Sede/$',Update_Product_Sede,name="Update_Product_Sede"),
		url(r'^New_Product_Sede/$',New_Product_Sede,name="New_Product_Sede"),
		url(r'^Delete_Record/$',Delete_Record,name="Delete_Record"),
]