# __auther__ == zhangqigao
# funcations:商品展示

from shopping_cart.modules.product import production_info


def product_show():
    product_info_str_list = []
    all_product_info_list = production_info.production_info()
    for index,production_tuple in enumerate(all_product_info_list):
        product_name,product_price = production_tuple
        product_info_str = "|-id:{0},name:{1},price:{2}".format(index,product_name,product_price)
        product_info_str_list.append(product_info_str)
    all_product_info_str = "\n".join(product_info_str_list)

    return all_product_info_str

