title1 = "url [483kd!32msw]"
title2 = "title stuff [Part 2 of series] [d21#322msd]"

import re
substring1 = re.search('\[(.*)\]', title1)
#print(substring1)
if substring1:
    result1 = substring1.group(1)
    print("The substring for title1 is: " + result1)

substring2 = re.search('\[.*\].*\[(.*)\]', title2)
if substring2:
    result2 = substring2.group(1)
    print("The substring for title2 is: " + result2)

techno_tim_url = "20201007 - Homelab adventure part 2 [this is part 2] {20201007} [yd30xm!2]"
#techno_tim_url = "20201007 - Homelab adventure part 2 {20201007} [yd30xm!2]"
techno_tim_url_substring = re.search('\[.*\].*\[(.*)\]', techno_tim_url)
if techno_tim_url_substring:
    techno_tim_url_extract = techno_tim_url_substring.group(1)
    print("techno_tim_url_extract is: " + techno_tim_url_extract)