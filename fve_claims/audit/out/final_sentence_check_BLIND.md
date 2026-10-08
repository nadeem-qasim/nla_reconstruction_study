# Final-sentence label check — BLIND (label every item before opening the KEY)

Judge each **Claim** against the **Passage** only. The activation is read at the passage's last token. The bold text is
where the claim appears in the AV's final sentence. Write `human_label: true`, `false` or `unsure`:

- true = stated in or entailed by the passage
- false = contradicted by the passage, or a specific (name, number, date, place, quote) the passage does not contain.
  After `false`, add `contradicted` or `absent`, e.g. `human_label: false absent`.
- unsure = you can't decide; say why in `note:`.

These are the definitions Claude's labels used (fve_claims/ANNOTATION_GUIDE.md, truth v2). Score with
`uv run python fve_claims/audit/score_final_sentence_sheet.py`.

## 1. F01

Model 27B · document 58

**Passage:** Europafilm was an influential Swedish film company established in 1929 by Schamyl Bauman and Gustaf Scheutz. The office was located at Kungsgatan in central Stockholm, while the film studio was located in Mariehäll, Bromma, northwest of Stockholm city. It was acquired by Bonnier in 1984 and merged with Svensk Filmindustri in 1985. It was best known for the films starring Edvard Persson. Aside from its film activities Europafilm also manufactured electroforming equipment for the vinyl record manufacturing industry. This division was later sold to the now defunct Alpha Toolex AB of Sundyberg, Sweden manufacturers of vinyl record pressing machinery. Both Europafilm plating equipment and Alpha Toolex pressing equipment is still considered to be the finest engineered equipment in their respective categories

**AV's final sentence:** "The company closed in 1990 and the two manufacturing divisions were sold to other companies. The **hydraulic press** and textile cutting machine developed by the company were sold to other companies. Both the hydraulic press and textile cutting machine developed by this company are still considered the best in their respective categories" — implies enduring legacy, final sentence needs closing period

**Claim:** The hydraulic press developed by the company was sold to another company.

human_label: 
note: 

## 2. F02

Model 7B · document 18

**Passage:** MCPON John-117, or "Master Chief", is a fictional character and the protagonist of the Halo fictional universe created by Bungie. Master Chief is a playable character in the series of science fiction first-person shooter video games, Halo 2, Halo 3, Halo 4, and. Outside video games, the character appears in books and graphic novels—,,, and —and has cameos in other Halo media, including,, The Halo Graphic Novel, Halo Legends and. The Master Chief is a towering biochemically and cybernetically-enhanced supersoldier, raised and trained from an early age to be a weapon; he is almost faceless, never seen without his green-colored armor and helmet. He is commonly referred to by his naval rank, rather than his given birth-name or serial-designation. The character is voiced by Steve Downes, a Chicago disc jockey, in the video games in which he appears. Downes based his personification of the Chief on an initial character sketch which called for a Clint Eastwood – type character of few words. The Master Chief is a video game icon, a relative newcomer among more established franchise characters, such as Mario, Sonic the Hedgehog and Lara Croft. The character has received a mostly positive reception. While some have described the Chief's silent and faceless nature as a weakness of the character, other publications have suggested these attributes better allow players to assume his role

**AV's final sentence:** Final token "role" **ends an incomplete clause** ("allow him to assume his role"), part of a parallel structure ("this may aid his ability to take on the character's perspective, allowing him to assume his role"), strongly expecting "and responsibility" or "in the narrative" or "as a player."

**Claim:** The visible ending is syntactically incomplete.

human_label: 
note: 

## 3. F03

Model 7B · document 23

**Passage:** Joseph Octave Mousseau (April 25, 1844 – December 13, 1898) was a physician and political figure in Quebec. He represented Soulanges in the House of Commons of Canada from 1891 to 1892 as an Independent member. He was born in Berthier, Canada East, the son of Louis Mousseau, who was the son of Alexis Mousseau, and Sophie Duteau, dit Grandpré. Mousseau was educated at Montreal and Nicolet. He served on the town council for Saint-Polycarpe and also served as mayor. Mousseau married Marie Rose-Avelina Cadieux. He ran unsuccessfully for a seat in the House of Commons in 1887. His election to the House of Commons in 1891 was overturned in 1892 and he was defeated by James William Bain in the two by-elections which followed. He was the brother of Joseph-Alfred Mousseau. His son Joseph-Octave was a member of the Quebec legislative assembly

**AV's final sentence:** **Final token "assembly"** ends an incomplete phrase ("who served in the ontario legislative assembly"), part of a "His brother was a member of the ontario provincial assembly" clause, strongly expecting "from 1890 to 1920" or "and was also a politician" or similar.

**Claim:** The final tokenizer token is “assembly”.

human_label: 
note: 

## 4. F04

Model 7B · document 60

