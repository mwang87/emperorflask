from flask import Flask
from flask import request
import urllib
import requests
import tempfile
import os
app = Flask(__name__)


 # beta_diversity.py -i myexample_bucket_table.biom -m gower -o  myexample_bucket_table_gower
 # validate_mapping_file.py -m mymapping_fileV02.txt -o validate_mapping_file_output
 # less validate_mapping_file_output/mymapping_fileV02.log
 # principal_coordinates.py -i myexample_bucket_table_gower/gower_myexample_bucket_table.txt -o mybeta_div_coords.txt
 # make_emperor.py -i mybeta_div_coords.txt -m mymapping_fileV02.txt -o emperor_output

@app.route("/")
def homepage():
    try:
        #metadata_url = request.args["metadata"]
        biom_url = request.args["biom"]
    except:
        return "ERROR"


    #temporary_metadata_file = tempfile.NamedTemporaryFile(delete=False)
    #temporary_metadata_file.close()
    #urllib.urlretrieve(metadata_url, temporary_metadata_file.name)

    temporary_biom_file = tempfile.NamedTemporaryFile(delete=False)
    temporary_biom_file.close()
    urllib.urlretrieve(biom_url, temporary_biom_file.name)

    temporary_betadiversity = tempfile.NamedTemporaryFile(delete=False)
    temporary_betadiversity.close()
    cmd = "beta_diversity.py -i %s -m gower -o %s" % (temporary_biom_file.name, temporary_betadiversity.name)

    #Cleaning up temporary files
    #os.unlink(temporary_metadata_file.name)


    #return temporary_metadata_file.name


    return "NONE"
