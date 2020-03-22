import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import matplotlib.animation as animation


mpl.rcParams['font.sans-serif'] = ["Microsoft YaHei"]
path1 = r"https://raw.githubusercontent.com/himizi1990/Make_gif/master/Data_resource/"
path1 = path1 + "Global_Wind_Turbine_Capacity2000-2018.csv"
path2 = "D:\\python exercise\\Global_Wind_Turbine_Capacity2000-2018.csv"
path3 = "D:\\python exercise\\fj.gif"
df = pd.read_csv(path2, encoding="gb2312")


def draw_data(year):
    df1 = df.sort_values(ascending=True, by=str(year), na_position='first')
    df1[str(year)] = df1[str(year)].fillna(0)
    # print(df1[str(year)])
    ax.clear()
    ax.barh(df1.iloc[:, 0], df1[str(year)], left=1, align='center',
            color=list(colors_list[x] for x in df1.iloc[:, 0]))
    dx = df1[str(year)].mean()/100
    for i, (name, value) in enumerate(zip(df1.iloc[:, 0], df1[str(year)])):
        ax.text(x=value-dx, y=i, s=name, ha='right', va='center')
        ax.text(x=value+dx, y=i, s=str(value), ha='left', va='center')

    ax.text(0, 1.1, "Global Wind Turbine Capacity2000-2018", transform=ax.transAxes, fontsize=18, fontweight='bold')
    ax.text(0.8, 0.4, str(year), fontsize=18, transform=ax.transAxes)
    ax.xaxis.set_ticks_position('top')

    # plt.show()


fig, ax = plt.subplots(figsize=(15, 8))
colors = ["red", "#6495ED", "#808080", "#FFFACD",
          "#90EE90", "#FF00FF", "#FFA500", "#CD853F", "#FFB6C1", "#8B008B"]
colors_list = dict(zip(list(df.iloc[:, 0]), colors[:df.iloc[:, 0].count()]))
# draw_data(2012)
animator = animation.FuncAnimation(fig, draw_data, frames=range(2000, 2019, 1), interval=200)
# plt.show()
animator.save(path3, writer='imagemagick')
