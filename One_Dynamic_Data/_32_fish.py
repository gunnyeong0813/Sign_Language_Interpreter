import numpy as np

fish = np.array([
[ -9.27646351, -88.47101593,   0.23602994,  -4.77201033,  30.00853539,
 -48.57491302,  -1.1534245 ,   3.50321579, -57.17694855,  -5.01984024,
  -9.21111298, -56.32728577,  -6.71505785, -16.15866089, -54.55833435,
  -4.52418852,  -8.2128315 , -56.52333832],
[ -9.33835983, -88.31145477,   0.14852826,  -4.98381519,  29.89921761,
 -48.62103271,  -1.27395868,   3.43684697, -57.17841721,  -5.10364866,
  -9.28619957, -56.30742264,  -6.77567053, -16.23841286, -54.52715683,
  -4.51591349,  -8.37041473, -56.50087738],
[ -9.45291138, -88.32082367,   0.112803  ,  -5.02908611,  29.77466393,
 -48.69275284,  -1.3054775 ,   3.32221317, -57.18448257,  -5.13700104,
  -9.39758015, -56.28590775,  -6.80879259, -16.34753227, -54.49041367,
  -4.60682821,  -8.67209244, -56.44801331],
[  4.92114258, -81.17747498,   7.87332726,   1.50590122,  21.5164032 ,
 -53.08090973,  -4.99575281,  -1.55869603, -57.05628204, -14.42253685,
 -12.70622444, -53.97544479, -14.72765923,  -8.85928631, -54.65725327,
 -10.61736488,  -2.57203341, -56.24466705],
[  5.108459  , -81.15247345,   7.8845253 ,   1.50398612,  21.70343781,
 -53.00476456,  -4.98187876,  -1.38379025, -57.0620079 , -14.43619919,
 -12.52010441, -54.01527023, -14.70706272,  -8.70139694, -54.68815613,
 -10.6585722 ,  -2.74037027, -56.22891998],
[  6.09471512, -82.18357086,   8.22416782,   2.06707001,  22.71053696,
 -52.56201172,  -4.75454044,  -0.20953482, -57.09778214, -14.5167942 ,
 -11.07723427, -54.30804825, -14.59872341,  -7.42368078, -54.90512466,
 -10.99885941,  -1.92013037, -56.19737244],
[  6.24862385, -81.6866684 ,   8.28811359,   1.97689199,  22.81739235,
 -52.51918793,  -4.6377449 ,  -0.17188311, -57.10751343, -14.67813683,
 -10.91785336, -54.29695511, -14.42140198,  -7.47667027, -54.94478226,
 -10.99468613,  -2.15698886, -56.18959808],
[  5.95264912, -81.6591568 ,   8.14689541,   1.8592838 ,  22.56186485,
 -52.63375092,  -4.77649975,  -0.46134081, -57.09447098, -14.75891018,
 -11.21734142, -54.2139473 , -14.55614567,  -7.75308371, -54.87089157,
 -10.77144241,  -2.46556592, -56.22013474],
[  5.74874926, -81.35816956,   7.99889517,   1.64943421,  22.36107063,
 -52.72635269,  -4.89182949,  -0.722619  , -57.08199692, -14.79129601,
 -11.67961121, -54.10739899, -14.63220024,  -8.05107117, -54.80771255,
 -10.82853889,  -2.75896788, -56.19552612],
[  5.83824444, -81.29434204,   7.94706106,   1.58073342,  22.44782066,
 -52.69158554,  -4.93681192,  -0.65002227, -57.07899857, -14.85859871,
 -11.87897491, -54.04552078, -14.66487694,  -7.99540758, -54.80712891,
 -10.95131493,  -2.8069241 , -56.16935349],
[  5.95466423, -81.38584137,   7.92775631,   1.58525336,  22.57146835,
 -52.6385994 ,  -4.96645689,  -0.51757985, -57.07777786, -14.89994526,
 -12.11963081, -53.98067093, -14.7020216 ,  -7.85641241, -54.817276  ,
 -10.98121929,  -2.74891973, -56.16638565],
[  6.06862831, -81.39340973,   7.98187208,   1.63321185,  22.6829319 ,
 -52.58919525,  -4.9138875 ,  -0.40663978, -57.08322906, -14.88560486,
 -12.26223087, -53.95241165, -14.64995003,  -7.75185251, -54.84609604,
 -11.01031971,  -2.79535317, -56.15839386],
[  6.12672853, -81.15633392,   7.83802986,   1.42994058,  22.7221489 ,
 -52.57818604,  -5.03108644,  -0.40152997, -57.07305527, -14.91089439,
 -13.34011841, -53.68903732, -14.73056507,  -7.78975677, -54.81912613,
 -11.00007057,  -3.33913684, -56.13069534],
[  6.16890574, -80.9446106 ,   7.73429298,   1.27168548,  22.74715614,
 -52.57143784,  -5.11096764,  -0.40646917, -57.06592178, -15.00594997,
 -14.28265953, -53.41941071, -14.77885437,  -7.8322525 , -54.80007172,
 -10.88273335,  -3.94882774, -56.11398315],
[  6.56481218, -80.58998108,   7.68567657,   1.10255265,  23.07512283,
 -52.43214417,  -5.11890841,  -0.10230491, -57.06656265, -15.09004307,
 -14.80251217, -53.2539444 , -14.73304081,  -7.61029863, -54.84366226,
 -10.80169678,  -4.12627172, -56.11687469],
[  7.06795359, -80.17615509,   7.56187677,   0.84041798,  23.49144745,
 -52.25181198,  -5.19408751,   0.2932981 , -57.05910873, -15.10702991,
 -14.77230263, -53.25751495, -14.74139214,  -7.31263113, -54.88190079,
 -10.79640865,  -4.05467892, -56.12311172],
[  7.29122877, -80.13343048,   7.56459427,   0.81867266,  23.69210243,
 -52.16148758,  -5.18670511,   0.499064  , -57.05835342, -15.23121452,
 -14.66697216, -53.25125504, -14.72399139,  -7.12777281, -54.91088486,
 -10.92489243,  -4.25002146, -56.08377838],
[  7.44955158, -80.1026535 ,   7.6439662 ,   0.87445587,  23.83457565,
 -52.09563446,  -5.10473204,   0.64401484, -57.06429291, -15.40770817,
 -14.56102562, -53.22955322, -14.6378336 ,  -6.99740076, -54.95067596,
 -11.12068748,  -4.54355001, -56.02225494],
[  7.5972023 , -80.09791565,   7.67510843,   0.89403516,  23.97085762,
 -52.0327301 ,  -5.07376051,   0.78482318, -57.06529236, -11.08094215,
  -4.63730049, -56.02244949, -15.55643749, -14.58215141, -53.18048859,
 -14.60410213,  -6.86665487, -54.97613907],
[  7.76227713, -79.98539734,   7.6699729 ,   0.84767884,  24.1107502 ,
 -51.96883392,  -5.06618977,   0.91935438, -57.0639534 , -10.95418453,
  -4.91522884, -56.02368164, -15.55455399, -14.566082  , -53.18544388,
 -14.57844257,  -6.76028728, -54.99612808],
[  8.37728691, -80.38292694,   7.59391785,   0.85675359,  24.70384598,
 -51.68938446,  -5.18879414,   1.59871888, -57.03794479, -11.07618237,
  -4.44649029, -56.03885651, -15.67376614, -13.82540798, -53.34789276,
 -14.73528767,  -6.05587006, -55.0363884 ],
[  8.8550787 , -82.0981369 ,   8.09144783,   1.7805835 ,  25.29158211,
 -51.3806572 ,  -4.89015436,   2.42742872, -57.03508377, -11.0810442 ,
  -3.49867487, -56.10504532, -15.71631813, -12.59620571, -53.63897324,
 -14.65641499,  -4.97912073, -55.16524506],
[  8.65756893, -81.24892426,   8.16450119,   1.61209273,  25.03798294,
 -51.51026154,  -4.72283745,   2.0496304 , -57.06400299, -11.12876701,
  -3.91451049, -56.06811523, -15.65512848, -12.96858788, -53.56807709,
 -14.39176846,  -5.48173904, -55.18726349],
[  8.52552414, -80.81771088,   8.06392956,   1.40452158,  24.88341522,
 -51.59117508,  -4.7738409 ,   1.82983112, -57.06723022, -11.21963215,
  -4.2390604 , -56.02639389, -15.73152256, -13.1944828 , -53.49047852,
 -14.38816071,  -5.76333523, -55.15950775],
[  8.49096012, -80.62290192,   8.04583454,   1.33447444,  24.83701897,
 -51.61538315,  -4.76986504,   1.754336  , -57.06993484, -11.33337021,
  -4.50163746, -55.98300171, -15.74851608, -13.2599802 , -53.46927643,
 -14.35960007,  -5.86818886, -55.15589523],
[  9.21110725, -84.00855255,   8.91685295,   3.06779313,  25.77248383,
 -51.08007431,  -4.27691126,   3.17960477, -57.04738998, -12.09400463,
  -2.98704672, -55.92511749, -16.17246246, -11.28944206, -53.79410934,
 -14.28883362,  -3.93337846, -55.34585953],
[  9.26310921, -85.02749634,   9.23557568,   3.65348148,  25.89687347,
 -50.97852707,  -4.06371689,   3.45213389, -57.0471344 , -12.53712273,
  -2.72475505, -55.84086609, -16.29413033, -10.81206894, -53.85542297,
 -14.20096779,  -3.49362969, -55.39795685],
[  9.02602291, -83.39726257,   9.19657707,   3.15430832,  25.55784798,
 -51.18254852,  -3.93485618,   2.86035633, -57.08889389, -12.46989441,
  -3.5568037 , -55.80911255, -16.12673759, -11.50896931, -53.76131058,
 -13.88779736,  -4.34179878, -55.41736603],

[ -8.65417957, -88.60532379,  -0.09087937,  -5.10453176,  30.35284615,
 -48.32654572,  -1.4253819 ,   4.12129498, -57.12958908,  -5.32151031,
  -8.58271217, -56.39880371,  -7.02094412, -15.5626545 , -54.69292831,
  -3.98656034,  -7.44254637, -56.67029572],
[ -8.78858566, -88.68350983,  -0.09176157,  -5.05682182,  30.24276352,
 -48.40052032,  -1.40793669,   3.98882151, -57.13941956,  -5.32153273,
  -8.70776176, -56.37963104,  -7.03059483, -15.68209743, -54.65756226,
  -4.02275467,  -7.49030733, -56.6614418 ],
[ -8.89211369, -88.74594879,  -0.09183338,  -5.01873398,  30.15714264,
 -48.4578743 ,  -1.39310431,   3.88672781, -57.14682007,  -5.32070303,
  -8.80380344, -56.36479187,  -7.03743887, -15.77393818, -54.63024902,
  -4.02570963,  -7.52514744, -56.65661621],
[ -8.98385334, -88.81533813,  -0.09144277,  -4.97510576,  30.08262634,
 -48.50866318,  -1.37639248,   3.7965591 , -57.15328598,  -5.31954622,
  -8.88761139, -56.35174561,  -7.04488325, -15.85354042, -54.60623932,
  -4.00494719,  -7.57194519, -56.65185547],
[ -8.76275444, -88.88967896,  -0.09793269,  -4.93296194,  30.27340698,
 -48.39414597,  -1.36520803,   4.01854944, -57.13837433,  -5.32525158,
  -8.66307354, -56.3861618 ,  -7.05979729, -15.63403702, -54.66756439,
  -4.0090065 ,  -7.34907293, -56.6809082 ],
[ -8.54441929, -88.866539  ,  -0.10890982,  -4.95887518,  30.4530468 ,
 -48.27864838,  -1.38026798,   4.23554277, -57.12233734,  -5.33537436,
  -8.45001507, -56.41752625,  -7.06667185, -15.42882538, -54.72494888,
  -4.04749489,  -7.17133951, -56.70093536],
[ -8.46220779, -88.85781097,  -0.1130888 ,  -4.96957397,  30.51939011,
 -48.23563766,  -1.38556433,   4.31712627, -57.11610031,  -5.33887863,
  -8.36969185, -56.4291687 ,  -7.06889009, -15.35175228, -54.74633408,
  -4.06184387,  -7.09507132, -56.70950317],
[ -8.4146328 , -88.85276031,  -0.11551851,  -4.97636366,  30.55698204,
 -48.21112823,  -1.38835335,   4.3642602 , -57.11244965,  -5.34067535,
  -8.32315636, -56.43587875,  -7.06990004, -15.30730915, -54.7586441 ,
  -4.08663511,  -7.05989552, -56.71211243],
[ -8.38017559, -88.84909821,  -0.11728355,  -4.98179674,  30.58353233,
 -48.1937294 ,  -1.39011753,   4.39833117, -57.10979462,  -5.34176064,
  -8.28940582, -56.44074631,  -7.07037687, -15.27527237, -54.76752853,
  -4.01986742,  -7.07349014, -56.71519089],
[ -8.35905743, -88.84684753,  -0.11836746,  -4.98547363,  30.59934616,
 -48.18331146,  -1.39101601,   4.41916466, -57.10816574,  -5.34227228,
  -8.26869011, -56.44373322,  -7.07048702, -15.25574684, -54.77295685,
  -3.97556329,  -7.07299709, -56.71837234],
[ -8.34322166, -88.84516144,  -0.11918131,  -4.9884882 ,  30.61086845,
 -48.17568207,  -1.3915484 ,   4.4347496 , -57.10694122,  -5.34253645,
  -8.25313282, -56.4459877 ,  -7.07042789, -15.24119186, -54.7770195 ,
  -3.97979975,  -7.06377411, -56.71922684],
[ -8.3295517 , -88.84371185,  -0.11988462,  -4.99133301,  30.62050056,
 -48.16926575,  -1.39186788,   4.44816828, -57.10589218,  -5.34264612,
  -8.23967934, -56.44794083,  -7.07023668, -15.22870922, -54.78050995,
  -4.02714777,  -7.10248137, -56.71105194],
[ -8.32108212, -88.84281158,  -0.12032069,  -4.99324226,  30.6262722 ,
 -48.16539383,  -1.39197803,   4.45645905, -57.10524368,  -5.34263992,
  -8.23132896, -56.44916153,  -7.07003069, -15.22103024, -54.78267288,
  -4.08808517,  -7.13952065, -56.70203781],
[ -8.31394196, -88.84204865,  -0.12068857,  -4.99496031,  30.63100052,
 -48.16221237,  -1.39200389,   4.46343231, -57.10469818,  -5.34257793,
  -8.22427845, -56.45019531,  -7.06978941, -15.21459675, -54.78448868,
  -4.13328028,  -7.14576769, -56.69797516],
[ -8.32713795, -88.81949615,  -0.12913331,  -5.01793623,  30.61666107,
 -48.1689415 ,  -1.4049176 ,   4.44963884, -57.10545731,  -5.3504324 ,
  -8.23925018, -56.44726944,  -7.07445621, -15.23029423, -54.77952957,
  -4.21608305,  -7.14677572, -56.69175339],
[ -8.2535677 , -88.48820496,  -0.23370059,  -5.32423592,  30.6481514 ,
 -48.11600113,  -1.58247054,   4.51527691, -57.09566116,  -5.45301008,
  -8.1967783 , -56.44363403,  -7.13210106, -15.20027924, -54.78038788,
  -4.40803766,  -7.05156326, -56.68907547],
[ -8.35808468, -88.20977783,  -0.34659147,  -5.6033082 ,  30.53378677,
 -48.15700912,  -1.75675821,   4.40434456, -57.09922791,  -5.56356812,
  -8.32500935, -56.41407013,  -7.20393562, -15.333992  , -54.73370361,
  -4.66089869,  -7.10783958, -56.66181183],
[ -8.34307003, -87.8549118 ,  -0.46890187,  -5.93955374,  30.51179504,
 -48.13064194,  -1.95729506,   4.41033506, -57.09224319,  -5.68324184,
  -8.34233379, -56.39958191,  -7.27499914, -15.36221886, -54.71638489,
  -4.82536602,  -7.12702179, -56.6456337 ],
[ -8.09097195, -87.3888855 ,  -0.70357394,  -6.43986511,  30.67649651,
 -47.96130753,  -2.2938664 ,   4.64927387, -57.06074524,  -5.91345787,
  -8.13581276, -56.40607834,  -7.43968296, -15.1761322 , -54.74616623,
  -5.08425856,  -6.91800165, -56.64889908],
[ -8.02657604, -87.23356628,  -0.79032993,  -6.61408234,  30.71351051,
 -47.91389084,  -2.41412067,   4.70911264, -57.05087662,  -5.99820614,
  -8.08619022, -56.40427017,  -7.50227213, -15.13290787, -54.74958801,
  -5.18802261,  -6.87536907, -56.64468384],
[ -8.09995174, -87.18331909,  -0.80927402,  -6.66434479,  30.64580154,
 -47.95026398,  -2.44390249,   4.63450909, -57.05572128,  -6.01621103,
  -8.16300964, -56.39128494,  -7.51307678, -15.20932388, -54.72692871,
  -5.15241766,  -7.04174137, -56.62749481],
[ -8.28134632, -87.24532318,  -0.81242055,  -6.62930822,  30.49897766,
 -48.04863358,  -2.43327808,   4.45541382, -57.07043839,  -6.01871157,
  -8.33611488, -56.36568451,  -7.52280951, -15.37591362, -54.67901993,
  -5.09903669,  -7.43034506, -56.58264923]
], "float32")
print np.shape(fish)