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
#__license__ = "GPL" ?
__version__ = "1.0.1"
__maintainer__ = "Natalie Shapira"
__email__ = "nd1234@gmail.com"

with open ('TopicModelResults_200_Topics_2020.txt', 'r', encoding='utf-8') as in_file:
    for i in range(200):
        line = in_file.readline()
        topic_number = line.strip().split('\t')[0]
        topic_prob = line.strip().split('\t')[1]
        words = line.strip().split('\t')[2:]
        words = words[0].split(' ')
        #words[0].replace(" ", "\n")
        padding =''
        if int(topic_number) < 10:
            padding = '00'
        elif int(topic_number) < 100:
            padding = '0'
        with open ('./Resources/LexiconsCollection_dev/ConversationTopics_Topic'+ padding + topic_number+'.txt', 'w', encoding='utf-8') as out_file:
            #out_file.write(words[0])
            for w in words:
                out_file.write(w)
                out_file.write('\n')
