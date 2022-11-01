import ex5


def search_in_target_w_callback(target, to_search, callback):
    try:
        return ex5.search_in_target(target, to_search)
    except Exception as e:
        callback(e)
