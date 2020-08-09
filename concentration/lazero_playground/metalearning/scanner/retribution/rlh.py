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
        self.content = sqeeze.newLineIndex(a)
        self.hiddenContent=[False for x in range(len(self.content))]
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
        self.hiddenContent=[False for x in range(len(self.content))]
        # return

    def Meta0(self):
        f = self.content
        return [sqeeze.Meta0(f0) for f0 in f]

    def eliminate(self, a):
        # a is a lambda expression
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

    def getCustomLines(self, a):
        r=[]
        for b in a:
            if self.hiddenContent[b]==False:
                r.append(self.content[b])
                self.hiddenContent[b]=True
            else:
                pass
        return r
        # chained reader needed.
        # use Bayes Classifier to do this job instead?
    # pop those shits, or simply mark them?