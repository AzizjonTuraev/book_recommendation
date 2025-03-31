import pandas as pd

def clean_countries(users : pd.DataFrame):
    for i in range(len(users)):

        if users.loc[i, "country"] in ['', "lj", "quit", '"', "n/a", "the", "somewherein space", "csa", "öð¹ú", "&#20013;&#22269;", "usa & canada", "-", "none",
                                    "01776", "home of the van!!", "bkk", "x", "no more", "galiza neghra", "everywhere and anywhere", "citrus.", "aaa", "dfg"
                                    '\\"n/a\\""', "tyrtyrt", "thing", "we`re global!", "r.o.c.", "-------", "&#32654;&#22269;", "*", "ä¸\xadå?½", "exactly where i am",
                                    "87510", "n/a - on the road", "nowhere", "k1c7b1", '\\n/a\\""', "a", "85021", "bbbzzzzz", "19104", "?ú?{", "c", "u.", "z", "23232", 
                                    "xxxxxx", "ouranos", "ust", "23232", "u", "europa", "l", "30064", "austbritania", "petrolwar nation", "lee", "in your heart", "unit",
                                    "in", "evil empire", "east africa", "lkjlj", "ee.uu", "aotearoa", "02458", ".", "far away...", "travelling", "id", "perãº", "dfg",
                                    "input error", "doodedoo", "space", "europe.", "the world tomorrow", "my", "tdzimi", "antarctica", "wood", "the great white north",
                                    "lake", "aruba", "bfe", "pa", "berguedà", "saint kitts and nevis", "saint luica", "hungary and usa", "pr", "equatorial geuinea",
                                    "universe", "az", "pr", "here and there", '-------', 'n/a', '\\"n/a\\"', '\\n/a\\"', 'ksa', 'europe', 'singapore/united kingdom',
                                    'diy', 'ysa', 'cn', 'adsgfdr', 'u.s.a>', 'rmi', 'heaven', 'country', 'uyo', 'spotsylvania', 'der', 'h.u.g.', 'cadd0', 'nh', 
                                    'yanhill', 'lleida', 'palau', 'micronesia', 'collin', 'guinea-bissau', 'hennipen', 'rice', 'cass', 'hampden', 'ama lurra', 'polk',
                                    'hamilton', 'fiji', 'bernalillo', 'windham', 'papua new guinea', 'burkina faso', 'gabon', 'pasco',  'ferrara', 'morgan', 'slo', 'marrion',


                                    'jackson', 'cherokee', 'lazio', 'dekalb', 'maricopa', 'san marino', 'nyhamnsläge', 'el salvador', 'saint loius', 'framingham', 'monroe', 'hornyonic',
                                    'san bernardino', 'malawi', 'channel islands', 'solomon islands', 'washtenaw', 'vanuatu', 'turkmenistan', 'mérida', 'antigua & barbuda', 'hillsborough', 
                                    'isle of man', '5057chadwick ct.', 'pinallas', 'orense', 'rutherford', 'bell', 'serbia and montenegro', 'camden', 'strongbadia', 'liaoning', 
                                    'clinton', 'lawrenceville', 'bladen', 'cook', 'mordor', 'fontana', 'kiribati', 'solano', 'vorce', 'pender', 'maracopa',
                                    'phila', 'guinea', 'rsa', 'smith', 'pueblo', 'pippo', 'burlington', 'johnson', 'maine', 'buncombe', 'bucks',  
                                    'houston', 'fortaleza', 'pistlavakia', 'mauritania', 'comoros', 'lecce', 'ventura', 'shelby', 'fred', 'mauritius', 'benin', 'holy see',
                                    'osceola', 'van wert', 'lornsenland', 'saint lucia', 'st. helena', 'fifi', 'djibouti', 'prince william', 'marshall islands',
                                    'lombardia', 'rosario', 'henry', 'kz', 'rosello', 'granville', 'macau', 'frome', "carter", "burkinafasu", "yugoslavia",


                                    'livingston', 'caribbean sea',

                                    "commonwealth of northern mariana islands", "euskal herria", "cape verde", "cayman islands", "st. vincent and the grenadines",
                                    'saint vincent and the grenadines"', "saint vincent and the grenadines", 'sao tome and principe"'
                                    ]:
            users.loc[i, "country"] = "unknown"

        elif users.loc[i, "country"] in ["clackamas", "usa", "jersey", "united staes", "hernando", "lane", "yakima", "fulton", "united sates", "america", "good old usa !",
                                        "disgruntled states of america", "st.thomasi", "kern", "cape may", "allen", "whatcom", "fort bend", "u.s. of a.", "ohio", "butler", 
                                        "davidson", "good old usa !", "los estados unidos de norte america", "nyc", "ussurfing", "texas", "oakland" , "baxter", "c.a.",
                                        "fredonia - land of the brave and free", "ua", "u.s>", "u.s.a!", 'good old u.s.a.', 'united stated of america', "united state",
                                        "uusa",  "united stated", "onondaga nation", 'usa"', "effingham", "richmond country", "rapides", "aroostook", "north carolina",
                                        "palm beach", "sao tome and principe", "orange co", "san mateo", "san franicsco", "alachua", "wonderful usa", "united states of america",
                                        'usa (currently living in england)', 'u.s. virgin islands', 'u.s. of a.', 'u.s.a.', 'united statea', "california", 'unite states',
                                        'baltimore', 'auckland', "united states of america", 'ventura county', 'santa barbara', 'missouri', 'united states',
                                        "american samoa", 'guam', 'new london', 'puerto rico', 
                                        ]:
            users.loc[i, "country"] = "us"

        elif users.loc[i, "country"] in ["united kingdom", "british virgin islands", "alderney", "queenspark", "guernsey", "minnehaha", "u.s. virgin islands",
                                        "united kingdom.", "gb", "u.k.", "worcester", "u k", "united kindgdom", "essex", "english", "west yorkshire",
                                        'united kingdom"', 'england', 'england uk', 'united kindgonm', 'wales', 'london', "scotland", ]:
            users.loc[i, "country"] = "uk"

        elif users.loc[i, "country"] in ["distrito federal", ]:
            users.loc[i, "country"] = "brazil"

        elif users.loc[i, "country"] in ["u.a.e", "united arab emirates", "u.a.e", 'u.a.e"']:
            users.loc[i, "country"] = "uae"

        elif users.loc[i, "country"] in ["españa", "basque country", "galiza", "asturies", 'españa"', "madrid", "catalunya", "espaã?â±a", "catalunya(catalonia)",
                                        "espanha / galiza", "euskadi", "catalunya spain", "espaã±a", 'catalonia']:
            users.loc[i, "country"] = "spain"

        elif users.loc[i, "country"] in ['israel"', ]:
            users.loc[i, "country"] = "israel"

        elif users.loc[i, "country"] in ['calabria', "l`italia", "sardinia", 'italy"', 'italia', "itlay", "toscana", "rep san marino", "vicenza",
                                        "italien", 'sicilia', 'milano', 'basilicata', 'sardegna', 'valtesse', "roma", ]:
            users.loc[i, "country"] = "italy"

        elif users.loc[i, "country"] in ['hong kong', "people`s republic of china", "yunling", "chinaöð¹ú", "p r china", "la chine éternelle !", "liushi", "p.r.china", 
                                        "la chine eternelle!", "china öð¹ú", "hongkong", "xinyu", 'cnina', 'china people`s republic', 'p.r.c', 'p.r. china', 'prc',
                                        "china people`s republic", "chian", 'la chine éternelle!', 'zhengjiang']:
            users.loc[i, "country"] = "china"

        elif users.loc[i, "country"] in ['cape verde"', ]:
            users.loc[i, "country"] = "cape verde"

        elif users.loc[i, "country"] in ['la argentina', ]:
            users.loc[i, "country"] = "argentina"

        elif users.loc[i, "country"] in ['phils', "the philippines", "philippinies", "philippine", 'phippines', "phillipines"]:
            users.loc[i, "country"] = "philippines"

        elif users.loc[i, "country"] in ['monterrey', "hidalgo", 'mexico"', "méxico", 'mã?â©xico']:
            users.loc[i, "country"] = "mexico"

        elif users.loc[i, "country"] in ['urugua', ]:
            users.loc[i, "country"] = "uruguay"

        elif users.loc[i, "country"] in ['dominica', ]:
            users.loc[i, "country"] = "dominican republic"

        elif users.loc[i, "country"] in ['faroe islands', 'denmark"']:
            users.loc[i, "country"] = "denmark"

        elif users.loc[i, "country"] in ['czech republic', ]:
            users.loc[i, "country"] = "czechia"

        elif users.loc[i, "country"] in ['la france', 'france"']:
            users.loc[i, "country"] = "france"

        elif users.loc[i, "country"] in ['maroc', ]:
            users.loc[i, "country"] = "morocco"

        elif users.loc[i, "country"] in ['fernando de la mora', "Paraguay"]:
            users.loc[i, "country"] = "paraguay" 

        elif users.loc[i, "country"] in ['trinidad', "trinidad/tobago.", "trinidad & tobago", "trinidad and tobago", "tobago", ]:
            users.loc[i, "country"] = "trinidad and tobago"

        elif users.loc[i, "country"] in ['austria"', ]:
            users.loc[i, "country"] = "austria"

        elif users.loc[i, "country"] in ['de', "deutschland", "deutsches reich", 'deutschland"', "germay", "geermany", "baden-württemberg", "ahrensburg", 
                                    "bademn würtemberg", "nrw", 'germany"', 'bavaria']:
            users.loc[i, "country"] = "germany"

        elif users.loc[i, "country"] in ['rep. san marino']:
            users.loc[i, "country"] = "san marino"

        elif users.loc[i, "country"] in ['victoria', "dauphin", "le canada", "il canada", "canada eh", "le canada", "can", "cananda", "courtenay",
                                        'canda', ]:
            users.loc[i, "country"] = "canada"

        elif users.loc[i, "country"] in ['la svizzera', "swaziland", "la suisse", 'swazilandia', 'suisse']:
            users.loc[i, "country"] = "switzerland"

        elif users.loc[i, "country"] in ['nl', "holland", 'netherlands"', 'netherlands antilles', 'the netherlands', 'neverland', 
                                        'nederlands']:
            users.loc[i, "country"] = "netherlands"

        elif users.loc[i, "country"] in ['w. malaysia', 'malaysia"', 'malaysian']:
            users.loc[i, "country"] = "malaysia"

        elif users.loc[i, "country"] in ['the gambia']:
            users.loc[i, "country"] = "gambia"

        elif users.loc[i, "country"] in ['bih', "bosnia", ]:
            users.loc[i, "country"] = "bosnia and herzegovina"

        elif users.loc[i, "country"] in ['mozambique"', 'moçambique']:
            users.loc[i, "country"] = "mozambique"

        elif users.loc[i, "country"] in ['le madagascar"', "le madagascar"]:
            users.loc[i, "country"] = "madagascar"

        elif users.loc[i, "country"] in ['autralia"', "autralia", "st. clair", "australii", "fairyland", 'queensland', ]:
            users.loc[i, "country"] = "australia"

        elif users.loc[i, "country"] in ['turkey"', 'türkiye', "turkei"]:
            users.loc[i, "country"] = "turkey"

        elif users.loc[i, "country"] in ['_ brasil"', "_ brasil", "_ brasil", "brasil"]:
            users.loc[i, "country"] = "brazil"

        elif users.loc[i, "country"] in ['nz', "newzealand", 'new zealand"', ]:
            users.loc[i, "country"] = "new zealand"

        elif users.loc[i, "country"] in ['sultanate of oman']:
            users.loc[i, "country"] = "oman"

        elif users.loc[i, "country"] in ['iceland"']:
            users.loc[i, "country"] = "iceland"

        elif users.loc[i, "country"] in ['romania"']:
            users.loc[i, "country"] = "romania"

        elif users.loc[i, "country"] in ['copenhagen']:
            users.loc[i, "country"] = "denmark"

        elif users.loc[i, "country"] in ['copenhagen']:
            users.loc[i, "country"] = "denmark"

        elif users.loc[i, "country"] in ['polska']:
            users.loc[i, "country"] = "poland"

        elif users.loc[i, "country"] in ['sri lanka\\"n/a\\""', "srilanka", 'sri lanka\\"n/a\\"']:
            users.loc[i, "country"] = "sri lanka"

        elif users.loc[i, "country"] in ['afganstand holla !!']:
            users.loc[i, "country"] = "afghanistan"

        elif users.loc[i, "country"] in ['la belgique', "belgi", 'belgique']:
            users.loc[i, "country"] = "belgium"

        elif users.loc[i, "country"] in ['s.corea', "republic of korea", 'korea']:
            users.loc[i, "country"] = "south korea"

        elif users.loc[i, "country"] in ['s.africa', 'cape town', ]:
            users.loc[i, "country"] = "south africa"

        elif users.loc[i, "country"] in ['nigeria"', ]:
            users.loc[i, "country"] = "nigeria"

        elif users.loc[i, "country"] in ['bangladesh"', ]:
            users.loc[i, "country"] = "bangladesh"

        elif users.loc[i, "country"] in ['serbia & montenegro', ]:
            users.loc[i, "country"] = "serbia"

        elif users.loc[i, "country"] in ['peru"', ]:
            users.loc[i, "country"] = "peru"

        elif users.loc[i, "country"] in ['greece (=hellas)', ]:
            users.loc[i, "country"] = "greece"

        elif users.loc[i, "country"] in ['algérie', ]:
            users.loc[i, "country"] = "algeria"

        elif users.loc[i, "country"] in ['indiai', ]:
            users.loc[i, "country"] = "india"

        elif users.loc[i, "country"] in ['dublin', ]:
            users.loc[i, "country"] = "irland"

        elif users.loc[i, "country"] in ['cote d`ivoire"', ]:
            users.loc[i, "country"] = "cote d`ivoire"

        elif users.loc[i, "country"] in ['portugal"', ]:
            users.loc[i, "country"] = "portugal"

        elif users.loc[i, "country"] in ['iran"', ]:
            users.loc[i, "country"] = "iran"

        elif users.loc[i, "country"] in ['finland"', ]:
            users.loc[i, "country"] = "finland"

        elif users.loc[i, "country"] in ['russian federation']:
            users.loc[i, "country"] = "russia"

        elif users.loc[i, "country"] in ['brunei darussalam']:
            users.loc[i, "country"] = "brunei"

        elif users.loc[i, "country"] in ['slovak republik']:
            users.loc[i, "country"] = "slovakia"

        elif users.loc[i, "country"] in ['ukrain']:
            users.loc[i, "country"] = "ukraine"

        elif users.loc[i, "country"] in ['thailoand']:
            users.loc[i, "country"] = "thailand"

        elif users.loc[i, "country"] in ['irland', "northern ireland"]:
            users.loc[i, "country"] = "ireland"

        elif users.loc[i, "country"] in ['pakistan.']:
            users.loc[i, "country"] = "pakistan"

        elif users.loc[i, "country"] in ['goteborg', ]:
            users.loc[i, "country"] = "sweden"

        elif users.loc[i, "country"] in ['republic of panama', ]:
            users.loc[i, "country"] = "panama"

        elif users.loc[i, "country"] in ['côte d', ]:
            users.loc[i, "country"] = "cote d`ivoire"

        elif users.loc[i, "country"] in ['l`algérie', ]:
            users.loc[i, "country"] = "algeria"

        elif users.loc[i, "country"] in ['harvatija', ]:
            users.loc[i, "country"] = "croatia"

        elif users.loc[i, "country"] in ['isreal', ]:
            users.loc[i, "country"] = "israel"

        elif users.loc[i, "country"] in ['burma', ]:
            users.loc[i, "country"] = "myanmar"

        elif users.loc[i, "country"] in ['saudia arabia', ]:
            users.loc[i, "country"] = "saudi arabia"

        elif users.loc[i, "country"] in ['burma', ]:
            users.loc[i, "country"] = "myanmar"

        elif users.loc[i, "country"] in ['burma', ]:
            users.loc[i, "country"] = "myanmar"

    return users


def get_correct_age(users):

    users["Age"] = [0 if pd.isna(i) else int(i) for i in users["Age"]]
    return users

def get_correct_location(users):
    # users = pd.read_csv("dataset/Users.csv")
    users["country"] = [i.split(",")[-1].strip() for i in users["Location"]]
    users["country"] = [i[:-1] if i.endswith('"') else i for i in users["country"]]
    users = clean_countries(users)
    users = users[["User-ID" ,"country","Age"]]
    # users.columns = users[["user-id" ,"country","age"]]
    return users




