import xml.etree.ElementTree as ET
from tqdm import tqdm
import os


class PublicationList:

    def __init__(self, xml_path: str):
        
        self.publications = []
        for path in tqdm(xml_path, desc='Parsing ...'):
            try:
                pub = PublicationBuilder(xml_path=path)
                self.publications.append(pub.data)
            except Exception as e:
                print('Unknown error as: {}'.format(e))


class PublicationBuilder:

    data = {}
    
    def __init__(self, xml_path: str):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        self.data = {d: v for d, v in root.attrib.items()}






