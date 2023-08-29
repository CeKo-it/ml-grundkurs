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
#  <b>Pandas Series</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Pandas Series.py -->
# <!-- python_courses/slides/module_610_pandas/topic_110_pandas_series.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Pandas Typ `Series`
#
# Eine Pandas `Series` Instanz stellt eine Folge von Werten dar, ähnlich wie
# eine Python-Liste. Die Elemente einer Serie können über ihren numerischen
# Index abgerufen werden, aber zusätzlich kann eine Serie einen semantisch
# sinnvollen Index haben (z. B. für Zeitreihen).
#
# Intern wird eine Pandas-Serie durch ein Numpy-Array unterstützt, daher sind
# die meisten der Numpy-Operationen auch auf Serien anwendbar sind.
#
# Darüber hinaus ist es einfach (und billig), Serien nach Numpy zu konvertieren.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Erzeugung
#
# ### Aus Listen

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Listen mit Index

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Range oder Iterable

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Dictionary

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Indizes

# %% tags=["keep"]
food = pd.Series({"Ice Cream": 2.49, "Cake": 4.99, "Fudge": 7.99})


# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Zugriff auf Werte

# %%

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Methoden

# %%

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def discount(price):
    return price * 0.9


# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Namen von Serien

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Plotten von Serien

# %% tags=["keep"]
food = pd.Series({"Ice Cream": 2.49, "Cake": 4.99, "Fudge": 7.99})

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import random

# %% tags=["keep"]
data = pd.Series(data=[random.gauss(0.0, 10.0) for _ in range(5_000)])

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Operationen auf mehreren Serien

# %% tags=["keep"]
food1 = pd.Series({"Ice Cream": 2.99, "Cake": 5.99, "Fudge": 6.99})
food2 = pd.Series({"Cake": 4.99, "Ice Cream": 2.99, "Pie": 3.49, "Cheese": 4.99})

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
all_food = pd.concat([food1, food2])

# %% tags=["keep"]
all_food

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Fehlende Werte

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Feststellen wie viele Werte `NaN`s sind:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Slices und Fancy Indexing

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Man kann auch ein Series-Objekt mit Booleschen Werten zum Indexing
# verwenden. Dann wird eine Teilfolge der Series ausgewählt:

# %% tags=["keep"]
food1

# %% tags=["keep"]
food1[pd.Series({"Ice Cream": False, "Cake": True, "Fudge": True})]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ### Mehrfach vorkommende Werte

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ### Mehrfach vorkommende Index-Werte

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Nochmal: Zugriff auf Werte

# %% tags=["keep"]
all_food

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Gruppieren

# %% tags=["keep"]
all_food

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ### Sortierte und unsortierte Indizes

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Fancy Indexing und sortierte Indizes

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# all_food.loc["Cake":"Fudge"]

# %%

# %%

# %% [markdown] lang="de"
#
# **Wichtig:** Der ober Wert der Slice, `"Fudge"` ist im Resultat enthalten!

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Einfache Zeitreihenanalyse
#
# Wir haben folgende Zeitreihe mit Messwerten:


# %% tags=["keep"]
measurements = pd.Series(
    [13.78, 13.41, 13.21, 10.24, 9.84, 9.35, 6.23, 5.78, 5.26, 3.44],
    index=[1, 4, 5, 6, 6, 7, 8, 8, 9, 11],
    name="Measurements",
)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Sind die Zeiten der Messungen aufsteigend geordnet?
# - Sind die Messwerte aufsteigend oder absteigend geordnet?
# - Sind die Zeiten der Messungen eindeutig?
# - Sind die Werte der Messungen eindeutig?

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was ist der Mittelwert, Median und Standardabweichung der Messwerte?

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erzeugen Sie drei neue Serien, die folgende Messwerte enthalten:
# - Für Zeiten mit einem eindeutigen Messwert soll dieser Wert enthalten sein
# - Für Zeiten mit mehreren Messungen soll
#   - der größte Wert
#   - der kleinste Wert
#   - der Mittelwert der Messungen zu diesem Zeitpunkt

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Erzeugen Sie eine neue Serie, die alle Messungen enthält, die zwischen
#   3 und 7 Sekunden stattfanden (einschließlich der Grenzen).
# - Erzeugen Sie eine neue Serie, die alle Messungen zwischen der 2. und der 6. Messung
#   enthält (einschließlich der Grenzen).

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# - Erzeugen Sie eine Serie, die alle Messungen enthält, deren Wert größer als 10 ist.
# - Erzeugen Sie eine Serie, die alle Messungen enthält, deren Wert zwischen 8 und 11
#   ist.

# %%

# %%
