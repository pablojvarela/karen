import pytest
from karen import stream
import numpy as np

TESTSTRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789!@#$%*()_-+="
TESTFILE = "htmlstring.html"
GEORAMP = np.array([
    1.0,
    1.0355357134987508,
    1.072334213931367,
    1.1104403753325403,
    1.1499006663678029,
    1.1907632069998717,
    1.2330778271686729,
    1.276896127556601,
    1.3222715425131168,
    1.3692594052154143,
    1.4179170151446192,
    1.4683037079598025,
    1.5204809278550155,
    1.5745123024875862,
    1.6304637205690438,
    1.6884034122132925,
    1.7484020321400173,
    1.8105327458347789,
    1.8748713187708703,
    1.9414962088017371,
    2.0104886618366264,
    2.08193281091614,
    2.155915778808505,
    2.23252778425168,
    2.311862251970849,
    2.394015926605462,
    2.4790889906847604,
    2.567185186795641,
    2.6584119440918483,
    2.7528805092987536,
    2.850706082373489,
    2.9520079569858604,
    3.0569096659913426,
    3.1655391320735733,
    3.2780288237400237,
    3.3945159168610965,
    3.5151424619496225,
    3.6400555573847573,
    3.7694075287915183,
    3.9033561147946885,
    4.042064659373629,
    4.185702311052556,
    4.33444422916918,
    4.488471797473249,
    4.647972845315482,
    4.813141876696587,
    4.984180307455716,
    5.161296710887579,
    5.344707072087726,
    5.534635051336182,
    5.731312256840609,
    5.934978527171575,
    6.145882223734383,
    6.364280533634075,
    6.590439783302971,
    6.8246357632731955,
    7.067154064490201,
    7.318290426577456,
    7.578351098476965,
    7.847653211905387,
    8.126525168081207,
    8.415307038194529,
    8.714350978107833,
    9.02402165779343,
    9.344696706031302,
    9.676767170909551,
    10.020637996689112,
    10.37672851761415,
    10.745472969270404,
    11.127321018114971,
    11.522738309823332,
    11.932207037122293,
    12.356226527801253,
    12.795313853618861,
    13.250004460847656,
    13.720852823225515,
    14.20843311811018,
    14.713339926661504,
    15.236188958905085,
    15.777617804561565,
    16.338286710557252,
    16.91887938616407,
    17.520103836750714,
    18.14269322716185,
    18.787406775778006,
    19.455030680346542,
    20.14637907671274,
    20.86229503162004,
    21.6036515707901,
    22.37135274353653,
    23.166334725210348,
    23.98956695882158,
    24.84205333722936,
    25.72483342734184,
    26.638983737818943,
    27.585619031823956,
    28.565893686424552,
    29.581003100301103,
    30.63218515147906,
    31.720721706862705,
    32.847940185411396,
    34.015215176864274,
    35.223970117987676,
    36.47567902838906,
    37.771868308014284,
    39.11411859852042,
    40.504066710793616,
    41.94340762096267,
    43.43389653734251,
    44.97735104082791,
    46.575653301347515,
    48.23075237308134,
    49.94466657124037,
    51.7194859333066,
    53.55737476773525,
    55.460574293226735,
    57.431405371787015,
    59.47227133890945,
    61.58566093432893,
    63.77415133692244,
    66.04041130745729,
    68.38720444301877,
    70.81739254708638,
    73.33393911936821,
    75.93991296964894,
    78.63849196005845,
    81.43296688032488,
    84.32674546073741,
    87.32335652771225,
    90.4264543070303,
    93.63982287999283,
    96.96738079793002,
    100.41318586068957,
    103.98144006493179,
    107.67649472826677,
    111.50285579548026,
    115.4651893333209,
    119.56832722054885,
    123.81727304018321,
    128.21720818113567,
    132.77349815667026,
    137.49169914739267,
    142.37756477675075,
    147.43705312730725,
    152.6763340063394,
    158.10179646962817,
    163.72005661261076,
    169.5379656383958,
    175.5626182124828,
    181.8013611143722,
    188.26180219661558,
    194.95181966223288,
    201.8795716718102,
    209.05350629199023,
    216.48237179749157,
    224.17522733921737,
    232.14145399146122,
    240.39076619168506,
    248.9332235868181,
    257.7792433005198,
    266.9396126363717,
    276.4255022324854,
    286.24847968356744,
    296.4205236470555,
    306.9540384505271,
    317.86186921818967,
    329.15731753490445,
    340.8541576668423,
    352.96665335854937,
    365.5095752269114,
    378.4982187732252,
    391.9484230353382,
    405.8765899026089,
    420.29970411723815,
    435.23535398635823,
    450.7017528301445,
    466.71776119210153,
    483.30290983860266,
    500.4774235757395,
    518.2622459125201,
    536.6790646004868,
    555.7503380809069,
    575.4993228717841,
    595.9501019280812,
    617.1276140097484,
    639.0576840933668,
    661.7670548644841,
    685.28341932906,
    709.6354545837821,
    734.8528567864274,
    760.9663773689281,
    788.0078605372929,
    816.01028210411,
    845.0077897009959,
    875.0357444200235,
    906.130763934899,
    938.3307671544942,
    971.6750204631597,
    1006.2041856042307,
    1041.960369265107,
    1078.9871744243649,
    1117.329753523535,
    1157.0348635283776,
    1198.1509229467888,
    1240.728070872889,
    1284.8182281292861,
    1330.4751605820616,
    1377.7545447057093,
    1426.714035477974,
    1477.4133366873664,
    1529.914273739121,
    1584.2808690483646,
    1640.5794201124197,
    1698.8785803574804,
    1759.249442858229,
    1821.7656270324767,
    1886.5033684165737,
    1953.5416116310541,
    2022.962106649864,
    2094.8495084906017,
    2169.2914804473235,
    2246.378800991781,
    2326.205474473491,
    2408.8688457536077,
    2494.4697189123754,
    2583.1124801749534,
    2674.9052252054994,
    2769.9598909247143,
    2868.392392011644,
    2970.3227622561676,
    3075.8753009345223,
    3185.1787243864133,
    3298.3663229785266,
    3415.576123645821,
    3536.9510582088706,
    3662.639137672486,
    3792.7936327181283,
    3927.573260610284,
    4067.142378744687,
    4211.671185074388,
    4361.3359256581325,
    4516.31910958413,
    4676.809731531247,
    4843.0035022391085,
    5015.103087168126,
    5193.318353640436,
    5377.8666267632025,
    5568.972954446355,
    5766.870381837855,
    5971.800235511273,
    6184.012417752177,
    6403.765711302138,
    6631.328094932091,
    6866.9770702298165,
    7110.999999999997])
