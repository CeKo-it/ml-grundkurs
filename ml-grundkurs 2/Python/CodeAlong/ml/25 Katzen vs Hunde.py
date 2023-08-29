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
# <div style="text-align:center; font-size:200%;">
#  <b>Katzen vs. Hunde</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 25 Katzen vs Hunde.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_700_cats_vs_dogs_pretrained.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Klassifikation von Bildern
#
# Mit vortrainierten Modellen ist es selbst mit geringem Trainingsaufwand
# möglich, Bilder zu klassifizieren.

# %% tags=["keep"]
from enum import Enum
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt

from fastai.data.core import DataLoaders
from fastai.learner import Learner, load_learner
from fastai.metrics import accuracy, error_rate
from fastai.vision.all import (
    ImageDataLoaders,
    Resize,
    URLs,
    get_image_files,
    untar_data,
)
from fastai.vision.core import PILImage
from fastai.vision.learner import vision_learner

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
config = EnvConfig()
# %% tags=["keep"]
def is_cat(filename: str) -> bool:
    """
    Returns true if filename is an image of a cat.

    In the dataset we are using this is indicated by the first letter of the
    filename; cats are labeled with uppercase letters, dogs with lowercase ones.
    """
    result = filename[0].isupper()
    # print(f"File: {filename}, initial: '{filename[0]}', result: {result}")
    return result


# %% tags=["keep"]
def create_dataloaders() -> DataLoaders:
    """
    Create the dataloaders for the cats vs. dogs dataset.
    """
    path = untar_data(URLs.PETS) / "images"
    dls = ImageDataLoaders.from_name_func(
        path,
        get_image_files(path),
        valid_pct=0.2,
        batch_size=8,
        seed=42,
        label_func=is_cat,
        item_tfms=Resize(224),
        device="cuda",
    )
    return dls

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%


# %%

# %%

# %%

# %% tags=["keep"]
image_file_dir = config.data_dir_path / "cats-vs-dogs/"
print("Place image files into 'cat' and 'dog' subdirectories of")
print(image_file_dir)

# %% tags=["keep"]
cat_images = list((image_file_dir / "cat").glob("*.jpg"))
dog_images = list((image_file_dir / "dog").glob("*.jpg"))

# %% tags=["keep"]
num_cats, num_cats_correct = evaluate_classification(cat_images, AnimalType.cat)
print(f"Classified {num_cats_correct} out of {num_cats} cat images correctly.")
num_dogs, num_dogs_correct = evaluate_classification(dog_images, AnimalType.dog)
print(f"Classified {num_dogs_correct} out of {num_dogs} dog images correctly.")
