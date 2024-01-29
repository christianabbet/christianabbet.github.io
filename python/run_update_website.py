from glob import glob
from utils.recipe_builder import RecipeList
import numpy as np
import pandas as pd
from utils.htlm_template import get_html_article, get_html_index, get_html_recipe, get_html_ingredient
import os
from PIL import Image
import sys


def resize_image(path, hmax=600, wmax=800, extension=".jpg", suffix="_resize"):
    # Split with extension
    path_new, ext = os.path.splitext(path)

    # Open image and resize it
    img = Image.open(path)
    img_size = img.size
    
    # Rescale to match minimal size (reference)
    factor = min(img_size[0] / wmax, img_size[1] / hmax)
    img_crop = img.resize(size=( int(img_size[0] / factor), int(img_size[1] / factor)))
        
    # Cropped image to fit dimmension
    left = int((img_crop.size[0] - wmax)/2)
    top = int((img_crop.size[1] - hmax)/2) 
    img_crop = img_crop.crop((left, top, left + wmax, hmax + top))

    # New output name and save
    path_new = path_new + suffix + extension
    img_crop.save(path_new)
    
    return path_new

def main():
    
    # Creating an update of the website
    print("Updating website")
    
    # 1 Read and parse all recipes to get categories
    raw_files = glob("data/recipe/*/*.xml")
    list = RecipeList(xml_path=raw_files)
    
    # 2. Build dataframe
    df = []
    for i, r in enumerate(list.recipes):
        data_info = r.info
        data_info.update({"id_recipe": i})
        df.append(r.info)
    df = pd.DataFrame(df)
    
    # 2.1 Print stats
    print("Categories: ", df["category"].value_counts())
    
    
    # 3. Build category index
    # Change working directory to match index ressources
    os.chdir("ressources")
    
    for n, dfcat in df.groupby(by="category"):
        print("Building index page {} ...".format(n))
            
        # Define folders and variables
        a_str = ""
        filename_index = "{}_index.html".format(n)
        
        # Create articles
        for i, (_, article) in enumerate(dfcat.iterrows()):
            
            filename_recipe = "{}.html".format(article['name'].lower().replace(" ", "_"))
            folder_recipe = os.path.join("recipes", n)
        
            try:
                # Check if image exists otherwise set dummy
                img_index = '../data/images/pic01.jpg'
                img_recipe = '../data/images/pic01.jpg'
                
                if article['pic'] is not None and os.path.exists(article['pic']):
                    # Open image and check for size
                    img_index = resize_image(article['pic'], hmax=600, wmax=800, extension=".jpg", suffix="_resize")
                    img_recipe = resize_image(article['pic'], hmax=300, wmax=800, extension=".jpg", suffix="_banner")
                else:
                    print("Missing picture: {}".format(article['pic']))
                    
                    
                # Create article
                a = get_html_article(
                    style = 1 + (i % 6),
                    img=img_index,
                    title=article['name'],
                    npers=article['people'],
                    time_prep=article['time_prep'] + " " + article['time_prep_unit'],
                    time_bake=article['time_bake'] + " " + article['time_bake_unit'],
                    url=os.path.join(folder_recipe, filename_recipe)
                )

                a_str = a_str + "\n" + a
                
                # Create ingredient list
                raw_data = list.recipes[article['id_recipe']]
                ingredient_tables = []
                for g in raw_data.ingredient_groups:
                    ingredient_table = get_html_ingredient(
                        title=g['name'], 
                        ingredients=g['ingredients'],
                    )
                    ingredient_tables.append(ingredient_table)
                # Merge all table content
                ingredient_tables = "\n".join(ingredient_tables)
                
                # Create recepe index page
                recipe = get_html_recipe(
                    url_back="../../{}".format(filename_index),
                    title_back=n,
                    title=article['name'],
                    url_image=os.path.join("../..", img_recipe),
                    npers=article['people'],
                    time_prep=article['time_prep'] + " " + article['time_prep_unit'],
                    time_bake=article['time_bake'] + " " + article['time_bake_unit'],
                    ingredient_tables=ingredient_tables,
                )

                
                # Check if folder exists
                os.makedirs(folder_recipe, exist_ok=True)
                
                f = open(os.path.join(folder_recipe, filename_recipe), "w")
                f.write(recipe)
                f.close()
                sys.exit(0)


            except Exception as e:
                print("Exepected error: {}".format(article['name']))
                print(e)
            
        
        # Get index page
        r = get_html_index(title=n.upper(), articles=a_str)

        f = open(filename_index, "w")
        f.write(r)
        f.close()


if __name__ == '__main__':
    main()
    
    
    
    