UPPERGEORAMP = np.array([
    84.32674546073741,
    87.32335652771225,
    90.4264543070303,
    93.63982287999283,
    96.96738079793002,
    100.41318586068957,
    103.98144006493179,
    107.67649472826677,
    111.50285579548026,
    115.4651893333209,
    119.56832722054885,
    123.81727304018321,
    128.21720818113567,
    132.77349815667026,
    137.49169914739267,
    142.37756477675075,
    147.43705312730725,
    152.6763340063394,
    158.10179646962817,
    163.72005661261076,
    169.5379656383958,
    175.5626182124828,
    181.8013611143722,
    188.26180219661558,
    194.95181966223288,
    201.8795716718102,
    209.05350629199023,
    216.48237179749157,
    224.17522733921737,
    232.14145399146122,
    240.39076619168506,
    248.9332235868181,
    257.7792433005198,
    266.9396126363717,
    276.4255022324854,
    286.24847968356744,
    296.4205236470555,
    306.9540384505271,
    317.86186921818967,
    329.15731753490445,
    340.8541576668423,
    352.96665335854937,
    365.5095752269114,
    378.4982187732252,
    391.9484230353382,
    405.8765899026089,
    420.29970411723815,
    435.23535398635823,
    450.7017528301445,
    466.71776119210153,
    483.30290983860266,
    500.4774235757395,
    518.2622459125201,
    536.6790646004868,
    555.7503380809069,
    575.4993228717841,
    595.9501019280812,
    617.1276140097484,
    639.0576840933668,
    661.7670548644841,
    685.28341932906,
    709.6354545837821,
    734.8528567864274,
    760.9663773689281,
    788.0078605372929,
    816.01028210411,
    845.0077897009959,
    875.0357444200235,
    906.130763934899,
    938.3307671544942,
    971.6750204631597,
    1006.2041856042307,
    1041.960369265107,
    1078.9871744243649,
    1117.329753523535,
    1157.0348635283776,
    1198.1509229467888,
    1240.728070872889,
    1284.8182281292861,
    1330.4751605820616,
    1377.7545447057093,
    1426.714035477974,
    1477.4133366873664,
    1529.914273739121,
    1584.2808690483646,
    1640.5794201124197,
    1698.8785803574804,
    1759.249442858229,
    1821.7656270324767,
    1886.5033684165737,
    1953.5416116310541,
    2022.962106649864,
    2094.8495084906017,
    2169.2914804473235,
    2246.378800991781,
    2326.205474473491,
    2408.8688457536077,
    2494.4697189123754,
    2583.1124801749534,
    2674.9052252054994,
    2769.9598909247143,
    2868.392392011644,
    2970.3227622561676,
    3075.8753009345223,
    3185.1787243864133,
    3298.3663229785266,
    3415.576123645821,
    3536.9510582088706,
    3662.639137672486,
    3792.7936327181283,
    3927.573260610284,
    4067.142378744687,
    4211.671185074388,
    4361.3359256581325,
    4516.31910958413,
    4676.809731531247,
    4843.0035022391085,
    5015.103087168126,
    5193.318353640436,
    5377.8666267632025,
    5568.972954446355,
    5766.870381837855,
    5971.800235511273,
    6184.012417752177,
    6403.765711302138,
    6631.328094932091,
    6866.9770702298165,
    7110.999999999997])
