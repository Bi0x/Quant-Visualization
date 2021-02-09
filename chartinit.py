from random import randrange, randint

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Pie
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode

#! Try to use tushare


def totalIncomeChart() -> Line:
    x_data = ["2.5", "2.6", "2.7", "2.8", "2.9"]
    y_data = [820, 932, 901, 934, 1290]
    c = (
        Line()
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="总收入曲线"
            )
        )
    )
    return c


def tomorrowHoldingPredictChart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["A", "B", "C", "D", "E"])
        .add_yaxis(
            "2%",
            [randrange(0, 100) for _ in range(5)]
        )
        .add_yaxis(
            "3%",
            [randrange(0, 100) for _ in range(5)]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="持有涨跌预测",
                subtitle="预测下个交易日收盘"
            )
        )
    )
    return c


def tomorrowTrendPredictChart() -> Pie:
    tmp = randint(0, 100)
    c = (
        Pie()
        .add(
            series_name="",
            data_pair=[["上涨", tmp], ["下跌", 100 - tmp]],
            radius=80
        )
        .set_colors(["#F56C6C", "#50B71E"])
        .set_global_opts(title_opts=opts.TitleOpts(title="涨跌幅"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def tomorrowSelectedPredictChart() -> Bar:
    list2 = [
        {"value": 12, "percent": 12 / (12 + 3)},
        {"value": 23, "percent": 23 / (23 + 21)},
        {"value": 33, "percent": 33 / (33 + 5)},
        {"value": 3, "percent": 3 / (3 + 52)},
        {"value": 33, "percent": 33 / (33 + 43)},
    ]

    list3 = [
        {"value": 3, "percent": 3 / (12 + 3)},
        {"value": 21, "percent": 21 / (23 + 21)},
        {"value": 5, "percent": 5 / (33 + 5)},
        {"value": 52, "percent": 52 / (3 + 52)},
        {"value": 43, "percent": 43 / (33 + 43)},
    ]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis([1, 2, 3, 4, 5])
        .add_yaxis("2%", list2, stack="stack1", category_gap="50%")
        .add_yaxis("4%", list3, stack="stack1", category_gap="50%")
        .set_series_opts(
            label_opts=opts.LabelOpts(
                position="right",
                formatter="{c}%"
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="自选涨跌预测",
                subtitle="预测下个交易日收盘"
            )
        )
    )
    return c

def accuracyChart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["日", "周", "月", "累计"])
        .add_yaxis("准确率", [20, 30, 40, 50])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right", formatter="{c}%"))
        .set_global_opts(title_opts=opts.TitleOpts(title="累计准确率"))
    )
    return c