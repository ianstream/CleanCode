from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.implicitly_wait(3)

browser.get('http://localhost:8000')

# 웹 페이지 타이틀과 헤더가 To-Do 를 표시하고 있다
assert 'To-Do' in browser.title