LOWERGEORAMP = np.array([
    1.0,
    1.0355357134987508,
    1.072334213931367,
    1.1104403753325403,
    1.1499006663678029,
    1.1907632069998717,
    1.2330778271686729,
    1.276896127556601,
    1.3222715425131168,
    1.3692594052154143,
    1.4179170151446192,
    1.4683037079598025,
    1.5204809278550155,
    1.5745123024875862,
    1.6304637205690438,
    1.6884034122132925,
    1.7484020321400173,
    1.8105327458347789,
    1.8748713187708703,
    1.9414962088017371,
    2.0104886618366264,
    2.08193281091614,
    2.155915778808505,
    2.23252778425168,
    2.311862251970849,
    2.394015926605462,
    2.4790889906847604,
    2.567185186795641,
    2.6584119440918483,
    2.7528805092987536,
    2.850706082373489,
    2.9520079569858604,
    3.0569096659913426,
    3.1655391320735733,
    3.2780288237400237,
    3.3945159168610965,
    3.5151424619496225,
    3.6400555573847573,
    3.7694075287915183,
    3.9033561147946885,
    4.042064659373629,
    4.185702311052556,
    4.33444422916918,
    4.488471797473249,
    4.647972845315482,
    4.813141876696587,
    4.984180307455716,
    5.161296710887579,
    5.344707072087726,
    5.534635051336182,
    5.731312256840609,
    5.934978527171575,
    6.145882223734383,
    6.364280533634075,
    6.590439783302971,
    6.8246357632731955,
    7.067154064490201,
    7.318290426577456,
    7.578351098476965,
    7.847653211905387,
    8.126525168081207,
    8.415307038194529,
    8.714350978107833,
    9.02402165779343,
    9.344696706031302,
    9.676767170909551,
    10.020637996689112,
    10.37672851761415,
    10.745472969270404,
    11.127321018114971,
    11.522738309823332,
    11.932207037122293,
    12.356226527801253,
    12.795313853618861,
    13.250004460847656,
    13.720852823225515,
    14.20843311811018,
    14.713339926661504,
    15.236188958905085,
    15.777617804561565,
    16.338286710557252,
    16.91887938616407,
    17.520103836750714,
    18.14269322716185,
    18.787406775778006,
    19.455030680346542,
    20.14637907671274,
    20.86229503162004,
    21.6036515707901,
    22.37135274353653,
    23.166334725210348,
    23.98956695882158,
    24.84205333722936,
    25.72483342734184,
    26.638983737818943,
    27.585619031823956,
    28.565893686424552,
    29.581003100301103,
    30.63218515147906,
    31.720721706862705,
    32.847940185411396,
    34.015215176864274,
    35.223970117987676,
    36.47567902838906,
    37.771868308014284,
    39.11411859852042,
    40.504066710793616,
    41.94340762096267,
    43.43389653734251,
    44.97735104082791,
    46.575653301347515,
    48.23075237308134,
    49.94466657124037,
    51.7194859333066,
    53.55737476773525,
    55.460574293226735,
    57.431405371787015,
    59.47227133890945,
    61.58566093432893,
    63.77415133692244,
    66.04041130745729,
    68.38720444301877,
    70.81739254708638,
    73.33393911936821,
    75.93991296964894,
    78.63849196005845,
    81.43296688032488])
