from rpy2.robjects.vectors import DataFrame
from rpy2.robjects.packages import importr, data
# this shit works like a fucking charm!
r_base = importr('base')

datasets = importr('datasets')
faithful_data = data(datasets).fetch('faithful')['faithful']

edsummary = r_base.summary(faithful_data.rx2("eruptions"))
for k, v in edsummary.items():
   print("%s: %.3f\n" %(k, v))

graphics = importr('graphics')

print("Stem-and-leaf plot of Old Faithful eruption duration data")
graphics.stem(faithful_data.rx2("eruptions"))

grdevices = importr('grDevices')
stats = importr('stats')
grdevices.png('faithful_histogram.png', width = 733, height = 550)
ed = faithful_data.rx2("eruptions")
graphics.hist(ed, r_base.seq(1.6, 5.2, 0.2),
              prob = True, col = "lightblue",
              main = "Old Faithful eruptions", xlab = "Eruption duration (seconds)")
graphics.lines(stats.density(ed,bw=0.1), col = "orange")
graphics.rug(ed)
grdevices.dev_off()

from rpy2.robjects.vectors import FloatVector

long_ed = FloatVector([x for x in ed if x > 3])
grdevices.png('faithful_ecdf.png', width = 733, height = 550)

stats = importr('stats')

params = {'do.points' : False,
          'verticals' : 1,
          'main' : "Empirical cumulative distribution function of " + \
                    "Old Faithful eruptions longer than 3 seconds"}
graphics.plot(stats.ecdf(long_ed), **params)
x = r_base.seq(3, 5.4, 0.01)
graphics.lines(x, stats.pnorm(x, mean = r_base.mean(long_ed),
                              sd = r_base.sqrt(stats.var(long_ed))),
               lty = 3, lwd = 2, col = "salmon")
grdevices.dev_off()

grdevices.png('faithful_qq.png', width = 733, height = 550)
graphics.par(pty="s")
stats.qqnorm(long_ed,col="blue")
stats.qqline(long_ed,col="red") # strangely in stats, not in graphics
grdevices.dev_off()
