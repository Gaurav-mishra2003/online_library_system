from django.contrib import admin
from .models import BorrowRecord,Author,Book

# # Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
#     list_display=['name','email','bio']


# class BookAdmin(admin.ModelAdmin):
#     list_display=['title','genre','published_date','author']



# class BorrowRecordAdmin(admin.ModelAdmin):
#     list_display=['user_name','book','borrow_date',' return_date ']


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BorrowRecord)