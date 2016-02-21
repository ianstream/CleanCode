from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


# Create your tests here.
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1, 2)

class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        print("*** test_root_url_resolve_to_home_page_view ***")
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        # https://docs.djangoproject.com/en/1.9/ref/request-response/
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'}
        )
        print(expected_html)
        print("*************************")
        print(response.content.decode())

        """
        아래 두 값은 같을수가 없음
        전자는 csrf 로 암호화된 코드가 포함된 반면, 후자는 평문 html 만을 포함한다
        """
        self.assertEqual(response.content.decode(), expected_html)



