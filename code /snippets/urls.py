from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# router를 생성하고 viewset을 등록한다
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippets")
router.register(r'users', views.UserViewSet, basename="users")

# API URL은 router에 의해 자동적으로 결정되어진다
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])


# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/', views.SnippetList.as_view(),
#          name='snippet-list'),
#     path('snippets/<int:pk>/',
#          views.SnippetDetail.as_view(),
#          name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#          views.SnippetHighlight.as_view(),
#          name='snippet-highlight'),
#     path('users/',
#          views.UserList.as_view(),
#          name='user-list'),
#     path('users/<int:pk>/',
#          views.UserDetail.as_view(),
#          name='user-detail')
# ]

# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]




# urlpatterns = format_suffix_patterns(urlpatterns)