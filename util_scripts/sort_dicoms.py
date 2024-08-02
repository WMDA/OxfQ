import os
import re
import argparse 

def config_args():
    """
    Function to define cmd arguments

    Parameters
    ----------
    None

    Returns
    -------
    dict: dictionary
        dictionary of cmd arguments
    """
    args = argparse.ArgumentParser()
    args.add_argument(
        "-d",
        "--dicom_dir",
        dest="dicom_dir",
        required=True,
        help="Full path to DICOM directory",
    )
    args.add_argument(
        "-o",
        "--output_dir",
        dest="output_dir",
        required=True,
        help="Where to save organised DICOM directory",
    )

    return vars(args.parse_args())

if __name__ == "__main__":
    args = config_args()
    path = args['dicom_dir']
    path_save = args['output_dir']
    
    os.mkdir(path_save)
    direct = [os.path.join(path, dir) for dir in os.listdir(path)]
    
    unique = list(set([re.findall(r'(\d{4})', file)[8] for file in direct]))
    organise_dict = dict(zip([key for key in unique], [[] for key in unique]))
    
    [os.mkdir(os.path.join(path_save, dir)) for dir in organise_dict.keys()]
    [organise_dict[re.findall(r'(\d{4})', file)[8]].append(file) for file in direct]
    
    for key, value in organise_dict.items():
        folder = os.path.join(path_save, key)
        [os.replace(file, re.sub(path, folder, file)) for file in value]


