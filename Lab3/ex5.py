def validate_dict(s, d):
    for key, val in d.items():
        key_found = False
        for rule in s:
            if key == rule[0]:
                key_found = True
                if not (verify_rule(val, rule)): return False
        if not key_found: return False
    return True


def verify_rule(sentence, rule):
    pref = rule[1]
    mid = rule[2]
    suf = rule[3]
    if not (sentence.startswith(pref)): return False
    if not (sentence.endswith(suf)): return False
    if sentence[1:-2].count(mid) == 0: return False
    return True
