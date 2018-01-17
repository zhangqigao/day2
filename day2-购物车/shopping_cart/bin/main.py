# __auther__ == zhangqigao
# funcation:主函数
import os,sys
from shopping_cart.modules.user import user_info,user_salary_login
from shopping_cart.modules.product import product_show,production_info
from shopping_cart.config import settings
from shopping_cart.plugins import reduce_money,show_spending_record
#执行路径地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# 定义购物车列表
cart_list = []

if __name__ == "__main__":
    all_user_info = user_info.user_info()
    user_salary_login_list = user_salary_login.user_salary_login()
    user_salary_login_dict = dict(user_salary_login_list)
    all_user_info_dict = dict(all_user_info)
    # 用户登录
    while True:
        login_flag = False
        user_name = input("请输入用户:").strip()
        if user_name in all_user_info_dict:
            while True:
                password = input("请输入密码:").strip()
                if password == all_user_info_dict.get(user_name):
                    login_flag = True
                    print("\033[42m{0}\033[0m登录成功，欢迎...".format(user_name))
                    break
                else:
                    print("\033[43m{0}\033[0m,密码输入错误...".format(user_name))
            if login_flag:
                break
        elif user_name == "q":
            exit("您选择的是退出...")
        else:
            print("\033[41m{0}\033[0m，此用户名输入错误...".format(user_name))
    #商品清单
    all_product_info_str = product_show.product_show()
    #新客户
    if user_name not in user_salary_login_dict:
        # 显示工资
        salary = input("输入工资：")
        if salary == "q":
            exit("您选择的是退出...")
        else:
            print("商品清单")
            print(all_product_info_str)
            print("您的工资是：\033[31m{0}\033[0m".format(salary))
    # 老客户
    else:
        print("\033[34m您上次的消费记录:\033[0m")
        show_spending_record_str = show_spending_record.show_spending_record(user_name)
        print(show_spending_record_str)
        salary = int(user_salary_login_dict.get(user_name))
        print("您的余额是：\033[31m{0}\033[0m".format(salary))
        while True:
            goon_buy_product = input("是否继续购买(y/n):")
            if goon_buy_product == "y":
                print("\033[42m请继续购买....\033[0m")
                break
            elif goon_buy_product == "n":
                exit("退出，不继续购买....")
            else:
                print("\033[41m输入错误，请重新输入...\033[0m")
    #添加商品
    salary = int(salary)
    all_product_info_list = production_info.production_info()
    all_product_info_len = len(all_product_info_list)
    while True:
        product_id_flag = True
        print("商品清单")
        print(all_product_info_str)
        while True:
            product_id = input("请输入购买的商品id：").strip()
            if product_id.isdigit():
                product_id = int(product_id)
                if product_id < all_product_info_len:
                    break
                else:
                    print("商品id：\033[31m{0}\033[0m,不存在...".format(product_id))
                    product_id_flag = False
                    break
            elif product_id == "q":
                exit("您选择的是退出...")
            else:
                product_id_flag = False
                print("\033[41m您输入的是id为空\033[0m，请重新输入...")
                break
        # 添加购物车
        if product_id_flag:
            account_flag = True
            cart_info_str_list = []
            cart_list.append(all_product_info_list[product_id])
            #购物车列表
            for index,product in enumerate(cart_list):
                product_name,product_price = product
                cart_info_str = "|-id:{0},name:{1},price:{2}".format(index,product_name,product_price)
                print("|-id:\033[42m{0},name:{1},price:{2}\033[0m加入购物车".format(index,product_name,product_price))
                cart_info_str_list.append(cart_info_str)
            cart_info = '\n'.join(cart_info_str_list)
            print("\033[32m购物车清单\033[0m")
            print(cart_info)
            #是否进入结算页
            while True:
                is_accounts = input("是否需要结算(y/n):")
                if is_accounts == "y":
                    account_flag = False
                    break
                elif is_accounts == "n":
                    print("请您继续选择商品...")
                    break
                else:
                    print("输入的是否结算字符错误，重新输入...")
            if not account_flag:
                print("进入结算页...")
                break
    # 结算
    all_account_money  = 0
    for cart_product in cart_list:
        all_account_money += int(cart_product[1])
    if all_account_money > salary:
        exit("余额不足,正在退出...")
    else:
        balance = reduce_money.reduce_money(salary,all_account_money)
    print("\033[31m消费清单：\033[0m")
    print(cart_info)
    print("您本次消费金额:\033[41m{0}\033[0m,剩余金额:\033[42m{1}\033[0m".format(all_account_money,balance))
    #记录消费记录
    user_spending_recod_file_name = "{0}_spending_record".format(user_name)
    user_spending_recod_path = os.path.join(settings.config_path,user_spending_recod_file_name)
    with open(user_spending_recod_path,"wb") as show_spending_record_file:
        cart_info = cart_info.encode()
        show_spending_record_file.write(cart_info)
    #输入用户消费信息
    user_name_info_list = []
    if user_name in user_salary_login_dict:
        user_salary_login_dict[user_name] = balance
        for user_name in user_salary_login_dict:
            user_name_info_str = "{0} {1}".format(user_name,user_salary_login_dict.get(user_name))
            user_name_info_list.append(user_name_info_str)
        all_user_name_info_str = "\n".join(user_name_info_list)
        with open(settings.user_salary_path,"wb") as user_salary_login_file:
            all_user_name_info_str = all_user_name_info_str.encode()
            user_salary_login_file.write(all_user_name_info_str)
    else:
        with open(settings.user_salary_path,"ab") as user_salary_login_file:
            user_salary_login_str = "{0} {1}\n".format(user_name,balance).encode()
            user_salary_login_file.write(user_salary_login_str)
