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
#  <b>Typannotationen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Typannotationen.py -->
# <!-- python_courses/slides/module_130_functions/topic_130_b3_type_annotations.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Typannotationen
#
# Python erlaubt es die Typen von Funktionsargumenten und den Rückgabetyp einer
# Funktion anzugeben:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Typannotationen dienen lediglich zur Dokumentation und werden von Python ignoriert:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Typannotationen
#
# Schreiben Sie eine Function `repeat(s: str, n: int) -> str`, die den String `s`
# `n` mal wiederholt:
#
# ```python
# >>> repeat("abc", 3)
# "abcabcabc"
# ```
#
# *Hinweis:* Sie können dazu den Multiplikationsoperator `*` verwenden:
# ```python
# >>> "abc" * 3
# "abcabcabc"
# ```


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was passiert, wenn Sie `repeat()` mit zwei Zahlen aufrufen?
# - Was passiert, wenn Sie `repeat()` mit zwei Strings aufrufen?

# %%

# %%
