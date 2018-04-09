docker rm gnpsqiime
docker run -d -p 5005:5000 -v $(pwd)/../flask:/server --name gnpsqiime  gnpsqiime /server/run_prod.sh
#docker run -it -p 5005:5000 -v $(pwd)/../flask:/server --name gnpsqiime gnpsqiime bash
