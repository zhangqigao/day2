# __auther__ == zhangqigao
#funcation:用户名

from shopping_cart.config import settings

def user_salary_login():
    user_salary_login_list = []
    with open(settings.user_salary_path,"rb") as user_salary_login_file:
        all_user_login_salary_bytes = user_salary_login_file.read()
        all_user_login_salary_bytes = all_user_login_salary_bytes.decode()
        user_salary_login_List = all_user_login_salary_bytes.splitlines()
        for user_salary_login in user_salary_login_List:
            user_salary_login = tuple(user_salary_login.split())
            user_salary_login_list.append(user_salary_login)

    return user_salary_login_list