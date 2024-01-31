from glob import glob
from utils.publication_builder import PublicationList
import numpy as np
import pandas as pd

import os
from PIL import Image
import sys

def main():
    
    # Creating an update of the website
    print("Updating website")
    
    # 1 Read and parse all recipes to get categories
    raw_files = glob("data/publication/*.xml")
    list = PublicationList(xml_path=raw_files)
    
    print(list.publications)
    


if __name__ == '__main__':
    main()
    
    
    
    