# %%
from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def plot_population():
    data = load("population_total.csv")
    countries = ["Belgium", "France"]
    # formatter = plt.ticker.ScalarFormatter()
    test = data[data['country'].isin(countries)]
    test_trimmed = test.loc["1800":"2050"]
    countries_val = []
    print("Trim", test_trimmed.values.shape)
    print("Trim", test_trimmed.values.squeeze())
    for country in test_trimmed.values:
        print("hello")
        countries_val.append([value[:-1] for value in country[1:]])
    years = test_trimmed.columns[1:]
    # print(test_trimmed.columns[1:])
    print(f"Shape 1 {years.shape}")
    print(countries_val)
    print(f"Shape 2 {np.asarray(countries_val).shape}")
    # plt.plot(years, countries_val)
    # for country in countries:
    #     country_data = data[data['country'] == country]
    #     # country_data.tr``
    #     values = country_data.loc[:, "1800":"2050"].values[0]
    #     trimmed_vals = [value[:-1] for value in values]
    #     # values = np.char.strip(values, 'M')
    #     # print(trimmed_vals)
    #     # values = np.char.strip(values, ("M",))
    #     # values = values.apply(lambda x: x.str.slice(0, -1))
    #     # print(values)
    #     # print(country_data.loc[:, "1800":"2050"].columns.to_numpy())
    #     plt.plot(country_data.loc[:, "1800":"2050"].columns, trimmed_vals)
        # break
    # plt.ticklabel_format(axis='x', useOffset=40.0)
    # if data.values.max() > 2000000:
    #     plt.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    # else:
    #     plt.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    plot_population()
# %%
