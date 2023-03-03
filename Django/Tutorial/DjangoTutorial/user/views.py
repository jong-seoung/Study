from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages
from user.forms import UserRegistrationForm, LoginForm, VerificationEmailForm
from django.contrib.auth.tokens import default_token_generator
from djangotutorial import settings
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from user.mixins import VerifyEmailMixin

from django.views.generic import CreateView, FormView

# 소셜 로그인
from django.conf import settings
from django.views.generic.base import TemplateView, View
from django.middleware.csrf import _compare_masked_tokens
from user.oauth.providers.naver import NaverLoginMixin


class UserRegistrationView(VerifyEmailMixin, CreateView):
    template_name = 'registration_form.html'
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/user/login/'
    verify_url = '/user/verify/'

    def form_valid(self,form):
        response = super().form_valid(form)
        if form.instance:
            self.send_verification_email(form.instance)
        return response

class UserLoginView(LoginView):           # 로그인
    authentication_form = LoginForm
    template_name = 'login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)  

class UserVerificationView(TemplateView):
    model = get_user_model()
    redirect_url = '/user/login/'
    token_generator = default_token_generator

    def get(self, request, *args, **kwargs):
        if self.is_valid_token(**kwargs):
            messages.info(request, '인증이 완료되었습니다.')
        else:
            messages.error(request, '인증이 실패되었습니다.')
        return HttpResponseRedirect(self.redirect_url)   # 인증 성공여부와 상관없이 무조건 로그인 페이지로 이동

    def is_valid_token(self, **kwargs):
        global pk, token, user, is_valid
        pk = kwargs.get('pk')
        token = kwargs.get('token')
        user = self.model.objects.get(pk=pk)
        is_valid = self.token_generator.check_token(user, token)
        if is_valid:
            user.is_active = True
            user.save()     # 데이터가 변경되면 반드시 save() 메소드 호출
        return is_valid

class ResendVerifyEmailView(VerifyEmailMixin, FormView):
    model = get_user_model()
    form_class = VerificationEmailForm
    success_url = '/user/login/'
    template_name = 'resend_verify_form.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = self.model.objects.get(email=email)
        except self.model.DoesNotExist:
            messages.error(self.request, '알 수 없는 사용자 입니다.')
        else:
            self.send_verification_email(user)
        return super().form_valid(form)

class SocialLoginCallbackView(NaverLoginMixin, View):

    success_url = settings.LOGIN_REDIRECT_URL
    failure_url = settings.LOGIN_URL
    required_profiles = ['email', 'name']
    
    model = get_user_model()

    def get(self, request, *args, **kwargs):

        provider = kwargs.get('provider')
        success_url = request.GET.get('next', self.success_url)

        if provider == 'naver': # 프로바이더가 naver 일 경우
            csrf_token = request.GET.get('state')
            code = request.GET.get('code')
            if not _compare_masked_tokens(csrf_token, request.COOKIES.get('csrftoken')): # state(csrf_token)이 잘못된 경우
                messages.error(request, '잘못된 경로로 로그인하셨습니다.', extra_tags='danger')
                return HttpResponseRedirect(self.failure_url)
            is_success, error = self.login_with_naver(csrf_token, code)
            if not is_success: # 로그인 실패할 경우
                messages.error(request, error, extra_tags='danger')
            return HttpResponseRedirect(success_url if is_success else self.failure_url)

        return HttpResponseRedirect(self.failure_url)

    def set_session(self, **kwargs):
        for key, value in kwargs.items():
            self.request.session[key] = value