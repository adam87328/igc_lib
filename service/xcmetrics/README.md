# XCMetrics Service

This service is built using Docker and depends on the igc_lib library.

## Building the Docker Image

From the repository root, run:

```bash
docker build -f service/xcmetrics/Dockerfile -t xcmetrics .
```

## How the Requirements Work

The Dockerfile uses a two-step approach to handle requirements:

1. First, it copies the igc_lib requirements.txt from the repository root to `/code/igc_lib/requirements.txt`
2. Then, it copies the service's requirements.txt to `/code/requirements.txt`
3. The service's requirements.txt includes a reference to igc_lib requirements using `-r igc_lib/requirements.txt`
4. When pip install runs, it resolves the relative path correctly and installs all dependencies

This approach maintains the relationship between the service and igc_lib requirements while working correctly inside the Docker container.

## Running the Container

```bash
docker run -p 8000:8000 xcmetrics
```
