from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(3)

    def tearDown(self):
        print("tearDown")
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        print("test_can_start_a_list_and_retrieve_it_later start")

        # 에디스는 웹 사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 To-Do 를 표시하고 있다
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 그녀는 작업을 추가한다

        # '공작깃털 사기'라고 텍스트 상자에 입력한다

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1: 공작깃털 사기" 아이템이 추가된다

        # 추가된 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "공작깃털을 이용해서 그물 만들기" 라고 입력한다

        # 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다
        # 에디스는 사이트가 입력한 목록을 저장하고 있는지 궁금하다
        # 사이트는 그녀를 위한 특정 url 을 생성해준다
        # 이 때 url 에 대한 설명도 함께 제공된다

        # 해당 url 에 접속하면 그녀가 만든 작업 목록이 그대로 있는 것을 확인할 수 있다

        # 만족하고 꿈나라로

        print("test_can_start_a_list_and_retrieve_it_later end")

if __name__ == "__main__":
    unittest.main(warnings='ignore')