LINERAMP = np.array([
    1.0,
    28.992125984251967,
    56.98425196850393,
    84.9763779527559,
    112.96850393700787,
    140.96062992125982,
    168.9527559055118,
    196.94488188976376,
    224.93700787401573,
    252.9291338582677,
    280.92125984251965,
    308.9133858267716,
    336.9055118110236,
    364.89763779527556,
    392.8897637795275,
    420.8818897637795,
    448.87401574803147,
    476.86614173228344,
    504.8582677165354,
    532.8503937007873,
    560.8425196850393,
    588.8346456692913,
    616.8267716535432,
    644.8188976377952,
    672.8110236220472,
    700.8031496062991,
    728.7952755905511,
    756.7874015748031,
    784.779527559055,
    812.771653543307,
    840.763779527559,
    868.755905511811,
    896.7480314960629,
    924.7401574803149,
    952.7322834645669,
    980.7244094488188,
    1008.7165354330708,
    1036.7086614173227,
    1064.7007874015746,
    1092.6929133858266,
    1120.6850393700786,
    1148.6771653543306,
    1176.6692913385825,
    1204.6614173228345,
    1232.6535433070865,
    1260.6456692913384,
    1288.6377952755904,
    1316.6299212598424,
    1344.6220472440943,
    1372.6141732283463,
    1400.6062992125983,
    1428.5984251968503,
    1456.5905511811022,
    1484.5826771653542,
    1512.5748031496062,
    1540.5669291338581,
    1568.55905511811,
    1596.551181102362,
    1624.543307086614,
    1652.535433070866,
    1680.527559055118,
    1708.51968503937,
    1736.511811023622,
    1764.503937007874,
    1792.4960629921259,
    1820.4881889763778,
    1848.4803149606298,
    1876.4724409448818,
    1904.4645669291338,
    1932.4566929133857,
    1960.4488188976377,
    1988.4409448818897,
    2016.4330708661416,
    2044.4251968503936,
    2072.4173228346453,
    2100.4094488188975,
    2128.4015748031493,
    2156.3937007874015,
    2184.3858267716532,
    2212.3779527559054,
    2240.370078740157,
    2268.3622047244094,
    2296.354330708661,
    2324.3464566929133,
    2352.338582677165,
    2380.3307086614172,
    2408.322834645669,
    2436.314960629921,
    2464.307086614173,
    2492.299212598425,
    2520.291338582677,
    2548.283464566929,
    2576.275590551181,
    2604.267716535433,
    2632.2598425196848,
    2660.251968503937,
    2688.2440944881887,
    2716.236220472441,
    2744.2283464566926,
    2772.220472440945,
    2800.2125984251966,
    2828.2047244094488,
    2856.1968503937005,
    2884.1889763779527,
    2912.1811023622045,
    2940.1732283464567,
    2968.1653543307084,
    2996.1574803149606,
    3024.1496062992123,
    3052.1417322834645,
    3080.1338582677163,
    3108.1259842519685,
    3136.11811023622,
    3164.1102362204724,
    3192.102362204724,
    3220.0944881889764,
    3248.086614173228,
    3276.0787401574803,
    3304.070866141732,
    3332.0629921259842,
    3360.055118110236,
    3388.047244094488,
    3416.03937007874,
    3444.031496062992,
    3472.023622047244,
    3500.015748031496,
    3528.007874015748,
    3556.0,
    3583.9921259842517,
    3611.9842519685035,
    3639.9763779527557,
    3667.9685039370074,
    3695.9606299212596,
    3723.9527559055114,
    3751.9448818897636,
    3779.9370078740153,
    3807.9291338582675,
    3835.9212598425192,
    3863.9133858267714,
    3891.905511811023,
    3919.8976377952754,
    3947.889763779527,
    3975.8818897637793,
    4003.874015748031,
    4031.8661417322833,
    4059.858267716535,
    4087.850393700787,
    4115.842519685039,
    4143.834645669291,
    4171.826771653543,
    4199.818897637795,
    4227.811023622047,
    4255.803149606299,
    4283.795275590551,
    4311.787401574803,
    4339.779527559055,
    4367.7716535433065,
    4395.763779527559,
    4423.755905511811,
    4451.748031496063,
    4479.740157480314,
    4507.7322834645665,
    4535.724409448819,
    4563.716535433071,
    4591.708661417322,
    4619.700787401574,
    4647.692913385827,
    4675.685039370079,
    4703.67716535433,
    4731.669291338582,
    4759.6614173228345,
    4787.653543307087,
    4815.645669291338,
    4843.63779527559,
    4871.629921259842,
    4899.622047244095,
    4927.614173228346,
    4955.606299212598,
    4983.59842519685,
    5011.5905511811025,
    5039.582677165354,
    5067.574803149606,
    5095.566929133858,
    5123.55905511811,
    5151.551181102362,
    5179.543307086614,
    5207.535433070866,
    5235.527559055118,
    5263.5196850393695,
    5291.511811023622,
    5319.503937007874,
    5347.496062992126,
    5375.488188976377,
    5403.48031496063,
    5431.472440944882,
    5459.464566929133,
    5487.456692913385,
    5515.4488188976375,
    5543.44094488189,
    5571.433070866141,
    5599.425196850393,
    5627.417322834645,
    5655.4094488188975,
    5683.401574803149,
    5711.393700787401,
    5739.385826771653,
    5767.377952755905,
    5795.370078740157,
    5823.362204724409,
    5851.354330708661,
    5879.346456692913,
    5907.338582677165,
    5935.330708661417,
    5963.322834645669,
    5991.314960629921,
    6019.3070866141725,
    6047.299212598425,
    6075.291338582677,
    6103.283464566929,
    6131.27559055118,
    6159.267716535433,
    6187.259842519685,
    6215.251968503937,
    6243.244094488188,
    6271.23622047244,
    6299.228346456693,
    6327.220472440945,
    6355.212598425196,
    6383.204724409448,
    6411.1968503937005,
    6439.188976377953,
    6467.181102362204,
    6495.173228346456,
    6523.165354330708,
    6551.157480314961,
    6579.149606299212,
    6607.141732283464,
    6635.133858267716,
    6663.1259842519685,
    6691.11811023622,
    6719.110236220472,
    6747.102362204724,
    6775.094488188976,
    6803.086614173228,
    6831.07874015748,
    6859.070866141732,
    6887.062992125984,
    6915.0551181102355,
    6943.047244094488,
    6971.03937007874,
    6999.031496062992,
    7027.023622047243,
    7055.015748031496,
    7083.007874015748,
    7111.0])
