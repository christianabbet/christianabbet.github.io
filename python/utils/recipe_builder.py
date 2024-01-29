import xml.etree.ElementTree as ET
from tqdm import tqdm
import os


class RecipeList:

    def __init__(self, xml_path: str):
        
        self.recipes = []
        for path in tqdm(xml_path, desc='Parsing ...'):
            try:
                recipe = RecipeBuilder(xml_path=path, meta=None)
                self.recipes.append(recipe)
            except Exception as e:
                print('Unknown error as: {}'.format(e))


class RecipeBuilder:

    def __init__(self, xml_path: str, meta: dict):
        tree = ET.parse(xml_path)
        root = tree.getroot()

        self.path = xml_path
        self.meta = meta
        self.info = None
        self.ingredient_groups = []
        self.steps = []
        self.hints = []
        for child in root:
            if child.tag == "ingredient_group":
                group = self._parse_ingredient_group(child)
                self.ingredient_groups.append(group)
            elif child.tag == "info":
                self.info = self._parse_info(child)
            elif child.tag == 'step':
                step = self._parse_step(child)
                self.steps.append(step)
            elif child.tag == 'hint':
                hint = self._parse_hint(child)
                self.hints.append(hint)
            else:
                raise NotImplementedError('Unknown tag {} in recipe: {}'.format(child.tag, xml_path))


    @staticmethod
    def _parse_info(info: ET.Element):
        return {d: v for d, v in info.attrib.items() if '_fr' not in d}
        
    @staticmethod
    def _parse_ingredient_group(ig: ET.Element):
        ig_meta = {d: v for d, v in ig.attrib.items() if '_fr' not in d}
        ig_meta['ingredients'] = []
        for child in ig:
            data = {d: v for d, v in child.attrib.items() if '_fr' not in d}
            ig_meta['ingredients'].append(data)
        return ig_meta

    @staticmethod
    def _parse_step(step: ET.Element):
        return {d: v for d, v in step.attrib.items() if '_fr' not in d}

    @staticmethod
    def _parse_hint(hint: ET.Element):
        return {d: v for d, v in hint.attrib.items() if '_fr' not in d}






