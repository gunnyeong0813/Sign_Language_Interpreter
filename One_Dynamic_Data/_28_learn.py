import numpy as np

learn = np.array([

[  39.98356247,  173.91767883,  -14.46600914,   -4.6010828 ,   54.37994766,
  -17.4487133 ,   -9.82699585,   51.67498398,  -22.71414375,   16.8738327 ,
   13.14539051,   53.15335083,   23.60835648,   14.27389145,   50.21660995,
   33.77619553,   18.56972313,   42.39269257],

[  46.4776268 ,  164.44857788,  -15.17357063,   -1.64679956,   54.82092667,
  -16.57590294,   -6.63330173,   54.34568024,  -16.89238739,   21.46062851,
    6.5745554 ,   52.71643829,   28.08627892,    7.38711071,   49.3902626 ,
   38.07304764,   11.50759125,   41.24105835],
[  47.54751587,  162.62132263,  -16.23373985,   -1.8511821 ,   54.59444427,
  -17.28658867,   -8.64343929,   54.76845169,  -14.44001007,   22.67004204,
    5.6393261 ,   52.31705093,   29.22978783,    6.44982767,   48.85514832,
   39.06642151,   10.61312771,   40.54605484],
[  48.73591614,  161.00822449,  -17.10959816,   -1.63735306,   54.64070129,
  -17.16156387,  -11.83846188,   54.91955566,  -11.24719715,   23.60404778,
    4.57713556,   52.00677872,   30.11182785,    5.40173912,   48.44487   ,
   39.83407974,    9.63997364,   40.03902435],
[  50.7531395 ,  160.62998962,  -16.31650925,   -0.80050862,   55.01763916,
  -15.97576809,  -12.76445961,   55.24106598,   -8.26437759,   22.82306671,
    2.461761  ,   52.49622726,   29.39618874,    3.35212278,   49.06560516,
   39.28729248,    7.79868364,   40.96944809],
[  49.92472076,  163.41207886,  -15.98623753,   -1.48620284,   54.80134201,
  -16.65565109,  -13.08115005,   55.03222656,   -9.11831379,   21.41713142,
    3.35438633,   53.03641129,   28.05922699,    4.34968567,   49.76511383,
   38.06301498,    8.92962933,   41.88406754],
[  51.42676544,  162.48628235,  -15.76531982,   -1.04092765,   55.11862946,
  -15.60959339,  -11.10951805,   55.61059952,   -8.17595863,   21.36986351,
    1.80839992,   53.13064194,   28.02819252,    2.82322264,   49.89244461,
   38.08611679,    7.50644445,   42.14151764],
[  45.39664459,  171.8117218 ,  -17.28718948,   -5.57275105,   52.92399597,
  -21.2320919 ,  -14.62837696,   53.63700867,  -13.85237789,   18.38343811,
    8.30717659,   53.62691879,   25.07893562,    9.69637394,   50.59480286,
   35.0348053 ,   14.6730442 ,   42.89604568],
[  41.008358  ,  178.74583435,  -15.97067261,   -7.22691822,   52.09147263,
  -22.73887253,  -16.13696289,   51.88206863,  -18.1839447 ,   14.45234966,
   12.43490601,   54.03063202,   21.22875977,   14.08534718,   51.32006454,
   31.37324905,   19.22634125,   43.9189415 ],
[  38.43412018,  179.34414673,  -15.42428493,   -7.13116217,   52.36558533,
  -22.1313858 ,  -16.13793182,   50.97857285,  -20.58054161,   14.10832405,
   14.8587389 ,   53.50681686,   20.89267921,   16.45500374,   50.74972916,
   31.06238174,   21.31193924,   43.17100906],
[  36.45093536,  178.73738098,  -15.12303448,   -6.48972273,   53.07803345,
  -20.57698441,  -15.84459305,   50.30801392,  -22.37987518,   14.53014469,
   16.73616219,   52.83542633,   21.31645393,   18.20142555,   49.97122574,
   31.47280121,   22.68799019,   42.16069794],
[  41.40007782,  170.35910034,  -16.8402462 ,   -3.41670775,   54.58179855,
  -17.08683014,  -15.01954651,   52.47543716,  -17.42263985,   19.79483604,
   12.11636066,   52.38477325,   26.458395  ,   13.22707844,   49.06938171,
   36.33774567,   17.3828907 ,   40.7456665 ],
[  44.12137985,  167.53387451,  -16.96620178,   -2.8927865 ,   53.90246201,
  -19.20839691,  -15.91589642,   53.19490433,  -14.13480759,   20.92229462,
    9.47188473,   52.49140167,   27.61217308,   10.47771549,   49.09777832,
   37.46921158,   14.67746544,   40.7852478 ],
[  44.64513779,  167.01100159,  -16.99197578,   -2.88953352,   53.63487244,
  -19.9438591 ,  -14.92705059,   53.40237808,  -14.42829704,   21.09898376,
    8.96797657,   52.50918579,   27.80664635,    9.95696163,   49.09638977,
   37.66155243,   14.17201614,   40.78686142],
[  44.9545517 ,  167.01786804,  -17.0659256 ,   -3.34344196,   52.90897751,
  -21.73172569,  -12.79715157,   53.52321243,  -15.94694138,   21.03310776,
    8.70324326,   52.58011246,   27.76461601,    9.70637131,   49.17030334,
   37.62850189,   13.97347641,   40.885746  ],
[  45.55518723,  167.33422852,  -17.23505592,   -3.64489174,   52.24008942,
  -23.24853325,  -11.63583183,   53.64590454,  -16.41739273,   20.75937462,
    8.18508625,   52.77176285,   27.51925278,    9.24918842,   49.39584732,
   37.39981842,   13.6517868 ,   41.203022  ],
[  46.56437683,  167.02723694,  -17.30546188,   -3.60462904,   51.6761055 ,
  -24.48250961,  -11.65544415,   53.9678688 ,  -15.31098461,   20.70170212,
    7.22218323,   52.93473434,   27.4862175 ,    8.31941414,   49.57924271,
   37.38741684,   12.83406258,   41.47619247],
[  47.45197678,  166.73062134,  -17.45504951,   -3.52136159,   51.57023621,
  -24.71673393,  -11.51834774,   54.25492477,  -14.37139988,   20.69531631,
    6.38561678,   53.0446434 ,   27.49586296,    7.5161767 ,   49.70202255,
   37.39484406,   12.13557339,   41.67924881],
[  48.34783936,  166.42295837,  -17.70725632,   -3.44956756,   51.64754105,
  -24.56498146,  -11.47559738,   54.56162643,  -13.19644642,   20.72673035,
    5.55539417,   53.12576294,   27.53807831,    6.72577143,   49.7918129 ,
   37.39981461,   11.46001244,   41.86559677],
[  49.26293564,  166.02816772,  -18.01039314,   -3.31485486,   51.68659592,
  -24.50130463,  -11.59485817,   54.88082504,  -11.68165016,   20.81109047,
    4.70914507,   53.17451096,   27.62907219,    5.91826105,   49.8439064 ,
   37.4688797 ,   10.76191044,   41.98893738],
[  49.85165787,  165.85507202,  -18.0984745 ,   -3.12779617,   51.73317719,
  -24.42747116,  -11.03043747,   55.14144135,  -10.97984505,   20.7666893 ,
    4.14830399,   53.23854446,   27.59887123,    5.38058901,   49.92152023,
   37.43152237,   10.29423904,   42.13924789],
[  50.51322937,  166.02615356,  -18.0990715 ,   -3.02038908,   51.87902451,
  -24.12986946,   -9.7367363 ,   55.42155075,  -10.79140472,   20.47714043,
    3.50445008,   53.39674377,   27.33864403,    4.79965162,   50.12353134,
   37.17108536,    9.80306911,   42.48548889],
[  50.89046478,  167.19786072,  -18.4361248 ,   -3.36315632,   52.099617  ,
  -23.60350037,   -8.86182404,   55.38721085,  -11.68467331,   19.86981964,
    3.21902633,   53.64358902,   26.76445389,    4.67147875,   50.44450378,
   36.56308746,    9.83966827,   43.00148773],
[  50.66424942,  168.68415833,  -19.2744751 ,   -3.93122435,   52.39096832,
  -22.85909653,   -9.2084074 ,   55.05033112,  -12.94112492,   19.46723938,
    3.61587524,   53.76577377,   26.36901474,    5.25148249,   50.59548569,
   36.00835419,   10.58203793,   43.29232407],
[  50.78152084,  168.72436523,  -19.55852699,   -3.66258097,   52.84403992,
  -21.83802795,  -10.01479435,   54.96660233,  -12.69578171,   19.51814651,
    3.58652902,   53.74927902,   26.43179703,    5.25622129,   50.56222534,
   35.90724182,   10.60381603,   43.37090683],
[  51.35497665,  168.07255554,  -19.71780968,   -3.31980181,   53.13557434,
  -21.17536354,  -11.03563118,   55.06070709,  -11.37275982,   19.7625351 ,
    3.06087637,   53.69245529,   26.68288612,    4.73275423,   50.481987  ,
   36.05949402,   10.09492111,   43.36602402],
[  51.25539398,  167.98162842,  -20.10301971,   -3.33501267,   53.18489075,
  -21.04878807,  -12.25565624,   54.94137573,  -10.67944431,   19.98424339,
    3.25277853,   53.59902954,   26.89783287,    4.94133663,   50.34775162,
   36.12896729,   10.31358814,   43.25660706],
[  52.34588242,  167.85862732,  -20.54542732,   -2.30066586,   54.55163574,
  -17.36756897,  -12.30100632,   55.11771393,   -9.67104149,   19.89724731,
    2.25484538,   53.68259811,   26.82761383,    4.01073742,   50.46780777,
   35.93404007,    9.51874733,   43.59982681],
[  52.26957321,  168.0448761 ,  -20.51042747,   -0.79366177,   55.92506027,
  -12.43239021,  -12.2513485 ,   55.10331726,   -9.81505585,   19.80745316,
    2.34495807,   53.71194077,   26.74664307,    4.10351658,   50.50331497,
   35.80018234,    9.60894012,   43.69006348],

[  50.66624832,  167.56349182,  -20.56673241,    1.02229571,   56.75313187,
   -7.80021715,  -13.23260689,   54.66547012,  -10.92660236,   20.55460167,
    3.99145722,   53.33275604,   27.45034027,    5.65619707,   49.97291946,
   36.34145355,   10.93650627,   42.92432785],
[  49.47533798,  166.22387695,  -20.45306396,    1.19464135,   56.28858185,
  -10.62895775,  -15.61363888,   54.14419174,  -10.36470985,   21.59322548,
    5.15488577,   52.82013321,   28.44170761,    6.66458321,   49.28954315,
   37.22082138,   11.66575623,   41.96816635],
[  50.03478241,  167.18994141,  -20.99492073,    0.67791671,   56.40121841,
  -10.06226254,  -19.05288887,   53.4316597 ,   -8.05304718,   21.11736107,
    4.72883701,   53.05187607,   27.97445869,    6.3597703 ,   49.59626389,
   36.72281647,   11.55651474,   42.43451309],
[  40.19278717,  178.2623291 ,  -19.75405693,   -3.8311305 ,   55.10478592,
  -15.2181282 ,   -2.47557998,   49.15611267,  -29.33180046,   16.2630558 ,
   14.13483143,   53.08979034,   23.16296005,   16.05073166,   49.88644791,
   31.83192635,   21.1961956 ,   42.66445923],
[  35.68740463, -179.48399353,  -18.25249863,   -4.68162537,   54.50315857,
  -17.03803253,   -2.01251841,   46.57206726,  -33.31364822,   14.69703388,
   18.16331291,   52.31536484,   21.62907028,   19.99604416,   49.14415359,
   30.36564827,   24.80410576,   41.77906418],
[  32.71183395, -178.37388611,  -17.6679554 ,   -5.36818266,   53.58056259,
  -19.57325172,   -2.12850475,   44.80411911,  -35.6492157 ,   13.96533203,
   20.8367939 ,   51.51314545,   20.8939743 ,   22.63310242,   48.31139755,
   29.62760162,   27.19761467,   40.80810547],
[  31.8874588 , -177.7928009 ,  -17.15587807,   -5.46451855,   53.08213806,
  -20.86221886,   -1.88823378,   44.30600357,  -36.27973175,   13.40764236,
   21.78059959,   51.27033234,   20.34747124,   23.66592216,   48.04904556,
   29.07704163,   28.07165718,   40.61174774],
[  32.09748459, -178.16287231,  -16.94490623,   -5.11599255,   53.01296616,
  -21.12483025,   -1.52995896,   44.36964417,  -36.21878433,   13.52295971,
   21.77741241,   51.24139023,   20.48537636,   23.63041878,   48.00790405,
   29.19847488,   27.93622589,   40.61801147],
[  32.27256393, -178.36721802,  -17.36675072,   -5.27933693,   52.34809494,
  -22.6850605 ,   -1.76088774,   44.43152237,  -36.13233566,   13.83117294,
   21.84630394,   51.12968063,   20.78895569,   23.67450333,   47.85544586,
   29.38095093,   28.04667282,   40.40977859],
[  32.70087814, -178.35424805,  -17.52142906,   -5.23627901,   51.69858551,
  -24.13801575,   -1.79740703,   44.68478775,  -35.8168335 ,   13.83372784,
   21.66874695,   51.20449066,   20.8323307 ,   23.49343491,   47.92576599,
   29.36811638,   27.96844864,   40.47327805],
[  33.30129623, -178.26678467,  -17.69213295,   -5.15533018,   51.37525177,
  -24.8357048 ,   -1.84683323,   45.05567932,  -35.34659195,   13.81236267,
   21.28354836,   51.37154388,   20.81311035,   23.14459801,   48.10351562,
   29.31099129,   27.72282219,   40.68313217],
[  33.69896698, -178.19718933,  -17.35333633,   -4.86795807,   51.46865845,
  -24.69992828,   -1.5112077 ,   45.3046875 ,  -35.04294968,   13.58878613,
   21.00404358,   51.5459137 ,   20.5856781 ,   22.85540009,   48.33908463,
   29.14293289,   27.44807625,   40.98900986],
[  33.96337128, -178.89653015,  -17.47621346,   -4.7447753 ,   51.69434738,
  -24.24846268,   -1.37281156,   45.37820816,  -34.95339966,   14.07742119,
   20.86428261,   51.47148895,   21.06287575,   22.66630173,   48.22240829,
   29.63064194,   27.19240952,   40.80936813],
[  33.78081131, -178.50241089,  -17.39296341,   -5.05081415,   51.62995911,
  -24.32371902,   -1.42811739,   45.30772781,  -35.04249954,   13.77755928,
   21.07814026,   51.46549606,   20.75847816,   22.89944458,   48.24425125,
   29.38379478,   27.46095276,   40.80802917],
[  35.65506363, -177.73519897,  -16.94796371,   -5.0349822 ,   52.73185349,
  -21.83590698,   -0.95806682,   46.51186371,  -33.44451141,   12.92760658,
   19.34316254,   52.35957718,   19.92331123,   21.28003311,   49.325737  ,
   28.69894218,   26.09389687,   42.16972351],
[  35.21315002, -177.61433411,  -16.62776184,   -5.0585289 ,   53.00657272,
  -21.15469742,   -0.79901803,   46.26437759,  -33.79016113,   12.72030735,
   19.78006744,   52.24700165,   19.71359444,   21.67002106,   49.24013519,
   28.58945084,   26.41936874,   42.04124832],
[  42.03995895,  173.67611694,  -18.28076553,   -2.18350601,   53.71363449,
  -19.82130814,   -6.97498274,   51.88577271,  -23.28138161,   18.13313866,
   13.65758228,   52.60671234,   25.04488564,   15.1920023 ,   49.24188232,
   33.91566467,   19.81393814,   41.71261597],
[  43.08706284,  174.01599121,  -19.15561485,   -3.28002858,   52.30310059,
  -23.16103935,   -6.82497263,   51.7026825 ,  -23.72885895,   18.0984726 ,
   12.80464077,   52.83268738,   24.99411011,   14.46682262,   49.48547363,
   33.88901901,   19.33097649,   41.96015167],
[  41.26266098,  177.75068665,  -18.87342644,   -4.54582834,   51.50741959,
  -24.68051147,   -5.96561384,   49.98729706,  -27.35851097,   15.99246597,
   14.48923397,   53.07645035,   22.91312408,   16.34760094,   49.90542221,
   31.91703033,   21.41049194,   42.49353409],
[  43.11166   ,  175.27891541,  -18.73107338,   -3.598387  ,   52.09039307,
  -23.58916855,  -11.95557308,   51.85921478,  -21.22480583,   17.15568542,
   12.71249104,   53.16842651,   24.07428169,   14.44884872,   49.94463348,
   33.16978455,   19.43618774,   42.48301315],
[  46.1330719 ,  171.4655304 ,  -18.47106552,   -2.19801807,   53.06906509,
  -21.48603249,  -11.91259956,   53.2848587 ,  -17.36722565,   18.73941994,
    9.71212196,   53.26645279,   25.65125084,   11.29271984,   49.97293472,
   34.83836746,   16.20273018,   42.50371933]
], "float32")
print np.shape(learn)