FROM condaforge/mambaforge

RUN mamba create -n pyimagej -c conda-forge pyimagej openjdk=8 unzip
#RUN conda activate pyimagej
# Make RUN commands use the new environment:
SHELL ["conda", "run", "--no-capture-output", "-n", "pyimagej", "/bin/bash", "-c"]

# Define Fiji install directory.
WORKDIR /opt/fiji

# Install Fiji.
RUN wget -q https://downloads.imagej.net/fiji/latest/fiji-nojre.zip \
    && unzip fiji-nojre.zip \
    && rm fiji-nojre.zip

# Add fiji to the PATH
ENV PATH $PATH:/opt/fiji/Fiji.app

# Init Fiji for quicker startups
COPY init_fiji.py .
RUN python /opt/fiji/init_fiji.py

WORKDIR /
COPY read_settings_and_process_tiff_stack.py .

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "pyimagej", "ImageJ-linux64", "--ij2", "--headless", "--run", "read_settings_and_process_tiff_stack.py"]
