# Glossary

## Application Programming Interface (API) <a id="api"></a>
A protocol that defines communication between a client and server, often used to request data. APIs can help retrieve data from remote repositories, anything from weather to Twitter and Facebook.

## Argument (in Python) <a id="argument"></a>
An input that is passed into a [function](#function). For example,

`print('Hello World')`

passes the argument `'Hello World'` (a [string](#string) [variable](#variable)) into a `print()` function. In a [function](#function) definition, the variable inside parentheses is called a [parameter](#parameter)

## Artificial Intelligence <a id="artificial-intelligence"></a>
The science of making intelligent machines, especially machines that react to input data in a way similar to a human being. Historically, artificial intelligence has tended to rely on simple if-then statements (e.g. if the user mentions their mother, ask how she is doing), but recent advancements in artificial intelligence have focused on [machine learning](#machine-learning): the ability of machines to rewrite their own algorithms to improve their accuracy.

## Assignment Statement (in Python) <a id="assignment-statement"></a>

A statement that creates and/or changes a [variable](#variable). For example,

`new_variable = 7`

Note that assignment statements use a single `=` sign. They should not be confused with the equality [comparison operator](#comparison-operator) `==`, which compares whether two values are equal and returns a [boolean value](#boolean-value), either **True** or **False**.

## Bag of Words (Model) <a id ="bag-of-words"></a>
A model of texts that counts individual words without regard to grammatical location or phrases. Just as the letters of a Scrabble game are tossed into a bag without order, a "bag of words" model gathers all the words of a text into a "bag" with no regard to where a particular word occurs within the document. In this model, the reader knows every word and its frequency within the text but does not have the context of the word's use.

## Bibliographic Metadata <a id="bibliographic-metadata"></a>
Also known as "descriptive metadata," informational [metadata](#metadata) that describes a published item such as a book or journal article.  Bibliographic metadata contains data elements to help users identify and retrieve the published items.   It often has a formalized bibliographic format.

## Bigram <a id="bigram"></a>
An [n-gram](#n-gram) with a length of two. For example, "chicken stock" is a word bigram.

## Bayesian Classification <a id="bayes"></a>
A classification method based on [Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) that describes the probability of an event based on available prior knowledge. For example, given a dataset of the historical weather conditions (temperature, humidity, windspeed) from December 25th for every year over the last century, will it snow on December 25th, 2027?

## Boolean Operator <a id="boolean-operator"></a>
The operators:
* and
* or
* not
which are used in [flow control statements](#flow-control-statement) to connect or separate [expressions](#expression) that evaluate to [Boolean values](#boolean-value).

Assuming two expressions are connected by **and**, the combination will evaluate to **True** only if both individual expressions are **True**. 

|Expression|Evaluation|
|---|---|
|True and True|True|
|True and False|False|
|False and True|False|
|False and False|False|

Assuming two expressions are connected by **or**, the combination will evaluate to **False** only if both individual expressions are **False**

|Expression|Evaluation|
|---|---|
|True or True|True|
|True or False|True|
|False or True|True|
|False or False|False|

## Boolean Value (in Python) <a id="boolean-value"></a>
A value of **True** or **False** (first letter must be capitalized) that is assigned to a variable, usually for the purpose of guiding a [flow control statement](#flow-control-statement). 

## Cell (in a Jupyter Notebook)<a id="cell"></a>
See [Code Cell (in a Jupyter Notebook)](#code-cell) and [Markdown Cell (in a Jupyter Notebook)](#markdown-cell). 

## Clean Data <a id="clean-data"></a>
Data that has been standardized and corrected for accurate results. This phrase can also be used as a verb such as "to clean data" or "cleaning data." (Data cleaning is sometimes called "munging.") In practice, data cleaning makes up the bulk of text analysis work. 

## Clustering <a id="clustering"></a>
The statistical process of grouping together similar items. For example, topic analysis may cluster together sets of words that commonly co-occur, genre analysis may attempt to cluster similar genres, or authorship attribution may attempt to cluster novels by the same author. The clusters can be:

* Hard Clusters (mutually exclusive groups)
* Soft/Fuzzy Clusters (items may be in multiple groups)
* Hierarchal Clusters (part of hierarchy)

![visualization of cluster types](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/clustering_types.png)

## Code Block (in Python)<a id="code-block"></a>
A snippet of code that begins with an indentation. A code block can be a single line or many lines long. Blocks can contain other blocks forming a hierarchal structure. In such a case, the second block is indented an additional degree. Any given block ends when the number of indentations in the current line is less than the number that started the block. 

![Visualization of code block indentations](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/code_block_indentation.png)

## Code Cell (in a Jupyter Notebook)<a id="code-cell"></a>
A cell in a [Jupyter notebook](#jupyter-notebook) that is executable. They can be distinguished by the presence of a set of brackets and a colon to the left of the cell. [ ]: 

See also, [Markdown Cell (in a Jupyter Notebook)](#markdown-cell). 

## Comparison Operator (in Python)<a id="comparison-operator"></a>

A way to compare two values in Python to see if they are equal, greater than, or less than. 

|Operator|Meaning|
|---|---|
|==|Equal to|
|!=|Not equal to|
|<|Less than|
|>|Greater than|
|<=|Less than or equal to|
|>=|Greater than or equal to|

Note that the equality comparison operator is `==`, whereas a [variable](#variable) [assignment statement](#assignment-statement) is `=`. An [expression](#expression) using a comparison operator will evaluate to a [boolean value](#boolean-value), either **True** or **False**. Comparison operators are used within [flow control statements](#flow-control-statement) to determine which code should be executed next.

## Concordance <a id="concordance"></a>
A text analysis method for creating a list of all the occurences of a particular word or phrase. The [JSTOR Understanding Series](https://www.jstor.org/understand/), for example, creates a concordance of every journal article in JSTOR that contains a particular phrase from a work of literature.

## Concatenation (of strings in Python)<a id="concatenation"></a>

The joining of two or more strings such as with the addition [operator](#operator).

> 'Hello ' + 'World' + '!'

evaluates to

> 'Hello World!'

## Content Words <a id="content-words"></a>
As opposed to [function words](#function-words) (e.g. articles, pronouns, conjuctions), content words (e.g. nouns, verbs, and adjectives) carry greater lexical meaning. Word frequency analysis typically attempts to filter out function words, in order to make content words more prominent. This filtering is accomplished with a [stop words](#stop-words) list.

## Corpus <a id="corpus"></a>
A large (and often structured) collection of texts used for analysis. For example, all of the plays written by Shakespeare. A simple example might be a set of plain text files in a folder on your computer. A more complicated example may use [JSON](#json), [XML](#xml), or another form of markup, to allow for deeper analysis. The plural form is corpora.

See also [TEI XML](#tei-xml). 

## Counter (in Python) <a id="python-counter"></a>
A data type similar to a [Python dictionary](#python-dictionary) with a few key differences:
* A counter object with a value of zero or less, always returns 0
* When a key is called that doesn't exist in the counter, it returns 0 instead of an error like in a dictionary
* A counter object has additional methods for counting including `.most_common(x)` that returns the x most common values.
* Counter objects can be added, subtracted, as well as being modified through unions (&) and intersections (|)

## CSV (file) <a id="csv-file"></a>
A .csv file, or Comma-Separated Value file, is a simple format for storing structured data where each entry in the file is separated by a comma. Similarly, a [TSV file](#tsv-file) uses tabs to separate individual data entries. 

## Dataframe (in [Pandas](#pandas)) <a id="pandas-dataframe"></a>
The primary data structure for analysis, manipulation, and presentation of data with the [Pandas library](#pandas).

## Dataset <a id="dataset"></a>
A collection of information, usually computer files, used for statistical analysis. Most datasets are digital text (either numbers, words, or both), but they can also be other formats such as image, audio, and/or video content. Datasets are usually referred to as structured, semi-structured, or unstructured.
Structured data fits into a predetermined format and can usually be represented by a table, spreadsheet, or relational database. 
Unstructured data is more freeform. For example, longform texts, audio, or video content are unstructured. 
Semi-structured data uses tags or elements to mark out structures within an unstructured data set. Email files, for example, have both structured aspects (Sender, Subject, etc.), but the body of an email is usually unstructured.

## Dataset ID <a id="dataset-id"></a>
A unique identifier for a [dataset](#dataset) created using the [corpus](#corpus) builder. A copy of your dataset ID will be sent to you in an email.

## Descriptive Metadata <a id="descriptive-metadata"></a>
See [bibliographic metadata](#bibliographic-metadata).

## Dictionary (in Python) <a id="dictionary"></a>
A variable in [Python](#python) that stores data in [key/value pairs](#key-value-pair). This differs from a [Python](#python) [list](#list) which stores data in numberical order beginning with item 0.

## Dictionary (gensim) <a id="gensim-dictionary"></a>
A list created by [gensim](#gensim) of all the words in a corpus. The command for creating a gensim dictionary:
>gensim.corpora.Dictionary(documents)

Each word in the corpus is assigned a unique gensim dictionary ID starting from 0. 

## Discipline
An academic field or body of knowledge taught and studied within colleges or universities. Generally academic disciplines are divided into three large groups: 
* The Humanities include disciplines like English, History, Law
* The Sciences include disciplines like Physics, Biology, Mathematics
* The Social Sciences include include disciplines like Anthropology, Economics, and Sociology

Academic disciplines as divisions are matters of convenience for organizing departments, but many, if not most, professors research in two or more disciplines at a time. 

## Expression (in Python)<a id="expression"></a>

A combination of values and [operators](#operator) in Python that evaluate to a single value. 

> 2 + 3

is an expression using the addition [operator](#operator) (+) that evaluates to 5.

## Extracted Features <a id="extracted-features"></a>
The [JSON](#json) data format for [non-consumptive research](#non-consumptive) used by [HathiTrust Research Center](#htrc) tools. The format is similar to that used by [JSTOR](#jstor) and [Portico](#portico). [Read more](https://wiki.htrc.illinois.edu/display/COM/Extracted+Features+Dataset) on the HathiTrust Research Center website.

## Floating-point number (float) <a id="float"></a>
A float is a data type that contains a decimal number that can assigned to a variable as a value. (Other kinds of data types in Python include [strings](#string) and [integers](#integer).) 

|  Data type             | Examples                                      |
| -----------------------|:---------------------------------------------:|
| Integers               | -5, -3, 0, 5, 201                             |
| Floating-point numbers | -3.74, -3.14, 0.0, 503.4, 506                 | 
| Strings                | 'potatoes', 'Hello world!, 'no', '24 pizzas'  |

## Flow Control Statement (in Python)<a id="flow-control-statement"></a>
A flow control statement guides the actions of a program, helping decide what code should be executed next depending on a series of tests such as:

* `if` statements
* `else` statements
* `elif` statements
* `while` loops
* `for` loops

## Function (in Python) <a id="function"></a>
A small snippet of code that can be referenced and run easily without having to be rewritten over again. There are three kinds of functions in Python:

* Native functions built into Python
* Functions others have written that can be imported
* Functions a programmer defines themself

Functions often take an input, in the form of an [argument](#argument), and return an output. 

## Function Words <a id="function-words"></a>
The words in a sentence that have little lexical meaning and express grammatical relationships. Function words include articles, pronouns, and conjunctions. When using a [word frequency](#word-frequency) approach, function words are often filtered out in favor of [content words](#content-words) using a [stopwords](#stop-words) list. 

## Gensim <a id="gensim"></a>

A [python library](#library) for implementing various natural language processing methods, such as [TF-IDF](#tf-idf), [Word2Vec](#word2vec), and [Topic Modeling](#topic-modeling).

## git <a id="git"></a>
A method for saving versions of your computer code that enables many people to work on a single project. Users can upload and download the most current version of a project's code in a repository (or "repo").

Popular implementations of git include [GitHub](http://github.com) and [GitLab](http://gitlab.com).

## GitHub <a id="github"></a>
A popular implementation of [git](#git) code revision management found at https://github.com.
    
## GitLab <a id="gitlab"></a>
A popular implementation of [git](#git) code revision management found at https://gitlab.com.

## Global Scope (in Python) <a id="global-scope"></a>
The entire scope of a program, not just the [local scope](#local-scope) of a particular [function](#function). A [variable](#variable) created in the global scope is a [global variable](#global-variable) that can be read from anywhere in the program. A [global variable](#global-variable) can be read within a [local scope](#local-scope), but a [local variable](#local-variable) cannot be read at [global scope](#global-scope).

## Global Statement (in Python) <a id="global-statement"></a>
A statement in the [local scope](#local-scope) of a [function](#function) that declares a [variable](#variable) is a [global variable](#global-variable). Without a global statement, the [variable](#variable) will be assumed to be a [local variable](#local-variable) during an [assignment statement](#assignment-statement) (even if there is a [global variable](#global-variable) with the same name). 

## Global Variable (in Python) <a id="global-variable"></a>
A [variable](#variable) created in the [global scope](#global-scope) of a program. A [global variable](#global-variable) can be read within a [local scope](#local-scope), but a [local variable](#local-variable) cannot be read at [global scope](#global-scope).
    
## HathiTrust <a id="hathitrust"></a>
A partnership of academic and research institutions, offering access to millions of digitized volumes through the [HathiTrust Digital Library](#hathitrust-digital-library). 

## HathiTrust Digital Library <a id="hathitrust-digital-library"></a>
An online library of ~14 million volumes created by [HathiTrust](#hathitrust). Most of the materials are from research libraries, including content digitized via [Google Books](https://books.google.com/) and [Internet Archive](https://archive.org/).

## HathiTrust Research Center (HTRC)<a id="htrc"></a>
A partnership between Indiana University and the University of Illinois at Urbana-Champaign that develops a suite of tools and services for text data mining the [HathiTrust Digital Library](#hathitrust-digital-library).

## Index Number (in Python) <a id="index-number"></a>
The items contained in a [Python](#python) [List](#list) are kept in a strict numerical order by index number, starting from 0. 

## Integer <a id="integer"></a>
An integer is a data type that contains a whole number that can assigned to a variable as a value. (Other kinds of data types in Python include [strings](#string) and [floating point numbers](#float).) 

|  Data type             | Examples                                      |
| -----------------------|:---------------------------------------------:|
| Integers               | -5, -3, 0, 5, 201                             |
| Floating-point numbers | -3.74, -3.14, 0.0, 503.4, 506                 | 
| Strings                | 'potatoes', 'Hello world!, 'no', '24 pizzas'  |

## JavaScript (Programming Language) <a id="javascript"></a>
An object-oriented computer programming language often used to create interactive effects within webbrowsers.  Learn more at [w3schools](https://www.w3schools.com/js/default.asp).

## JSON (JavaScript Object Notation)<a id="json"></a>
An open-standard file format for storing and exchanging data that is intended to be easy to read and write humans and machines. Like [XML](#xml), JSON is often used by [APIs](#api) to transmit data from a remote repository (say weather data or Twitter data) to a local machine. 

## JSON Lines<a id="jsonl"></a>
Also called newline-delimited [JSON](#json), JSON Lines (file extension .jsonl) is structured so it may be processed one record at a time. Each line is a valid value. The file extension for JSON Lines is ".jsonl".

## json (Python library)<a id="json-python-library"></a>
A library for interpreting and converting [JSON](#json) into [Python](#python) code.

## JSTOR <a id="jstor"></a>
A not-for-profit that collaborates with the academic community and manages the [JSTOR Digital Library](#jstor-digital-library), a digital library for scholars, researchers, and students featuring more than 12 million academic journal articles, books, and primary sources in 75 disciplines. JSTOR is part of [ITHAKA](http://ithaka.org), a not-for-profit organization that also includes [Artstor](http://artstor.org), [Ithaka S+R](http://www.sr.ithaka.org/), and [Portico](http://portico.org).

## JSTOR Digital Library <a id="jstor-digital-library"></a>
A digital library for scholars, researchers, and students featuring more than 12 million academic journal articles, books, and primary sources in 75 disciplines.

## JupyterHub <a id="jupyterhub"></a>
A multi-user version of [The Jupyter Notebook](#the-jupyter-notebook), ideal for teaching environments.

## JupyterLab <a id="jupyterlab"></a>
The newest software from [Project Jupyter](#project-jupyter), intended to replace [The Jupyter Notebook](#the-jupyter-notebook), for executing and editing [Jupyter notebook](#jupyter-notebook) files.

## Jupyter Notebook, The (software) <a id="the-jupyter-notebook"></a>
A single-user web application for executing and editing [Jupyter notebook files](#jupyter-notebook). Will be replaced by [JupyterLab](#jupyterlab).

## Jupyter notebook (file)
A file with extension .ipynb that contains computer code (e.g. [Python](#python) or [R](#r)) alongside other explanatory media (text, images, video).

## Jupyter Server <a id="jupyter-serve"></a>
A server with the appropriate software environment (e.g. [JupyterHub](#jupyterhub), [JupyterLab](#jupyterlab), [Google Colab](#google-colab)) for running and editing [Jupyter notebooks](#jupyter-notebook).

## Key/Value Pair<a id="key-value-pair"></a>
A key/value pair is a data organizational structure where a key is associated with a unique value or set of values. For example, the user could supply the key **Age** and receive a value **58 years**. 

In Python](#python), Key/Value pairs are a key organizational structure for [dictionaries](#python-dictionary) and [Counters](#python-counter).

[JSON](#json) also encodes key/value pairs, such as:

>"title": "The Souls of Black Folk"

where the key is “title” and the value is “The Souls of Black Folk”. 

## Latent Dirichlet Allocation (LDA) <a id="lda"></a>
An algorithm commonly used for [topic modeling](#topic-modeling). Pronounced (lay-tent deer-ish-lay al-lo-cay-shun).

## Lemmatization <a id="lemmatization"></a>
The process of grouping together the conjugated forms of a word into a base form. For example, "jumping," "jumped," and "jumps" could be combined into "jump," the base form or *lemma*.

## Library (in Python) <a id="library"></a>
A large collection of methods and [functions](#function) for achieving certain tasks (e.g. image manipulation, web scraping). This saves time since the code can be added quickly and all at once around a specific group of tasks. The [Natural Language Toolkit (NLTK)](#nltk) is a common library used in [natural language processing](#nlp).

## List (in Python) <a id="list"></a>
A [variable](#variable) data type that stores items in numbered order beginning with item 0. The number for each item is called its [index number](#index-number). A list is different than a [Python](#python) [dictionary](#dictionary) [variable](#variable) which stores data in [key/value pairs](#key-value-pair). 

## List Comprehensions (in Python)<a id="list-comprehensions"></a>
A way to create a [Python list](#python-list) from another list. For example, when using a JSTOR/Portico [dataset](#dataset) converted to a [Python list](#python-list) called ``all_documents``, the code:

>reduced_list = [all_documents[x] for x in range(len(all_documents)) if all_documents[x].get('language') == ['eng']]

creates a ``reduced_list`` from ``all_documents`` by only including documents whose language is English. See also [documention on list comprehensions from python.org](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

## Local Scope (in Python) <a id="local-scope"></a>
The scope of a [function](#function) where a [local variable](#local-variable) can be created and used without conflicting with higher-order, [global variables](#global-variable). A [global variable](#global-variable) can be read within a [local scope](#local-scope), but a [local variable](#local-variable) cannot be read at [global scope](#global-scope).

## Local Variable (in Python) <a id="local-variable"></a>
A [variable](#variable) created in the [local scope](#local-scope) of a [function](#function). The [variable](#variable) name is erased after the [function](#function) executes and is not accessible in the larger [global scope](#global-scope) of the program. A [global variable](#global-variable) can be read within a [local scope](#local-scope), but a [local variable](#local-variable) cannot be read at [global scope](#global-scope).

## Machine Learning <a id="machine-learning"></a>
A subset of [artificial intelligence](#artificial-intelligence) that focuses on a machine algorithms that improve accuracy when exposed to additional data without being explicitly reprogrammed by a human.

## Markdown Cell (in a Jupyter Notebook)<a id="markdown-cell"></a>

A cell in a [Jupyter notebook](#jupyter-notebook) that contains explanatory information such as text, images, and links.

See also [Code Cell (in a Jupyter Notebook)](#code-cell), which can contain executable code. 

## Metadata <a id="metadata"></a>
Data that describes data. In the humanities and library contexts, this often refers to [bibliographic metadata](#bibliographic-metadata) that describes information such as author, publication date, medium, etc. It may also describe other kinds of data like files, for example "date created" or "file size."

## Method (in Python) <a id="method"></a>
Like a [function](#function), a method executes a set of pre-written code but on a particular object like a [list](#list). 

## Module (in Python) <a id="module"></a>
A set of [functions](#function) that can be imported for use in a [Python](#python) program. Modules can be gathered into even larger groups, such as a [package](#package) or [library](#library).

## Modulo (in Python)<a id="modulo"></a>
Notated as "%", an arithmetic operation that gives the remainder of a division. 34 % 6 = 4

## N-gram <a id ="n-gram"></a>
A sequence of n items from a given sample of text or speech. Most often, this refers to a sequence of words, but it can also be used to analyze text at the level of syllables, letters, or phonemes. N-grams are often described by their length. For example, word n-grams might include:
* stock (a 1-gram, or unigram)
* chicken stock (a 2-gram, or [bigram](#bigram))
* homemade chicken stock (a 3-gram, or [trigram](#trigram))
A text analysis approach that looks only at unigrams at the word level will not be able to differentiate between the "stock" in "stock market" and "chicken stock."

One of the most popular examples of text analysis with n-grams is the [Google N-Gram Viewer](https://books.google.com/ngrams).

See also [Natural Language Processing](#nlp). 

## Named Entity Recognition (NER)
A text analysis technique that seeks to identify and extract entities from a document. Entities could include things like:

* Person
* Organization
* Date
* Time
* Location

The [Natural Language Toolkit](#nltk), a suite of libraries in [Python](#python), can be used for Named Entity Recognition.

## Natural Language Processing (NLP) <a id="nlp"></a>
The study of how computers can understand and manipulate natural human language whether in spoken or written forms. This includes areas such as:

* Text Analysis
* Natural Language Generation
* Speech recognition
* Transcription
* Translation

Natural Language Processing is a subfield that connects linguistics, computer science, information engineering, digital humanities, and data science.

## Natural Language Toolkit (NLTK) <a id="nltk"></a>
A suite of libraries and programs for [Natural Language Processing](#nlp) written in [python](#python). NLTK includes libraries for tokening, collocation, n-grams, Part of Speech (POS) Tagging, and Named Entity Recognition (NER).

See the [project documentation](https://www.nltk.org/) and book [Natural Language Processing with Python](http://www.nltk.org/book/).

## Neural Network (in Artificial Intelligence) <a id="neural-network"></a>
In [artificial intelligence](#artificial-intelligence) (as opposed to biology), a neural network refers to a simplified model of brain neurons that enables machines to complete tasks through methods such as [machine learning](#machine-learning). Neural networks are commonly used on problems that involve data classification (Who is in this image?) and prediction (What price should this house sell for?). 

## Non-consumptive Research<a id="non-consumptive"></a>
Non-consumptive research allows analysts to do text analysis without displaying or reading substantial portions of copyrighted materials. In practice, this usually means giving analysts a [bag of words](#bag-of-words) that describes the frequency of every word in a text but not the order in which they occur. 

## Operator (in Python)<a id="operator"></a>

Changes a value through operations such as addition, multiplication, and [concatenation](#concatenation).

|Operator| Operation| Example | Evaluation |
|---|----|---|---|
|\*\*| Exponent/Power| 3 ** 3 | 27 |
|%| Modulus/Remainder| 34 % 6 | 4 |
|/| Division | 30 / 6 | 5|
|\*| Multiplication | 7 * 8 | 56 |
|-| Subtraction | 18 - 4| 14|
|+| Addition | 4 + 3 | 7 |

## Optical Character Recognition (OCR)<a id="ocr"></a>
The process of turning printed text into machine-readable digital text. Physical materials are scanned into digital images then specialized software attempts to turn the image into text. Two popular examples of OCR software are [Tesseract (Open Source)](https://github.com/tesseract-ocr/tesseract) and [ABBYY Finereader (Proprietary)](https://www.abbyy.com/en-us/finereader/).

## Package (in Python) <a id="package"></a>
A group of [modules](#module) that contain [functions](#function) that can be imported and used within a [Python](#python) program. Packages can be gathered into a larger group called a [library](#library).

## Pandas (in Python)<a id="pandas"></a>
A [library](#library) for visualizing, analyzing, and manipulating data in Python. Learn more about [Pandas at pydata.org](https://pandas.pydata.org/pandas-docs/version/0.15/tutorials.html).

## Parameter (in Python) <a id="parameter"></a>
A [variable](#variable) in a [function](#function) definition statement. The actual value or [variable](#variable) passed during execution is called an [argument](#argument).

## Part of Speech (POS) Tagging <a id="pos-tagging"></a>
The act of marking the grammatical part of speech (such as nouns, verbs, and adjectives) for each word in a document. The linguistic models for POS tagging can be very complex, often using over 100 separate parts of speech. 

POS Tagging can be accomplished using the [Natural Language Toolkit](#nltk) in [Python](#python).

## Plain text <a id="plain-text"></a>
A file that only contains text and can be easily read in a text editor (as opposed to a binary or executable file)

## Portico
A community-supported preservation archive that safeguards access to e-journals, e-books, and digital collections. One of the [data sources](https://docs.tdm-pilot.org/data-sources/) for the [dataset builder](https://tdm-pilot.org/builder/).

## Project Jupyter <a id="project-jupyter"></a>
A non-profit that develops open-source software, open standards, and services across many programming languages. They are most well-known for software such as [The Jupyter Notebook](#the-jupyter-notebook), [JupyterLab](#jupyterlab), and [JupyterHub](#jupyterhub). All three of these programs are used to create, edit, and share programming notebooks, known as [Jupyter notebooks](#jupyter-notebook).

## Python (Programming Language) <a id="python"></a>
A highly-flexible, easy-to-learn programming language that is widely-used in the digital humanities and data science.

## R (Programming Language) <a id="r"></a>
A programming language that is widely-used for statistical analysis and data mining, commonly in the areas of digital humanities and data science.

## Repository (for git, GitHub, GitLab, etc) <a id="repository"></a>
Also known as a "repo". A repository is a place to store all the versions of the code for a computer programming project.

See also [git](#git).

## Sentiment Analysis <a id="sentiment-analysis")</a>
A text analysis method that attempts to discover the emotions expressed in a sample of writing. Depending on the complexity of the method, it may discover simple distinctions (positive vs. negative) or more nuanced concepts (gratitude, anger, sadness, frustation, etc.).

## Slice (in Python) <a id="slice"></a>
A subset of items created from a [list](#list) using [index numbers](#index-number).
> example_list[2:4]
The slice above creates a new [list](#list) from `example_list` that contains the items at index 2 and 3 (but not 4).

## Stop Words (List) <a id="stop-words"></a>
A stop words list is a set of words or phrases that are ignored in [word frequency](#word-frequency) analysis. It is common for a researcher who is interested in prominent nouns and verbs to remove [function words](#function-words) (e.g. the, and, I, to, of, a). A stop word list may also include other common words, such as character ids which are usually the most common words in a play text.

## String (in Python) <a id="string"></a>
A string is a data type that contains a set of characters that can assigned to a variable as a value. (Other kinds of data types in Python include [integers](#integer) and [floating point numbers](#float).) 

|  Data type             | Examples                                      |
| -----------------------|:---------------------------------------------:|
| Integers               | -5, -3, 0, 5, 201                             |
| Floating-point numbers | -3.74, -3.14, 0.0, 503.4, 506                 | 
| Strings                | 'potatoes', 'Hello world!, 'no', '24 pizzas'  |  

## Tag Cloud (or Word Cloud)<a id ="tag-cloud"></a>
A tag cloud is a visualization of the relative word frequencies in a [corpus](#corpus). The relative size of each word in a tag cloud depends on its frequency within a text. Larger words occur more frequently.

![Word Cloud of the content of journal African American Review](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/wordcloud.jpeg)

**A Tag Cloud of the journal *African American Review* (and its precursors *Black American Literature Forum* and *Negro American Literature Forum*).** 

## tdm_client<a id="tdm-client"></a>
A module that automatically pulls in a [dataset](#dataset) to the [JupyterLab](#jupyterlab) environment based on a [dataset ID](#dataset-id). 

## TEI XML <a id ="tei-xml"></a>
A form of [XML Markup](#xml), or tagging, created by the [Text Encoding Initiative](https://tei-c.org/) to describe digital documents. This markup can help computers recognize particular aspects of the text. Text analysis often requires explicit marking, even for textual aspects that a human reader can easily pick out:
* Title
* Author Name
* Name of the speaker in a play
* A paragraph
* The speaker in a play
* Stage directions
* A stanza

See also [Parts of Speech Tagging](#pos-tagging), [Lemmatization](#lemmatization), [Tokenization](#tokenization).

## Term Frequency-Inverse Document Frequency (TFIDF)<a id="tf-idf"></a>
A statistical method that intends to reflect how important a particular word is within a [corpus](#corpus). A simple measurement of "term frequency" is divided by inverse document frequency, limiting the weight of common words like "the", "of", and "to".

## Token <a id="token"></a>
A chunk or [string](#string) of text, most often a single word. 

## Topic Modeling (or Topic Analysis)<a id="topic-modeling"></a>

A [machine learning](#machine-learning) text analysis method that attempts to discover a group of words that [cluster](#clustering) together in a set of documents. One of the most common algorithms for topic modeling is [Latent Dirichlet Allocation (LDA)](#lda). 

## Trigram <a id="trigram"></a>
An [n-gram](#n-gram) with a length of three. For example, "homemade chicken stock" is a word trigram.

## TSV (file) <a id="tsv-file"></a>
A .tsv file, or Tab-Separated Value file, is a simple format for storing structured data where each entry in the file is separated by a tab. Similarly, a [CSV file](#csv-file) uses commas to separate individual data entries.

## Tuple (in Python) <a id="tuple"></a>
A data type similar to a [Python list](#python-list), except that tuples are:

1. Notated with parentheses
```python
list = [1, 'monkey', 33.3234]
tuple = (1, 'monkey', 33.3234)
```

2. Immutable. Like a string, the elements of a tuple cannot be changed. 

## Unigram <a id="unigram"></a>
An [n-gram](#n-gram) with a length of one. For example, "chicken" is a unigram.

## Variable (in Python) <a id="variable"></a>
A named object that stores a value in Python, such as an [integer](#integer), [float](#float), or [string](#string). 

Variables are created with an [assignment statement](#assignment-statement).

## Voyant <a id="voyant"></a>
A flexible, web-based platform for text analysis that can also be run locally. [Voyant](https://voyant-tools.org/) has many kinds of visualizations, supports saving, and creates embeddable html objects. To learn more, see [the documentation](https://voyant-tools.org/docs/#!/guide/start). 

## Word Cloud<a id="word-cloud"></a>
See [Tag Cloud](#tag-cloud).

## Word Embedding
A collective name for [Natural Language Processing](#nlp) techniques that map words to vectors of real numbers using [neural networks](#neural-network) and dimensionality reduction on a word co-occurence matrix. Word2vec is a common model for producing word embeddings. 

## Word Frequency <a id="#word-frequency"></a>
A text analysis method that counts the number of occurences of individual words within a particular text. Word frequency uses a [bag of words](#bag-of-words) model where the order of words is not significant. Just as the letters of a Scrabble game are tossed into a bag without order, word frequency merely records the number of occurences with no regard to where a particular word occurs within a document. 

An alternative to this approach is using [n-grams](#n-gram) which can capture phrases in addition to individual words.

## XML <a id="xml"></a>
Short for (eXtensible markup language), XML uses tags to identify parts of a document for a machine to understand. Like HTML, these tags have an opening tag (e.g. <l>) and a closing tag marked by a forward slash (e.g. </l>). Unlike HTML, these tags can be freely created according to whatever standard the creator needs. One prominent example is the [Text Encoding Initiative](https://tei-c.org/). The example below uses [TEI-XML](#tei-xml) to describe Shakespeare's Sonnet 130 by labeling lines, quatrains, and the final couplet. This kind of markup enables computers to do complex analysis quickly such as comparing every couplet, quatrain, or line in Shakespeare's sonnets.
```
<text>
 <body>
  <lg>
   <lg type="quatrain">
    <l>My Mistres eyes are nothing like the Sunne,</l>
    <l>Currall is farre more red, then her lips red</l>
    <l>If snow be white, why then her brests are dun:</l>
    <l>If haires be wiers, black wiers grown on her head:</l>
   </lg>
   <lg type="quatrain">
    <l>I have seene Roses damaskt, red and white,</l>
    <l>But no such Roses see I in her cheekes,</l>
    <l>And in some perfumes is there more delight,</l>
    <l>Then in the breath that from my Mistres reekes.</l>
   </lg>
   <lg type="quatrain">
    <l>I love to heare her speake, yet well I know,</l>
    <l>That Musicke hath a farre more pleasing sound:</l>
    <l>I graunt I never saw a goddesse goe,</l>
    <l>My Mistres when shee walkes treads on the ground.</l>
   </lg>
  </lg>
  <lg type="couplet">
   <l>And yet by heaven I think my love as rare,</l>
   <l>As any she beli'd with false compare.</l>
  </lg>
 </body>
</text>
```