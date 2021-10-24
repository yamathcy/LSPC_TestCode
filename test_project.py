import pytest
from function import is_even

# pytestの場合はtest_*.pyという名前のファイルの関数がテストされる

def test_is_even():
    """
    is_evenに対するテスト
    :return:
    """
    # テストケースとして2を入力
    a = 2

    # 関数に入力
    result = is_even(a)

    # 標準出力で一応チェックする
    print("return: ", result)

    # 2は偶数なのでTrueを返してほしい．
    # pythonのassert文は判定文がFalseだとエラーを出す
    assert result == True

'''
# 複数のテストケースを試したい場合，pytestをインポートして以下のデコレータをつける
@pytest.mark.parametrize(
    "a", [0, 1, 2, 3]
)
def test_is_even_multiple(a):
    # 上で作ったテストケースを実行する
    result = is_even(a)
    print("return: ", result)
    assert result == True


def test_check_float_input():
    # テストケースとして2を入力
    a = 0.2

    # 関数に入力
    result = is_even(a)

    # 標準出力で一応チェックする
    print("return: ", result)

    # 2は偶数なのでTrueを返してほしい．
    # pythonのassert文は判定文がFalseだとエラーを出す
    assert result == False
'''