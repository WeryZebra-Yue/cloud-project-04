from regex import regex as re
string = """1039560
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089]
w006jwn
Mon 28 Oct 2024 05:18:06 PM EDT
________________________________________
777660
[1, 577, 6, 2, 5, 4, 7, 46, 407, 746, 1027, 927, 658, 212, 953, 124, 403, 800, 604, 249, 561, 921, 96, 24, 268, 104, 452, 379, 950, 54, 117, 714, 565, 332, 548, 321, 1012, 931, 41, 271, 39, 114, 230, 38, 300, 961, 962, 749, 713, 520, 314, 52, 53, 804, 751, 750, 918, 1023, 60, 59, 477, 63, 353, 831, 147, 66, 239, 830, 584, 165, 1085, 743, 1061, 74, 887, 491, 972, 289, 801, 709, 384, 708, 872, 187, 578, 328, 241, 568, 475, 973, 910, 424, 93, 1045, 900, 155, 153, 108, 838, 101, 103, 573, 999, 611, 1051, 1056, 617, 3, 823, 702, 213, 772, 526, 126, 924, 62, 418, 747, 635, 120, 620, 208, 32, 730, 428, 37, 127, 585, 760, 8, 25, 133, 134, 132, 675, 311, 309, 138, 140, 139, 142, 665, 141, 144, 191, 753, 65, 394, 727, 817, 559, 23, 154, 327, 152, 592, 628, 755, 164, 312, 161, 162, 163, 399, 198, 166, 196, 432, 157, 170, 888, 172, 149, 247, 523, 1069, 726, 794, 1084, 216, 440, 932, 382, 185, 735, 734, 722, 686, 414, 471, 146, 600, 391, 563, 402, 544, 865, 200, 197, 159, 481, 955, 99, 725, 206, 1087, 630, 94, 210, 775, 316, 654, 741, 980, 355, 320, 942, 821, 219, 220, 222, 221, 223, 224, 217, 574, 1055, 248, 284, 78, 624, 894, 841, 1029, 849, 238, 236, 237, 293, 240, 1036, 1014, 605, 866, 1025, 908, 245, 228, 784, 969, 252, 443, 956, 254, 255, 256, 781, 260, 121, 258, 826, 1028, 266, 762, 1002, 622, 192, 145, 374, 786, 959, 1011, 644, 514, 278, 369, 1067, 396, 81, 1043, 819, 1033, 283, 177, 180, 971, 50, 215, 290, 135, 991, 299, 67, 631, 994, 462, 779, 790, 45, 292, 503, 740, 302, 906, 304, 307, 306, 136, 160, 137, 313, 70, 199, 51, 625, 209, 242, 323, 20, 360, 43, 593, 365, 1048, 33, 335, 151, 86, 329, 80, 465, 333, 34, 791, 375, 337, 336, 814, 861, 411, 682, 612, 272, 71, 319, 347, 348, 346, 349, 606, 857, 352, 444, 115, 44, 715, 1080, 1004, 361, 507, 982, 764, 441, 388, 480, 184, 582, 993, 276, 510, 269, 839, 818, 203, 545, 378, 989, 376, 778, 879, 84, 538, 706, 408, 420, 57, 765, 766, 285, 69, 835, 985, 417, 919, 549, 886, 1034, 398, 310, 158, 225, 188, 244, 903, 757, 684, 362, 339, 409, 1013, 981, 334, 589, 88, 1052, 856, 427, 1024, 909, 1063, 358, 422, 871, 226, 833, 946, 970, 123, 557, 364, 1047, 303, 97, 433, 647, 648, 435, 214, 468, 657, 442, 363, 1008, 723, 688, 111, 527, 807, 776, 449, 28, 878, 529, 564, 770, 181, 395, 540, 459, 868, 182, 636, 1060, 129, 331, 583, 1017, 470, 439, 469, 926, 472, 567, 401, 473, 476, 1046, 704, 478, 156, 533, 1044, 732, 607, 608, 486, 263, 489, 488, 22, 820, 295, 497, 595, 493, 761, 495, 498, 902, 506, 1037, 662, 663, 48, 55, 998, 291, 389, 509, 869, 873, 536, 846, 645, 392, 516, 167, 519, 748, 125, 676, 446, 525, 524, 844, 851, 809, 448, 453, 763, 768, 410, 733, 534, 11, 522, 836, 381, 541, 458, 938, 356, 930, 1019, 642, 1076, 1077, 783, 456, 550, 122, 673, 496, 554, 555, 679, 569, 627, 434, 855, 742, 562, 782, 829, 287, 492, 598, 190, 87, 883, 774, 262, 102, 905, 1003, 825, 98, 73, 9, 597, 736, 1071, 1022, 547, 960, 1070, 447, 543, 413, 590, 591, 767, 318, 393, 1074, 596, 18, 898, 599, 267, 173, 438, 16, 795, 535, 350, 340, 694, 426, 257, 451, 264, 843, 615, 288, 1001, 106, 616, 1057, 621, 259, 265, 864, 231, 626, 901, 189, 966, 515, 116, 174, 634, 632, 633, 119, 638, 680, 893, 341, 537, 500, 920, 148, 343, 183, 436, 646, 437, 716, 113, 668, 179, 667, 47, 799, 656, 243, 12, 940, 660, 501, 301, 891, 664, 143, 56, 10, 798, 670, 671, 669, 944, 1032, 1030, 36, 1073, 521, 677, 118, 681, 639, 296, 721, 579, 797, 89, 703, 246, 109, 690, 490, 701, 695, 484, 485, 697, 881, 698, 512, 518, 692, 1041, 687, 531, 707, 837, 705, 421, 1062, 357, 712, 710, 842, 1066, 176, 957, 719, 720, 870, 1006, 683, 274, 923, 724, 280, 397, 601, 95, 211, 504, 641, 201, 852, 913, 581, 912, 979, 419, 897, 305, 430, 560, 711, 385, 1086, 917, 558, 377, 1082, 386, 666, 987, 566, 925, 862, 756, 739, 758, 367, 130, 1042, 193, 586, 279, 699, 387, 530, 479, 412, 769, 494, 1054, 281, 1089, 728, 425, 777, 27, 297, 788, 15, 368, 35, 19, 780, 1031, 787, 270, 553, 685, 227, 351, 344, 345, 915, 793, 653, 652, 178, 79, 17, 935, 802, 30, 806, 805, 450, 609, 587, 812, 811, 810, 729, 467, 859, 354, 899, 204, 771, 232, 218, 745, 689, 824, 575, 64, 277, 505, 317, 1059, 253, 261, 808, 853, 992, 759, 508, 860, 815, 934, 571, 594, 1009, 175, 845, 168, 847, 813, 233, 42, 650, 483, 26, 21, 205, 315, 792, 827, 372, 371, 423, 556, 325, 623, 308, 580, 460, 867, 693, 1007, 330, 431, 294, 1058, 875, 1026, 576, 952, 610, 880, 696, 110, 324, 1018, 951, 75, 858, 171, 643, 539, 939, 390, 637, 499, 895, 342, 405, 941, 415, 988, 848, 947, 404, 655, 92, 513, 737, 672, 738, 91, 640, 366, 186, 914, 298, 904, 1005, 828, 58, 49, 691, 922, 511, 752, 963, 429, 659, 461, 929, 588, 1010, 13, 933, 840, 803, 949, 937, 890, 661, 457, 195, 754, 202, 207, 1072, 528, 76, 885, 984, 936, 29, 834, 380, 1021, 370, 1088, 282, 958, 1053, 83, 464, 128, 169, 400, 965, 990, 967, 789, 250, 603, 31, 613, 974, 90, 976, 1078, 977, 1068, 907, 602, 943, 359, 85, 948, 674, 1015, 61, 150, 700, 964, 383, 487, 194, 131, 996, 997, 105, 863, 100, 1000, 618, 896, 877, 82, 916, 717, 718, 251, 614, 77, 928, 1064, 986, 454, 455, 1016, 338, 884, 517, 1020, 954, 326, 629, 731, 445, 678, 273, 235, 572, 570, 785, 416, 649, 542, 1038, 474, 502, 229, 882, 1040, 1049, 968, 373, 482, 551, 816, 14, 466, 1039, 275, 995, 552, 40, 773, 532, 619, 107, 546, 1075, 945, 744, 1081, 72, 850, 1065, 286, 1050, 1079, 1035, 322, 911, 892, 876, 112, 874, 463, 68, 978, 975, 983, 406, 889, 1083, 822, 796, 651, 854, 832, 234]
w006jwn
Wed Oct 30 13:10:24 EDT 2024
________________________________________
48541
[33, 583, 773, 363, 643, 55, 724, 731, 466, 79, 50, 382, 375, 147, 613, 603, 114, 1065, 1048, 850, 67, 1076, 392, 289, 935, 998, 496, 1082, 843, 999, 1058, 652, 344, 796, 1085, 410, 338, 478, 385, 531, 604, 884, 605, 684, 711, 745, 962, 932, 422, 872, 85, 84, 644, 72, 212, 243, 656, 13, 1047, 129, 357, 343, 11, 514, 535, 395, 814, 960, 292, 722, 797, 299, 763, 274, 323, 19, 179, 467, 440, 651, 904, 580, 101, 800, 716, 176, 34, 132, 675, 42, 1017, 1010, 771, 230, 388, 333, 282, 799, 7, 555, 585, 579, 705, 1062, 916, 670, 768, 590, 798, 891, 549, 915, 1005, 1070, 71, 461, 398, 928, 706, 866, 156, 480, 929, 45, 503, 991, 285, 721, 331, 361, 709, 1004, 180, 272, 517, 206, 501, 389, 593, 464, 624, 982, 538, 413, 658, 404, 650, 543, 678, 231, 1073, 383, 1026, 216, 365, 507, 851, 1037, 1011, 359, 301, 80, 291, 1019, 113, 526, 167, 407, 1080, 588, 20, 307, 320, 837, 934, 903, 197, 683, 82, 534, 655, 860, 374, 854, 203, 162, 875, 844, 743, 175, 662, 138, 139, 140, 784, 815, 1084, 99, 280, 696, 958, 456, 40, 127, 596, 319, 725, 561, 372, 818, 1043, 746, 790, 199, 336, 47, 165, 137, 698, 164, 494, 136, 399, 309, 311, 160, 865, 1030, 597, 284, 350, 394, 66, 35, 244, 117, 403, 548, 44, 88, 802, 500, 418, 332, 641, 759, 1088, 943, 894, 836, 460, 572, 528, 687, 803, 931, 614, 240, 1009, 1064, 918, 545, 441, 245, 730, 657, 347, 842, 491, 565, 869, 65, 927, 1041, 355, 349, 1012, 126, 484, 510, 457, 215, 233, 736, 427, 640, 981, 273, 288, 537, 606, 77, 714, 645, 693, 202, 695, 809, 294, 955, 1071, 186, 717, 734, 867, 366, 582, 185, 914, 148, 337, 883, 18, 801, 69, 832, 48, 482, 570, 53, 17, 671, 666, 1023, 78, 972, 182, 508, 1034, 783, 51, 554, 159, 178, 198, 308, 310, 431, 313, 676, 163, 166, 312, 306, 200, 161, 70, 939, 10, 1054, 1086, 880, 269, 668, 760, 524, 521, 839, 345, 667, 348, 346, 21, 205, 278, 858, 560, 792, 222, 1087, 840, 993, 396, 193, 277, 133, 351, 369, 827, 75, 933, 1050, 742, 486, 910, 106, 1057, 911, 192, 912, 530, 268, 808, 257, 340, 777, 913, 936, 994, 29, 951, 367, 184, 379, 735, 623, 28, 228, 581, 984, 946, 607, 1027, 767, 261, 674, 135, 754, 807, 43, 115, 36, 703, 557, 409, 455, 448, 450, 532, 449, 248, 949, 864, 426, 610, 609, 447, 104, 878, 592, 145, 853, 15, 220, 616, 881, 1001, 527, 996, 256, 146, 753, 391, 1067, 855, 887, 562, 275, 419, 762, 973, 600, 738, 1083, 782, 265, 255, 907, 612, 978, 819, 221, 618, 171, 611, 1074, 639, 975, 281, 638, 1049, 1042, 462, 495, 90, 296, 595, 761, 789, 553, 876, 1079, 902, 1014, 952, 769, 266, 242, 519, 879, 748, 704, 697, 727, 479, 334, 318, 487, 425, 453, 258, 529, 121, 499, 218, 599, 619, 1006, 1018, 286, 378, 568, 776, 594, 659, 1022, 505, 37, 751, 863, 985, 506, 62, 713, 969, 290, 110, 181, 940, 125, 919, 393, 707, 646, 1028, 586, 541, 211, 376, 490, 834, 689, 22, 322, 1035, 105, 620, 895, 234, 260, 64, 93, 550, 663, 587, 451, 953, 264, 833, 941, 1055, 452, 781, 412, 885, 786, 1021, 992, 219, 368, 845, 820, 253, 232, 841, 26, 576, 1089, 956, 262, 947, 1029, 498, 191, 849, 128, 774, 826, 8, 76, 571, 493, 682, 621, 112, 922, 155, 438, 14, 267, 976, 236, 622, 25, 566, 1078, 295, 342, 968, 116, 835, 497, 681, 223, 254, 723, 1002, 194, 977, 1068, 492, 896, 263, 131, 213, 536, 60, 41, 772, 39, 987, 1053, 563, 908, 271, 1032, 923, 61, 812, 959, 1046, 364, 752, 830, 390, 636, 239, 893, 1075, 68, 626, 737, 979, 430, 387, 741, 816, 1025, 246, 511, 352, 630, 174, 522, 728, 46, 63, 83, 207, 765, 445, 873, 901, 551, 59, 353, 477, 672, 654, 601, 688, 699, 1045, 111, 95, 944, 94, 874, 341, 584, 899, 637, 961, 1077, 238, 680, 892, 173, 677, 1059, 122, 293, 775, 463, 300, 848, 692, 1072, 1040, 130, 210, 988, 316, 856, 546, 150, 702, 811, 415, 810, 470, 718, 882, 259, 831, 997, 823, 109, 209, 297, 542, 779, 649, 691, 921, 177, 149, 813, 788, 251, 673, 661, 502, 870, 857, 229, 416, 1007, 397, 715, 468, 190, 458, 890, 957, 287, 469, 108, 439, 214, 516, 380, 315, 995, 726, 283, 442, 74, 690, 539, 6, 224, 720, 96, 38, 1033, 633, 938, 1038, 1051, 1024, 1069, 489, 824, 356, 23, 237, 632, 434, 559, 980, 204, 327, 852, 119, 154, 778, 665, 144, 567, 241, 732, 405, 920, 806, 153, 598, 758, 900, 963, 817, 520, 27, 208, 326, 435, 679, 89, 488, 729, 805, 828, 886, 627, 437, 648, 602, 481, 373, 552, 964, 533, 1044, 168, 370, 141, 634, 142, 433, 201, 483, 276, 97, 694, 608, 411, 2, 846, 304, 513, 152, 859, 475, 965, 577, 1, 377, 402, 631, 196, 4, 747, 617, 756, 5, 1036, 898, 169, 591, 485, 512, 547, 414, 1060, 523, 401, 544, 945, 118, 558, 417, 930, 324, 476, 32, 569, 787, 589, 107, 303, 195, 87, 158, 926, 473, 157, 225, 1056, 24, 305, 3, 948, 98, 188, 302, 472, 474, 471, 877, 740, 432, 421, 143, 1003, 700, 989, 518, 578, 120, 660, 685, 384, 151, 838, 635, 750, 52, 744, 1020, 954, 459, 358, 1052, 905, 653, 937, 540, 825, 73, 625, 868, 575, 889, 424, 793, 279, 249, 314, 362, 509, 81, 189, 328, 30, 847, 764, 9, 647, 1063, 970, 339, 664, 86, 1081, 436, 983, 183, 966, 822, 226, 92, 861, 444, 942, 710, 91, 556, 712, 862, 371, 925, 780, 429, 270, 217, 400, 1031, 102, 1016, 755, 686, 906, 785, 871, 574, 821, 250, 794, 909, 420, 1061, 628, 733, 329, 974, 54, 49, 16, 103, 564, 829, 1015, 423, 770, 454, 573, 971, 227, 406, 897, 381, 708, 739, 795, 330, 986, 408, 187, 757, 298, 791, 917, 967, 1000, 669, 1066, 642, 321, 990, 325, 615, 1013, 950, 701, 719, 1039, 57, 123, 360, 100, 12, 235, 172, 924, 386, 247, 804, 525, 170, 515, 124, 317, 335, 428, 749, 31, 888, 58, 629, 443, 446, 134, 56, 465, 354, 252, 1008, 504, 766]
w103jhn
Wed Oct 30 22:19:18 EDT 2024
________________________________________"""

pattern = r'(\d+)(?=\n\s*\[)'
best_distances = re.findall(pattern, string)
print(best_distances, "best_distances")