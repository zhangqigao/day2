# __auther__ == zhangqigao
#funcation:消费记录
import os
from shopping_cart.config import settings

def show_spending_record(user_name):
    user_spending_recod_file_name = "{0}_spending_record".format(user_name)
    user_spending_recod_path = os.path.join(settings.config_path,user_spending_recod_file_name)
    with open(user_spending_recod_path,"rb") as show_spending_record_file:
        all_spending_recode = show_spending_record_file.read()
        all_spending_recode = all_spending_recode.decode()

    return all_spending_recode





