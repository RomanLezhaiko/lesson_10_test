""" 
4. Сделать функцию валидации email адресов при помощи регулярных выражений. Общий
вид email адреса "username@hostname"

(a) username может состоять из латиницы, цифр, таких символов как !#%&'+-/=?^_`{~}|
и точки, за исключением первого и последнего знака, которая не может повторяться

(b) hostname состоит из нескольких компонентов, разделенных точкой и не превышающих
63 символа. Компоненты, в свою очередь, состоят из латинских букв, цифр 
и дефисов, причем дефисы не могут быть в начале или в конце компонента.
"""
import re


def email_validation(email: str) -> bool:
    """ 
    Checks email for the following conditions:
    (a) username may consist of latin characters, numbers, characters such 
    as !#%&'+-/=?^_`{~}| and a dot, except for the first and last character, which cannot be repeated.
    (b) hostname consists of multiple components, separated by a dot, and not exceeding 63 characters. 
    Components, in turn, consist of Latin letters, numbers and hyphens, and hyphens cannot be at the 
    beginning or at the end of the component.
    
    :param email: email which need check for valid
    :returns: return True if email valid, False otherwise
    """
    try:
        username, hostname = email.split('@')
        
        user_regular_pattern = r''
        user_match = re.match(user_regular_pattern, username)
        if not user_match:
            return False
        
        host_regular_pattern = r''
        host_match = re.match(host_regular_pattern, hostname)
        if not host_match:
            return False
    except ValueError:
        return False
    
   
    return True


# print(email_validation('example@gmail@com'))
# print(email_validation('example@gmail.com'))


pattern = r'[d]{2}'
test_str = 'fgfdgh6bfbgcx'
# result = re.match(pattern, test_str)
result = re.search(pattern, test_str)
print(result)