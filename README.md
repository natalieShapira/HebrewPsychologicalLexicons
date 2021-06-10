# Hebrew Psychological Lexicons

This is the official code accompanying a paper on the [Hebrew Psychological Lexicons](https://www.aclweb.org/anthology/2021.clpsych-1.6.pdf) was presented at CLPsych 2021.
## Summary

* A large collection of Hebrew psychological lexicons and word lists
* Easy-to-use Python interface for Hebrew clinical psychology
text analysis
* Useful for various psychology applications such as detecting emotional state,
well being, relationship quality in conversation, identifying topics (e.g., family, work)
and many more
* Lexicons were developed through data driven means, and verified by domain experts, clinical psychologists and psychology students, in a process of reconciliation
with three judges
* Development and verification relied on a dataset of a total of 872 psychotherapy session transcripts
* Initial results of research studies employing this resource confirm its value

## Usage

First, install the package using `pip`:
```shell script
pip install hepsylex
```

OR

```shell script
git clone https://github.com/natalieShapira/HebrewPsychologicalLexicons
python setup.py install
```

Then, in Python, to load the lexicons:
```python
from hepsylex import Lexicons
lexicons = Lexicons()
```
and a usable wrapper:
```python
from hepsylex import LexiconsAPI
print(LexiconsAPI.number_of_words("אני אוהבת אותך"))
# out: 3
print(LexiconsAPI.number_of_words_in_lexicon("אני לא מבינה", lexicons.DataDrivenSupervised_WellBeing_NonClinical))
# out: 0
print(LexiconsAPI.number_of_words_in_lexicon("אני לא מבינה", lexicons.DataDrivenSupervised_WellBeing_Clinical))
# out: 1
print(LexiconsAPI.frequency_of_lexicon("אני לא מבינה", lexicons.DataDrivenSupervised_WellBeing_Clinical))
# out: 0.333333

print(LexiconsAPI.number_of_words_in_lexicon("וואוו מדהים", lexicons.EmotionalVariety_Enthusiastic))
# out: 2
print(LexiconsAPI.number_of_words_in_lexicon("אני סומכת עליך", lexicons.EmotionalVariety_Trust))
# out: 1
print(LexiconsAPI.number_of_words_in_lexicon("אממ אהה מה זה אומר", lexicons.DepressiveCharacteristics_NonFluenciesAhEm))
# out: 2
lex1 = lexicons.EmotionalVariety_Trust
lex2 = lexicons.DepressiveCharacteristics_NonFluenciesAhEm
lex3 = LexiconsAPI.lexicons_union([lex1, lex2])
print(LexiconsAPI.number_of_words_in_lexicon("אממ אני סומכת עליך", lex3))
# out: 2
```
There is also option to work with files (see input and output example files in /src/hepsylex/Resources/For documentation purposes/):
```python
import pandas as pd
df_in = pd.read_csv('Resources/For documentation purposes/df_example.csv')
df_out = pd.DataFrame() #or df_in
LexiconsAPI.df_to_lexicons(df_in, df_out, lexicons, 'story','story')
df_out.to_csv('./Resources/For documentation purposes/df_example_out.csv', index=False)
```

## Citation

If you make use of this software for research, we would appreciate the following citation:

```console
@inproceedings{shapira2021hebrew,
  title={Hebrew Psychological Lexicons},
  author={Shapira, Natalie and Atzil-Slonim, Dana and Juravski, Daniel and Baruch, Moran and Stolowicz-Melman, Dana and Paz, Adar and Alfi-Yogev, Tal and Azoulay, Roy and Singer, Adi and Revivo, Maayan and others},
  booktitle={Proceedings of the Seventh Workshop on Computational Linguistics and Clinical Psychology: Improving Access},
  pages={55--69},
  year={2021}
}
```
Title: [Hebrew Psychological Lexicons](https://www.aclweb.org/anthology/2021.clpsych-1.6.pdf)


Authors:  Natalie Shapira, Dana Atzil-Slonim, Daniel Juravski, Moran Baruch, Adar Paz,
Dana Stolowicz-Melman, Tal Alfi-Yogev, Roy Azoulay, Adi Singer, Maayan Revivo,
Chen Dahbash, Limor Dayan, Tamar Naim, Lidar Gez, Boaz Yanai, Adva Maman,
Adam Nadaf, Elinor Sarfati, Amna Baloum, Tal Naor, Ephraim Mosenkis,
Matan Kenigsbuch, Badreya Sarsour, Yarden Elias, Liat Braun, Moria Rubin,
Jany Gelfand Morgenshteyn, Noa Bergwerk, Noam Yosef, Sivan Peled, Coral Avigdor,
Rahav Obercyger, Rachel Mann, Tomer Alper, Inbal Beka, Ori Shapira, Yoav Goldberg

Affiliation: Bar-Ilan University, Israel

Published: Proceedings of the Seventh Workshop on Computational Linguistics and Clinical Psychology, June 2021, Association for Computational Linguistics.

## Licensing

- The code is provided with license (apache 2.0), as is, and without warranties. 
- The data word lists and lexicon is provided with creative commons license CC-BY-SA, as is, and without warranties.
