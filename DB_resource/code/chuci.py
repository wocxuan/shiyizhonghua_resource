# -*- coding: utf-8 -*-

"""
Author:by 王林清 on 2021/11/15 15:03
FileName:chuci.py in shiyizhonghua_resource
Tools:PyCharm python3.8.4
"""

from util import *

if __name__ == '__main__':
    authors = {
        '屈原': {
            'name': "屈原",
            'time': "战国",
            'desc': "屈原（约公元前340—公元前278年），芈姓，屈氏，名平，字原，又自云名"
                    "正则，字灵均，出生于楚国丹阳秭归（今湖北宜昌），战国时期楚国诗人、"
                    "政治家。楚武王熊通之子屈瑕的后代。少年时受过良好的教育，博闻强识，"
                    "志向远大。早年受楚怀王信任，任左徒、三闾大夫，兼管内政外交大事。 "
                    "提倡“美政”，主张对内举贤任能，修明法度，对外力主联齐抗秦。因遭贵族"
                    "排挤诽谤，被先后流放至汉北和沅湘流域。楚国郢都被秦军攻破后，自沉于"
                    "汨罗江，以身殉楚国。"
        },
        '宋玉': {
            'name': "宋玉",
            'time': "战国",
            'desc': "宋玉（公元前298年—公元前222年)，楚国诗人，宋国公族后裔，生于楚国，"
                    "曾事楚顷襄王，为楚国士大夫。战国著名辞赋家，宋玉与唐勒，景差齐名，"
                    "传世作品有《九辩》等。所谓“下里巴人”、“阳春白雪”、“曲高和寡”便说的"
                    "是他，典故皆他而来。始皇帝二十五年己卯，公元前222年因病去世享年七十六岁。"
        },
        '景差': {
            'name': "景差",
            'time': "战国",
            'desc': "景差[cuō]（前290年—前223年），芈姓，景氏，名差，战国时期楚国辞赋家。"
                    "后于屈原，与宋玉、唐勒同时以赋见称，主要作品有楚辞《大招》"
        },
        '贾谊': {
            'name': "贾谊",
            'time': "汉",
            'desc': "贾谊（公元前200年～公元前168年），汉族，洛阳（今河南省洛阳市）人，"
                    "西汉初年著名政论家、文学家，世称贾生。贾谊少有才名，十八岁时，以善文"
                    "为郡人所称。文帝时任博士，迁太中大夫，受大臣周勃、灌婴排挤，谪为长沙王"
                    "太傅，故后世亦称贾长沙、贾太傅。三年后被召回长安，为梁怀王太傅。梁怀王"
                    "坠马而死，贾谊深自歉疚，抑郁而亡，时仅三十三岁。司马迁对屈原、贾谊都寄"
                    "予同情，为二人写了一篇合传，后世因而往往把贾谊与屈原并称为“屈贾”。"
        },
        '淮南小山': {
            'name': "淮南小山",
            'time': "汉",
            'desc': "淮南小山是西汉淮南王刘安的一部分门客的共称。今仅存辞赋《招隐士》1篇。"
                    "《汉书·艺文志》著录“淮南王群臣赋四十四篇”，《招隐士》当是其中仅存的"
                    "1篇。此篇始见于东汉王逸的《楚辞章句》,题为淮南小山作，然而萧统《文选》"
                    "则题刘安作。关于文章写作的背景，说法也不一。王逸说是小山之徒“闵伤屈原"
                    "”之作，王夫之《楚辞通释》说是淮南小山“为淮南王召致山谷潜伏之士”而作，"
                    "而不少研究者则以为是淮南小山思念淮南王的作品。"
        },
        '东方朔': {
            'name': "东方朔",
            'time': "汉",
            'desc': "东方朔（约前161年—前93年？），字曼倩，平原郡厌次县人，西汉时期著名"
                    "文学家。汉武帝即位，征辟四方士人。东方朔上书自荐，拜为郎。后任常侍郎"
                    "中、太中大夫等职。性格诙谐，言词敏捷，滑稽多智，常在汉武帝面前谈笑取"
                    "乐，曾言政治得失，上陈“农战强国”之计。汉武帝始终视为俳优之言，不以采"
                    "用。东方朔一生著述甚丰，有《答客难》、《非有先生论》等名篇。亦有后人"
                    "假托其名作文。明朝张溥汇为《东方太中集》。"
        },
        '庄忌': {
            'name': "庄忌",
            'time': "汉",
            'desc': "庄忌(约前188-前105）西汉辞赋家。会稽吴（今苏州吴县）人。因避汉明帝"
                    "刘庄讳改名严忌，与邹阳、枚乘等唱和，是梁孝王门下著名辞赋家。作品仅存"
                    "《哀时命》一篇。 此赋感叹屈原生不逢时，空怀壮志而不得伸。是咏屈赋中的"
                    "佳品。此赋纯属骚体，保持了由贾谊开创的西汉早期骚赋所具有的特点。感情真"
                    "挚，篇幅短小精悍，是咏屈赋中的佳品。"
        },
        '王褒': {
            'name': "王褒",
            'time': "汉",
            'desc': "王褒（前90年—前51年），字子渊，别号桐柏真人，蜀郡资中（今四川省资阳市"
                    "雁江区昆仑乡墨池坝村）人。西汉时期辞赋家，与扬雄并称“渊云”。汉宣帝时"
                    "期，授谏议大夫，才华横溢。甘露三年去世，年四十。王褒一生留下《洞箫赋》"
                    "等辞赋16篇、《桐柏真人王君外传》 1卷，辑有《王谏议集》11篇"
        },
        '刘向': {
            'name': "刘向",
            'time': "汉",
            'desc': "刘向（公元前77年～公元前6年），原名刘更生，字子政，沛郡丰邑（今江苏"
                    "省徐州市）人。汉朝宗室大臣、文学家，楚元王刘交（汉高祖刘邦异母弟）之"
                    "玄孙，阳城侯刘德之子，经学家刘歆之父，中国目录学鼻祖。以门荫入仕，起"
                    "家辇郎。汉宣帝时，授谏大夫、给事中。汉元帝即位，授宗正卿。反对宦官弘恭"
                    "、石显，坐罪下狱，免为庶人。汉成帝即位后，出任光禄大夫，改名为“向”，"
                    "官至中垒校尉，世称刘中垒。建平元年，去世，时年七十二岁。曾奉命领校秘"
                    "书，所撰《别录》，是我国最早的图书公类目录。今存《新序》《说苑》"
                    "《列女传》《战国策》《五经通义》。编订《楚辞》，联合儿子刘歆共同编订"
                    "《山海经》。散文主要是奏疏和校雠古书的“叙录”，较有名的有《谏营昌陵疏》"
                    "和《战国策·叙录》，叙事简约，理论畅达、舒缓平易为主要特色，作品收录于《刘子政集》。"
        },
        '王逸': {
            'name': "王逸",
            'time': "汉",
            'desc': "王逸，字叔师，生卒年不详，南郡宜城（今湖北省襄阳市宜城县）人，东汉著名"
                    "文学家。官至豫州刺史、豫章太守。所作《楚辞章句》，是《楚辞》中最早的完"
                    "整注本，颇为后世楚辞学者所重。又作有赋、诔、书、论等21篇，及《汉诗》1"
                    "23篇，今多散佚，仅存《九思》，为哀悼屈原而作。明人辑有《王叔师集》。 "
        }
    }

    datas = []

    data = get_json(r'./../data/chuci/chuci.json')
    for dic in data:
        time = get_time_str()
        datas.append({
            'title': f"{dic['section']}·{dic['title']}",
            'author': authors[dic['author']],
            'type': '楚辞',
            'content': dic['content'],
            'create_time': time,
            'update_time': time,
            'valid_delete': True
        })

    save_split_json('chuci', datas)
