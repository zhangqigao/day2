# __auther__ == zhangqigao
#funcation:商品信息

from shopping_cart.config import settings

def production_info():
    product_list = []
    all_product_info_list = []
    with open(settings.production_file_path,"rb") as production_file:
        all_production_file_bytes = production_file.read()
        #根据字节读数据，需要解码
        all_production_file_bytes = all_production_file_bytes.decode()
        all_production_list = all_production_file_bytes.splitlines()
        #获取商品价格列表
        for product_info in all_production_list:
            product_name,product_price = product_info.split()
            product_list.append(product_name)
            product_list.append(product_price)
            product_tuple = tuple(product_list)
            all_product_info_list.append(product_tuple)
            product_list.clear()

    return all_product_info_list
