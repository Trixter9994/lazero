def rkRoyal(flist,standard,indicator):
    # this is an upsign.
    for f in flist:
        if f > standard and indicator:
            return False
        else:
            pass
    return True
