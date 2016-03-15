#!/usr/bin/env python
# encoding: utf-8

"""
unique-word-abbreviation.py
 
Created by Shuailong on 2016-03-15.

https://leetcode.com/problems/unique-word-abbreviation/.

"""

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = {}
        for word in dictionary:
            ab = self.abbr(word)
            self.d[ab] = word if ab not in self.d else '' if self.d[ab] != word else self.d[ab]

    def abbr(self, word):
        return word[0] + str(len(word)-2) + word[-1] if len(word) > 2 else word

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        ab = self.abbr(word)
        return ab not in self.d or self.d[ab] == word
        
def main():
    dictionary = ["deer", "door", "cake", "card", "card"]
    vwa = ValidWordAbbr(dictionary)
    print vwa.isUnique("dear") == False
    print vwa.isUnique("cart") == True
    print vwa.isUnique("cane") == False
    print vwa.isUnique("make") == True
    print vwa.isUnique("cake") == True

    print vwa.isUnique("daer") == False
    print vwa.isUnique("deer") == False
    print vwa.isUnique("card") == True

    dictionary = ["a", "a"]
    vwa = ValidWordAbbr(dictionary)
    print vwa.isUnique("a") == True

    dictionary = ["eersynoiyqkqubhdd","ylz","yldongowlrnsafafcgmz","rxcjc","dvgdtnknareecongydc","ixiwz","erjfyctsla","xovvrnbbvivbsuhb","bpslbpzbwphhwvhtcr","wptflnqkvekpkt","hwoiniqvfe","dgidjd","ecgsghxuesvqmhxe","kfgppbbvwfyp","qntzitqjuazrqwz","yjbycoyngfrreiyibdsk","nguqbtdistlgicmjfrs","yjqrqibgp","avulamdverhdpkpqjtae","cbwvtowh","yhgvjnvo","rihywmuspvzvp","rbkpetmovkwj","jtsehilffmfkicusup","ficdolmdtvk","qwldknj","hseogl","pdyxrfdxekk","xnrliooqnsqfzwgd","utnumabyrkasiizsjx","urygh","odj","nttcedxgpkjqzwfb","gxs","rkizfdlfmm","pjlz","fvjm","edkozzeuhxp","pbjcmakwqkdm","ppuhqdpaokitaowrzkfh","yimgbxllumgkbqadjjqf","sqsytssfjbaldz","llkw","aliw","hagvoxjnuuhsafkmxww","hahndehh","fqmrjyuogqpxyv","gnzbcrikf","auopjpwsepqwmend","xfgsbfafytrrkyevtz","acrtfozvjdvg","hspkwabiheogyk","uvlcpqien","eaamufqeal","wsvuyeysox","oywhf","kasdlmnj","fjpryefc","ftdqq","ftfqzqqig","dloh","tleszaz","yajyoyaxmmos","zbobgedfdpacbkzmxt","lmcj","dtjonkbwsg","xeiqjxvsfjdfddclnso","gpeutivfqwzfyrtax","wjoo","pptzwdcynnfpnirfkfo","wsudzgwuouof","ykjmbtoafrjjsehckh","oqhamskusmqofrsgkqfv","yifmkodzvk","vmufzdavpwjagmlcv","dtamuegujvtzdxui","nxdyotptdjdhst","rsthatscf","kdpwhmjtnkunabzaxv","ggzytma","sdypdz","xncvkmcddpkhkoalh","qnjndoizypqqqxewgla","czc","ojhzmxxceltwzg","hmwvynbzpuebokl","weuuontazzovia","ohwqtugyirw","lrtftghr","fngstcishaseslmb","athpsapnlyx","tcdnqc","fjfyvg","fneurgd","xddiwjfbshgfbbejmpe","ynscraxwlwsqhsioe","eaderhxrlwrjpp","wpnlrfxgnbfpuuiggsvo","ogqmzw","xai","fdtbvhaosybjczyfcsdx","abbcbqhcuoiaggs","qtdwhsqqjt","dqdvabloavvjhunafwhw","gcpqevfuos","hipvttjbniv","acheeyf","seqrnvez","hszzzvbvmhjg","kkwpshwuvsrbjqm","jqxo","sukagbkkrvbquzkfsj","axbrmcroycbyykkdhl","zrtshq","cgwssttvz","nbwccbisxtkccgmkmped","ivplojduvs","wmblfkhtnj","jeoodscttkmjrszzjgh","qmadddn","ssdauwepilwi","wghuntzaltedkacttafj","rxojnfrleq","qzkuejnvhncjzc","cromyllbcleqipqaitzd","yjdzifptqtcmrfyjrfj","svinvs","uftn"]
    vwa = ValidWordAbbr(dictionary)
    print vwa.isUnique("vlfdxuv")


if __name__ == '__main__':
    main()

        