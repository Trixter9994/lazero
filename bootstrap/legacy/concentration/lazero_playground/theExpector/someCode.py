import traceback
def adding(a):
    try:
        assert type(a)==int
        return a+1
    except:
        e=traceback.format_exc()
        print(e)
        return a
