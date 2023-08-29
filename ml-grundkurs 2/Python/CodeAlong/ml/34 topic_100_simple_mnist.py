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

# %% [markdown]
#
# # Trainin Neural Networks using Skorch
#
# Skorch is a library for PyTorch that simplifies training in a Scikit Learn

# %%

# %%

# %%

# %% [markdown]
#
# ## Transforming the data:
#
# Neural nets generally expect their inputs as `float32` (or possibly `float16`)
# values. Furthermore `skorch` expects classes to be stored as `int64` values,
# so we change the type of the arrays accordingly.


# %%

# %%

# %% [markdown]
#
# ## Normalize / Standardize
#
# Neural networks generally prefer their input to be in the range $(0, 1)$ or
# $(-1, 1)$ so we need to convert the integer array to floating point:

# %%

# %% [markdown]
#
# Don't use `Standard Scaler` for this data, since it will scale each feature
# independently:

# %%

# %% [markdown]
#
# Since we know the range of the value, we can easily perform the processing
# manually:

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

# %%

# %%
