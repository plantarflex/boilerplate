docker run \
    --rm \
    -v $PWD:/frontend \
    -w /frontend \
    node:8.16.1-slim \
    /bin/bash -c "yarn;"
