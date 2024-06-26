from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import Userform

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),  # Added parentheses
    path('post/new/', views.CreatePostView.as_view(), name="post_new"),  # Added parentheses
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Added missing slash
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),  # Added missing slash
    path('draft/', views.DraftListView.as_view(), name='draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_commment_to_post'),  # Fixed typo in name
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('signup/',views.Userform.as_view(),name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)