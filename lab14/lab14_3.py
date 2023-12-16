import random
import xml.etree.ElementTree as ET

def process_tuple_to_xml():

    original_tuple = tuple(random.randint(1, 128) for _ in range(10))
    new_tuple = tuple(0 if x % 5 == 0 else x for x in original_tuple)

    root = ET.Element("tuple_data")

    original_element = ET.SubElement(root, "original_tuple")
    original_element.text = ', '.join(map(str, original_tuple))

    new_element = ET.SubElement(root, "new_tuple")
    new_element.text = ', '.join(map(str, new_tuple))

    tree = ET.ElementTree(root)
    with open("lab14_3.xml", "wb") as xml_file:
        tree.write(xml_file)

process_tuple_to_xml()



def xml_read():
    
    tree = ET.parse("lab14_3.xml")
    root = tree.getroot()

    original_element = root.find("original_tuple")
    original_str = original_element.text
    original_tuple = tuple(map(int, original_str.split(', ')))
    print("Прочитанный из XML кортеж: ", original_tuple)

    new_element = root.find("new_tuple")
    new_str = new_element.text
    new_tuple = tuple(map(int, new_str.split(', ')))
    print("Прочитанный из XML новый кортеж: ", new_tuple)
xml_read()
