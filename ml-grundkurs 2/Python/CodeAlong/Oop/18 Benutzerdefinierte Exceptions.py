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
#  <b>Benutzerdefinierte Exceptions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 18 Benutzerdefinierte Exceptions.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_130_a3_user_defined_exceptions.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Benutzerdefinierte Exceptionklassen
#
# - Es ist möglich, eigenen Exceptionklassen zu definieren.
# - Dazu genügt es, von `Exception` oder einer Unterklasse von `Exception` zu
#   erben.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Behandeln von Unterklassen einer Exception
#
# - Eine `except`-Klausel für eine Klasse `A` behandelt auch alle Unterklassen von `A`

# %% tags=["keep"]
print("Before try")
try:
    print("Before raise")
    # raise ValueError("ValueError")
    raise MyValueError("MyValueError")
    print("After raise")  # noqa
except ValueError as error:
    print(f"Caught: {error}")
print("After except")
