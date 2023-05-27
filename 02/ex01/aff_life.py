# %%
from load_csv import load
import matplotlib.pyplot as plt


def plot_life_expectancy():
    data = load("life_expectancy_years.csv")
    country = "Germany"
    country_data = data[data['country'] == country]
    plt.plot(country_data.columns[1:].astype(int), country_data.iloc[0, 1:].values)
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(f'{country} Life expectancy Projections')
    plt.show()


if __name__ == "__main__":
    plot_life_expectancy()
# %%
