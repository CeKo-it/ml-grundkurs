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

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# `torchvision.datasets.mnist.MNIST` is a PyTorch `Dataset`, which means that it
# defines `__getitem__()` and `__len__()` methods, that can be used by
# `DataLoader`s.

# %%

# %%

# %%

# %%


# %%

# %%

# %%

# %%

# %% [markdown]
#
# For PyTorch to use `Dataset` it has to be wrapped in a `DataLoader` that
# performs useful operations such as batching or shuffling of the data. (For
# `Dataset`s like the one used in this file, the `DataLoader` instantiates a
# `Sampler` based on the parameters passed to the `DataLoader`'s constructor to
# perfrom the actual work.) See [the PyTorch
# documentation](https://pytorch.org/docs/stable/data.html#module-torch.utils.data)
# for more information.
#
# For deep learning models you typically want the `DataLoader` to shuffle the
# data, since you will train for multiple epochs, and you want to batch the
# data, in particular when you train on a GPU. To build a batch from a list of
# samples, the `collate_fn` (if supplied to the `DataLoader`'s constructor) is
# called on the list of items in the batch. This can be used to, e.g., convert
# pad sequential items to the same length in each batch.
#
# `DataLoader`s can load data in single- or multi-process modes. There are
# several intricacies to keep in mind when using multi-process data loading, in
# paricular when using CUDA. See [the PyTorch
# documentation](https://pytorch.org/docs/stable/data.html#single-and-multi-process-data-loading)
# for a discussion.

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
