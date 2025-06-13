from django.urls import path
from .views.home_views import (
    Home, Create_blog, Single_blog, Your_blogs,
    Delete_blog, Edit_blog, Read_blog, Contact, About_blogs
)
from .views.auth_views import Register, Login, Logout, VerifyOTP  # Import VerifyOTP
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("home", Home, name="home"),
    path("contact", Contact, name="contact"),
    path("about", About_blogs, name="About"),
    path("register", Register, name="register"),
    path("verify_otp", VerifyOTP, name="verify_otp"),  # Added OTP verification URL
    path("login", Login, name="login"),
    path("logout", Logout, name="logout"),
    path("create", Create_blog, name="Create_blog"),
    path("read", Read_blog, name="Read_blog"),
    path("single_page/<int:blog_id>", Single_blog, name="Single_blog"),
    path("your", Your_blogs, name="Your_blogs"),
    path("delete_blog/<int:blog_id>", Delete_blog, name="Delete_blog"),
    path("edit_blog/<int:blog_id>", Edit_blog, name="Edit_blog"),
]

# (optional) add static/media URLs if needed
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
