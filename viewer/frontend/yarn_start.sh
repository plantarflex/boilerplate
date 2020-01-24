docker rm -f viewer_frontend
docker run -d \
    --name viewer_frontend \
    -p 3000:3000 \
    -w /frontend \
    -v $PWD:/frontend \
    --restart="always" \
    node:8.16.1-slim \
    yarn start
docker logs -f viewer_frontend
