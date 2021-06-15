import re

TEXT = "Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look " \
       "about her 33.179.51.137and to wonder what was going to happen next. First, she tried to look down and make " \
       "out what she was coming to, but it was too dark to see anything; then she looked at the side153.237.67.105s " \
       "of the well, and noticed that they were filled with cu198.124.44.100boards and book-shelves; here and there " \
       "she saw maps and pictures hung upon pegs. S57.134.21.120he took down a jar from one of the shelves as she " \
       "passed; it was labelled, but to her great di169.153.58.171 disappointment it was empty: she did not like to " \
       "drop " \
       "the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it. "

IP_REGEX = r"(?:(?:25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)"

addresses = re.findall(IP_REGEX, TEXT)

print(addresses)
