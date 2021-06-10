__author__ = "Natalie Shapira"
__copyright__ = "Copyright 2021, Hebrew Psychological Lexicons Project"
__credits__ = ["Natalie Shapira", "Dana Atzil-Slonim", "Daniel Juravski", "Moran Baruch",
               "Adar Paz", "Dana Stolowicz-Melman" , "Tal Alfi-Yogev" , "Roy Azoulay" ,
               "Adi Singer", "Maayan Revivo", "Chen Dahbash", "Limor Dayan", "Tamar Naim",
               "Lidar Gez", "Boaz Yanai", "Adva Maman", "Adam Nadaf", "Elinor Sarfati",
               "Amna Baloum", "Tal Naor", "Ephraim Mosenkis", "Matan Kenigsbuch",
               "Badreya Sarsour", "Yarden Elias", "Liat Braun", "Moria Rubin",
               "Jany Gelfand Morgenshteyn", "Noa Bergwerk", "Noam Yosef", "Sivan Peled",
               "Coral Avigdor", "Rahav Obercyger", "Rachel Mann", "Tomer Alper", "Inbal Beka",
               "Ori Shapira", "Yoav Goldberg"]
__license__ = "Apache-2.0; CC-BY-SA"
__version__ = "1.0.4"
__maintainer__ = "Natalie Shapira"
__email__ = "nd1234@gmail.com"

from .Lexicons import Lexicons

class LexiconsAPI(object):

    @staticmethod
    def number_of_words(text):
        word_n = 0
        for word in text.split():
            word_n += 1
        return word_n

    @staticmethod
    def number_of_words_in_lexicon(text, lexicon):
        lex_word_n = 0
        for word in text.split():
            if word in lexicon:
                lex_word_n += 1
        return lex_word_n

    @staticmethod
    def lexicons_union(lexicons_list):
        union_lexicons = set()
        for lexicon in lexicons_list:
            union_lexicons = union_lexicons.union(lexicon)
        return list(union_lexicons)

    @staticmethod
    def frequency_of_lexicon(text, lexicon):
        return LexiconsAPI.number_of_words_in_lexicon(text, lexicon)/LexiconsAPI.number_of_words(text)

    @staticmethod
    def df_to_lexicons(in_df,out_df,lexicons, col_name,new_col_prefix):
        for lexicon_name, lexicon_words in lexicons:
            out_df[new_col_prefix + '_' + lexicon_name] = in_df[col_name].apply(
                lambda x: LexiconsAPI.number_of_words_in_lexicon(str(x), lexicon_words))
        return out_df

if __name__ == '__main__':
    lexicons = Lexicons()
    print(LexiconsAPI.number_of_words("היא אמרה הוא אמר והיא אמרה היא גם אני אני אני"))
    print(LexiconsAPI.number_of_words_in_lexicon("היא אמרה הוא אמר והיא אמרה היא גם אני אני אני", lexicons.DataDrivenSupervised_WellBeing_NonClinical))

    print(LexiconsAPI.number_of_words_in_lexicon("זה בכלל לא מעניין אותי אני אדיש לזה", lexicons.EmotionalVariety_Calm))
    print(LexiconsAPI.number_of_words_in_lexicon("זה בכלל לא מעניין אותי אני אדיש לזה", lexicons.EmotionalVariety_NotInterested))

    lex1 = lexicons.EmotionalVariety_Calm
    lex2 = lexicons.EmotionalVariety_NotInterested
    lex3 = LexiconsAPI.lexicons_union([lex1, lex2])
    print(LexiconsAPI.number_of_words_in_lexicon("זה בכלל לא מעניין אותי אני אדיש לזה", lex3))
    print(LexiconsAPI.frequency_of_lexicon("זה בכלל לא מעניין אותי אני אדיש לזה", lex3))

    import pandas as pd
    df_in = pd.read_csv('../Resources/For documentation purposes/df_example.csv')
    df_out = pd.DataFrame() #or df_in
    LexiconsAPI.df_to_lexicons(df_in, df_out, lexicons, 'story','story')
    df_out.to_csv('./Resources/For documentation purposes/df_example_out.csv', index=False)