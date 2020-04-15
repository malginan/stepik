#  инструкция assert, которая проверяет истинность утверждений
# assert abs(-42) == -42
# можно при вызове assert через запятую написать нужное сообщение, которое будет выведено в случае ошибки
#sssert abs(-42) == -42, "Should be absolute value of a number"
#-----------------------------------------------------------------------------
# форматирование строк
# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
#
# str1 = "one"
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
#
# actual_result = "abrakadabra"
# print(f"Wrong text, got {actual_result}, something wrong")
#
# print(f"{2+3}")
#-----------------------------------------------------------------------------

# ============================================================================
# Задача https://stepik.org/lesson/36285/step/8
"""
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

test_input_text(8,11)
test_input_text(11,11)
test_input_text(11,15)
"""
# ============================================================================
# Задача https://stepik.org/lesson/36285/step/9

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

test_substring("fulltext", "some_value")