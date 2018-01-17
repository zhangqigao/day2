# __auther__ == zhangqigao
# funcation:record all config file path
import os

#config dir path
config_path = os.path.dirname(os.path.abspath(__file__))

#production file path
production_file_path = os.path.join(config_path,"production")

#user file path
user_info_path = os.path.join(config_path,"user_info")

# user_login_salary file_path
user_salary_path = os.path.join(config_path,"user_login_salary")