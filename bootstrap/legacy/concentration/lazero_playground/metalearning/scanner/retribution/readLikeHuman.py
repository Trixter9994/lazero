import squeeze as sqeeze
#WTF?
# line next to line. then increase the step.
# when patterns are found, skip those shits.
import continuality

class Meta:
    # what about using regex to express the pattern?
    # that is way too fucking easy.
    # good for verification.
    # we need a system for this.
    # shit.
    def __init__(self, a):
        self.content, self.name= sqeeze.newLineIndex(a)
        # True for unread.
        self.hiddenContent=[True]*len(self.content)
        # print(len(self.hiddenContent))
        self.step = 1
        # may increase later.
        # may begin subsentence patten discovery which may need other function.
        self.pattern = []
        self.tags = {a0: [] for a0 in range(len(self.content))}
        # damn I don't know how to do this.
        # should be able to get shit from this.
        # custom pairs, custom slices.
        # build up from Metadata.

    def refresh(self):
        self.hiddenContent=[True for x in range(len(self.content))]
        # match the length.
        # return

    def Meta0(self):
        f = self.content
        return [sqeeze.Meta0(f0) for f0 in f]

    def eliminate(self, a):
        # a is a lambda expression
        # must collect the shit somehow.
        self.content = list(filter(a, self.content))
        self.refresh()
        # warning! hiddenContent regenerated.

    def dumpCore(self):
        return self.content

    def customReset(self, a):
        self.content = a
        self.refresh()

    def Meta1(self):
        f = self.content
        # must be used after 0 len is eliminated.
        return [sqeeze.Meta1(f0) for f0 in f]

    def Meta1v2(self):
        # is this ok? no exception?
        # we should use a matrix processor.
        # not this fuck.
        # to show up the thing more clearly.
        # shall we define a new class over this?
        # shall we export the sequence?
        f = self.Meta1()
        return sqeeze.Method2(f, f)

    def Meta0v2(self):
        f = self.Meta0()
        # find things within yourself.
        # how to do this shit?
        return sqeeze.Method2(f, f)

    def tryOnce(self):
        f = self.content
        # it may fail due to no length.
        # oh please what the fuck is this?
        return [
            sqeeze.Method2(f[a], f[a + self.step])
            for a in range(len(f) - (1 + self.step))
        ]

    def customTry(self, f):
        return [
            sqeeze.Method2(f[a], f[a + self.step])
            for a in range(len(f) - (1 + self.step))
        ]

    def setStep(self, a):
        self.step = a

    def getCustomLines(self, a, c=False):
        # c -> incongito mode
        r=[]
        for b in a:
            if self.hiddenContent[b]:
                r.append(self.content[b])
                if not c:
                    self.hiddenContent[b]=False
            else:
                pass
        return r

    def getFractalRange(self):
        return continuality.moveOn(self.hiddenContent,1,0)[0]

    def extractUnread(self,a=False):
        # standard choice is destructive?
        s=self.getFractalRange()
        # hidden slicing.
        # one article -> multiple articles.
        if a:
            return [self.content[x[0]:x[1]+1] for x in s]
        else:
            return [self.getCustomLines(list(range(x[0],x[1]+1)),a) for x in s]
        # chained reader needed.
        # use Bayes Classifier to do this job instead?
    # pop those shits, or simply mark them?

# how to automatically select the range?