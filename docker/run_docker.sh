docker run -it -p 5001:5000 -v $(pwd)/../flask:/server gnpsqiime bash
#docker run -it -p 5001:5000 -v $(pwd)/../flask:/server gnpsqiime "gunicorn webserver:app -b 0.0.0.0:5000 --threads 4"
