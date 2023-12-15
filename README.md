# Tech Screener for ETS AI Engineer Positions

Please carefully read all of the information below before starting the task.

## Table of contents
- [Repository structure](#repository-structure)
- [Task description](#task-description)
  - [Valid prepositions](#valid-prepositions)
  - [Feature extraction](#feature-extraction)
  - [Output format](#output-format)
  - [Example](#example)
  - [Suggested Python libraries](#suggested-python-libraries)
  - [Using ChatGPT or another LLM](#using-chatgpt-or-another-llm)
- [Submission requirements](#submission-requirements)
- [Submission instructions](#submission-instructions)
- [Important notes](#important-notes)

## Repository structure

This repository contains the following files:

* `README.md` - the description of the task (this file).

* `sentences.csv` - a comma-separated file containing one sentence per line,
which will be the input for the programming task. This file contains two
columns: the first is the sentence ID (called "Id") and the second is the
actual sentence text (called "Sentence").

## Task description

This screener is designed to evaluate the technical skills of candidates
applying for engineering or internship positions in the ETS Product Innovation
& Development division. The specific task is to write Python code that extracts
features around prepositions in sentences. These are the types of features that
are generally used to train supervised grammatical error correction models.

### Valid prepositions
The following set of tokens are considered to be valid prepositions for this
task:

- *on*
- *for*
- *of*
- *to*
- *at*
- *in*
- *with*
- *by*

**Important**: "to" should *not* be considered a preposition when followed by a
verb in a sentence.

### Feature extraction

Assume that a sentence consists of tokens $w_1...w_n$ and corresponding
part-of-speech tags $t_1...t_n$. For preposition $w_i$ at position $i$ in this
sentence, its features would be the following 12 token and tag sequences:

1. $w_{i-1}\ w_i$

2. $w_i\ w_{i+1}$

3. $w_{i-1}\ w_i\ w\_{i+1}$

4. $w\_{i-2}\ w_{i-1}\ w\_i$

5. $w_i\ w\_{i+1}\ w_{i+2}$

6. $w\_{i-2}\ w_{i-1}\ w\_i\ w\_{i+1}\ w\_{i+2}$

7. $t_{i-1}\ t_i$

8. $t_i\ t_{i+1}$

9. $t_{i-1}\ t_i\ t\_{i+1}$

10. $t\_{i-2}\ t_{i-1}\ t\_i$

11. $t_i\ t\_{i+1}\ t_{i+2}$

11. $t\_{i-2}\ t\_{i-1}\ t_i\ t\_{i+1}\ t_{i+2}$

Each set of features should have an ID that consists of the sentence number
(one-indexed) and the token number (zero-indexed). So for example, if the
second token in the first sentence is a preposition, its ID would be "1_1".

### Output format
The format of the output file should be a [jsonlines](https://jsonlines.org)
file, i.e., *each* line in the file should be a valid JSON object with the
following fields:

```json
{"id": "<preposition_id>", "prep": "<preposition>", "features": "<list_of_features>"}
```

**Important**: Make sure your output is a jsonlines file with one line per
preposition, and *not* a file containing a single JSON object for all
prepositions.

### Example

For example, the output for the first preposition `in` which occurs at token
position 6 in the first sentence should be the following JSON line:

```json
{
    "id":"1_5",
    "prep": "in",
    "features": ["entered in", "in to", "entered in to", "once entered in",
                 "in to the", "once entered in to the", "VBN IN", "IN TO",
                 "VBN IN TO", "RB VBN IN", "IN TO DT", "RB VBN IN TO DT"]
}
```

Note that we have included additional newlines here for readability but the
actual output would be on a single line.

### Suggested Python libraries

Feel free to use any publicly available Python library for tokenizing and
tagging the input sentences. Here are a couple of suggestions:

- [NLTK](https://www.nltk.org)
- [Spacy](https://spacy.io)

### Using ChatGPT or another LLM

It is acceptable to take the help of ChatGPT or another LLM to write your code
and your tests. However, you are expected to understand every detail of your
submission since it may form the basis of subsequent interview rounds. If you
do use one of these models, we strongly recommend that you submit a link to or
screenshot of your LLM chat session as part of your submission since that will
also help us evaluate your familiarity with LLMs and prompting techniques
which are relevant skills for an AI Engineer at ETS.

## Submission requirements

Your submission should meet the following requirements:

* It should be contained in a text-only `.py` file that can be run on the
command line. *Do not* submit Jupyter notebooks.

* It should tokenize sentences, tag them, and extract features for prepositions
(see below for feature definitions). The input data consists of one sentence
per line and is contained in the file `sentences.csv` in this repository.

* It should be written in Python 3 following best practices and coding conventions.

* It should contain appropriate unit and functional tests in a *separate* `.py`
file. There should be at least 3 relevant tests in total. Tests should be
written either using the built-in `unittest` module or `pytest`.

* It should contain sufficient documentation for users and for other
developers. This includes inline documentation in the code and tests files as
well as a README describing your approach and assumptions and how to run
the code and tests.

* The code must run successfully and produce non-empty output in jsonlines format.

* All included tests must be non-trivial and should pass.

* If you used ChatGPT or another LLM for writing code and/or tests, include a
link to or screenshot of your LLM chat session.


## Submission instructions

1. Clone this repository.

2. Create a new branch called "submission". Add your code, tests, and
   documentation to this branch. All files should be text-only. Do not use any
   binary formats.

3. Once your code is complete, push your branch, and submit a pull request to
   have your branch merged into the `main` branch. Submit all your work to this
  repository. Do *not* create a new repository or any other external online
  resources.

4. **Do not merge this pull request. Leave it open.**

## Important Notes

- Approach the task as if your were asked to write code with this functionality
to be used by other developers working on the same grammar error correction
system. In addition to documenting your code, you should provide a README
documenting your solution and any assumptions you made.

- We expect that 24 hours are sufficient to complete this task in its entirety.
