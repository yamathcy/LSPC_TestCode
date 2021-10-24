def is_even(num: int) -> bool:
    """
    入力した整数が偶数ならTrue, 奇数ならFalseを返す関数
    :param num: 偶奇判定をしたい整数 int
    :return: 偶数かどうか bool
    """
    assert type(num) == int

    if num % 2 == 0:
        return False
    else:
        return True
