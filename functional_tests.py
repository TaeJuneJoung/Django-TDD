from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): #unittest.TestCase를 상속해서 클래스 형태로 만든다
    """
    setUp, tearDown은 특수한 메소드로, 각 테스트 시작 전과 후에 실행
    테스트에 에러가 발생해도 tearDown이 실행된다.

    암묵적 대기 implicitly_wait
    : 셀레늄은 비교적 안정적으로 페이지 로딩이 끝날 때까지 기다렸다가
    테스트를 진행하지만 완벽하진 않기에 암묵적 대기를 사용
    [주의할점]
    implicitly_wait도 완벽하지 않기에
    복잡한 애플리케이션에서는 세련되면서도 명시적인 대기 알고리즘을 구현해야한다.
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) #3초 대기

    def tearDown(self):
        self.browser.quit()

    def test_can_start(self):
        self.browser.get('http://localhost:8000')
        #assert를 대신해서 사용(assertEqual, assertTrue, assertFalse, assertIn)
        self.assertIn('TDD', self.browser.title)
        #강제적 테스트 실패 발생시켜 에러 메시지 출력
        self.fail('Finish the test!')

#파이썬 스크립트가 다른 스크립트에 임포트된 것이 아닌, 커맨드라인을 통해 실행됐다는 것을 확인하는 코드
if __name__ == '__main__':
    """
    unittest.main() -> unittest 테스트 실행자를 가동
    : 자동으로 파일 내 테스트 클래스와 메소드를 찾아 실행해주는 역할
    """
    unittest.main(warnings='ignore') #warnings='ignore': 테스트 작성시 발생하는 불필요한 리소스 경고 제거