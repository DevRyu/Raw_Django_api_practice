from django.urls import path, include

urlpatterns = [
    path('comment', include('comment.urls')),
    path('user', include('user.urls')),
    # path('write', include('write.urls')),
]
