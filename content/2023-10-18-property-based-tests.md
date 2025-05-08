Title: Less neat, less tidy, and more unpredictable: Improving your code with property-based tests
Date: 2023-10-18
Category: Talks
Tags: property-based-tests, ehrQL
Slug: 2023/10/18/property-based-tests

I gave a talk today at the [NHS-R][] conference.
It was called *Less neat, less tidy, and more unpredictable: Improving your code with property-based tests*.

[NHS-R]: https://nhsrcommunity.com/

## Abstract

As conscientious data scientists,
we know that it's good practice to write unit tests to check that our code is working correctly.
However, unit tests cover single scenarios and, despite our best intentions,
these scenarios are often far neater, far tidier, and far more predictable than those we encounter in the wild.

How can we cover less neat, less tidy, and more unpredictable scenarios?
One answer is to complement unit tests with property-based, or generative, tests.
Popularised by Haskell's Quickcheck library,
property-based tests can cover tens, hundreds, or even thousands of disparate scenarios
by generating large amounts of input data to match a specification,
and by checking that the results of operating on these data are consistent with one or more guarantees.
As conscientious data scientists,
our job becomes one of carefully crafting the specifications and guarantees,
rather than one of carefully crafting the input data.

In this talk, I'll introduce property-based tests with examples in Python and R.
I'll also discuss how to switch from thinking about input data to thinking about specifications and guarantees.
Finally, I'll describe how we use property-based tests in our work at the Bennett Institute for Applied Data Science
to improve our research and to improve ehrQL, the Electronic Health Records Query Language.
