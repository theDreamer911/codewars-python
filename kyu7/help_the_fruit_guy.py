import re


def remove_rotten(bag_of_fruits):
    answer = []
    try:
        for text in bag_of_fruits:
            change = re.sub(r'rotten', '', text).lower()
            answer.append(change)
        return answer
    except:
        return answer


# Best
def remove_rotten(bag_of_fruits):
    return [x.replace('rotten', '').lower() for x in bag_of_fruits] if bag_of_fruits else []