TOPFREQ = 7111
LOWFREQ = 1
AVGFREQ = 3556.0
TOPTEN = [('e', 7111), ('t', 6578), ('i', 6146), (' ', 5912), ('a', 5888), ('r', 4413), ('"', 4318), ('l', 4273),
          ('s', 4269), ('o', 4122)]


@pytest.fixture
def stream_fixture():
    with open(TESTFILE) as testfile:
        s = testfile.read()
    return stream.Stream(s)


@pytest.mark.stream
def test_read(stream_fixture):
    stream.Stream.read(stream_fixture, TESTFILE)
    assert type(stream_fixture.data) == str, "Stream.data is not string."


@pytest.mark.stream
def test_stream(stream_fixture):
    stream.Stream.read(stream_fixture, TESTFILE)

    assert np.all(stream_fixture.georamp == GEORAMP)
    assert np.all(stream_fixture.uppergeoramp == UPPERGEORAMP)
    assert np.all(stream_fixture.lowergeoramp == LOWERGEORAMP)
    assert np.all(stream_fixture.lineramp == LINERAMP)
    assert stream_fixture.topfreq == TOPFREQ
    assert stream_fixture.lowfreq == LOWFREQ
    assert stream_fixture.avgfreq == AVGFREQ
    assert stream_fixture.topten == TOPTEN

# @pytest.mark.stream
# def test_get_frecuency(stream_fixture):
#     stream.Stream.get_frequency(stream_fixture)
#
#     for freq in stream_fixture.frequency:
#         assert freq[1] == 1, "Count not equal to 1 ocurrence in fixture"
#
#
# @pytest.mark.stream
# def test_average_frequency(stream_fixture):
#     stream.Stream.get_frequency(stream_fixture)
#     avgf = stream.Stream.average_frequency(stream_fixture)
#
#     assert avgf == 1, "Average frequency calculation error"
#
# @pytest.mark.stream
# def test_lower_frequency_ramp(stream_fixture):
#     stream.Stream.get_frequency(stream_fixture)
#     lfr = stream.Stream.lower_frequency_ramp(stream_fixture)
#
#     assert lfr == 1, "Average frequency calculation error"
