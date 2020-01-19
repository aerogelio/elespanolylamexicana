from django.urls import path
from elespanolylamexicanaapp.views.home_view import HomeView
from elespanolylamexicanaapp.views.signin_view import SignInView
from elespanolylamexicanaapp.views.login_view import LogInView
from elespanolylamexicanaapp.views.dashboard_view import DashboardView
from elespanolylamexicanaapp.views.order_view import OrderView
from elespanolylamexicanaapp.views.order_show_view import OrderShowView
from elespanolylamexicanaapp.views.refresh_order_view import RefreshOrderServiceView
from elespanolylamexicanaapp.views.successfully_registered import SuccessfullyRegisteredView
from elespanolylamexicanaapp.views.logout_view import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path( '',  HomeView.as_view(), name='home'),
    path( 'signin', SignInView.as_view(), name='signin' ),
    path( 'login', LogInView.as_view(), name='login'),
    path( 'successfully-registered', SuccessfullyRegisteredView.as_view(), name='successfully-registered' ),
    path( 'dashboard', DashboardView.as_view(), name='dashboard' ),
    path( 'order', OrderView.as_view(), name='order' ),
    path( 'order/show/<int:order_id>', OrderShowView.as_view(), name='order_show' ),
    path( 'refresh-orders', RefreshOrderServiceView.as_view(), name='refresh-order' ),
    path( 'logout', LogoutView.as_view(), name='logout' ),
] + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )