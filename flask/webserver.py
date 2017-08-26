from flask import Flask
from flask import request
import urllib
import requests
import tempfile
import os
app = Flask(__name__, static_url_path='/emperor_required_resources', static_folder="./static/emperor_required_resources")

SCRATCH_FOLDER = "./scratch"
 # beta_diversity.py -i myexample_bucket_table.biom -m gower -o  myexample_bucket_table_gower
 # validate_mapping_file.py -m mymapping_fileV02.txt -o validate_mapping_file_output
 # less validate_mapping_file_output/mymapping_fileV02.log
 # principal_coordinates.py -i myexample_bucket_table_gower/gower_myexample_bucket_table.txt -o mybeta_div_coords.txt
 # make_emperor.py -i mybeta_div_coords.txt -m mymapping_fileV02.txt -o emperor_output

@app.route("/")
def homepage():
    try:
        metadata_url = request.args["metadata"]
        biom_url = request.args["biom"]
    except:
        return "ERROR"


    """File Retrievel"""
    temporary_metadata_file = tempfile.NamedTemporaryFile(delete=False)
    temporary_metadata_file.close()
    urllib.urlretrieve(metadata_url, temporary_metadata_file.name)

    temporary_biom_file = tempfile.NamedTemporaryFile(delete=False)
    temporary_biom_file.close()
    urllib.urlretrieve(biom_url, temporary_biom_file.name)

    """Input file validation"""
    cmd = "validate_mapping_file.py -m %s -o validate_mapping_file_output"


    """Beta Diversity"""
    temporary_betadiversity = os.path.join(SCRATCH_FOLDER, "beta_diversity")
    beta_diversity_output_filename = os.path.join(temporary_betadiversity, "gower_%s.txt" % (os.path.basename(temporary_biom_file.name)))
    cmd = "beta_diversity.py -i %s -m gower -o %s" % (temporary_biom_file.name, temporary_betadiversity)
    print(cmd)
    os.system(cmd)

    """Principal Coordinates Analysis"""
    temporary_pcoa_file = tempfile.NamedTemporaryFile(delete=False)
    temporary_pcoa_file.close()
    cmd = "principal_coordinates.py -i %s -o %s" % (beta_diversity_output_filename, temporary_pcoa_file.name)
    print(cmd)
    os.system(cmd)

    """Make Emprorer"""
    cmd = "make_emperor.py -i %s -m %s -o %s" % (temporary_pcoa_file.name, temporary_metadata_file.name, SCRATCH_FOLDER)
    print(cmd)
    os.system(cmd)

    path_to_emporer_html = os.path.join(SCRATCH_FOLDER, "index.html")
    return open(path_to_emporer_html).read()


    #Cleaning up temporary files
    #os.unlink(temporary_metadata_file.name)


    #return temporary_metadata_file.name


    return "NONE"
