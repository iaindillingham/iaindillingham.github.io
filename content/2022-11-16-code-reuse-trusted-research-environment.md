Title: Code Reuse in a Trusted Research Environment
Date: 2022-11-16
Category: Talks
Tags: OpenSAFELY, TRE
Slug: 2022/11/16/code-reuse-trusted-research-environment

I gave a talk today at the [NHS-R][] conference.
It was called *Code Reuse in a Trusted Research Environment: Reusable Actions in OpenSAFELY*.

[NHS-R]: https://nhsrcommunity.com/

## Abstract

OpenSAFELY is a secure, transparent, open-source software platform for analysis of electronic health records data.
It can be deployed to create a Trusted Research Environment (TRE) or, alternatively, as a privacy-enhancing layer on any existing TRE.

When undertaking a project within OpenSAFELY, a researcher will typically write one or more scripted actions;
logical units of analytic Python, R, or Stata code.
However, to encourage the development of well-tested, well-documented code that can be shared between projects, OpenSAFELY supports reusable actions.

Reusable actions are similar to packages in Python or R:
versioned collections of analytic code, tests, and documentation that can be made available to other researchers via <https://actions.opensafely.org/>, the OpenSAFELY equivalent of PyPI or CRAN.

In this talk, I will discuss the challenges of code reuse within a TRE.
I will then discuss how reusable actions in OpenSAFELY overcome these challenges,
situating reusable actions within OpenSAFELY's strict security protocols.

I will describe the structure of an OpenSAFELY project,
and how a researcher can convert a scripted action, which promotes reusing code within a project;
to a reusable action, which promotes sharing code between projects.
Although I will give an example in Python, the same principles apply to R or Stata.
Finally, I will survey the landscape of existing reusable actions, from the vantage point of <https://actions.opensafely.org/>.

## What is OpenSAFELY?

> [OpenSAFELY][] is a secure, transparent, open-source software platform for analysis of electronic health records data.

It can be deployed to create

* a TRE
* a privacy-enhancing layer on an existing TRE

[OpenSAFELY]: https://www.opensafely.org/

## Why reuse code?

* Avoid duplicating identical lines of code in different locations (e.g. by copying-and-pasting)
* Instead, use the same lines of code in each location
* Over time, improve the functionality that those lines of code implement
  * Tests
  * Documentation
  * Bugs
  * Features
* Do this within, as well as between, projects

## Code reuse in practice

Code reuse within a project:

* Factor code into functions, classes, methods
* Factor these into modules or packages

Code reuse between projects:

* Release these to software repositories, such as PyPI or CRAN

## TREs and code reuse: some challenges

### Skills challenges

Releasing code requires a different set of skills to writing code.

We need to make choices:

* Tooling (Flit, Poetry, Setuptools)
* Versions of our chosen programming language (3.8, 3.9, 3.10)
* Operating systems (Unix-like, Windows)
* Versioning scheme (SemVer, CalVer)

### Security challenges

You may be familiar with this

```
pip install matplotlib
```

or this

```
conda install matplotlib
```

or this

```
install.packages("ggplot2")
```

In each case we're downloading a package from the Internet to a computer.
What if the computer is within a TRE?

If packages can be downloaded, then can data be uploaded?<br>
→ TREs probably shouldn't have unrestricted access to the Internet

Where are packages hosted? Which software repository? Which mirror?<br>
Software repositories and mirrors can be compromised.<br>
→ TREs probably shouldn't have unrestricted access to software repositories and mirrors.

Did we get the package we asked for?<br>
Packages can be compromised.<br>
→ TREs probably shouldn't have unrestricted access to packages.

### Summary

The skills and security challenges can be addressed,
but they distract us from achieving our aims:

* Avoid duplicating identical lines of code in different locations
* Instead, use the same lines of code in each location
* Over time, improve the functionality that those lines of code implement
* Do this within, as well as between, projects

## What are scripted actions?

An OpenSAFELY project is a set of steps, which when run, produce a result.
We call each step an *action*.
Each action is run within a Docker container, which doesn't have access to the Internet.

Some actions address specific tasks:
a cohort-extractor action, for example, allows a researcher to extract a cohort.

The researcher analyses the cohort by writing one or more *scripted actions* in Python, R, or Stata.
For example, the researcher may write a scripted action to round counts in a contingency table to the nearest seven.

Scripted actions help us achieve our aims, in part, but they are project-specific:
we achieve code reuse within a project, but not between projects.

## What are reusable actions?

*Reusable actions* are scripted actions that have been decoupled from their projects.
They help us achieve code reuse within, as well as between, projects.

Whilst we could think of reusable actions as packages,
it's better to think of them as reusable projects.

## From scripted to reusable

### First step: refactoring

Typically, project-specific information is hard-coded in a scripted action.
For example, we may hard-code the location of an input file like this

```
path_to_input_file = "data/input.csv"

def my_function():
    my_other_function(path_to_input_file)
```

which we may run like this

```
python my_scripted_action.py
```

In a reusable action, project-specific information is passed as arguments to a command-line interface.
For example, we may rewrite our scripted action as a reusable action like this

```
def my_function():
    parser = ArgumentParser()
    parser.add_argument("--path-to-input-file")
    args = parser.parse_args()

    my_other_function(args.path_to_input_file)
```

which we may run like this

```
python my_scripted_action.py --path-to-input-file data/input.csv
```

Refactoring requires some knowledge of how to make a command-line interface in our chosen programming language,
but that's a writing code skill, not a releasing code skill.

Remember: we use the same workflow whether we are working on a scripted action or a reusable action.

### Next steps

* Create a new project in <https://github.com/opensafely-actions>
* Copy the scripted action to the new project: the scripted action is now a reusable action
* Add README.md
* Add action.yaml, which contains the run command
* Point the existing project to the reusable action like this

```
my_reusable_action:v0.0.1 --path-to-input-file data/input.csv
```

Remember: we use the same workflow whether we are working on a scripted action or a reusable action.

## Why create reusable actions?

By decoupling scripted actions from their projects we:

* Create a location for making improvements (a new project)
* Access a mechanism for sharing improvements
* Access a mechanism for receiving credit for our work (potentially!)

## Security redux

OpenSAFELY restricts access to the Internet; only

* <https://github.com/opensafely>
* <https://github.com/opensafely-actions>

are accessible, by proxy.

We have more control over these GitHub organisations than we do over software repositories and mirrors.

Reusable actions have a similar security profile to scripted actions.

## Where can I find reusable actions?

* Actions Registry: <https://actions.opensafely.org/>
* Code: <https://github.com/opensafely-actions>
* Documentation: <https://docs.opensafely.org/actions-reusable/>
