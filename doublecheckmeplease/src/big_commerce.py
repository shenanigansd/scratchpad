import json
import os
from random import randint

import requests

from databases.postgresql import connect

headers = {
    "X-Auth-Client": os.getenv('client'),
    "X-Auth-Token": os.getenv('token'),
    "Accept": "application/json",
    "Content-Type": "application/json"
}

sizes_list = ['XS', 'S', 'M', 'L', 'XL', '2X', '3X', '4X', '5X', '6X']
logo_options = ['Black Text Logo', 'White Text Logo']


def lookup_product(style_number):
    connection = connect()
    cursor = connection.cursor()

    rows = cursor.execute(
        "SELECT DISTINCT available_sizes, color_name, product_title, product_description, case_price, "
        "piece_weight, front_model_image_url, back_model_image_url FROM sanmar_sdl_s s WHERE s.\"STYLE#\" IN ("
        "\'%s\')" % style_number)

    keys = [k[0].decode('ascii') for k in cursor.description]
    product_information = [dict(zip(keys, row)) for row in rows]

    rows = cursor.execute(
        "SELECT DISTINCT  \"STYLE#\", size, color_name, case_price, front_model_image_url "
        "FROM sanmar_sdl_s s WHERE s.\"STYLE#\" IN (\'%s\')" % style_number)
    keys = [k[0].decode('ascii') for k in cursor.description]
    colors_and_sizes = [dict(zip(keys, row)) for row in rows]

    return product_information, colors_and_sizes


def create_variations(product_information):
    variations = []
    count = 0
    for result in product_information:
        if count <= 600:
            count += 1
            for logo_option in logo_options:
                variations.append(
                    {"sku": "SKU2-%s-%s-%s-%s-%s" % (
                        randint(100, 999), result["STYLE#"], result["color_name"], result["size"], logo_option),
                     "price": str((float(result["case_price"]) * 1.3 + 7.50) * 1.2),
                     "image_url": result["front_model_image_url"],
                     "option_values": [{"option_display_name": "Color", "label": result["color_name"]},
                                       {"option_display_name": "Size", "label": result["size"]},
                                       {"option_display_name": "Logo", "label": logo_option}]})
    return variations


def create_images(product_information):
    images = [{
        "is_thumbnail": True,
        "sort_order": 1,
        "image_url": product_information[0]["front_model_image_url"]
    }, {
        "is_thumbnail": False,
        "sort_order": 2,
        "image_url": product_information[0]["back_model_image_url"]
    }, {
        "is_thumbnail": False,
        "sort_order": 3,
        "image_url": "http://darbia.io/LOGO_OPTIONS.PNG"
    }]
    return images


def create_product_from_sanmar(product_information, colors_and_sizes):
    product_information = product_information[0]
    return {"name": product_information["product_title"],
            "price": str((float(product_information["case_price"]) * 1.3 + 7.50) * 1.2),
            "weight": str(product_information["piece_weight"]), "type": "physical", "categories": [25],
            "variants": create_variations(colors_and_sizes)}


def post_product(product):
    url = "https://api.bigcommerce.com/stores/%s/v3/catalog/products" % os.getenv('store')
    response = requests.post(url=url, headers=headers, data=product)
    return response


def post_product_images(product_id, images):
    for image in images:
        url = "https://api.bigcommerce.com/stores/%s/v3/catalog/products/%s/images" % (os.getenv('store'), product_id)
        response = requests.post(url=url, headers=headers, data=json.dumps(image))
        print(response.text)


def create_new_product(style_number):
    product_information, colors_and_sizes = lookup_product(style_number)
    if len(product_information) > 0:
        product = create_product_from_sanmar(product_information, colors_and_sizes)
        product_response = post_product(json.dumps(product))
        print(product_response.text)
        if product_response.ok:
            product_id = json.loads(product_response.text)["data"]["id"]
            post_product_images(product_id, create_images(product_information))


styles = ['LK584', 'K584', 'F235', 'L235', 'PC90ZH', 'LPC78ZH', 'PC78', 'PC90', 'C914', 'CP80', 'LPWU',
          'C112', 'NE200', 'CTA205', 'CP90', 'STC10', 'K100', 'L100', 'K600', 'LK600', 'K540', 'L540', 'K540P', 'K525',
          'L525', 'ST652', 'ST655', 'LST652', 'LST655', 'S608', 'L608', 'W100', 'LW100', 'LK583', 'K583', 'CT102418',
          'CT102417']

for style in styles:
    create_new_product(style)
