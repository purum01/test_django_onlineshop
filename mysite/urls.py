from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('qna/', include('qna.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('coupons/', include('coupons.urls')),
    path('', include('shop.urls')),

]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
