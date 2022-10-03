import os, glob
import random

#Торубара Даниил, 922403
# C:\Users\User\Desktop\Песни

class Crawler:
    def __init__(self, path_to_files):
        self.path_to_files = path_to_files
        list1 = []
        files_list = glob.glob(os.path.join(self.path_to_files, '*.txt'))
        print(files_list)
        files_list = filter(lambda x: 'mix.txt' not in x, files_list)
        for filename in files_list:
            print(f'Filename: {filename}')
            with open(filename, 'r', encoding="utf8") as file:
                data = file.read()
                data_into_list = data.split("\n")
                for i in data_into_list:
                    list1.append(i.replace(',', '').replace('.', '').replace('"', ''))
        list_of_strings = [i for i in list1 if i]
        self.list_of_strings = list_of_strings


class Generator(Crawler):
    def __init__(self, path_to_files, lines_couplet, lines_chorus):
        super().__init__(path_to_files)
        couplet_list = []
        chorus_list = []

        a = 0
        while a < 3:
            couplet_list.append(random.choices(self.list_of_strings, k = lines_couplet))
            a = a + 1

        chorus_list.append(random.choices(self.list_of_strings, k=lines_chorus))

        self.couplet_list = couplet_list
        self.chorus_list = chorus_list

        song = [self.couplet_list[0], [" "], ["Припев:"], self.chorus_list[0], [" "], self.couplet_list[1], [" "], ["Припев:"], self.chorus_list[0], [" "], self.couplet_list[2], [" "], ["Припев:"], self.chorus_list[0]]
        self.song = song
        print(song)

class Saver(Generator):
    def __init__(self, path_to_files, lines_couplet, lines_chorus):
        super().__init__(path_to_files, lines_couplet, lines_chorus)
        with open(os.path.join(self.path_to_files, "mix.txt"), "w", encoding="utf8") as temp_file:
            for _list in self.song:
                for _string in _list:
                    temp_file.write(str(_string) + '\n')

mix = Saver(r'C:\Users\User\Desktop\Песни', 6, 6)