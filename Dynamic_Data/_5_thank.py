import numpy as np

thank = np.array([
[  1.18520534,   1.33070779,  43.93717194,  54.08809662, -12.3577528 ,
 -14.30279922,  41.54853058,  -7.96412373, -38.64063644,  34.61552429,
 -10.76039124, -44.3710022 ,  21.58222198,  -6.50507689, -52.67540359,
  34.20524216,  -9.78574467, -44.91154861, -26.63476944,  35.70628738,
 -36.03410339, -30.92258835,   5.11620808, -47.96273804, -32.85431671,
  -4.64875412, -46.70962906, -34.58971405,  -6.253263  , -45.24659729,
 -35.93998718,  -9.08182526, -43.68803024,  -4.83971691, -83.96150208,
 -36.71030426],
[  1.18520534,   1.33070779,  43.93717194,  54.08809662, -12.3577528 ,
 -14.30279922,  41.54853058,  -7.96412373, -38.64063644,  34.61552429,
 -10.76039124, -44.3710022 ,  21.58222198,  -6.50507689, -52.67540359,
  34.20524216,  -9.78574467, -44.91154861, -26.63476944,  35.70628738,
 -36.03410339, -30.92258835,   5.11620808, -47.96273804, -32.85431671,
  -4.64875412, -46.70962906, -34.58971405,  -6.253263  , -45.24659729,
 -35.93998718,  -9.08182526, -43.68803024,  -1.08124149, -87.85713196,
 -40.26202774],
[  1.18520534,   1.33070779,  43.93717194,  54.08809662, -12.3577528 ,
 -14.30279922,  41.54853058,  -7.96412373, -38.64063644,  34.61552429,
 -10.76039124, -44.3710022 ,  21.58222198,  -6.50507689, -52.67540359,
  34.20524216,  -9.78574467, -44.91154861, -26.63476944,  35.70628738,
 -36.03410339, -30.92258835,   5.11620808, -47.96273804, -32.85431671,
  -4.64875412, -46.70962906, -34.58971405,  -6.253263  , -45.24659729,
 -35.93998718,  -9.08182526, -43.68803024,  -4.83971691, -83.96150208,
 -36.71030426],
[  1.18520534,   1.33070779,  43.93717194,  54.08809662, -12.3577528 ,
 -14.30279922,  41.54853058,  -7.96412373, -38.64063644,  34.61552429,
 -10.76039124, -44.3710022 ,  21.58222198,  -6.50507689, -52.67540359,
  34.20524216,  -9.78574467, -44.91154861, -26.63476944,  35.70628738,
 -36.03410339, -30.92258835,   5.11620808, -47.96273804, -32.85431671,
  -4.64875412, -46.70962906, -34.58971405,  -6.253263  , -45.24659729,
 -35.93998718,  -9.08182526, -43.68803024,  -1.08124149, -87.85713196,
 -40.26202774],
[ -1.30860877,   0.60655308,  42.91399384,  53.81015396, -14.10076618,
 -13.72742462,  41.78144836,  -9.80453396, -37.96035004,  34.81032181,
 -12.20086575, -43.84275436,  20.69322777,  -8.89425564, -52.68291092,
  34.02191925, -11.75505447, -44.57728195, -26.15484047,  36.40227127,
 -35.68760681, -30.72194481,  10.90922928, -47.11642075, -33.6787796 ,
  -2.58146739, -46.28047562, -35.37343216,  -5.09854746, -44.78316116,
 -37.19744492,  -8.49407673, -42.74350357,  -1.08124149, -87.85713196,
 -40.26202774],
[ -1.30860877,   0.60655308,  42.91399384,  53.81015396, -14.10076618,
 -13.72742462,  41.78144836,  -9.80453396, -37.96035004,  34.81032181,
 -12.20086575, -43.84275436,  20.69322777,  -8.89425564, -52.68291092,
  34.02191925, -11.75505447, -44.57728195, -26.15484047,  36.40227127,
 -35.68760681, -30.72194481,  10.90922928, -47.11642075, -33.6787796 ,
  -2.58146739, -46.28047562, -35.37343216,  -5.09854746, -44.78316116,
 -37.19744492,  -8.49407673, -42.74350357,  -0.5763613 , -86.86445618,
 -40.36560059],
[ -1.38709199,   0.92909014,  42.21383286,  51.81715012, -15.33843136,
 -19.04001236,  41.72652054,  -8.19307804, -38.40022659,  34.88708496,
 -10.11157417, -44.31087494,  20.52806282,  -7.44320107, -52.97172928,
  34.05795288,  -9.15810871, -45.15518951, -24.49898529,  37.48526764,
 -35.74158478, -31.96412468,   9.15245628, -46.66191101, -34.62285614,
  -3.08354759, -45.54729843, -35.70616913,  -5.71701574, -44.44312668,
 -37.44321823,  -8.19210434, -42.58757401,  -0.5763613 , -86.86445618,
 -40.36560059],
[ -1.38709199,   0.92909014,  42.21383286,  51.81715012, -15.33843136,
 -19.04001236,  41.72652054,  -8.19307804, -38.40022659,  34.88708496,
 -10.11157417, -44.31087494,  20.52806282,  -7.44320107, -52.97172928,
  34.05795288,  -9.15810871, -45.15518951, -24.49898529,  37.48526764,
 -35.74158478, -31.96412468,   9.15245628, -46.66191101, -34.62285614,
  -3.08354759, -45.54729843, -35.70616913,  -5.71701574, -44.44312668,
 -37.44321823,  -8.19210434, -42.58757401,   0.57848424, -87.79592896,
 -40.00056458],
[ -1.97513402,   0.8055169 ,  41.92650604,  52.68018723, -12.03102207,
 -19.04884911,  42.16356277,  -6.47199631, -38.25119019,  35.47159576,
  -8.50240231, -44.18462753,  20.64086342,  -5.71733236, -53.14200974,
  34.34233856,  -7.80095816, -45.1946373 , -28.25811577,  29.04476929,
 -40.50539398, -32.09822464,   7.58289909, -46.85093689, -34.09341049,
  -3.42097378, -45.92104721, -35.42380524,  -5.8986578 , -44.64488983,
 -37.34414673,  -9.89794254, -42.31137085,   0.57848424, -87.79592896,
 -40.00056458],
[ -1.97513402,   0.8055169 ,  41.92650604,  52.68018723, -12.03102207,
 -19.04884911,  42.16356277,  -6.47199631, -38.25119019,  35.47159576,
  -8.50240231, -44.18462753,  20.64086342,  -5.71733236, -53.14200974,
  34.34233856,  -7.80095816, -45.1946373 , -28.25811577,  29.04476929,
 -40.50539398, -32.09822464,   7.58289909, -46.85093689, -34.09341049,
  -3.42097378, -45.92104721, -35.42380524,  -5.8986578 , -44.64488983,
 -37.34414673,  -9.89794254, -42.31137085,  -7.43046808, -86.30781555,
 -40.86426926],
[ -1.19474852,   1.01141953,  41.40276718,  52.71384811, -10.9763279 ,
 -19.58512115,  42.61577225,  -6.14013338, -37.80213165,  36.01137543,
  -8.39690399, -43.76618576,  21.02999306,  -5.28223324, -53.03436279,
  34.62371445,  -7.30354166, -45.06287766, -24.38036537,  36.55902481,
 -36.76739883, -31.25934792,   6.52981091, -47.57122421, -33.83094406,
  -2.55718136, -46.17071152, -34.98562622,  -5.66890097, -45.01861572,
 -38.09539032,  -9.38761997, -41.75428391,  -7.43046808, -86.30781555,
 -40.86426926],
[ -1.19474852,   1.01141953,  41.40276718,  52.71384811, -10.9763279 ,
 -19.58512115,  42.61577225,  -6.14013338, -37.80213165,  36.01137543,
  -8.39690399, -43.76618576,  21.02999306,  -5.28223324, -53.03436279,
  34.62371445,  -7.30354166, -45.06287766, -24.38036537,  36.55902481,
 -36.76739883, -31.25934792,   6.52981091, -47.57122421, -33.83094406,
  -2.55718136, -46.17071152, -34.98562622,  -5.66890097, -45.01861572,
 -38.09539032,  -9.38761997, -41.75428391,  -9.47553921, -83.57822418,
 -41.60057449],
[ -1.3223418 ,   0.77949297,  41.6553688 ,  52.72477341, -11.03399277,
 -19.52321434,  42.77837372,  -6.11451817, -37.62220001,  36.18259048,
  -8.65015125, -43.57524109,  21.28027153,  -5.40691042, -52.9218483 ,
  34.83090973,  -7.53258181, -44.86506653, -24.80984497,  36.38994217,
 -36.64765167, -31.97879982,   9.88773346, -46.50156403, -34.41596222,
  -5.61120987, -45.46276093, -35.73561478,  -5.5860467 , -44.43611526,
 -38.41895294,  -8.53860855, -41.63991928,  -9.47553921, -83.57822418,
 -41.60057449],
[ -1.3223418 ,   0.77949297,  41.6553688 ,  52.72477341, -11.03399277,
 -19.52321434,  42.77837372,  -6.11451817, -37.62220001,  36.18259048,
  -8.65015125, -43.57524109,  21.28027153,  -5.40691042, -52.9218483 ,
  34.83090973,  -7.53258181, -44.86506653, -24.80984497,  36.38994217,
 -36.64765167, -31.97879982,   9.88773346, -46.50156403, -34.41596222,
  -5.61120987, -45.46276093, -35.73561478,  -5.5860467 , -44.43611526,
 -38.41895294,  -8.53860855, -41.63991928,  -6.93812561, -84.86628723,
 -41.81505203],
[ -1.09397316,   0.82213885,  42.22191238,  53.01839447, -10.66299534,
 -18.92502785,  42.87282944,  -6.03734064, -37.52702332,  36.44538498,
  -8.67224693, -43.35126877,  21.90072441,  -5.44817162, -52.66386032,
  35.33214569,  -7.74963617, -44.43409729, -26.13580322,  36.4871521 ,
 -35.61480331, -30.8464489 ,  15.93059158, -45.5798111 , -35.14715576,
  -3.92155313, -45.0788765 , -36.46034241,  -5.95651674, -43.79463196,
 -38.72785187,  -8.10716915, -41.43951797,  -6.93812561, -84.86628723,
 -41.81505203],
[ -1.09397316,   0.82213885,  42.22191238,  53.01839447, -10.66299534,
 -18.92502785,  42.87282944,  -6.03734064, -37.52702332,  36.44538498,
  -8.67224693, -43.35126877,  21.90072441,  -5.44817162, -52.66386032,
  35.33214569,  -7.74963617, -44.43409729, -26.13580322,  36.4871521 ,
 -35.61480331, -30.8464489 ,  15.93059158, -45.5798111 , -35.14715576,
  -3.92155313, -45.0788765 , -36.46034241,  -5.95651674, -43.79463196,
 -38.72785187,  -8.10716915, -41.43951797,   2.66595078, -86.9420929 ,
 -42.46907043],
[ -0.79777616,   0.97161329,  42.06724548,  52.71664429, -10.78388405,
 -19.68425369,  42.70388031,  -5.90267324, -37.74047852,  36.27570724,
  -8.70891094, -43.48602676,  21.82071304,  -5.23631239, -52.71853638,
  35.16912842,  -7.55053091, -44.59740448, -24.73849106,  38.14802933,
 -34.86461639, -31.35037994,  14.58485794, -45.68634415, -35.7541275 ,
  -5.42815924, -44.44079208, -37.28316879,  -7.27752972, -42.89299774,
 -39.89223099, -11.99691772, -39.33815002,   2.66595078, -86.9420929 ,
 -42.46907043],
[ -0.79777616,   0.97161329,  42.06724548,  52.71664429, -10.78388405,
 -19.68425369,  42.70388031,  -5.90267324, -37.74047852,  36.27570724,
  -8.70891094, -43.48602676,  21.82071304,  -5.23631239, -52.71853638,
  35.16912842,  -7.55053091, -44.59740448, -24.73849106,  38.14802933,
 -34.86461639, -31.35037994,  14.58485794, -45.68634415, -35.7541275 ,
  -5.42815924, -44.44079208, -37.28316879,  -7.27752972, -42.89299774,
 -39.89223099, -11.99691772, -39.33815002,   3.17654681, -87.30782318,
 -42.42355347],
[ -0.77571374,   0.67372811,  42.35684967,  52.48020935, -11.00139999,
 -20.1891861 ,  42.63254547,  -5.97666693, -37.80941772,  36.22813034,
  -8.86707592, -43.49372482,  21.64904213,  -5.03949976, -52.80841446,
  35.10937881,  -7.49663067, -44.65353775, -26.28009605,  35.12545013,
 -36.85601044, -32.7772522 ,  11.01761913, -45.6844635 , -36.22573853,
  -4.68271923, -44.14265823, -37.42625046,  -7.95188475, -42.64797592,
 -40.51184082, -12.11906242, -38.66168213,   3.17654681, -87.30782318,
 -42.42355347],
[ -0.77571374,   0.67372811,  42.35684967,  52.48020935, -11.00139999,
 -20.1891861 ,  42.63254547,  -5.97666693, -37.80941772,  36.22813034,
  -8.86707592, -43.49372482,  21.64904213,  -5.03949976, -52.80841446,
  35.10937881,  -7.49663067, -44.65353775, -26.28009605,  35.12545013,
 -36.85601044, -32.7772522 ,  11.01761913, -45.6844635 , -36.22573853,
  -4.68271923, -44.14265823, -37.42625046,  -7.95188475, -42.64797592,
 -40.51184082, -12.11906242, -38.66168213,  -1.0733428 , -85.17984009,
 -42.65368652],
[ -1.14950049,   0.46755552,  42.51200485,  52.6579628 , -10.9670496 ,
 -19.74003983,  42.54410172,  -6.23466396, -37.86733246,  36.10692215,
  -9.09258747, -43.54792404,  21.66997337,  -5.25507355, -52.77881241,
  35.02006912,  -7.69107914, -44.69058609, -26.29799843,  35.99232101,
 -35.99686813, -33.52626419,  11.74244308, -44.95454407, -36.89484787,
  -5.93041897, -43.43278503, -38.09908295,  -8.55789948, -41.9288559 ,
 -41.05189514, -11.69162846, -38.22112274,  -1.0733428 , -85.17984009,
 -42.65368652],
[ -1.14950049,   0.46755552,  42.51200485,  52.6579628 , -10.9670496 ,
 -19.74003983,  42.54410172,  -6.23466396, -37.86733246,  36.10692215,
  -9.09258747, -43.54792404,  21.66997337,  -5.25507355, -52.77881241,
  35.02006912,  -7.69107914, -44.69058609, -26.29799843,  35.99232101,
 -35.99686813, -33.52626419,  11.74244308, -44.95454407, -36.89484787,
  -5.93041897, -43.43278503, -38.09908295,  -8.55789948, -41.9288559 ,
 -41.05189514, -11.69162846, -38.22112274,  -0.82498592, -85.42137146,
 -42.96227646],
[ -1.05101359,   0.41979778,  42.19195557,  52.90395737, -10.48981953,
 -19.33756256,  42.25490952,  -5.86529493, -38.2482338 ,  35.82666397,
  -8.77491379, -43.84355545,  21.23194695,  -4.57318926, -53.01977921,
  34.72859955,  -7.59259558, -44.93421173, -26.58845139,  36.24521255,
 -35.52668381, -34.06113815,  11.69365692, -44.56347656, -37.1410408 ,
  -6.69282341, -43.11096954, -38.45632553,  -9.00188541, -41.50762939,
 -41.38479233, -13.54577065, -37.23731232,  -0.82498592, -85.42137146,
 -42.96227646],
[ -1.05101359,   0.41979778,  42.19195557,  52.90395737, -10.48981953,
 -19.33756256,  42.25490952,  -5.86529493, -38.2482338 ,  35.82666397,
  -8.77491379, -43.84355545,  21.23194695,  -4.57318926, -53.01977921,
  34.72859955,  -7.59259558, -44.93421173, -26.58845139,  36.24521255,
 -35.52668381, -34.06113815,  11.69365692, -44.56347656, -37.1410408 ,
  -6.69282341, -43.11096954, -38.45632553,  -9.00188541, -41.50762939,
 -41.38479233, -13.54577065, -37.23731232,   0.2045693 , -85.94652557,
 -43.64443588],
[ -0.79117203,   0.53681046,  42.23551178,  53.06664658, -10.23814774,
 -19.02413559,  42.34594345,  -6.05742741, -38.11738586,  35.94457626,
  -9.05587673, -43.68964386,  21.60455513,  -5.25672197, -52.80546188,
  34.89802551,  -7.92174149, -44.74572754, -25.14392853,  37.90058136,
 -34.84444427, -35.90468216,  10.09352398, -43.49460602, -37.73264313,
  -6.21371412, -42.66666412, -38.77124786,  -7.58073902, -41.49854279,
 -41.5506897 , -11.00315666, -37.88505554,   0.2045693 , -85.94652557,
 -43.64443588],
[ -0.79117203,   0.53681046,  42.23551178,  53.06664658, -10.23814774,
 -19.02413559,  42.34594345,  -6.05742741, -38.11738586,  35.94457626,
  -9.05587673, -43.68964386,  21.60455513,  -5.25672197, -52.80546188,
  34.89802551,  -7.92174149, -44.74572754, -25.14392853,  37.90058136,
 -34.84444427, -35.90468216,  10.09352398, -43.49460602, -37.73264313,
  -6.21371412, -42.66666412, -38.77124786,  -7.58073902, -41.49854279,
 -41.5506897 , -11.00315666, -37.88505554,   1.83635914, -87.58062744,
 -43.38222504],
[ -0.57002217,   0.73025274,  42.17982864,  52.95350266, -10.36142063,
 -19.27107239,  42.36018753,  -5.9471755 , -38.11891556,  35.96952438,
  -9.13178539, -43.65329361,  21.66602325,  -5.10686827, -52.7949791 ,
  34.92155457,  -7.6699481 , -44.7712326 , -26.66462898,  36.43510437,
 -35.27445602, -36.44706726,  11.08373356, -42.79682922, -38.4396019 ,
  -6.75019789, -41.94804001, -39.33197403,  -7.33151245, -41.0128212 ,
 -42.28848648, -10.43109703, -37.22475433,   1.83635914, -87.58062744,
 -43.38222504],
[ -0.57002217,   0.73025274,  42.17982864,  52.95350266, -10.36142063,
 -19.27107239,  42.36018753,  -5.9471755 , -38.11891556,  35.96952438,
  -9.13178539, -43.65329361,  21.66602325,  -5.10686827, -52.7949791 ,
  34.92155457,  -7.6699481 , -44.7712326 , -26.66462898,  36.43510437,
 -35.27445602, -36.44706726,  11.08373356, -42.79682922, -38.4396019 ,
  -6.75019789, -41.94804001, -39.33197403,  -7.33151245, -41.0128212 ,
 -42.28848648, -10.43109703, -37.22475433,   5.28120232, -87.02104187,
 -43.17640686],
[ -0.61222821,   0.67224908,  42.42206573,  53.16229248, -10.38448906,
 -18.67456245,  42.56108093,  -5.9376421 , -37.89598083,  36.15163422,
  -9.51273918, -43.42089081,  22.11829376,  -5.5594306 , -52.56120682,
  35.16384506,  -7.8886447 , -44.5430069 , -27.07048225,  36.46590042,
 -34.9318428 , -38.12670898,   7.95024633, -42.02325439, -39.24497604,
  -7.1870532 , -41.12158203, -39.57838058,  -7.96831369, -40.65542984,
 -42.85489273, -13.0761795 , -35.7110405 ,   5.28120232, -87.02104187,
 -43.17640686],
[ -0.61222821,   0.67224908,  42.42206573,  53.16229248, -10.38448906,
 -18.67456245,  42.56108093,  -5.9376421 , -37.89598083,  36.15163422,
  -9.51273918, -43.42089081,  22.11829376,  -5.5594306 , -52.56120682,
  35.16384506,  -7.8886447 , -44.5430069 , -27.07048225,  36.46590042,
 -34.9318428 , -38.12670898,   7.95024633, -42.02325439, -39.24497604,
  -7.1870532 , -41.12158203, -39.57838058,  -7.96831369, -40.65542984,
 -42.85489273, -13.0761795 , -35.7110405 ,   4.25414848, -87.49780273,
 -43.5570755 ],
[ -0.28000352,   0.98538041,  42.14636612,  52.7787323 , -11.05090714,
 -19.3672142 ,  42.53771973,  -6.61034489, -37.81074142,  36.14416122,
  -9.46658802, -43.43719482,  22.27913284,  -5.63044071, -52.48566437,
  35.18552017,  -8.17850399, -44.47356033, -30.17098427,  31.42406464,
 -37.21620941, -39.360569  ,   3.55719876, -41.48371124, -39.80218506,
  -8.56233501, -40.31475067, -40.51001358,  -9.88470459, -39.29425049,
 -43.04893112, -13.87809181, -35.17093658,   1.85312295, -88.24150848,
 -42.76815796],
[ -0.28000352,   0.98538041,  42.14636612,  52.7787323 , -11.05090714,
 -19.3672142 ,  42.53771973,  -6.61034489, -37.81074142,  36.14416122,
  -9.46658802, -43.43719482,  22.27913284,  -5.63044071, -52.48566437,
  35.18552017,  -8.17850399, -44.47356033, -30.17098427,  31.42406464,
 -37.21620941, -39.360569  ,   3.55719876, -41.48371124, -39.80218506,
  -8.56233501, -40.31475067, -40.51001358,  -9.88470459, -39.29425049,
 -43.04893112, -13.87809181, -35.17093658,   3.16669011, -88.17681122,
 -42.03800201],
[  0.88050747,   1.40953994,  42.28952789,  52.49327087, -10.66301346,
 -20.33624268,  42.12778091,  -6.11582708, -38.34909821,  35.96837997,
  -9.51403332, -43.57252502,  22.0473156 ,  -4.88123417, -52.65829468,
  34.92918777,  -7.70597076, -44.75909042, -31.44216537,  29.7899971 ,
 -37.50670242, -40.12796021,  -0.64509177, -40.89177704, -39.69091797,
  -8.78130245, -40.37730026, -40.59866714, -10.78721714, -38.96396255,
 -43.07891846, -13.70711613, -35.20125198,   3.77198815, -88.02514648,
 -42.17368317],
[  0.88050747,   1.40953994,  42.28952789,  52.49327087, -10.66301346,
 -20.33624268,  42.12778091,  -6.11582708, -38.34909821,  35.96837997,
  -9.51403332, -43.57252502,  22.0473156 ,  -4.88123417, -52.65829468,
  34.92918777,  -7.70597076, -44.75909042, -31.44216537,  29.7899971 ,
 -37.50670242, -40.12796021,  -0.64509177, -40.89177704, -39.69091797,
  -8.78130245, -40.37730026, -40.59866714, -10.78721714, -38.96396255,
 -43.07891846, -13.70711613, -35.20125198,   4.09924841, -87.70445251,
 -42.22792816],
[  0.95593405,   1.44897282,  42.41090775,  52.30930328, -10.90396786,
 -20.67962074,  41.97451401,  -6.23516941, -38.49765015,  35.8387146 ,
  -9.52600479, -43.67663193,  21.98561668,  -4.97652531, -52.67516708,
  34.77125931,  -7.90144444, -44.84788895, -31.48672867,  29.58867073,
 -37.62848282, -39.95371246,  -0.71086085, -41.06095505, -39.49863434,
  -9.02406693, -40.51210403, -40.63260651, -11.44897461, -38.73911285,
 -42.92851639, -14.1905365 , -35.19343185,   4.09924841, -87.70445251,
 -42.22792816],
[  0.95593405,   1.44897282,  42.41090775,  52.30930328, -10.90396786,
 -20.67962074,  41.97451401,  -6.23516941, -38.49765015,  35.8387146 ,
  -9.52600479, -43.67663193,  21.98561668,  -4.97652531, -52.67516708,
  34.77125931,  -7.90144444, -44.84788895, -31.48672867,  29.58867073,
 -37.62848282, -39.95371246,  -0.71086085, -41.06095505, -39.49863434,
  -9.02406693, -40.51210403, -40.63260651, -11.44897461, -38.73911285,
 -42.92851639, -14.1905365 , -35.19343185,   4.27017736, -86.98738098,
 -42.30653381],
[  1.31136596,   1.19192111,  42.31912231,  52.49108887,  -9.8457346 ,
 -20.74978065,  41.83504868,  -5.47919559, -38.76355743,  35.64692688,
  -8.95535851, -43.95343399,  21.76037407,  -4.59394026, -52.80329895,
  34.67583847,  -7.64551067, -44.9659729 , -30.15643692,  30.98386002,
 -37.59516525, -39.76074982,  -1.50061512, -41.22666168, -39.17444229,
  -8.91307926, -40.85005188, -40.16683578, -10.39550781, -39.51411438,
 -42.58757782, -13.02361202, -36.04844284,   4.27017736, -86.98738098,
 -42.30653381],
[  1.31136596,   1.19192111,  42.31912231,  52.49108887,  -9.8457346 ,
 -20.74978065,  41.83504868,  -5.47919559, -38.76355743,  35.64692688,
  -8.95535851, -43.95343399,  21.76037407,  -4.59394026, -52.80329895,
  34.67583847,  -7.64551067, -44.9659729 , -30.15643692,  30.98386002,
 -37.59516525, -39.76074982,  -1.50061512, -41.22666168, -39.17444229,
  -8.91307926, -40.85005188, -40.16683578, -10.39550781, -39.51411438,
 -42.58757782, -13.02361202, -36.04844284,   3.53129292, -86.79627228,
 -42.25085068],
[  1.04062843,   0.78758389,  42.33942795,  52.69325256,  -9.63743496,
 -20.33094025,  41.95954514,  -5.5480752 , -38.618927  ,  35.74747086,
  -9.12904358, -43.83588791,  21.94524574,  -5.10164785, -52.68003082,
  34.6617012 ,  -7.83215857, -44.94474411, -30.66398811,  30.03772354,
 -37.95077896, -38.21219635,  -2.51268196, -42.61831665, -39.26736069,
 -10.56211376, -40.36487198, -41.76870728, -12.36389256, -37.21982956,
 -38.11336136,  -9.74208832, -41.65657043,   3.53129292, -86.79627228,
 -42.25085068],
[  1.04062843,   0.78758389,  42.33942795,  52.69325256,  -9.63743496,
 -20.33094025,  41.95954514,  -5.5480752 , -38.618927  ,  35.74747086,
  -9.12904358, -43.83588791,  21.94524574,  -5.10164785, -52.68003082,
  34.6617012 ,  -7.83215857, -44.94474411, -30.66398811,  30.03772354,
 -37.95077896, -38.21219635,  -2.51268196, -42.61831665, -39.26736069,
 -10.56211376, -40.36487198, -41.76870728, -12.36389256, -37.21982956,
 -38.11336136,  -9.74208832, -41.65657043,   2.03290224, -85.19629669,
 -42.62275314],
[  0.77828693,   1.24720573,  42.18712997,  52.22776031, -11.15131664,
 -20.75369453,  42.05701447,  -5.814394  , -38.47345734,  35.89685059,
  -9.24816895, -43.68860245,  21.84296417,  -4.57778215, -52.77059174,
  34.94243622,  -7.40668392, -44.79925919, -30.47273636,  30.69152641,
 -37.57989883, -37.5279541 ,  -3.23008871, -43.17436218, -37.73791885,
 -10.1749115 , -41.89423752, -38.61844254, -10.19571018, -41.07882309,
 -41.19514465, -12.97717476, -37.64783096,   2.03290224, -85.19629669,
 -42.62275314],
[  0.77828693,   1.24720573,  42.18712997,  52.22776031, -11.15131664,
 -20.75369453,  42.05701447,  -5.814394  , -38.47345734,  35.89685059,
  -9.24816895, -43.68860245,  21.84296417,  -4.57778215, -52.77059174,
  34.94243622,  -7.40668392, -44.79925919, -30.47273636,  30.69152641,
 -37.57989883, -37.5279541 ,  -3.23008871, -43.17436218, -37.73791885,
 -10.1749115 , -41.89423752, -38.61844254, -10.19571018, -41.07882309,
 -41.19514465, -12.97717476, -37.64783096,   0.15374686, -85.35588837,
 -42.40276337],
[  0.83969289,   0.9671123 ,  42.17737961,  52.13420486, -10.75347233,
 -21.1941967 ,  42.05514526,  -5.76669264, -38.48267746,  35.85877609,
  -9.11888218, -43.74700546,  21.72916794,  -4.4205966 , -52.83093643,
  34.89957428,  -7.20782185, -44.8650589 , -30.8197403 ,  30.71861839,
 -37.27353287, -38.4886322 ,  -2.76820493, -42.35290909, -38.13661575,
 -13.17039394, -40.68102264, -41.61738586, -13.74720955, -36.90275955,
 -38.95747757, -10.85694218, -40.58630753,   0.15374686, -85.35588837,
 -42.40276337],
[  0.83969289,   0.9671123 ,  42.17737961,  52.13420486, -10.75347233,
 -21.1941967 ,  42.05514526,  -5.76669264, -38.48267746,  35.85877609,
  -9.11888218, -43.74700546,  21.72916794,  -4.4205966 , -52.83093643,
  34.89957428,  -7.20782185, -44.8650589 , -30.8197403 ,  30.71861839,
 -37.27353287, -38.4886322 ,  -2.76820493, -42.35290909, -38.13661575,
 -13.17039394, -40.68102264, -41.61738586, -13.74720955, -36.90275955,
 -38.95747757, -10.85694218, -40.58630753,   1.345734  , -85.28232574,
 -42.38440704],
[  0.61319649,   1.05298781,  42.18323898,  51.87882233, -11.52187443,
 -21.41589355,  42.12926102,  -5.9582305 , -38.37227249,  35.91017532,
  -9.11667156, -43.70528793,  22.1011734 ,  -4.53876925, -52.6663475 ,
  34.9644165 ,  -7.40940714, -44.78165436, -31.27771378,  30.4851532 ,
 -37.08324051, -39.11778641,  -3.28361583, -41.7351532 , -38.20972443,
 -13.56443596, -40.48246002, -41.4071579 , -14.89465332, -36.69336319,
 -38.94348526, -11.41623688, -40.44602585,   1.345734  , -85.28232574,
 -42.38440704],
[  0.61319649,   1.05298781,  42.18323898,  51.87882233, -11.52187443,
 -21.41589355,  42.12926102,  -5.9582305 , -38.37227249,  35.91017532,
  -9.11667156, -43.70528793,  22.1011734 ,  -4.53876925, -52.6663475 ,
  34.9644165 ,  -7.40940714, -44.78165436, -31.27771378,  30.4851532 ,
 -37.08324051, -39.11778641,  -3.28361583, -41.7351532 , -38.20972443,
 -13.56443596, -40.48246002, -41.4071579 , -14.89465332, -36.69336319,
 -38.94348526, -11.41623688, -40.44602585,   1.49022317, -86.2808609 ,
 -42.10774612],
[  1.32467997,   0.70023608,  42.0213356 ,  51.53982544, -10.53285599,
 -22.70488548,  42.14053726,  -5.53464937, -38.42329025,  35.88164139,
  -8.81848621, -43.78982162,  22.17164993,  -4.73351908, -52.61956024,
  35.01985931,  -7.24352837, -44.7654686 , -31.96858215,  29.23834991,
 -37.49580383, -38.88460541,  -2.16191292, -42.02523041, -38.81673813,
 -10.88328457, -40.71389771, -41.32777786, -13.65826416, -37.25953674,
 -37.94265366, -11.33285618, -41.40926743,   1.49022317, -86.2808609 ,
 -42.10774612],
[  1.32467997,   0.70023608,  42.0213356 ,  51.53982544, -10.53285599,
 -22.70488548,  42.14053726,  -5.53464937, -38.42329025,  35.88164139,
  -8.81848621, -43.78982162,  22.17164993,  -4.73351908, -52.61956024,
  35.01985931,  -7.24352837, -44.7654686 , -31.96858215,  29.23834991,
 -37.49580383, -38.88460541,  -2.16191292, -42.02523041, -38.81673813,
 -10.88328457, -40.71389771, -41.32777786, -13.65826416, -37.25953674,
 -37.94265366, -11.33285618, -41.40926743,   2.87084007, -86.46072388,
 -41.30058289],
[  1.26608658,   0.75439435,  42.05604553,  51.02779388, -11.71398926,
 -23.2755909 ,  42.18305206,  -5.88133812, -38.32501221,  35.87612152,
  -9.12548351, -43.73140335,  22.04722023,  -5.09928656, -52.63766479,
  34.9958992 ,  -7.62334347, -44.72111511, -31.07979012,  31.08901978,
 -36.74678421, -38.92102814,  -2.19587946, -41.98973846, -37.89648819,
 -12.40681744, -41.14284134, -38.8990593 , -11.52364635, -40.4583168 ,
 -41.49803543, -15.46768093, -36.35203171,   2.87084007, -86.46072388,
 -41.30058289],
[  1.26608658,   0.75439435,  42.05604553,  51.02779388, -11.71398926,
 -23.2755909 ,  42.18305206,  -5.88133812, -38.32501221,  35.87612152,
  -9.12548351, -43.73140335,  22.04722023,  -5.09928656, -52.63766479,
  34.9958992 ,  -7.62334347, -44.72111511, -31.07979012,  31.08901978,
 -36.74678421, -38.92102814,  -2.19587946, -41.98973846, -37.89648819,
 -12.40681744, -41.14284134, -38.8990593 , -11.52364635, -40.4583168 ,
 -41.49803543, -15.46768093, -36.35203171,   2.94058013, -86.50014496,
 -41.57471848]
], "float32")
print np.shape(thank)
#a = np.ones((50,1), dtype=np.int)*3

#target_data = np.array([[0], [1], [2]], "float32")

#print np.reshape(np.append(training_data10,two),(53,18))