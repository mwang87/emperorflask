from flask import Flask
from flask import request
import urllib
import requests
import tempfile
import os
import uuid
app = Flask(__name__, static_url_path='/emperor_required_resources', static_folder="./static/emperor_required_resources")

SCRATCH_FOLDER = "./scratch"

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
    os.system(cmd)

    """Principal Coordinates Analysis"""
    temporary_pcoa_file = tempfile.NamedTemporaryFile(delete=False)
    temporary_pcoa_file.close()
    cmd = "principal_coordinates.py -i %s -o %s" % (beta_diversity_output_filename, temporary_pcoa_file.name)
    os.system(cmd)

    """Make Emprorer"""
    emperor_folder = os.path.join(SCRATCH_FOLDER, str(uuid.uuid4()))
    cmd = "make_emperor.py -i %s -m %s -o %s" % (temporary_pcoa_file.name, temporary_metadata_file.name, emperor_folder)
    os.system(cmd)

    path_to_emporer_html = os.path.join(emperor_folder, "index.html")
    return open(path_to_emporer_html).read()




    return "NONE"
