import sma_crossover
from mooquant import plotter
# from mooquant.tools import yahoofinance
from mooquant.analyzer import sharpe
from mooquant.tools import quandl

def main(plot):
    instrument = "AAPL"
    smaPeriod = 163

    # Download the bars.
    # feed = yahoofinance.build_feed([instrument], 2011, 2012, ".")
    feed = quandl.build_feed('WIKI',[instrument], 2011, 2012, ".")

    strat = sma_crossover.SMACrossOver(feed, instrument, smaPeriod)
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    strat.attachAnalyzer(sharpeRatioAnalyzer)

    if plot:
        plt = plotter.StrategyPlotter(strat, True, False, True)
        plt.getInstrumentSubplot(instrument).addDataSeries("sma", strat.getSMA())

    strat.run()
    print("Sharpe ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05))

    if plot:
        plt.plot()


if __name__ == "__main__":
    main(True)