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
# ## Workshop: Vorbereiten der Fashion-MNIST Daten
#
# Bereiten Sie die Fashion-MNIST Daten für Machine-Learning Algorithmen vor:
#
# - Laden Sie die in einem vorhergehenden Workshop gespeicherte Pickle-Datei.
# - Analysieren Sie das Format der wichtigsten Attribute.
# - Konvertieren Sie die beiden Attribute in Numpy Arrays und speichern Sie die
#   Resultate in Variablen `X` und `y`.
# - Lassen Sie sich Bilder der ersten Einträge in `X` anzeigen.
# - Konvertieren Sie die Werte in `y` in `int`-Werte.
# - Teilen Sie die Daten in Trainings- und Test-Daten auf.
# - Speichern Sie die bearbeiteten Daten.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:  # noqa
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
from textwrap import wrap

# %% tags=["keep"]
config = EnvConfig()


# %% tags=["keep"]
def print_wrapped(text: str):
    for paragraph in text.split("\n"):
        print("\n".join(wrap(paragraph)))


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Laden Sie die in einem vorhergehenden Workshop gespeicherte Pickle-Datei.


# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Analysieren Sie den Typ und die Keys des geladenen Objekts
# - Analysieren Sie das Format der `data`- und `target`-Attribute.
# - Lassen Sie sich die Beschreibung im `DESCR`-Attribut anzeigen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Konvertieren Sie die beiden Attribute in Numpy Arrays und speichern Sie die
#   Resultate in Variablen `X` und `y`.
# - Analysieren Sie dir Form der erhaltenen Arrays und die Wertebereiche der Elemente.


# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Lassen Sie sich Bilder der ersten Einträge in `X` anzeigen.

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Konvertieren Sie die Werte in `y` in `int`-Werte.

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Teilen Sie die Daten in Trainings- und Test-Daten auf.

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Speichern Sie ein Dictionary mit den bearbeiteten Daten.
# - Überprüfen Sie, dass die richtigen Daten gespeichert wurden.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
processed_fashion_mnist_data = {
    "x_train": x_train,
    "x_test": x_test,
    "y_train": y_train,
    "y_test": y_test,
}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep"]
print("\n\nDone!")
