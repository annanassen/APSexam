FROM problemtools/icpc

RUN apt-get update \
    && apt-get install -y --no-install-recommends mono-mcs \
    && rm -rf /var/lib/apt/lists/*
