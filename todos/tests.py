from django.urls import resolve 
# resolve는 Django가 내부적으로 사용하는 함수로,
# URL을 해석해서 일치하는 뷰 함수를 찾는다.
from django.test import TestCase
from django.http import HttpRequest
from todos.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_views(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # HttpRequest 객체를 생성해서 사용자가 어떤 요청을 브라우저에 보내는지 확인
        request = HttpRequest()
        # 이 객체는 HttpResponse라는 클래스의 인스턴스다
        # 응답 내용(HTML 형태로 사용자에게 보내는 것)이 특정 속성을 가지고 있는지 확인
        response = home_page(request)
        # <html> </html>로 끝나는지 확인
        # response.content는 byte형 데이터로, 파이썬 문자열이 아니다.
        self.assertTrue(response.content.startswith(b'<html>'))
        # 앞선 기능 테스트에서 확인한 것이기 때문에 단위 테스트도 확인해어야 한다.
        self.assertIn(b'<title>TDD Python</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))