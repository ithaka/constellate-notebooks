# Open Educational Resources for Text Analysis
A set of notebooks for JSTOR's text analysis project, [Constellate](https://tdm-pilot.org/). 

## Installing

These [examples and tutorials](https://docs.tdm-pilot.org/topic/beginner-lessons/) are intended to be run via a hosted Binder solution in conjuction with our [dataset builder web application](https://tdm-pilot.org/).


You can also clone this repository and run the examples in a local Jupyter Notebook environment. 
Please keep in mind that this project is in a beta phase and both the notebooks and client code may change frequently. 
If you have created your own notebooks, or used the client code in some way, we would like to hear about it. Please let us know either here via Github issues or by emailing tdm@ithaka.org.

To install the client run the following.

* `python -m pip install -r requirements.txt`
* `python tdm_client.py install`

Some of the examples use also use [nltk](https://www.nltk.org/) model files. Download these with:

* `python -m nltk.downloader stopwords wordnet`

<hr/>

Created by [Nathan Kelber](http://nkelber.com) and [Ted Lawless](https://github.com/lawlesst) for [JSTOR Labs](https://labs.jstor.org/) under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/)
**For questions/comments/improvements, email tdm@ithaka.org.**<br />![CC BY License Logo](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/CC_BY.png)
