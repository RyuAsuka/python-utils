# coding:utf-8
import ROTN

tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

THIS_YEAR_TIANGAN = 3
THIS_YEAR_DIZHI = 9
THIS_YEAR = 2017


def get_lunar_year(ad_year):
    if ad_year == THIS_YEAR:
        return tiangan[THIS_YEAR_TIANGAN] + dizhi[THIS_YEAR_DIZHI]
    elif ad_year < THIS_YEAR:
        diff = THIS_YEAR - ad_year
        dz = THIS_YEAR_DIZHI
        tg = THIS_YEAR_TIANGAN
        for i in range(diff):
            dz -= 1
            if dz < 0:
                dz = 11
            tg -= 1
            if tg < 0:
                tg = 9
        return tiangan[tg] + dizhi[dz]
    elif ad_year > THIS_YEAR:
        diff = ad_year - THIS_YEAR
        dz = THIS_YEAR_DIZHI
        tg = THIS_YEAR_TIANGAN
        for i in range(diff):
            dz += 1
            if dz > 11:
                dz = 0
            tg += 1
            if tg > 9:
                tg = 0
        return tiangan[tg] + dizhi[dz]


if __name__ == '__main__':
    k = 1
    i = 0
    j = 0
    dic = {}
    while k <= 60:
        # print('%d: %s' % (k + 60, tiangan[i] + dizhi[j]))
        dic[tiangan[i] + dizhi[j]] = k + 60  # 建立天干地支表
        i += 1
        j += 1
        k += 1
        if i >= 10:
            i = 0
        if j >= 12:
            j = 0
    key1 = chr(dic['辛卯']) + chr(dic['癸巳']) + chr(dic['丙戌']) + chr(dic['辛未']) + chr(dic['庚辰']) + chr(dic['癸酉']) \
        + chr(dic['己卯']) + chr(dic['癸巳'])
    print key1
    # for i in range(1, 27):
    #    print i, ROTN.rot_n(key1, i)
    # 这里试了所有26种情况，只有i=21时是对的，感觉缺少一点提示，如果要把26个全部试一遍的话显然不可能
    key2 = ROTN.rot_n(key1, 21)  # 这个是自己写的ROT-N模块，很好实现
    print key2
    ans = ROTN.barrier_decode(key2, 2)  # 栅栏密码
    print ans
