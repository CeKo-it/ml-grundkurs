# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Download der Fashion-MNIST Daten
#
# [Fashion-MNIST](https://www.openml.org/search?type=data&sort=runs&id=40996)
# ist ein Datensatz, der im gleichen Format wie MNIST ist, aber Bilder
# von verschiedenen Kleidungsstücken enthält.
#
# - Laden Sie den Fashion-MNIST Datensatz von der OpenML Website herunter:<br>
#   `fetch_openml(data_id=40996)` oder<br>
#   `fetch_openml("Fashion-MNIST", version=1)`
# - Schreiben Sie die Daten in eine Pickle-Datei
#
# *Hinweis:* Die `EnvConfig`-Klasse enthält dafür ein Attribut `fashion_mnist_pkl_path`.


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
import pickle

from sklearn.datasets import fetch_openml

# %% tags=["keep"]
config = EnvConfig()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(f"Path to Fashion-MNIST pickle file: {config.fashion_mnist_pkl_path}")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
config.fashion_mnist_pkl_path.parent.mkdir(exist_ok=True, parents=True)

# %%

# %%

# %%
