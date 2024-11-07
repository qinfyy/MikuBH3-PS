import betterproto
from game_server.net.session import Session
from lib.proto import GetFinishGuideDataReq,GetFinishGuideDataRsp

async def handle(session: Session, msg: GetFinishGuideDataReq) -> betterproto.Message:
    return GetFinishGuideDataRsp(
        retcode=0,
        guide_id_list=[
            2007,
            5007,
            5008,
            5009,
            2002,
            5648,
            2974,
            5391,
            5392,
            5537,
            1080,
            1274,
            1275,
            1276,
            1299,
            1302,
            1500,
            1501,
            1502,
            1503,
            1504,
            1505,
            1506,
            1507,
            1508,
            1509,
            1510,
            1511,
            1512,
            1513,
            1514,
            1515,
            1516,
            1517,
            1518,
            1519,
            1520,
            1521,
            1522,
            1523,
            1524,
            1525,
            1527,
            1528,
            1529,
            1530,
            1531,
            1532,
            1533,
            1534,
            1535,
            1536,
            1537,
            1538,
            1539,
            1540,
            1541,
            1542,
            1543,
            1544,
            1545,
            1546,
            1547,
            1550,
            1624,
            1625,
            2003,
            2400,
            2401,
            2402,
            2403,
            2404,
            2405,
            2501,
            2519,
            2521,
            2539,
            2540,
            2600,
            2700,
            2701,
            2703,
            2900,
            2901,
            2902,
            2903,
            2904,
            2920,
            2960,
            2963,
            2968,
            2969,
            2985,
            2986,
            2994,
            3000,
            3001,
            3002,
            3003,
            3005,
            3006,
            3007,
            3008,
            3009,
            3010,
            3011,
            3012,
            3013,
            3014,
            3015,
            3016,
            3017,
            3020,
            3023,
            3024,
            3025,
            4112,
            5006,
            5008,
            5009,
            5010,
            5102,
            5104,
            5105,
            5108,
            5109,
            5110,
            5112,
            5114,
            5202,
            5231,
            5367,
            5368,
            5369,
            5830,
            5831,
            5832,
            5833,
            5851,
            5852,
            5853,
            5854,
            5889,
            6010,
            6015,
            6022,
            6023,
            6024,
            6025,
            6401,
            6402,
            6403,
            6501,
            6521,
            6522,
            6523,
            6551,
            6715,
            6716,
            6835,
            6838,
            6852,
            7056,
            7057,
            7058,
            7060,
            7069,
            7070,
            7100,
            7101,
            7102,
            7103,
            7200,
            7230,
            7301,
            7302,
            7303,
            7304,
            7305,
            7306,
            7307,
            7308,
            7309,
            7310,
            7311,
            7312,
            7313,
            7501,
            7502,
            7503,
            7505,
            7507,
            7508,
            7509,
            7510,
            7511,
            7512,
            7513,
            7514,
            7515,
            7516,
            7517,
            7518,
            7523,
            7528,
            7529,
            7530,
            7531,
            7533,
            7534,
            7535,
            7537,
            7539,
            7540,
            7541,
            7542,
            7543,
            7545,
            7601,
            7602,
            7603,
            7605,
            7615,
            7616,
            7617,
            7618,
            7619,
            7620,
            7621,
            7631,
            7632,
            7637,
            7638,
            7639,
            7640,
            7641,
            7642,
            7643,
            7701,
            7750,
            7751,
            7752,
            7753,
            7834,
            7835,
            7836,
            7837,
            7839,
            7851,
            7852,
            7853,
            7854,
            7855,
            7856,
            7858,
            7859,
            7860,
            7867,
            7868,
            7869,
            7884,
            7885,
            7886,
            7887,
            9101,
            9202,
            9301,
            9302,
            9311,
            9313,
            9483,
            9484,
            9485,
            9488,
            9495,
            9496,
            9497,
            9498,
            9502,
            9505,
            9508,
            9530,
            9550,
            9562,
            9563,
            9564,
            9566,
            9567,
            9576,
            9581,
            9630,
            9631,
            9632,
            9642,
            9644,
            9650,
            9651,
            9702,
            9714,
            9783,
            9784,
            9785,
            9786,
            9787,
            9788,
            9790,
            9793,
            9905,
            9906,
            9993,
            9996,
            9997,
            20041,
            20042,
            20043,
            20044,
            20045,
            20046,
            20047,
            20048,
            20049,
            20050,
            20051,
            20052,
            20053,
            20057,
            20059,
            20060,
            20062,
            20063,
            20064,
            20065,
            20066,
            20067,
            20068,
            20069,
            20070,
            20071,
            20072,
            20073,
            20074,
            20075,
            20076,
            40001,
            40005,
            40006,
            40007,
            40008,
            40009,
            40023,
            40024,
            40025,
            40026,
            40027,
            40028,
            40029,
            40030,
            40031,
            40032,
            40033,
            40034,
            40035,
            40036,
            40037,
            40038,
            40039,
            40040,
            40044,
            40045,
            40046,
            40047,
            40048,
            40055,
            40056,
            40057,
            40058,
            40059,
            40060,
            40061,
            40062,
            40063,
            40064,
            40065,
            40067,
            40068,
            40069,
            40070,
            40071,
            40072,
            40073,
            40084,
            40085,
            40086,
            40087,
            40088,
            40089,
            40115,
            40116,
            40117,
            40118,
            40119,
            40120,
            40121,
            40122,
            40123,
            40124,
            41001,
            42000,
            42001,
            42002,
            42003,
            42004,
            42005,
            42006,
            42007,
            42008,
            42009,
            42010,
            42012,
            42013,
            42014,
            42015,
            42016,
            42017,
            42020,
            42021,
            42024,
            42027,
            42028,
            42047,
            42050,
            42051,
            42052,
            42053,
            42055,
            42066,
            42067,
            42070,
            42085,
            42087,
            42090,
            42114,
            42116,
            42122,
            42124,
            42126,
            42129,
            42141,
            42142,
            42143,
            42144,
            42145,
            42146,
            42156,
            42157,
            42159,
            42161,
            42163,
            42166,
            42180,
            42181,
            42182,
            42184,
            42210,
            42213,
            42214,
            42215,
            42262,
            42263,
            42264,
            42269,
            42274,
            42275,
            42288,
            42309,
            42310,
            42311,
            42312,
            42313,
            42316,
            42318,
            42320,
            42321,
            42325,
            42328,
            42333,
            42338,
            42372,
            42382,
            42383,
            42392,
            42400,
            42403,
            42413,
            42414,
            42419,
            42433,
            42439,
            42440,
            42441,
            42452,
            42453,
            42454,
            42464,
            42465,
            42494,
            42517,
            42519,
            42521,
            42532,
            42533,
            42572,
            42573,
            42745,
            42747,
            42751,
            42775,
            44618,
            44619,
            44620,
            44621,
            44622,
            44747,
            44748,
            44751,
            44754,
            44756,
            44758,
            44761,
            44762,
            45000,
            45001,
            45002,
            45009,
            45010,
            45011,
            45023,
            45024,
            48256,
            48258,
            48272,
            48278,
            48280,
            48283,
            48289,
            48290,
            48291,
            48294,
            48319,
            48347,
            50079,
            50080,
            50081,
            50084,
            50087,
            50102,
            50103,
            50104,
            50105,
            50252,
            50253,
            50254,
            50255,
            50256,
            50262,
            50263,
            50266,
            50271,
            50272,
            50274,
            50276,
            50277,
            50281,
            50282,
            50284,
            50290,
            50291,
            50292,
            50294,
            50299,
            50304,
            50312,
            50316,
            50317,
            50318,
            50322,
            50323,
            50325,
            50332,
            50340,
            50351,
            50352,
            50353,
            50355,
            50357,
            50360,
            50361,
            50362,
            50366,
            50376,
            50377,
            50379,
            50380,
            50382,
            50383,
            50385,
            50386,
            50387,
            50388,
            50396,
            50397,
            50398,
            50399,
            50404,
            50407,
            50408,
            50409,
            50410,
            50411,
            50412,
            50416,
            50417,
            50418,
            50419,
            50422,
            50423,
            50424,
            50425,
            50432,
            50433,
            50436,
            50446,
            50447,
            50449,
            50467,
            50468,
            50469,
            50473,
            50474,
            50475,
            50476,
            50477,
            50478,
            50479,
            50480,
            50486,
            50492,
            50493,
            100002,
            100003,
            100004,
            100005,
            100006,
            100007,
            100078,
            100079,
            100080,
            100082,
            100083,
            100086,
            100087,
            100088,
            100089,
            100091,
            100095,
            100097,
            100098,
            100100,
            100101,
            100102,
            100106,
            100107,
            100108,
            100109,
            100111,
            100113,
            100115,
            100116,
            100117,
            100139,
            100140,
            100142,
            100143,
            100144,
            100145,
            100146,
            100147,
            100148,
            100149,
            100150,
            100151,
            100152,
            100153,
            100154,
            100158,
            100159,
            100160,
            100162,
            100163,
            100356,
            100357,
            100366,
            100367,
            100369,
            100372,
            100373
        ]
    )