**Passage:** The Old Loggers Path (OLP) is a loop hiking trail in Lycoming County in north-central Pennsylvania in the United States. Marked with international orange blazes, the Old Loggers Path is located entirely within the Loyalsock State Forest. Most hikers take two and a half to three days and two nights to complete the Old Loggers Path, making it popular for weekend hikes. Highlights of the trail include waterfalls, several scenic streams and creeks (most of which do not have bridges), and panoramic vistas. The land the Old Loggers Path is on was initially owned and clear-cut by the Union Tanning Company, followed by the Central Pennsylvania Lumber Company. The trail chiefly follows the grades of abandoned logging roads and railroads, and its trailhead is the lumber ghost town of Masten. Parts of the trail were made by the Civilian Conservation Corps, which operated a camp in the area from 1933 to 1941

**AV's final sentence:** Final token "1941" closes a date range clause (**"until 1933 to 1941 and a CCC from 1933 to 1941"**), expecting continuation like "." or "and constructed infrastructure."

**Claim:** The text contains the phrase "until 1933 to 1941 and a CCC from 1933 to 1941".

human_label: 
note: 

## 5. F05

Model 7B · document 89

**Passage:** Guido Bonatti (died between 1296 and 1300) was an Italian mathematician, astronomer and astrologer, who was the most celebrated astrologer of the 13th century. Bonatti was advisor of Frederick II, Holy Roman Emperor, Ezzelino da Romano III, Guido Novello da Polenta and Guido I da Montefeltro. He also served the communal governments of Florence, Siena and Forlì. His employers were all Ghibellines (supporters of the Holy Roman Emperor), who were in conflict with the Guelphs (supporters of the Pope), and all were excommunicated at some time or another. Bonatti's astrological reputation was also criticised in Dante's Divine Comedy, where he is depicted as residing in hell as punishment for his astrology. His most famous work was his Liber Astronomiae or 'Book of Astronomy', written around 1277. This remained a classic astrology textbook for two centuries

**AV's final sentence:** **Final token "centuries"** ends an incomplete clause ("lasted for two centuries"), part of a claim about the manuscript's influence lasting "for two centuries" — likely followed by "and" or "after," or "and was subsequently copied," or "as a standard text" completing the duration claim.

**Claim:** The final token is "centuries".

human_label: 
note: 

## 6. F06

Model 7B · document 5

