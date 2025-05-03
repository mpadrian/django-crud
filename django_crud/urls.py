from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post import views
from post.views import PostListView, PostDetail, PostUpdate
from authentication.views import HomeView

urlpatterns = [
    # Página principal
    path('', HomeView.as_view(), name='home'),

    # Administración
    path('admin/', admin.site.urls),

    # CRUD de posts
    path('post-create/', views.upload_image, name='upload_image'),
    path('posts/',       PostListView.as_view(), name='post_list'),
    path('post/detail/<int:pk>/',        PostDetail.as_view(), name='post_detail'),
    path('post/detail/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),

    # Autenticación (login, signup, logout)
    path('authentication/', include('authentication.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
