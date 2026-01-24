# Base docker image that will be build
FROM python:3.13.11-slim

# Set up image by installing dependencies ; in this case pandas, pyarrow
# RUN pip install pandas pyarrow

# Copy uv binary from official uv image to this image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set the working directory inside the docker image
WORKDIR /app

# Add virtual environment to the PATH so installed packages can be used
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependencies file to the working directory (better layer catching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Install dependencies inside a virtual environment located at /app/venv
RUN uv sync --locked

# Copy the pipeline code into the docker image. 1st name is source, 2nd is destination
COPY ingest_data.py ingest_data.py

# Define the first command to be run when starting the container
ENTRYPOINT [ "uv", "run", "python", "ingest_data.py" ]