
def left_join(ht1,ht2):
    output = []
    for node in ht1._buckets:
        if node != None:
            key = node.head.data[0]
            val_left  = node.head.data[1]
            if ht2.contains(key): val_right = ht2.get(key)
            else: val_right = "NULL"
            output.append([key, val_left, val_right])

    return output
