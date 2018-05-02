# GNBR_clean_part_i_files.py
# Written: 04/26/18
# Last updated: 04/26/18
"""
This code parses and cleans the raw files of the GNBR network.
"""

import gzip
import sys
import numpy as np
from gnbr_parse_utils import *


# Check input and print usage if number of arguments is invalid
def clean_predicates(path_to_part_i_file, path_to_cleaned_out_file)
    # Assign input file paths to their variables
    themeFile = path_to_part_i_file
    outFile = path_to_cleaned_out_file

    # Open buffer to out csv file
    out_parti_CSV=open_csv(outFile)

    with open(themeFile, "r") as themeIn:

        # Extract raw header from the part-i file
        raw_header = themeIn.readline().strip().split("\t")
        
        # Reformat header for compliance with neo4j
        parti_header = ["path"] + [x.lower().replace(" ", "_").replace('.ind', '_ind') + ':float' for x in raw_header[1:]]

        # Write header to file
        out_parti_CSV.writerow(parti_header)
        
        for line in themeIn.readlines():
            info = line.strip().split("\t")
            out_parti_CSV.writerow(info)

def clean_entities_and_sentences(path_to_part_ii_file, path_to_cleaned_out_file)
    # Assign input file paths to their variables
    depPathFile = path_to_part_ii_file
    outFile = path_to_cleaned_out_file

    # Default file header for the part-ii files
    part_ii_header = [
        "pmid", "loc", 
        "subj_name", "subj_loc", 
        "obj_name", "obj_loc",
        "subj_name_raw", "obj_name_raw", 
        "subj_id", "obj_id", 
        "subj_type", "obj_type", "species",
        "path", "text"
        ] 

    # Open buffer to out csv file
    out_partii_CSV=open_csv(outFile)

    # Write header to file
    out_partii_CSV.writerow(part_ii_header)

    # Iterate over file lines and clean the data
    with open(depPathFile, "r") as dpathIn:
        for line in dpathIn.readlines():
            info = line.strip().split("\t")

            # Omit entry if either entity is missing an identifier
            if info[8] == "null" or info[9] == "null":
                continue

            # GNBR uses ";" to mark unresolved entities, so we exclude these from our cleaned data
            if ";" in info[8] or ";" in info[9]:
                    continue

            if "gene" in depPathFile:
                # Prepend ncbigene prefix to genes, for data provinence 
                if "MESH:" not in info[8]:
                    info[8] = "ncbigene:" + info[8]
                if "MESH:" not in info[9]:
                    info[9] = "ncbigene:" + info[9]
                
                # Get species used in the study
                if "(Tax:" in info[9]:
                    temp = info[9].split("(")
                    info[9] = temp[0]
                    species = temp[1].strip("Tax:").strip(")")

                if "(Tax:" in info[8]:
                    temp = info[8].split("(")
                    info[8] = temp[0]
                    species = temp[1].strip("Tax:").strip(")")

                else:
                    species = "9606"
            else:
                species = "9606"
            # Convert dependency paths to lowercase to make them consistent with part-i files
            info[12] = info[12].lower()

            # Add in species as separate column
            info = info[:12] + [species] + info[12:]

            # Write cleaned line to file
            out_partii_CSV.writerow(info)




if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Error: wrong number of arguments, check usage statement below:\n")
        print("USAGE: python GNBR_2_csv.py <path/to/downloaded-file.txt.gz> <path/to/cleaned-outfile.csv.gz>")
        exit()

        if '-i-' in sys.argv[1]:
            clean_predicates( sys.argv[1], sys.argv[2] )

        elif '-ii-' in sys.arv[1]:
            clean_entities_and_sentences( sys.argv[1], sys.argv[2] )
            