**Passage:** Wayne Gretzky Drive is a freeway in Edmonton, Alberta, Canada. Originally Capilano Drive, it was officially renamed October 1, 1999 after NHL hockey player Wayne Gretzky, as a tribute to his years with the Edmonton Oilers. The same day, Wayne Gretzky's number 99 jersey was retired at the Skyreach Centre, which lies just west of Wayne Gretzky Drive, at 118 Avenue. 66/75 Street is a major arterial road in east Edmonton which serves residential and industrial areas. Wayne Gretzky Drive and 75 Street, both located between Whitemud Drive and Yellowhead Trail, is part of Edmonton's eastern leg of its Inner Ring Road. Wayne Gretzky Drive and 75 Street are part of a continuous roadway that runs from 41 Avenue SW to 33 Street NE (Edmonton's northeastern city limit) and includes portions of 66 Street and Fort Road, as well as all of Manning Drive

**AV's final sentence:** Final token "Drive" **ends mid-phrase** ("all of Millwood Drive"), part of a parenthetical list of named streets ("including all of Millwood Drive and its extension via Don Mills Drive"), strongly expecting "and its extension" or "and the surrounding area" or "and other."

**Claim:** The text ends mid-phrase.

human_label: 
note: 

## 7. F07

Model 27B · document 22

**Passage:** CKNL-FM is a Canadian radio station that broadcasts a mainstream rock format at 101.5 FM in Fort St. John, British Columbia. The station is branded as 101.5 The Bear and is owned by Bell Media. It is one of three "Bear" rock stations in Canada; the others are CFBR-FM in Edmonton, Alberta, and CKRX-FM in Fort Nelson, British Columbia. The station originally began broadcasting June 20, 1962 at 970 AM, and later moved to 560 AM and finally to the FM dial at 101.5 FM in 2003. When the FM flip was approved, the station was to continue the country music format of the former 560 CKNL. However, likely in response to the recent licensing of CKFU-FM in the same market at that time, when the station flipped to FM the format was switched to a rock station

**AV's final sentence:** "the sister stations were rebranded as 99 Rock. Initially planned as a country station, the format was later abandoned due to competition from WQXI, and the format was changed to a rock station" — **the final clause mirrors the opening description**, sister

**Claim:** The final clause mirrors the opening description.

human_label: 
note: 

## 8. F08

Model 27B · document 83

**Passage:** Luis Roche was an important Venezuelan urbanist and was the Venezuelan ambassador to Argentina. He was also an amateur film director. In the 1930s, Roche advocated for the redesign of Caracas, to include developed corridors to a multi-purpose center. His suggestion involved a 36-meter-wide avenue based on Avenue des Champs-Élysées. He was responsible in great measure for the development of Caracas' east side during the 1940s. He contributed to the development of neighborhoods such as La Castellana, Altamira and La Florida. Roche was a relevant diplomatic figure as well, being appointed as Venezuela's ambassador to Argentina. He married a Colombian / French lady by the name of Beatrice Dugand, with whom he had four children, Beatrice Roche, Lilianne Roche, Marcel Roche and Luis Armando Roche. An important avenue in Altamira (Caracas) bears the name Luis Roche in his honor

**AV's final sentence:** "He is also remembered for his contributions to the city of Guadalajara, and **is considered one of the most important figures in the city's history**. A street in Guadalajara is named 'Posadas' after him in honor" — final sentence ends with "in his honor" implying a period closes the article

**Claim:** He is considered one of the most important figures in the city's history.

human_label: 
note: 

## 9. F09

Model 27B · document 70

**Passage:** Carl Gösta Björn Joachim von der Esch (11 January 1930 – 10 March 2010) was a Swedish Christian democratic politician, member of the Riksdag 1998 – 2006. Esch had a farming business and did a Ph.D. in business administration at Uppsala University in 1972. Before joining the Christian Democrats, he had previously represented Moderate Party in the Riksdag 1991 – 1994, replacing Per Westerberg during his time as a minister. At the time of the Swedish 1994 referendum on membership in the European Union, Esch clashed with the Moderate Party as he campaigned on the "no" side. When he subsequently formed a list of EU critics that ran in the 1995 European Parliament election in Sweden, he was expelled from the party. This list was unsuccessful in the election, and von der Esch returned to parliamentary politics in 1998 as a Christian Democrat. In the 2003 referendum on joining the Economic and Monetary Union and the euro, he again campaigned on the "no" side. He later joined the June List, became its vice chairman in 2008, and was on second place on the June List ballot in the 2009 European Parliament election in which the party lost its representation in the European Parliament

**AV's final sentence:** "He later served as secretary of the Christian Democratic Party until 2006, when **he was on the party's list for the European Parliament**, which was defeated and failed to win a seat in the European Parliament" — the final clause ends on the list leader's final defeat, implying his career ended

**Claim:** He was on the Christian Democratic Party's list for the European Parliament.

human_label: 
note: 

## 10. F10

Model 27B · document 28

**Passage:** Santa Elena de Uairén () is a small Venezuelan city (29,795 inhabitants in 2006) in the state of Bolívar near the border with Brazil and Guyana. It was Founded by Lucas Fernandez Peña in 1923. The city's name originates from the first daughter of Lucas Fernandez Pena Elena, and Uairén by the river that crosses the city. Located in the middle of La Gran Sabana (Great Plains), Santa Elena is home to many travel agencies offering tours in Canaima National Park, flights over Angel Falls, and hiking tours to the famous Monte Roraima. The town is notable for its influential presence of indigenous peoples; there is even a community called Manakrü (pronounced mah-nah-CREE) populated entirely by indigenous people. The schools in this neighborhood use both Spanish and Pemon, an indigenous language. Due to its proximity to the Brazilian state of Roraima, Santa Elena sees a busy exchange between the two countries of Brazilian consumer products from Brazil and Venezuelan oil and petrol. Other Brazilian cities that trade with Santa Elena de Uairen are Manaus, Santarém, Macapá, Belém

**AV's final sentence:** "they would travel to other cities in Brazil such as: **Boa Vista, Macapá, Santarém, Belém**" — final token expects continuation with another Brazilian city like "Belém do Pará"

**Claim:** The list of cities includes "Boa Vista, Macapá, Santarém, Belém".

human_label: 
note: 

## 11. F11

Model 27B · document 67

**Passage:** Bloomberg L.P. is a privately held financial, software, data, and media company headquartered in Midtown Manhattan, New York City. It was founded by Michael Bloomberg in 1981, with the help of Thomas Secunda, Duncan MacMillan, Charles Zegar, and a 30% ownership investment by Merrill Lynch. Bloomberg L.P. provides financial software tools such as an analytics and equity trading platform, data services, and news to financial companies and organizations through the Bloomberg Terminal (via its Bloomberg Professional Service), its core revenue-generating product. Bloomberg L.P. also includes a wire service (Bloomberg News), a global television network (Bloomberg Television), digital websites, radio stations (Bloomberg Radio), subscription-only newsletters, and two magazines: Bloomberg Businessweek and Bloomberg Markets. In 2014, Bloomberg L.P. launched Bloomberg Politics, a multiplatform media property that merged the company's political news teams, and has recruited two veteran political journalists, Mark Halperin and John Heilemann, to run it

**AV's final sentence:** "It also launched Bloomberg Politics in 2011, a political news and media initiative. He hired former Washington Post editor Josh Marshall and **former MTV News president Jon Landman** to run it" — the final clause describes the political initiative, suggesting the sentence ends here, period.

**Claim:** Bloomberg also hired former MTV News president Jon Landman to run the initiative.

human_label: 
note: 

## 12. F12

Model 7B · document 99

**Passage:** Delphine "Delphi" Greenlaw is a fictional character on the New Zealand soap opera Shortland Street, who was portrayed by Anna Hutchison between 2002 and 2004. The character arrived in early 2002 as the teenage sister of Geoff (Andrew Laing) and his adoptive sister, Anne Greenlaw (Emmeline Hawthorne). The characters tomboy ways saw her favour rugby over fashion and as a result, she was isolated from her peers. The character participated in a hugely high profile storyline in 2003 where she fell for much older man, Dom (Shane Cortese), who went on to murder Geoff. The character departed in 2004 following the death of both her siblings and intimidation from Dom. Delphi was highly praised throughout her two-year run, with Hutchison receiving numerous award nominations and winning the "Rising Star" prize in the 2004 TV Guide Best on the Box People's Choice Awards. The characters romance with Dom and struggle with anorexia has seen the character's storylines become iconic since her departure

**AV's final sentence:** **Final token "departure"** ends the phrase "since her departure from the show following her departure from the show after her departure" — part of a concluding summary clause ("continued appearances and fan content since her departure..."), strongly expecting "from the show" or "and the show's finale."

**Claim:** The final token is "departure".

human_label: 
note: 

## 13. F13

Model 7B · document 12

**Passage:** The Committee against the Finnish White Terror () was an organization in Sweden, formed at the end of the Finnish Civil War. The formation of the Committee was preceded by a call from the Social Democratic Left Party published in Politiken in February 1918 to mobilize protests around the country to counter the official Swedish government position on the Finnish question. The Committee sought to unite the Swedish labour movement for a common position against what they termed the” White Terror” in Finland. The Committee raised funds for humanitarian aid to the victims of the repression. The Committee also opposed denials of political asylum for Finnish refugees. Sven Linderot was one of the three members of the Committee. The Committee managed to gather 21,851.53 kronor, 14,518.73 for Finnish refugees in Sweden and 6,920 kronor for affected in Finland. The Committee published 100,000 leaflets titled 'Truth about Finland', and more than 100 public meetings were organized

**AV's final sentence:** Final token "organized" ends an incomplete clause ("where **150 lectures and protest meetings were organized** and several demonstration meetings organized"), strongly expecting a continuation like "in support of the campaign" or "across the country" or "by the activists during the campaign period."

**Claim:** A total of 150 lectures and protest meetings were organized.

human_label: 
note: 

## 14. F14

Model 7B · document 41

**Passage:** Hvidovre Kommune is a municipality (Danish, kommune) in Region Hovedstaden near Copenhagen on the island of Zealand (Sjælland) in eastern Denmark. The municipality covers an area of 22 km², and has a total population of 52,027 (1 April 2014). Its mayor is Helle Moesgaard Adelborg, a member of the Social Democrats (Socialdemokraterne) political party. The main town and the site of its municipal council is the town of Hvidovre. Other towns in the municipality are Avedøre and Friheden. Neighboring municipalities are Copenhagen to the east, Rødovre to the north, and Brøndby to the west. Part of its eastern border are the waters of Kalveboderne, and to the south is Køge Bay (Køge Bugt). The southern-most section of the municipality, known as Avedøre Holme, juts out into Køge Bay and forms part of the entryway into Kalveboderne, the waters of which separate the island of Zealand from neighboring Amager. Avedøre Holm houses two harbours

**AV's final sentence:** **Final token "harbours"** ends mid-clause ("This town holds two harbours"), part of a parenthetical list ("Two harbours contain two harbours"), strongly expecting continuation like "which are:" or "the northernmost of which are" or "and associated industrial storage areas."

**Claim:** The final tokenizer token is “harbours”.

human_label: 
note: 

## 15. F15

Model 27B · document 63

**Passage:** Bicycles & Tricycles is the sixth studio album from the Orb. It brought together The Orb's style of the early 1990s with current electronic music to mixed reactions. The Daily Telegraph praised Bicycles & Tricycles as being "inclusive, exploratory, and an enjoyable journey"; however, many other publications dismissed it as "stoner dub" and largely irrelevant to current electronic music culture. In addition to Paterson, Roome, Phillips, and Fehlmann, The Corporal contributed with vocoder affected singing and MC Soom-T provided lyrics and rapped. Orb co-founder Jimmy Cauty, too, made a guest appearance as co-writer on Bicycles & Tricycles' "From a Distance". After departing from Island Records, The Orb released Bicycles & Tricycles in 2004 on Cooking Vinyl in the United Kingdom and Sanctuary Records in the United States. To promote the album, The Orb began a UK tour with dub reggae artist Mad Professor, who had remixed The Orb in the past. Though The Orb still pulled in large crowds, The Guardian described one London performance as "joyless" and stated that "few of the new tracks... really go anywhere". They also noted that Paterson seemed to be far more comfortable and happier to play material from Bicycles & Tricycles rather than older tracks. Paterson's biggest influences for the album were drum and bass and trip hop music

**AV's final sentence:** **Eminem's main influences for the project** were funk and trip hop music" — final clause expects elaboration or period  
(also earlier in the explanation: "Eminem's "The Marshall Mathers LP" … Eminem's stated musical influences … Eminem's main influences for the album")

**Claim:** The article is about Eminem's 'The Marshall Mathers LP'.

human_label: 
note: 

## 16. F16

Model 27B · document 72

**Passage:** Leone Marucci (born March 28, 1973, Youngstown, Ohio) is an American filmmaker, and founder of Independent Film and Media company Steelyard Pictures through which he wrote, directed and produced the 2012 film The Power of Few, which featured the ensemble cast of Christopher Walken, Christian Slater, Q'orianka Kilcher, Anthony Anderson, Jesse Bradford, Moon Bloodgood, Nicky Whelan, Devon Gearhart, Juvenile and others. Through The Power of Few website, Marucci and producing partner Q'orianka Kilcher developed and delivered a ground breaking interactive experience embarked upon in 2006. From online casting to online editing, the global audience was provided original material from the film (and an online editing system) and invited to help create the finished film. Marucci's interactive approach was featured in The Hollywood Reporter's article on "Digital-Do-It-Yourself." Leone Marucci is repped by Stuart Manashil at William Morris Endeavor

**AV's final sentence:** **Hollywood industry affiliation**

**Claim:** The passage concerns Hollywood industry affiliation.

human_label: 
note: 

## 17. F17

Model 7B · document 8

**Passage:** Frédéric Talgorn (born 2 July 1961 in Toulouse, France) is a French composer for film and television. He studied music at the Paris Conservatoire where his teachers included Sabine Lacoraet and Yvonne Loriod, but he completed his studies on his own. In 1987 he moved to the United States where he began to compose film music. He also wrote the official music to accompany the Olympic flame for the 1992 Winter Olympic Games. Notable film scores include Edge of Sanity (1989), (1990), Robot Jox (1990), Fortress (1992) and The Temp (1993). He also has an extensive catalogue of concert music, and has often conducted his own works in concert and recording sessions. He has also conducted and recorded film scores of others with the Royal Scottish National Orchestra

**AV's final sentence:** Final token "Orchestra" **ends an incomplete phrase** ("with the Pittsburgh Symphony Orchestra"), part of a parenthetical list of orchestral recordings ("has recorded with some works with the Philadelphia Philharmonic Orchestra"), expecting continuation like "and other orchestras," or "and the Royal Philharmonic."

**Claim:** The final phrase is incomplete.

human_label: 
note: 

## 18. F18

Model 27B · document 1

**Passage:** Clark Lake is a lake located in Gogebic County in the U.S. state of Michigan. Clark Lake is one of about two dozen clear, clean lakes located in the Sylvania Wilderness of Ottawa National Forest a few miles (6 to 8 km) to the west of the town of Watersmeet. The shoreline is undeveloped except for a picnic area and boat launch at the northern end. The lake possesses several islands and numerous bays and coves. Large boulders strewn about the shoreline and lake bed add to the scenic beauty of this lake. It is not uncommon to see nesting loons and eagles around the lake's islands, and black bear and wolves inhabit the old-growth forest around the lake. The total surface area of the lake is, with maximum depths of. Like all lakes in Sylvania, Clark Lake has numerous special regulations designed to protect and ensure its wilderness quality for future generations. No motorized watercraft are allowed, and a catch and release policy is in place for bass species

**AV's final sentence:** "The lake is protected by a state park designation, and is maintained by volunteer groups who have installed a boat launch and fishing pier. Fishing is permitted, though **the lake is a no-kill zone**, and catch-and-release is enforced for bass species" — the final word "species" ends mid-list, expecting a period or continuation specifying which bass species or additional regulations.

**Claim:** The lake is a no-kill zone.

human_label: 
note: 

## 19. F19

Model 27B · document 37

**Passage:** Fatih Terim, Commendatore OSSI, T.C, (born 4 September 1953) is a Turkish association football manager and former player. He is currently the manager of Galatasaray, a position he previously held three times. Terim has managed several clubs in Italy and Turkey, as well as the Turkish national football team, most recently from 2013 to 2017. In a survey conducted by the International Federation of Football History & Statistics (IFFHS) in 80 countries, he was placed among the best eight managers in the world, receiving his award at a ceremony held in Rothenburg, Germany, on 8 January 2001. Terim received a nomination for UEFA manager of the year 2008, and Eurosport named him the best coach at UEFA Euro 2008. In December 2008, he was ranked the seventh-best football manager in the world by World Soccer Magazine in 2008. His Turkish nickname is "İmparator", and his Italian nickname is "Imperatore". Both names mean

**AV's final sentence:** **Both names mean**" — identical meaning expected next  
(also earlier in the explanation: "Both names mean")

**Claim:** Both names mean the same thing.

human_label: 
note: 

## 20. F20

Model 27B · document 56

**Passage:** The Atlantic Charter was a pivotal policy statement issued during World War II on 14 August 1941 which defined the Allied goals for the post-war world. The leaders of the United Kingdom and the United States drafted the work and all the Allies of World War II later confirmed it. The Charter stated the ideal goals of the war: no territorial aggrandizement; no territorial changes made against the wishes of the people (self-determination); restoration of self-government to those deprived of it; reduction of trade restrictions; global cooperation to secure better economic and social conditions for all; freedom from fear and want; freedom of the seas; and abandonment of the use of force, as well as disarmament of aggressor nations. Adherents of the Atlantic Charter signed the Declaration by United Nations on 1 January 1942, which became the basis for the modern United Nations. The Atlantic Charter set goals for the postwar world and inspired many of the international agreements that followed the war. The General Agreement on Tariffs and Trade (GATT), the postwar independence of European colonies, and much more are derived from the Atlantic Charter

**AV's final sentence:** Many of the most important agreements and policies, such as the United Nations Charter and **the Bretton Woods Agreement**, are all derived from the Atlantic Charter" — the final clause mirrors the earlier sentence, suggesting a closing period or reinforcing its foundational legacy.  
(also earlier in the explanation: "the Bretton Woods Agreement")

**Claim:** The Bretton Woods Agreement is among the agreements derived from the Atlantic Charter.

human_label: 
note: 

## 21. F21

Model 27B · document 49

**Passage:** Aspren or Asprenas () was a 1st-century Christian saint and venerated as the first Bishop of Naples. Aspren lived at the end of the 1st century and in the early 2nd century, as confirmed by archaeological studies regarding the early Neapolitan Church as well as the fact that "Aspren" was a common name during the days of the Roman Republic and the early years of the Roman Empire and afterwards fell into disuse. The Marble Calendar of Naples (Calendario Marmoreo di Napoli) attests to Aspren's existence and the fact that he lived during the reigns of Trajan and Hadrian; Aspren's episcopate is stated as lasting twenty-three years. Nothing is known of his life, but an ancient legend holds that Saint Peter, on his way to Rome, stopped at Naples and converted an old woman (identified as Candida the Elder) after he cured her of an illness. Numerous other converts to Christianity were made during this time in Naples, including Aspren, who was converted either by Peter or Candida herself and who had also been ill. The legend holds that Peter consecrated Aspren as bishop of Naples and asked him to construct the oratory of Santa Maria del Principio, which would form the basis for the basilica of Santa Restituta; San Pietro ad Aram was also said to have been built during this time

**AV's final sentence:** "According to legend, **Thomas also founded the Cathedral of St. Thomas during this visit, which is said to have been built during this time**. Additionally, the Santa Casa is said to have been built around this time" — period  
(also earlier in the explanation: "the Cathedral of St. … Thomas … the Cathedral of St. Thomas is said to have been built during this time")

**Claim:** The Cathedral of St. Thomas is said to have been built during this time.

human_label: 
note: 

## 22. F22

Model 7B · document 79

**Passage:** Joseph Alexander Cooper (November 25, 1823 – May 20, 1910) was an American farmer, soldier, and civil servant. A Southern Unionist, he fought for the Union Army during the American Civil War, commanding units at Mill Springs, Stones River, Chickamauga, Franklin, Nashville, Bentonville, and in the Knoxville and Atlanta campaigns. He had achieved the rank of Brevet Major General by the time he was mustered out in early 1866. After the war, Cooper commanded the Tennessee State Guard, a state militia organized by Governor William G. Brownlow to quell postwar violence across Tennessee. He served as an internal revenue agent during the 1870s before moving to Kansas, where he spent the final decades of his life

**AV's final sentence:** Final token "life" ends an incomplete phrase (**"spent the remainder of his life's wealth and ended his life's work in Ohio, spent the remainder of his life"**), strongly expecting "as a farmer" or "in retirement" or "living quietly," completing the concluding summary of his post-career activities.

**Claim:** The text contains the phrase "spent the remainder of his life's wealth and ended his life's work in Ohio, spent the remainder of his life".

human_label: 
note: 

## 23. F23

Model 7B · document 77

**Passage:** "Word to the Mutha!" is a song co-written and performed by American contemporary R&B; group Bell Biv DeVoe. It originally appeared on their debut studio album Poison under the title "Ronnie, Bobby, Ricky, Mike, Ralph and Johnny (Word to the Mutha)! ", but the title was shortened and a remixed version of the song was issued as the only official single from the group's remix album The song features vocals from Bobby Brown, Ralph Tresvant and Johnny Gill; and it was the first recorded song to feature all six members of New Edition; although Brown, Tresvant and Gill are credited separately on the single rather than collectively as New Edition. The song samples "A Star in the Ghetto" by Average White Band and "The Jam" by Graham Central Station. A music video was filmed in and around the Roxbury Housing Projects in Boston, where five of the six (excluding Johnny Gill) New Edition members grew up

**AV's final sentence:** Final token "up" ends an incomplete clause (**"the neighborhoods where they and some of the members who grew up in the same neighborhood where they grew up"**), strongly expecting "during their youth" or "and lived" or "the neighborhood," completing the biographical context about childhood surroundings.

**Claim:** The text contains the phrase "the neighborhoods where they and some of the members who grew up in the same neighborhood where they grew up".

human_label: 
note: 

## 24. F24

Model 7B · document 7

**Passage:** Edward Rowan Finnegan (June 5, 1905 – February 2, 1971) was a U.S. Representative from Illinois from 1961 to 1964. Finnegan was born in Chicago and graduated with a BA from Loyola University Chicago and a law degree from the DePaul University School of Law in 1930. He started practicing as an attorney in 1931 and then served as an Assistant State's attorney in Cook County. Later, Finnegan served as the Assistant Corporation Counsel for Chicago. Finnegan unsuccessfully sought the Democratic nomination for the position of a Chicago municipal court judge in 1939. In 1960, Finnegan was elected to Congress from Illinois' 12th district. After redistricting, Finnegan's district was merged with the neighboring 9th District of fellow Democrat Sidney Yates. Finnegan transferred to the 9th, since Yates was giving up his seat to run for the United States Senate. Yates lost, and Chicago's machine bosses persuaded Finnegan to stand down in 1964 and hand the 9th back to Yates. In return for his co-operation, Finnegan was appointed as a judge for the Circuit Court of Cook County. He resigned his seat in Congress on December 6, 1964 and commenced his service on the bench the following day. He continued to serve until his death in 1971

**AV's final sentence:** Final token "1971" **ends an incomplete clause** ("died in 1971...and died in 1971..."), strongly expecting "." or "." or "with cancer" or "and his retirement from the Ohio State Medical Society."

**Claim:** The text ends in an incomplete clause.

human_label: 
note: 

## 25. F25

Model 27B · document 52

**Passage:** Młociny is a Warsaw Metro station serving as a northern terminus to Line M1. It is situated within Warsaw administrative boundaries and ZTM ticketing zone 1, in the dzielnica of Bielany, in a close proximity to Warsaw's ArcelorMittal steelworks. The station opened on 25 October 2008 and is the final northern extension of Line M1. The area beyond the station has been remodelled into a major public transportation junction after Młociny opened. It is served by trams and both urban and suburban buses. Although there are no plans to extend Line M1 further, the station is built in such way that it will be possible to do so if need be. The trains are turned back at sidings behind Młociny. Terminating trains arrive at eastern side platform, whereas southbound trains depart from western side platform

**AV's final sentence:** "**The station is a terminal**, and therefore trains must reverse direction before departing. The station is also equipped with a dedicated maintenance shed. Trains bound for London depart from the left-hand platform, while trains returning to London depart from the right-hand platform" — the final sentence likely ends with a period, noting the separation of departure tracks

**Claim:** The station is a terminal.

human_label: 
note: 

## 26. F26

Model 7B · document 61

**Passage:** The Cambodia – Vietnam Friendship Monument in Phnom Penh, capital of Cambodia, is a large concrete monument commemorating the former alliance between Vietnam and Cambodia. It was built in the late 1970s by the communist regime that took power after the Cambodian-Vietnamese War, which overthrew the Khmer Rouge regime. The monument is located at the Botum Park near the centre of Phnom Penh not far from the Royal Palace. It features heroic statues of Vietnamese and Cambodian soldiers in the "Socialist realist" style developed in the Soviet Union in the 1930s, together with images of a woman and baby representing Cambodian civilians. The monument is in a popular park in the middle of the city. The monument has occasionally become a political focal point. On August 30, 1998, during post-electoral protests, several people climbed onto the monument with hammers, poured gasoline on it and set it on fire. This damage was repaired two months later by the authorities. On July 29, 2007, a bomb exploded at the base of the monument, causing little damage

**AV's final sentence:** Final token "damage" ends an incomplete clause ("caused little damage, causing no significant damage, causing little damage"), strongly expecting "to the structure" or "but" or "and the actual structure" or "to the blast shelter" — completing the damage assessment of **the attempted demolition attempt**.

**Claim:** The bombing was an attempted demolition attempt.

human_label: 
note: 

## 27. F27

Model 27B · document 91

**Passage:** The Tule Lake camp was a federal work facility and WRA isolation center located in Siskiyou County, five miles west of Tulelake, California. It was established by the United States government in 1935 during the Great Depression for vocational training and work relief for young men, in a program known as the Civilian Conservation Corps. The camp was established initially for CCC enrollees to work on the Klamath Reclamation Project. During World War II, in 1942 the Tule Lake War Relocation Center was built next to the camp as one of ten concentration camps in the interior of the US for the incarceration of Japanese Americans who had been forcibly relocated from the West Coast, which was defined as an Exclusion Zone by the US military. Two-thirds of the 120,000 incarcerated individuals were United States citizens. Renamed the Tule Lake Isolation Center, this facility was adapted in the wartime years to shelter Japanese-American strikebreakers used against resisters at the main segregation camp, imprison Japanese-American dissidents, and house Italian and German prisoners of war (POWs) who were assigned to work as farm laborers in the region. After the war, on 25 April 1946, the camp was transferred from the Army to the Fish and Wildlife Service, which had managed it just prior to the establishment of the segregation camp. The four remaining buildings are being restored in a project to return the camp to its 1940s appearance

**AV's final sentence:** "The site is now a museum and research facility. The building is being preserved as part of a project to restore the site. **The old plant is being preserved and restored** as part of an effort to restore the site to its 1950s appearance" — final clause expects a period or elaborating phrase about the restoration project or historical interpretation goal.

**Claim:** The old plant is being preserved and restored.

human_label: 
note: 

## 28. F28

Model 7B · document 98

**Passage:** Houshang Seyhoun, () (August 22, 1920 – May 26, 2014) was an Iranian architect, sculptor, painter, scholar and professor. He studied fine arts at the École nationale supérieure des Beaux-Arts in Paris, and earned a degree in architecture from University of Tehran. Seyhun is noted specially for his innovative and creative architectural design. His architectural legacy includes countless monuments and over one thousand private villas. After the Iranian Revolution he moved to Vancouver and lived in exile until his death. Seyhoon became famous for his design work in the 1950s in Iran, including: Tehran's Central Railway Station and tombs of scientific / literary figures (such as the Avicenna Mausoleum in Hamadan). He has been a faculty member of Tehran University's College of Architecture, where he also served as Dean of the College of Fine Arts (Beaux arts) of Tehran University for six years

**AV's final sentence:** **Final token "years"** ends an incomplete clause ("for six years and served as president of the association for six years"), strongly expecting continuation like "from 1960 to 1966" or "during his tenure" or "and he also served as a professor."

**Claim:** The final token is "years".

human_label: 
note: 

## 29. F29

Model 27B · document 66

**Passage:** Dollar General Corporation is an American chain of variety stores headquartered in Goodlettsville, Tennessee. As of July 2018, Dollar General operates 15,000 stores in 45 of the 48 contiguous United States (the exceptions being three states in the northwest: Idaho, Montana, and Washington). The company first began in 1939 as a family-owned business called J.L. Turner and Son in Scottsville, Kentucky by James Luther Turner and Cal Turner. In 1968, the name changed to Dollar General Corporation and the company went public on the New York Stock Exchange. Fortune 500 recognized Dollar General in 1999 and in 2018 reached # 123. Dollar General has grown to become one of the most profitable stores in the rural United States with revenue reaching around $21 billion in 2017

**AV's final sentence:** "Uber is a very successful company that is **ranked as the 10th largest technology company in the world**. It is also ranked as the 1st largest transportation company in the world. It also has a large workforce of over 10,000 employees and is a very profitable company with a revenue of around 14 billion in 2017"

**Claim:** The company is ranked as the 10th largest technology company in the world.

human_label: 
note: 

## 30. F30

Model 7B · document 0

**Passage:** The vesper sparrow (Pooecetes gramineus) is a medium-sized American sparrow. It is the only member of the genus Pooecetes. Adults have light brown upperparts and light underparts, both with darker streaking. They have a white eye ring and a long dark brown tail which shows white outer feathers in flight. Their breeding habitat is open grassy areas across most of North America. The nest is an open cup on the ground under a clump of grass. These birds migrate to the southern and central United States and Mexico. These birds forage on the ground, mainly eating insects and seeds. Outside the nesting season they often feed in small flocks. The male sings from a higher perch, such as a shrub or fencepost, which indicates his ownership of the nesting territory. The musical song begins with two pairs of repeated whistled notes and ends in a series of trills, somewhat similar to that of the song sparrow. This bird's numbers are declining in the eastern parts of its range due to habitat loss

**AV's final sentence:** Final token "loss" ends an incomplete phrase ("due to habitat loss due to habitat loss"), part of a parenthetical clause ("**decline has been slowed due to habitat loss** due to habitat loss"), strongly expecting continuation like "and other factors" or "and the disappearance of winter habitat" or "and."

**Claim:** Habitat loss has slowed the Eastern Towhee population decline.

human_label: 
note: 
