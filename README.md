# Constellate Collaborative Notebooks and Lessons
Constellate is a platform to learn and perform text analysis, build datasets, and share analytics course materials. Open the black box of text analysis with [Constellate](https://constellate.org/), from JSTOR and Portico. 

This repository is a collection of Jupyter Notebooks that may be used by individuals for learning or teaching text analytics.  You may access them in our textbook, [Teaching Text Analysis with Constellate](https://ithaka.github.io/tdm-notebooks/book/intro.html), and also interact with a number of them from your [Constellate datasets](https://constellate.org/dataset/dashboard/).  All these Notebooks will run in the Constellate environment.  

Read more about Constellate below, after the nuts and bolts of cloning these notebooks.

## Local Installation

You can also clone this repository and run the examples in a local Jupyter Notebook environment. 
Please keep in mind that this project is in a beta phase and both the notebooks and client code may change frequently. 
If you have created your own notebooks, or used the client code in some way, we would like to hear about it. Please let us know either here via Github issues or by emailing tdm@ithaka.org.

To install the client run the following.

* `python -m pip install -r requirements.txt`
* `python src/tdm_client.py install`

Some of the examples use [nltk](https://www.nltk.org/) model files. Download these with:

* `python -m nltk.downloader stopwords wordnet`

# About Constellate
## Problem:
Text analytics, or the process of deriving new information from pattern and trend analysis of the written word, has the potential to revolutionize research across disciplines. Sadly, there is a massive hurdle facing those eager to unleash its power.  The coding skills and statistical knowledge that text mining requires can take years to develop.   All too often, researchers learn about the promise of text mining, only to have it revealed that the promise can be realized solely by the select few with the necessary technical skills.  Ted Underwood, Professor of English at the University of Illinois, likens this scenario to researchers being presented with a “[deceptively gentle welcome mat, followed by a trapdoor](https://tedunderwood.com/2018/01/04/a-broader-purpose/)."

## Solution:
ITHAKA has addressed this problem by building Constellate, a text analytics platform aimed at teaching and enabling a generation of researchers to text mine. Two of ITHAKA’s services, [JSTOR](https://www.jstor.org/) and [Portico](https://www.portico.org/), are the initial sources of content for the new platform, which now includes [Chronicling America](https://chroniclingamerica.loc.gov/), collections from [Documenting the American South](https://docsouth.unc.edu/docsouthdata/), the [South Asia Open Archives](https://www.jstor.org/site/saoa/) and [Independent Voices](http://revealdigital.com/independent-voices/) from [Reveal Digital](http://revealdigital.org/).  

Constellate provides value to users in three core areas -- they can teach and learn text analytics, build datasets from across multiple content sources, and visualize and analyze their datasets:

### Learn & Teach
* Template and Tutorial Code: Work with template Jupyter Notebooks to analyze your dataset and learn about text analytics (with additional environments forthcoming, such as R Studio).
* Lessons and Documentation: Lessons and educational materials created by a community of experts, including those from the NEH-funded [Text Analysis Pedagogy Institutes](http://labs.jstor.org/tapi/).
* Collaborative Teaching Materials Creation: Users may create, edit, reuse and collaborate in the creation of tutorials, code, documentation, and other educational resources for text analysis.

### Build
* Multiple Collections: Anchor collections from JSTOR and Portico, with additional content sources continually added (such as Library of Congress’ Chronicling America). Further [details about the collections](https://docs.constellate.org/data-sources/) are available.
* Data Download in JSON
    * All content - bibliographic metadata, unigrams, bigrams, trigrams
    * Open content - bibliographic metadata, full-text, unigrams, bigrams, trigrams
* Dataset Dashboard: Easily view datasets you have built or accessed.

### Analyze
* Analytics Lab: Integrated computational environment powered by BinderHub that will allow users to seamlessly analyze text content using provided template Jupyter Notebooks and tutorials.
* Visualize: Built-in visualizations for your datasets.
* Work with Rights Restricted Full Text: We are investigating the best way to meet this need -- please contact us at [tdm@ithaka.org](mailto:tdm@ithaka.org) if you need rights restricted full-text or just want to talk about your research.

# Interested in Participating?
Reach out to us to participate in [our beta program](https://docs.constellate.org/participate-and-launch/#roll-out-and-beta-evaluation) and get access to larger datasets and text analytics classes.

<hr/>

Created by [Nathan Kelber](http://nkelber.com) and [Ted Lawless](https://github.com/lawlesst) for [JSTOR Labs](https://labs.jstor.org/) under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/)

**For questions/comments/improvements, email [tdm@ithaka.org](mailto:tdm@ithaka.org).**

<br />

![CC BY License Logo](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/CC_BY.png)
