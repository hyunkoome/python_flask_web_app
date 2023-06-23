# import pytest
def test_func1():
    assert 1 == 1


def test_func2():
    assert 2 == 2


# Flask의 테스트 클라이언트를 반환하는 픽스처 함수를 작성한다
# @pytest.fixture 를 추가 한다
# @pytest.fixture
# def app_data():
#     return 3

# 픽스처의 함수를 인수로 지정하면 함수의 실행 결과가 건네진다
def test_func3(app_data):
    assert app_data == 3
