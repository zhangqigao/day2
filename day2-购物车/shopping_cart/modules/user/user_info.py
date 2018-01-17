# __auther__ == zhangqigao
#funcation:显示用户信息

from shopping_cart.config.settings import user_info_path

def user_info():
    all_user_info = []
    with open(user_info_path,"rb") as user_info_file:
        all_user_info_bytes = user_info_file.read()
        all_user_info_bytes = all_user_info_bytes.decode()
        user_info_list = all_user_info_bytes.splitlines()
        for user in user_info_list:
            user_info_tuple = tuple(user.split())
            all_user_info.append(user_info_tuple)

        return all_user_info

