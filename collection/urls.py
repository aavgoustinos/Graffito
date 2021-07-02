from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.collections_home, name="collection/collection_home.html"),
        path('/items', views.items, name="collection/items"),
        path('/sides', views.sides, name="collection/sides"),
        path('/item/<slug:slug>/', views.item, name="collection/item"),
        path('/side/<slug:slug>/', views.side, name="collection/side"),



        path('/sides_json', views.json_sides, name="collection/sides_json"),
        path('/items_json', views.json_items, name="collection/items_json"),

        path('load_json', views.load_json, name="collection/load_json"),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
