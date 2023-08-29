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
#  <b>Propagation von Exceptions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 Propagation von Exceptions.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_114_a1_stack_unwinding.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Stack-Unwinding
#
# Visualisierung auf [PythonTutor](shorturl.at/nuxCG).
#
# Wenn eine Exception ausgelöst wird, werden geschachtelte Funktionsaufrufe so lange
# abgebrochen, bis ein passender Handler gefunden wird:

# %% tags=["keep"]
def outer_caller(raise_value_error=True):
    print("outer_caller() before try")
    try:
        print("outer_caller() before calling")
        intermediate_fun(raise_value_error)
        print("outer_caller() after calling")
    except Exception as error:
        print(f"<<<< Case Exception: {error}")
    print("outer_caller() after except")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def intermediate_fun(raise_value_error):
    print("  intermediate_fun() before call")
    raise_and_handle_error(raise_value_error)
    print("  intermediate_fun() after call")


# %% tags=["keep"]
def raise_and_handle_error(raise_value_error):
    print("    raise_and_handle_error() before try")
    try:
        print("    raise_and_handle_error() before raise")
        if raise_value_error:
            raise ValueError(">>>>  ValueError was raised")
        else:
            raise TypeError(">>>>  TypeError was raised")
        print("    raise_and_handle_error() after raise")  # noqa
    except ValueError as error:
        print(f"<<<<  Case ValueError: {error}")
    print("    raise_and_handle_error() after except")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
outer_caller(True)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
outer_caller(False)  # noqa

# %%
