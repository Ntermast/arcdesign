from django.urls import include, path
from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'arc'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    # path('service/', views.service, name='service'),
    path('service/', include(
	        (
	            [
	                path('', views.service, name='service'),
	                path('imprimerie', views.service, name='service'),
	                path('affichage/', views.affichage, name='service-affichage'),
	                path('decoupage/', views.decoupage, name='service-decoupage'),
	                path('estampage/', views.estampage, name='service-estampage'),
	                path('graphisme/', views.graphisme, name='service-graphisme'),
	                path('software-design/', views.softdesign, name='service-softdesign'),
	                path('grand-format/', views.grandformat, name='service-grandformat'),
	                path('autocollant/', views.autocollant, name='service-autocollant'),
	                path('finition/', views.finition, name='service-finition'),
	            ]
	        ),
	    ) ),
    path('blog/', views.blog, name='blog'),
    # path('command/', views.command, name='command'),

    path('command/', HomeView.as_view(), name='command'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]

