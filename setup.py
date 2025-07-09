from setuptools import setup, find_packages

setup(
    name="chatglm-rag-pdf",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch",
        "sentence_transformers",
        "faiss-cpu"
    ],
)
