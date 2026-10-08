# Final-sentence examples

Documents [15, 40, 64, 65, 82] (random, seed in claims_data.py). The activation is read at the last token of the passage.
Drops are percentage points of FVE with each model's local denominator. Claims are atomic propositions; labels are Claude's.

## Document 15: Hong Kong Chinese official football team

**End of passage:** …tion, South Korean Huh Yoon-jung also received call-up. The team also one of the teams to participate in friendly match against football club that visited Hong Kong, along with Hong Kong national football team and Hong Kong League XI. The team also toured in Australia in 1953 and Asia in August 1959

**7B final sentence:** Final token "1959" ends an incomplete date range ("in September 1959 and July 1959"), strongly expecting "." or "and other tours" or "with the Singapore Football Association."

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| The final tour occurred in September 1959. | date | false | 1.06 |
| The final tour occurred in July 1959. | date | false | 1.00 |
| The final tokenizer token is “1959”. | final_token | true | 2.03 |
| The visible ending is syntactically incomplete. | local_text | false | 0.27 |

**27B final sentence:** "They also conducted international tours, notably to Korea in 1953 and across Asia in October 1959"

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| The team toured in 1953. | event | true | 10.66 |
| The 1953 tour destination was Korea. | identification | false | 0.99 |

## Document 40: James McLamore

**End of passage:** … introduce the Whopper burger in 1957, when it also dropped "Insta" from the name. The pair sold the business to Pillsbury in 1967 and McLamore served as Burger King's president until 1970, and was chairman to 1976. McLamore died of cancer in Coral Gables, Florida on August 9, 1996, at the age of 70

**7B final sentence:** Final token "70" ends an age figure ("at the age of 70... at age 70"), strongly expecting "." or "." or "and" or "in his final years," completing the death statement about his premature death.

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| The subject died at age 70. | quantity | true | 9.46 |
| The ending is an age figure. | local_text | true | -0.91 |
| The final tokenizer token is “70”. | final_token | true | 0.87 |

**27B final sentence:** "He was a prominent figure in the California legal community. He died of cancer on December 21, 1996, in Los Angeles, at the age of 70" — age 70 closes the

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| He died of cancer. | event | true | 2.95 |
| He died on December 21, 1996. | date | false | 10.85 |
| He died in Los Angeles. | attribute | false | 1.85 |
| He died at the age of 70. | quantity | true | 84.86 |
| He was a prominent figure in the California legal community. | attribute | false | 1.26 |

## Document 64: University (album)

**End of passage:** …s were disappointingly low, and the band was dropped from Sire's roster, ending the Muses' major label years. The band has continued sporadically ever since, releasing two more albums on the independent 4AD, one in 1996 and one in 2003, before releasing 2013's Purgatory / Paradise on their own label

**7B final sentence:** Final token "label" ends an incomplete noun phrase ("through his own label on his own label"), part of a concluding clause ("after retiring from his record deal he has released new material via his own independent label via his own label"), expecting "Red Ant Records" or "The Independent" or similar.

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| The text contains the phrase "his own label". | exact_words | false | 0.51 |
| The final token is "label". | final_token | true | 5.82 |
| The text ends with an incomplete noun phrase. | local_text | false | 0.64 |
| The final phrase is part of a concluding clause about later releases. | local_text | true | -0.19 |
| The text contains the sentence "after retiring from his record deal he has released new material via his own independent label via his own label". | exact_words | false | 0.48 |

**27B final sentence:** "on Merge, and finally on 2013 on their own label"

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| One of the labels named is Merge. | identification | false | 0.74 |
| Their final album was released on their own label. | attribute | true | 71.82 |

## Document 65: Barry University School of Podiatric Medicine

**End of passage:** …ation of Barry University's School of Podiatric medicine. The school has affiliations with such Miami hospitals as: Mount Sinai Medical Center & Miami Heart Institute, Mercy Hospital, DVA Miami, North Shore Medical Center and Jackson Memorial Hospital. The Dean of the school is Albert Armstrong, DPM

**7B final sentence:** Final token "DPM" ends an incomplete credential designation ("Dr. Robert J. Kirschner, DPM"), strongly expecting continuation like " , MD" or " , FACS" or " , former president," or " , a prominent podiatric surgeon," completing the honorific title.

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| The text contains the phrase "Dr. Robert J. Kirschner, DPM". | exact_words | false | 5.22 |
| The final token is "DPM". | final_token | true | 11.81 |
| The text ends with an incomplete credential designation. | local_text | false | -0.03 |

**27B final sentence:** Miller, DPM" — DPM is the podiatric medical degree abbreviation, ending mid-credential, likely followed by a period or

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| DPM is a professional/podiatric medical degree abbreviation. | attribute | true | 0.67 |

## Document 82: List of longest rivers of Canada

**End of passage:** …ow entirely within Canada. Sources report hydrological quantities with varied precision. Biologist and author Ruth Patrick, describing a table of high-discharge rivers, wrote that data on discharge, drainage area, and length varied widely among authors whose works she consulted. "It seems," she said

**7B final sentence:** Final token "said" closes a direct quote mid-sentence ("But when she said... Midgley said, she said"), immediately requiring a continuation like " " " or " "This was an inappropriate claim" or "of," completing the quoted statement about her general attitude toward ambiguity.

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| The final token is "said". | final_token | true | 23.56 |
| The final token closes a direct quote mid-sentence. | local_text | true | 27.59 |

**27B final sentence:** "A historian, Mary R. Dawson, wrote in 1976 that the records 'provide a useful basis for understanding the region's history. Consistency, she wrote, is essential. 'Consistency,' she said" — final token demands a closing quotation mark and concluding sentence fragment

| claim | subtype | Claude | drop (pp) |
|---|---|---|---|
| A historian named Mary R. Dawson is being quoted. | identity | false | -0.67 |
| This is a 1976 assessment (she wrote in 1976). | date | false | 0.32 |
| She wrote that the records "provide a useful basis for understanding the region's history." | exact_words | false | 1.57 |
