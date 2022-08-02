from docker.client import DockerClient
from docker.types import Mount
from pathlib import Path


def run_trackmate(settings_path: Path, data_path: Path):
    # settings_mount = Mount(
    #     target="/settings",
    #     source=str(settings_path.parent.absolute()),
    #     type="bind",
    #     read_only=True,
    # )
    data_mount = Mount(
        target="/data",
        source=str(data_path.parent.absolute()),
        type="bind",
        read_only=False,
    )

    container = docker_client.containers.run(
        image="trackmate",
        detach=True,
        mounts=[data_mount],
        environment={"SETTINGS_XML": settings_path.name, "TIFF_STACK": data_path.name},
    )

    for line in container.logs(stream=True):
        print(line.decode("utf-8"))


docker_client = DockerClient()

settings = Path(__file__).parent / 'settings.xml'
data = Path(__file__)

run_trackmate(settings, data)
