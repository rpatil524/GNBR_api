import json, sys, os, csv
from os.path import join
import shutil

def open_csv(name, delimiter=','):
    return csv.writer(open('{}'.format(name), 'w'), doublequote=False, delimiter=delimiter, escapechar='\\')

#################################################
############# DEFINE PATHS ######################
#################################################
DATA_DIR='../data/GNBR'

PROCESSED_DIR = '../data/GNBR_processed'
if not os.path.isdir(PROCESSED_DIR):
    os.mkdirs(PROCESSED_DIR)
print("data dir: ",DATA_DIR)
print("processed data dir: ",PROCESSED_DIR)


# note the header for each of these files is:
## pubmed_id   sentence_num    entity_a_formatted  entity_a_loc    entity_b_formatted  entity_b_loc    entity_a_raw    entity_b_raw    entity_a_id entity_b_id entity_a_type   entity_b_type   rel_path    rel_sentence

chem_dis_theme_file = join(DATA_DIR, 'part-i-chemical-disease-path-theme-distributions.txt.gz')
chem_gene_theme_file = join(DATA_DIR, 'part-i-chemical-gene-path-theme-distributions.txt.gz')
gene_dis_theme_file = join(DATA_DIR, 'part-i-gene-disease-path-theme-distributions.txt.gz')
gene_gene_theme_file = join(DATA_DIR, 'part-i-gene-gene-path-theme-distributions.txt.gz')

chem_dis_file = join(DATA_DIR, 'part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt.gz')
chem_gene_file = join(DATA_DIR, 'part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt.gz')
gene_dis_file = join(DATA_DIR, 'part-ii-dependency-paths-gene-disease-sorted-with-themes.txt.gz')
gene_gene_file = join(DATA_DIR, 'part-ii-dependency-paths-gene-gene-sorted-with-themes.txt.gz')
test_file = join(DATA_DIR, 'part-ii-chem-gene-test.txt')

#################################################
######## CREATE RELATIONSHIP HEADER FILES #######
#RELATIONSHIP FILES USE THE ORIGINAL GNBR FILES # 
#################################################
chem_dis_rel_header = join(PROCESSED_DIR,'chem_dis_rel_header.csv')
chem_dis_rel = join(PROCESSED_DIR,'chem_dis_rel.csv')
chem_gene_rel_header = join(PROCESSED_DIR,'chem_gene_rel_header.csv')
chem_gene_rel = join(PROCESSED_DIR,'chem_gene_rel.csv')
gene_dis_rel_header = join(PROCESSED_DIR,'gene_dis_rel_header.csv')
gene_dis_rel = join(PROCESSED_DIR,'gene_dis_rel.csv')
gene_gene_rel_header = join(PROCESSED_DIR,'gene_gene_rel_header.csv')
gene_gene_rel = join(PROCESSED_DIR,'gene_gene_rel.csv')


#################################################
######## Combine part i and ii into rel csv######
#################################################
# this part was done in command line because of encoding/decoding utf-8 issues...
# print(' '.join(["python", "GNBR_2_csv_neo4j.py", chem_dis_theme_file, chem_dis_file, chem_dis_rel_header, chem_dis_rel]))
# print(' '.join(["python", "GNBR_2_csv_neo4j.py", chem_gene_theme_file, chem_gene_file, chem_gene_rel_header, chem_gene_rel]))
# print(' '.join(["python", "GNBR_2_csv_neo4j.py", gene_dis_theme_file, gene_dis_file, gene_dis_rel_header, gene_dis_rel]))
# print(' '.join(["python", "GNBR_2_csv_neo4j.py", gene_gene_theme_file, gene_gene_file, gene_gene_rel_header, gene_gene_rel]))


# os.system(' '.join(["python", "GNBR_2_csv_neo4j.py", chem_dis_theme_file, chem_dis_file, chem_dis_rel_header, chem_dis_rel]))
# os.system(' '.join(["python", "GNBR_2_csv_neo4j.py", chem_gene_theme_file, chem_gene_file, chem_gene_rel_header, chem_gene_rel]))
# os.system(' '.join(["python", "GNBR_2_csv_neo4j.py", gene_dis_theme_file, gene_dis_file, gene_dis_rel_header, gene_dis_rel]))
# os.system(' '.join(["python", "GNBR_2_csv_neo4j.py", gene_gene_theme_file, gene_gene_file, gene_gene_rel_header, gene_gene_rel]))

#################################################
###### REWrite the header files (MANUALLY) #####
#################################################
# old_header = ["PMID","sentence_number","first_entity_name",
          # "first_entity_name_loc_char","second_entity_name","second_entity_name_loc_char",
          # "first_entity_name_raw", "second_entity_name_raw","first_entity_db_id", "second_entity_db_id",
          # "first_entity_type", "second_entity_type", "dependency_path","sentence_tokenized", "tax_id"] + outThemeHeader

with open(chem_dis_rel_header, 'w') as f:
    # old_header = f.readline()
    # new_header = old_header.strip().split(',')
    # new_header[2] = ':START_ID(Chemical)'
    # new_header[4] = ':END_ID(Disease)'
    f.write("PMID,sentence_number,first_entity_name,first_entity_name_loc_char,second_entity_name,second_entity_name_loc_char,first_entity_name_raw,second_entity_name_raw,:START_ID(Chemical),:END_ID(Disease),first_entity_type,second_entity_type,dependency_path,sentence_tokenized,tax_id,t:float,t.ind:float,c:float,c.ind:float,sa:float,sa.ind:float,pr:float,pr.ind:float,pa:float,pa.ind:float,j:float,j.ind:float,mp:float,mp.ind:float")

with open(chem_gene_rel_header, 'r+') as f:
    f.write("PMID,sentence_number,first_entity_name,first_entity_name_loc_char,second_entity_name,second_entity_name_loc_char,first_entity_name_raw,second_entity_name_raw,:START_ID(Chemical),:END_ID(Gene),first_entity_type,second_entity_type,dependency_path,sentence_tokenized,tax_id,a+:float,a+.ind:float,a-:float,a-.ind:float,b:float,b.ind:float,e+:float,e+.ind:float,e-:float,e-.ind:float,e:float,e.ind:float,n:float,n.ind:float,o:float,o.ind:float,k:float,k.ind:float,z:float,z.ind:float")

with open(gene_dis_rel_header, 'r+') as f:
    
    f.write("PMID,sentence_number,first_entity_name,first_entity_name_loc_char,second_entity_name,second_entity_name_loc_char,first_entity_name_raw,second_entity_name_raw,:START_ID(Gene),:END_ID(Disease),first_entity_type,second_entity_type,dependency_path,sentence_tokenized,tax_id,u:float,u.ind:float,ud:float,ud.ind:float,d:float,d.ind:float,j:float,j.ind:float,te:float,te.ind:float,y:float,y.ind:float,g:float,g.ind:float,md:float,md.ind:float,x:float,x.ind:float,l:float,l.ind:float")


with open(gene_gene_rel_header, 'r+') as f:
    f.write("PMID,sentence_number,first_entity_name,first_entity_name_loc_char,second_entity_name,second_entity_name_loc_char,first_entity_name_raw,second_entity_name_raw,:START_ID(Gene),:END_ID(Gene),first_entity_type,second_entity_type,dependency_path,sentence_tokenized,tax_id,b:float,b.ind:float,w:float,w.ind:float,v+:float,v+.ind:float,e+:float,e+.ind:float,e:float,e.ind:float,i:float,i.ind:float,h:float,h.ind:float,rg:float,rg.ind:float,q:float,q.ind:float")

