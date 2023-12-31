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
#  <b>Klassifikation von Ziffern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 12 Klassifikation von Ziffern.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_190_mnist.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Klassifikation von Ziffern
#
# Wir wenden uns jetzt dem Multi-Klassen-Klassifikationsproblem zu: Wir wollen
# erkennen, welche Ziffern auf den MNIST-Bildern dargestellt sind.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import pickle

import matplotlib.pyplot as plt  # noqa
import numpy as np  # noqa

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
config = EnvConfig()
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
with open(config.processed_mnist_pkl_path, "rb") as file:
    mnist_data = pickle.load(file)

# %% tags=["keep"]
x_train = mnist_data["x_train"]
x_test = mnist_data["x_test"]
y_train = mnist_data["y_train"]
y_test = mnist_data["y_test"]
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, classification_report


# %% tags=["keep"]
def plot_confusion_matrices(clf, x_train, x_test, y_train, y_test, normalize=None):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 9))
    fig.tight_layout()
    fig.suptitle(f"Confusion Matrices (Normalize={normalize})")
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        clf.predict(x_test),
        normalize=normalize,
        ax=ax1,
        colorbar=False,
        values_format=".3f" if normalize else None,
    )
    ax1.set_title("Test Data")
    ConfusionMatrixDisplay.from_predictions(
        y_train,
        clf.predict(x_train),
        normalize=normalize,
        ax=ax2,
        colorbar=False,
        values_format=".3f" if normalize else None,
    )
    ax2.set_title("Training Data")
    plt.show()
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def plot_numbers(nrows=1, ncols=1):
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols, nrows))
    fig.tight_layout()
    for idx, ax in enumerate(np.array(axes).ravel()):
        ax.imshow(x_test[idx].reshape(28, 28), cmap="binary")
        ax.set_title(f"Label:  {y_test[idx]}")
        ax.set_xticks([], [])
        ax.set_yticks([], [])
    plt.show()


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_numbers(4, 4)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_test, ridge_clf.predict(x_test)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_train, ridge_clf.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(ridge_clf, x_train, x_test, y_train, y_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(ridge_clf, x_train, x_test, y_train, y_test, normalize="true")

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(ridge_clf, x_train, x_test, y_train, y_test, normalize="pred")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_test, dt_clf.predict(x_test)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_train, dt_clf.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf, x_train, x_test, y_train, y_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf, x_train, x_test, y_train, y_test, normalize="true")

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf, x_train, x_test, y_train, y_test, normalize="pred")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_test, dt_clf2.predict(x_test)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_train, dt_clf2.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf2, x_train, x_test, y_train, y_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf2, x_train, x_test, y_train, y_test, normalize="true")

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf2, x_train, x_test, y_train, y_test, normalize="pred")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_test, rf_clf.predict(x_test)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_train, rf_clf.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rf_clf, x_train, x_test, y_train, y_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rf_clf, x_train, x_test, y_train, y_test, normalize="true")

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rf_clf, x_train, x_test, y_train, y_test, normalize="pred")

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.model_selection import RandomizedSearchCV

# %% tags=["keep"]
parameters = {
    "n_estimators": [400],
    "min_samples_split": [2, 8, 32],
    "min_samples_leaf": [1, 4, 16],
    "max_leaf_nodes": [None, 100, 1000],
    "max_features": ["sqrt", 16, 32, 64],
}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["keep"]
RANDOM_SEARCH_SAMPLES = 12_000

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_test, rs_best_clf.predict(x_test)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(y_train, rs_best_clf.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rs_best_clf, x_train, x_test, y_train, y_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rs_best_clf, x_train, x_test, y_train, y_test, normalize="true")

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rs_best_clf, x_train, x_test, y_train, y_test, normalize="pred")

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Workshop: Klassifikation von Kleidungsstücken mit Fashion-MNIST
#
# Klassifizieren Sie die verschiedenen Arten von Kleidungsstücken aus dem Fashion-MNIST
# Datensatz mit folgenden Klassifikations-Algorithmen:
#
# - Ridge
# - Entscheidungsbaum
# - Random Forest

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import pickle

import matplotlib.pyplot as plt  # noqa
import numpy as np  # noqa

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
config = EnvConfig()
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
with open(config.processed_fashion_mnist_pkl_path, "rb") as file:
    fashion_mnist_data = pickle.load(file)

# %% tags=["keep"]
x_train = fashion_mnist_data["x_train"]
x_test = fashion_mnist_data["x_test"]
y_train = fashion_mnist_data["y_train"]
y_test = fashion_mnist_data["y_test"]
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, classification_report


# %% tags=["keep"]
def plot_confusion_matrices(clf, x_train, x_test, y_train, y_test, normalize=None):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 9))
    fig.tight_layout()
    fig.suptitle(f"Confusion Matrices (Normalize={normalize})")
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        clf.predict(x_test),
        normalize=normalize,
        ax=ax1,
        colorbar=False,
        values_format=".3f" if normalize else None,
    )
    ax1.set_title("Test Data")
    ConfusionMatrixDisplay.from_predictions(
        y_train,
        clf.predict(x_train),
        normalize=normalize,
        ax=ax2,
        colorbar=False,
        values_format=".3f" if normalize else None,
    )
    ax2.set_title("Training Data")
    plt.show()
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
label_names = {
    0: "T-shirt/top",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle boot",
}


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def plot_fashion_items(nrows=1, ncols=1):
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols, nrows))
    fig.tight_layout()
    for idx, ax in enumerate(np.array(axes).ravel()):
        ax.imshow(x_test[idx].reshape(28, 28), cmap="binary")
        ax.set_title(label_names[y_test[idx]])
        ax.set_xticks([], [])
        ax.set_yticks([], [])
    plt.show()


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_fashion_items(10, 10)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Optimieren Sie die Parameter für einen Random Forest Klassifizierer mit einem der
# Suchverfahren, die scikit-learn bereitstellt.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep"]
parameters = {
    "n_estimators": [400],
    "min_samples_split": [2, 8, 32],
    "min_samples_leaf": [1, 4, 16],
    "max_leaf_nodes": [None, 100, 1000],
    "max_features": ["sqrt", 16, 32, 64],
}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["keep"]
RANDOM_SEARCH_SAMPLES = 12_000

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
