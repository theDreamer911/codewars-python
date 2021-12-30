from collections import Counter
import re

def top_3_words(text):
    counts = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))

    return [w for w,_ in counts.most_common(3)]


print(top_3_words("  //wont won't won't"))