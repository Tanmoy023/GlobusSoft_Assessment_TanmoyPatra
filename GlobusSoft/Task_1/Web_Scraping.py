import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# Get HTML
def get_html(URL=None):
    if URL == None:
        URL = input("Enter the product URL from amazon.in: ")
    
    if not URL.startswith("https://www.amazon.in"):
        print("Product URL is not from amazon.in!")
        return False

    html_text = requests.get(URL).content
    html = BeautifulSoup(html_text, 'html.parser')
    return html


def is_laptop(html):
    # Check Product
    c1 = html.select_one("#wayfinding-breadcrumbs_feature_div")
    c2 = c1.select(".a-color-tertiary")[2]
    if c2.string.strip() == "Laptops":
        return True
    else:
        return False


# Get product Details
def get_details(html):
    # Get productTitle
    try:
        productTitle = html.select("#productTitle")[0].string
        productTitle = productTitle.strip()
    except:
        productTitle = "Not Found!"

    # Get rating
    try:
        c1 = html.select("#acrPopover")[0]
        rating = c1.select(".a-size-small")[0].string
        rating = str(rating.strip())
    except:
        rating = "Not Found!"
        

    # Get price
    try:
        c1 = html.select("body > #a-page > #dp > #dp-container > #ppd > #centerCol > #apex_desktop")[0]
        c2 = c1.select_one("div")
        c3 = c2.select_one("div")
        c4 = c3.select_one("#corePriceDisplay_desktop_feature_div")
        price = str(c4.select_one(".a-price-whole").string)
    except:
        price = "Not Found!"
        

    # Get product info table
    try:
        c1 = html.select_one("#poExpander")
        table = c1.select_one("table")
        tr = table.select("tr")
        product_info_table = {}
        for i in tr:
            td1 = i.select("td > span")[0]
            td2 = i.select("td > span")[1]
            product_info_table[td1.string] = td2.string
    except:
        product_info_table = {'info': 'All info not loades properly'}
        


    # Get product image table
    try:
        c1 = html.select_one("#main-image-container")
        c2 = c1.select(".imgTagWrapper")
        product_image_table = []
        for i in c2:
            img = i.select(".a-image-wrapper")
            if len(img) == 1:
                img = img[0]
                product_image_table.append(img["data-old-hires"])
        
        images = ""
        if len(product_image_table) > 0:
            for link in product_image_table:
                images += f", {link}"

        images = images[2:]
    except:
        images = "Not Found!"
        
    
    # Get ads
    try:
        adds = ""
        c1 = html.select_one(".cardRoot")
        c2 = c1.select_one("._p13n-desktop-sims-fbt_fbt-desktop_flex-fbt-container__3fI_9")
        c3 = c2.select("._p13n-desktop-sims-fbt_fbt-desktop_new-thumbnail-box__36bD3")[0]
        c4 = c3.select(".a-size-base")
        for i in c4[2:]:
            adds += str(i.string.strip()) + ", "
        adds = adds[:-2]
    except:
        adds= "Not Found!"

    return productTitle, rating, price, product_info_table, images, adds


# Combine all information into a single dictionary
def create_full_data_dict(productTitle, rating, price, product_info_table, images, adds):
    full_data = {}
    
    timestamp = datetime.now().strftime("%d/%m/%y-%H-%M-%S")
    full_data["timestamp"] = timestamp
    
    full_data["productTitle"] = productTitle
    full_data["rating"] = rating
    full_data["price"] = price
    
    for key, value in product_info_table.items():
        # print(key, "---", value)
        full_data[key] = value
            
    full_data["images"] = images
    
    full_data["adds"] = adds

    return full_data

# Save data in CSV with duplicate check
def save_data(data):
    data_df = pd.DataFrame([data])
    
    if os.path.exists("./amazon-laptop-dataset.csv"):
        prev_df = pd.read_csv("./amazon-laptop-dataset.csv")
        
        new_data_df_no_timestamp = data_df.drop(columns=['timestamp'])
        prev_data_df_no_timestamp = prev_df.drop(columns=['timestamp'])
        
        new = new_data_df_no_timestamp.astype(str)
        prev = prev_data_df_no_timestamp.astype(str)
        
        is_deplicate = (
            (prev == new.iloc[0]).all(axis=1).any()
        )

        if is_deplicate:
            print("Duplicate Data!")
        else:
            data_df.to_csv("./amazon-laptop-dataset.csv", mode="a", header=False, index=False)
            print("New Data is added!")
    else:
        data_df.to_csv("./amazon-laptop-dataset.csv", index=False)
        print("New Dataframe!")


if __name__ == "__main__":
    html = get_html()

    if not html:
        print("Invalid input!")
    else:
        ch = is_laptop(html)
        if not ch:
            print("This web scripting is only for Laptops!")
        else:
            productTitle, rating, price, product_info_table, images, adds = get_details(html)
            
            full_data = create_full_data_dict(productTitle, rating, price, product_info_table, images, adds)
            
            save_data(full_data)
            

# https://www.amazon.in/HP-Anti-Glare-Micro-Edge-fc0690au-Graphics/dp/B0CY2PLQ8N/ref=sr_1_3?sr=8-3