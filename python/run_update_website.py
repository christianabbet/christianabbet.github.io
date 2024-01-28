from glob import glob
from utils.recipe_builder import RecipeList
import numpy as np
import pandas as pd
from utils.htlm_template import get_html_article, get_html_index
import os


def main():
    
    # Creating an update of the website
    print("Updating website")
    
    # 1 Read and parse all recipes to get categories
    raw_files = glob("data/recipe/*/*.xml")
    list = RecipeList(xml_path=raw_files)
    
    # 2. Build dataframe
    df = []
    for r in list.recipes:
        df.append(r.info)
    df = pd.DataFrame(df)
    
    # 2.1 Print stats
    print("Categories: ", df["category"].value_counts())
    
    
    # 3. Build category index
    # Change working directory to match index ressources
    os.chdir("ressources")
    
    for n, dfcat in df.groupby(by="category"):
        print("Building index page {} ...".format(n))
            
        a_str = ""
        # Create articles
        for i, (_, article) in enumerate(dfcat.iterrows()):
            
            try:
                # Check if image exists otherwise set dummy
                img = '../data/images/pic01.jpg'
                if article['pic'] is not None and os.path.exists(article['pic']):
                    img = article['pic']
                else:
                    print("Missing picture: {}".format(article['pic']))
                    
                    
                # Create article
                a = get_html_article(
                    style = 1 + (i % 6),
                    img=img,
                    title=article['name'],
                    npers=article['people'],
                    time_prep=article['time_prep'] + " " + article['time_prep_unit'],
                    time_bake=article['time_bake'] + " " + article['time_bake_unit'],
                )

                a_str = a_str + "\n" + a

            except Exception as e:
                print("Exepected error: {}".format(article['name']))
                print(e)
            
        
        # Get index page
        r = get_html_index(title=n.capitalize, articles=a_str)

        f = open("{}_index.html".format(n), "w")
        f.write(r)
        f.close()
    


if __name__ == '__main__':
    main()
    
    
    
    