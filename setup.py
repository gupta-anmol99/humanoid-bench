from pathlib import Path
from setuptools import find_packages, setup


long_description = (Path(__file__).parent / "README.md").read_text()

core_requirements = [
    "gymnasium==0.29.1",
    "rich",
    "tqdm",
    "ipdb",
    "mujoco==3.1.6",
    "mujoco-mjx==3.1.6",
    "dm_control==1.0.20",
    "imageio",
    "gymnax",
    "brax",
    "torch",
    "opencv-python",
    "natsort",
]

setup(
    name="humanoid_bench",
    version="0.2",
    author="RLL at UC Berkeley",
    url="https://github.com/carlosferrazza/humanoid-bench",
    description="Humanoid Benchmark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">3.7",
    install_requires=core_requirements,
)
