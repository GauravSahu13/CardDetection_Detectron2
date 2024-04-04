import os
import shutil

curr_dir = os.getcwd()
file_location = 'image_with_xml'
xml_path = os.path.join(curr_dir,file_location)


def extarct_xml(path, _format, folder_name, destination_path):
    for file in os.listdir(path):
        if file.split('.')[1] == _format:
            folders = os.listdir()
            if folder_name not in folders:
                directory  = folder_name
                make = os.path.join(curr_dir, directory)
                os.mkdir(make)
                shutil.move(xml_path + "/" + file , destination_path + "/"+ folder_name)
            else:
                shutil.move(xml_path + "/" + file , destination_path + "/"+ folder_name)
                
    print("Moved!")
    

extarct_xml(xml_path, 'xml', 'annotations', curr_dir)            
                
                
                
    
