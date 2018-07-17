# SemAxis: A Lightweight Framework to Characterize Domain-Specific Word Semantics Beyond Sentiment

Authors: Jisun An, Haewoon Kwak, and Yong-Yeol Ahn

## Abstract
Because word semantics can substantially change across communities and contexts, capturing domain-specific word semantics is an important challenge. Here, we propose *SemAxis*, a simple yet powerful framework to characterize word semantics using many semantic axes in word-vector spaces beyond sentiment. We demonstrate that *SemAxis* can capture nuanced semantic representations in multiple online communities. We also show that, when the sentiment axis is examined, *SemAxis* outperforms the state-of-the-art approaches in building domain-specific sentiment lexicons. 


## Highlights

## Citing SemAxis

If you make use of this work in your research please cite the following paper:

Jisun An, Haewoon Kwak, and Yong-Yeol Ahn. 2018. SemAxis: A Lightweight Framework to Characterize Domain-Specific Word Semantics Beyond Sentiment. *In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL'18)*




## Using the code

To use SemAxis you will need to download some that are pre-trained. Once this is done, you would specify the path (variable: EMBEDDING_PATH) to these embeddings in semaxis.py. The file semaxis.py contains implementations for computing semantic axes given two pole words and projecting target word on the semantic axes along with some comments/documentation on how to use them.


### Pre-trained word embeddings used in the study

We make pre-trained word embeddings used in this study availalbe to download. 

* [Google300D](https://code.google.com/archive/p/word2vec) Note that for SemAxis, bin file needs to be converted to text file: [see](https://stackoverflow.com/questions/27324292/convert-word2vec-bin-file-to-text)
* [Reddit20M](https://drive.google.com/file/d/1ewmS5Uu4tWAkwWsuY8FZVgLr85vvZXye/view?usp=sharing)
* Subreddits
	* [/r/SandersForPresident](https://drive.google.com/file/d/1rfHPRY8_wTpqIYvh4CRzv7FZIw_PaVyy/view?usp=sharing)
    * [/r/The_Donald](https://drive.google.com/file/d/1QE3X9CUsKndKguyNoHwRrTsxa4sBUt5V/view?usp=sharing)
    * [/r/atheism](https://drive.google.com/file/d/11790E6eEI2QxcJNpZtXDpmieEnPqqKSv/view?usp=sharing)
    * [/r/Christianity](https://drive.google.com/file/d/1nM1YSzSh04rdNoAfpXYvanVVB8CvmMUR/view?usp=sharing)
    * [/r/NintendoSwitch](https://drive.google.com/file/d/1NdJDz6SxfByfCGWIGdI82ATqEhbiPv5x/view?usp=sharing)
    * [/r/PS4](https://drive.google.com/file/d/1G-6Tbzue_LdwG7yj0kjFywCmDauHYC7a/view?usp=sharing)
    * [/r/AskWomen]()
    * [/r/AskMen]()


### 732 Pre-defined Semantic Axes for download

We systematically induce 732 semantic axes based on the antonym pairs from [ConceptNet](http://conceptnet.io/). You can download them in the following: [732 Pre-defined Semantic Axes for download](https://github.com/ghdi6758/SemAxis/blob/master/axes/732_semaxis_axes.tsv). The file includes 732 antonym word pairs. The file is tab-separated. 


## Dependencies

An up-to-date Python 3.5 distribution, with the standard packages provided by the anaconda distribution is required. 

In particular, the code was tested with:

numpy (1.14.0)
gensim (3.4.0)
scipy (1.0.0)
sklearn (0.18.dev0 or 0.17.1)