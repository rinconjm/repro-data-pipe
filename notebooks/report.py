import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    return mo, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Final Report
    """)
    return


@app.cell(hide_code=True)
def _(pd):
    df = pd.read_csv('data/features/events.csv')
    return (df,)


@app.cell
def _(df, plt, sns):
    sns.histplot(df, x="duration_minutes")
    plt.title("Distribution of Duration Minutes")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
