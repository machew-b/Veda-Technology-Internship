"""Future Demand Dashboard: Sales & Service Demand Forecasting System (Day 48).

Run from the repository root or from this folder:

    streamlit run day-48/app.py

The app reads the files saved on Days 45 to 48 in datasets/veda_demand/.
All data is simulated (synthetic).
"""
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).resolve().parent.parent / "datasets" / "veda_demand"

LINES = ["Internship Programs", "Training Programs", "IT Services", "Digital Services"]
LINE_COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
LINE_SCALE = alt.Scale(domain=LINES, range=LINE_COLORS)
FORECAST_COLOR = "#6250d6"
INK, INK_SOFT = "#0b0b0b", "#52514e"
PLANS = ["No campaigns", "Typical campaign load", "Campaigns +50%"]

st.set_page_config(page_title="Future Demand Dashboard", layout="wide")


@st.cache_data
def load_data():
    weekly = pd.read_csv(DATA_DIR / "cleaned" / "demand_weekly.csv", parse_dates=["week_start"])
    future = pd.read_csv(DATA_DIR / "forecasts" / "future_demand_forecast_weekly.csv", parse_dates=["week_start"])
    scenarios = pd.read_csv(DATA_DIR / "forecasts" / "campaign_scenarios_weekly.csv", parse_dates=["week_start"])
    metrics = pd.read_csv(DATA_DIR / "forecasts" / "model_metrics.csv")
    monitor = pd.read_csv(DATA_DIR / "forecasts" / "forecast_monitor_weekly.csv", parse_dates=["week_start"])
    return weekly, future, scenarios, metrics, monitor


weekly, future, scenarios, metrics, monitor = load_data()
WEEK = pd.Timedelta(weeks=1)
future_weeks = sorted(future["week_start"].unique())
history_end = weekly["week_start"].max()

# Revenue per unit of each line over the last 52 weeks, and the same 26 weeks one year earlier
last_52 = weekly[weekly["week_start"] > history_end - 52 * WEEK].groupby("service_line")[["demand_units", "revenue_inr"]].sum()
revenue_per_unit = last_52["revenue_inr"] / last_52["demand_units"]
year_earlier = weekly[weekly["week_start"].isin(pd.DatetimeIndex(future_weeks) - 52 * WEEK)].groupby("service_line")[["demand_units", "revenue_inr"]].sum()


def inr(value):
    """Format an amount in INR with a readable unit."""
    if abs(value) >= 1e6:
        return f"INR {value / 1e6:,.1f}M"
    if abs(value) >= 1e3:
        return f"INR {value / 1e3:,.1f}K"
    return f"INR {value:,.0f}"


st.title("Future Demand Dashboard")
st.caption("Veda Technology service demand (simulated data). Forecast of the next 26 weeks "
           f"({pd.Timestamp(future_weeks[0]).date()} to {pd.Timestamp(future_weeks[-1]).date()}) from the Poisson regression selected on Day 47, "
           "with a level correction. Ranges are about 80%.")

# ---- Filters -----------------------------------------------------------------------------------
with st.sidebar:
    st.header("Settings")
    chosen = st.multiselect("Service lines", LINES, default=LINES)
    plan = st.radio("Campaign plan", PLANS, index=1,
                    help="The forecast assumes a campaign plan. 'Typical' is the average campaign load of the last 52 weeks.")
    show_range = st.checkbox("Show the 80% range", value=True)
    show_uncorrected = st.checkbox("Show the forecast without the level correction", value=False)
    history_weeks = st.slider("Weeks of history to show", 13, 104, 39)
    st.markdown("---")
    st.caption("The settings apply to every tab, except that the accuracy tab always shows the test weeks of Day 47.")

if not chosen:
    st.warning("Choose at least one service line in the sidebar.")
    st.stop()

# The forecast of the chosen plan; the range is scaled by the same factor as the forecast
typical = scenarios[scenarios["plan"] == "Typical campaign load"][["week_start", "service_line", "forecast_units"]].rename(columns={"forecast_units": "typical"})
picked = scenarios[scenarios["plan"] == plan][["week_start", "service_line", "forecast_units"]]
view = future.merge(picked, on=["week_start", "service_line"]).merge(typical, on=["week_start", "service_line"])
factor = view["forecast_units"] / view["typical"]
view["forecast_plan"] = view["forecast_units"]
view["range_low_plan"] = view["range_low"] * factor
view["range_high_plan"] = view["range_high"] * factor
view["uncorrected_plan"] = view["model_forecast"] * factor
view = view[view["service_line"].isin(chosen)]

# ---- KPI row -----------------------------------------------------------------------------------
units = view["forecast_plan"].sum()
earlier_units = year_earlier.loc[chosen, "demand_units"].sum()
revenue = sum(view[view["service_line"] == line]["forecast_plan"].sum() * revenue_per_unit[line] for line in chosen)
earlier_revenue = year_earlier.loc[chosen, "revenue_inr"].sum()
low, high = view["range_low_plan"].sum(), view["range_high_plan"].sum()
k1, k2, k3, k4 = st.columns(4)
k1.metric("Forecast units, next 26 weeks", f"{units:,.0f}", f"{(units / earlier_units - 1) * 100:+.1f}% vs the same weeks a year earlier", delta_color="off")
k2.metric("Forecast revenue", inr(revenue), f"{(revenue / earlier_revenue - 1) * 100:+.1f}% vs a year earlier", delta_color="off")
k3.metric("Busiest week", f"{view.groupby('week_start')['forecast_plan'].sum().max():,.0f} units",
          f"week of {view.groupby('week_start')['forecast_plan'].sum().idxmax().date()}", delta_color="off", delta_arrow="off")
k4.metric("Sum of the weekly ranges", f"{low:,.0f} to {high:,.0f}", "a rough upper bound on the range of the total", delta_color="off", delta_arrow="off")

tab_forecast, tab_plan, tab_accuracy, tab_monitor, tab_about = st.tabs(
    ["Forecast", "Monthly plan", "Accuracy", "Why trends fail", "About"])

# ---- Forecast ----------------------------------------------------------------------------------
with tab_forecast:
    st.subheader("Weekly forecast with its range")
    history = weekly[weekly["service_line"].isin(chosen) & (weekly["week_start"] > history_end - history_weeks * WEEK)]
    columns = st.columns(2)
    for position, line in enumerate(chosen):
        h, v = history[history["service_line"] == line], view[view["service_line"] == line]
        parts = [alt.Chart(h).mark_line(color=INK, strokeWidth=1.6).encode(
            x=alt.X("week_start:T", title=None), y=alt.Y("demand_units:Q", title="Units per week"),
            tooltip=["week_start:T", alt.Tooltip("demand_units:Q", title="Actual")])]
        if show_range:
            parts.append(alt.Chart(v).mark_area(color=FORECAST_COLOR, opacity=0.15).encode(x="week_start:T", y="range_low_plan:Q", y2="range_high_plan:Q"))
        if show_uncorrected:
            parts.append(alt.Chart(v).mark_line(color=FORECAST_COLOR, strokeWidth=1.2, strokeDash=[4, 3]).encode(x="week_start:T", y="uncorrected_plan:Q"))
        parts.append(alt.Chart(v).mark_line(color=FORECAST_COLOR, strokeWidth=2.4).encode(
            x="week_start:T", y="forecast_plan:Q",
            tooltip=["week_start:T", alt.Tooltip("forecast_plan:Q", format=".1f", title="Forecast"),
                     alt.Tooltip("range_low_plan:Q", format=".1f", title="Range low"), alt.Tooltip("range_high_plan:Q", format=".1f", title="Range high")]))
        with columns[position % 2]:
            st.markdown(f"**{line}**")
            st.altair_chart(alt.layer(*parts).properties(height=240), width="stretch")
    st.caption(f"Black: actual demand. Purple: forecast under the plan '{plan}'. Shaded: range of about 80% (scaled with the plan). "
               "A range describes ordinary randomness; it cannot cover a change in the pattern.")

    st.subheader("Units, revenue, and change against a year earlier")
    table = view.groupby("service_line").agg(forecast_units=("forecast_plan", "sum"), range_low=("range_low_plan", "sum"), range_high=("range_high_plan", "sum")).reindex(chosen)
    table["units_year_earlier"] = year_earlier["demand_units"].reindex(chosen)
    table["change_pct"] = (table["forecast_units"] / table["units_year_earlier"] - 1) * 100
    table["forecast_revenue_INR_M"] = table["forecast_units"] * revenue_per_unit.reindex(chosen) / 1e6
    table["revenue_year_earlier_INR_M"] = year_earlier["revenue_inr"].reindex(chosen) / 1e6
    st.dataframe(table.round(1).rename(columns={
        "forecast_units": "Forecast units", "range_low": "Sum of weekly range, low", "range_high": "Sum of weekly range, high",
        "units_year_earlier": "Units a year earlier", "change_pct": "Change (%)", "forecast_revenue_INR_M": "Forecast revenue (INR M)",
        "revenue_year_earlier_INR_M": "Revenue a year earlier (INR M)"}), width="stretch")

# ---- Monthly plan ------------------------------------------------------------------------------
with tab_plan:
    st.subheader("Units per week by plan month")
    plan_view = view.copy()
    plan_view["plan_month"] = (plan_view["week_start"] + pd.Timedelta(days=3)).dt.to_period("M").astype(str)
    monthly = plan_view.pivot_table(index="plan_month", columns="service_line", values="forecast_plan", aggfunc="sum")[chosen]
    weeks = plan_view[plan_view["service_line"] == chosen[0]].groupby("plan_month").size()
    per_week = monthly.div(weeks, axis=0)
    long = per_week.reset_index().melt(id_vars="plan_month", var_name="service_line", value_name="units_per_week")
    long["relative"] = long["units_per_week"] / long.groupby("service_line")["units_per_week"].transform("mean")
    heat = alt.Chart(long).mark_rect().encode(
        x=alt.X("service_line:N", sort=chosen, title=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y("plan_month:O", title=None),
        color=alt.Color("relative:Q", scale=alt.Scale(scheme="blues", domain=[0.4, 1.7]), legend=None),
        tooltip=["plan_month", "service_line", alt.Tooltip("units_per_week:Q", format=".1f")])
    text = alt.Chart(long).mark_text(fontSize=13).encode(
        x=alt.X("service_line:N", sort=chosen), y="plan_month:O", text=alt.Text("units_per_week:Q", format=".1f"),
        color=alt.condition(alt.datum.relative > 1.25, alt.value("white"), alt.value(INK)))
    st.altair_chart((heat + text).properties(height=320), width="stretch")
    st.caption("Plan month = the month of the Thursday of each week, so every one of the 26 weeks belongs to one month and months have 4 or 5 weeks. "
               "Units are per week, so months can be compared. Darker = busier than the line's own average.")
    summary = monthly.copy()
    summary["All chosen lines"] = summary.sum(axis=1)
    summary["Weeks"] = weeks
    st.dataframe(summary.round(0).astype(int), width="stretch")

    st.subheader("The three busiest weeks of each line")
    peaks = (view.sort_values("forecast_plan", ascending=False).groupby("service_line").head(3)
             .sort_values(["service_line", "forecast_plan"], ascending=[True, False])[["service_line", "week_start", "forecast_plan", "range_high_plan"]])
    peaks["week_start"] = peaks["week_start"].dt.date
    st.dataframe(peaks.rename(columns={"service_line": "Line", "week_start": "Week starting", "forecast_plan": "Forecast units",
                                       "range_high_plan": "Top of the range (capacity to plan for)"}).round(1), hide_index=True, width="stretch")

    st.subheader("What is the campaign plan worth?")
    plan_table = scenarios[scenarios["service_line"].isin(chosen)].pivot_table(index="service_line", columns="plan", values="forecast_units", aggfunc="sum").reindex(chosen)[PLANS]
    plan_table["Typical campaigns add (units)"] = plan_table["Typical campaign load"] - plan_table["No campaigns"]
    plan_table["Typical campaigns add (INR M)"] = plan_table["Typical campaigns add (units)"] * revenue_per_unit.reindex(chosen) / 1e6
    st.dataframe(plan_table.round(1), width="stretch")
    st.caption("A scenario, not a prediction: the model assumes each extra campaign day adds the same percentage, and campaign costs are not in the data.")

# ---- Accuracy ----------------------------------------------------------------------------------
with tab_accuracy:
    st.subheader("How accurate were the methods on the 26 test weeks of Day 47?")
    scope = st.selectbox("Scope", ["All lines"] + LINES)
    shown = metrics[metrics["service_line"] == scope].copy()
    order = shown.sort_values("WAPE_pct")["method"].tolist()
    st.altair_chart(
        alt.Chart(shown).mark_bar(cornerRadiusEnd=3, size=22).encode(
            y=alt.Y("method:N", sort=order, title=None, axis=alt.Axis(labelLimit=260)),
            x=alt.X("WAPE_pct:Q", title="WAPE (%), lower is better"),
            color=alt.Color("method:N", legend=None, scale=alt.Scale(domain=order, range=["#6250d6", "#008300", "#e87ba4", "#52514e", "#9aa3b2"][:len(order)])),
            tooltip=["method", alt.Tooltip("WAPE_pct:Q", format=".1f"), alt.Tooltip("bias_pct:Q", format=".1f", title="Bias %"), alt.Tooltip("MAE:Q", format=".1f")],
        ).properties(height=240), width="stretch")
    st.dataframe(shown.set_index("method").loc[order][["MAE", "WAPE_pct", "bias_pct"]].rename(
        columns={"WAPE_pct": "WAPE (%)", "bias_pct": "Bias (%)"}).round(1), width="stretch")
    st.caption("WAPE is the total absolute miss over the total demand. Bias above 0 means the forecast was too high. "
               "'All lines' scores the weekly total, where errors of different lines can cancel; the lines are scored one by one.")

# ---- Why trends fail ---------------------------------------------------------------------------
with tab_monitor:
    st.subheader("Is the forecast still on track?")
    st.write("The **8-week ratio** is the actual demand of the last 8 weeks divided by the forecast for the same weeks, minus 1. "
             "The weeks below are the test weeks of Day 47. After June 1 the demand of Digital Services lifted and that of IT Services slowed down, "
             "which a model fitted on the earlier weeks could not know.")
    band = st.slider("Alert band (+/- %)", 10, 40, 20)
    mon = monitor[monitor["service_line"].isin(chosen)].copy()
    mon["outside"] = mon["ratio_8wk_pct"].abs() > band
    rule = alt.Chart(pd.DataFrame({"y": [-band, band]})).mark_rule(color="#9aa3b2", strokeDash=[4, 3]).encode(y="y:Q")
    lines = alt.Chart(mon.dropna(subset=["ratio_8wk_pct"])).mark_line(strokeWidth=2.2).encode(
        x=alt.X("week_start:T", title=None), y=alt.Y("ratio_8wk_pct:Q", title="8-week actual vs forecast (%)"),
        color=alt.Color("service_line:N", scale=LINE_SCALE, legend=alt.Legend(title=None, orient="bottom")),
        tooltip=["week_start:T", "service_line", alt.Tooltip("ratio_8wk_pct:Q", format=".1f")])
    points = alt.Chart(mon[mon["outside"]]).mark_point(filled=True, size=45).encode(
        x="week_start:T", y="ratio_8wk_pct:Q", color=alt.Color("service_line:N", scale=LINE_SCALE, legend=None))
    st.altair_chart((rule + lines + points).properties(height=360), width="stretch")
    first_flag = mon[mon["outside"]].groupby("service_line")["week_start"].min().dt.strftime("%Y-%m-%d")
    flags = first_flag.reindex(chosen).fillna("no flag").rename("First week outside the band")
    st.dataframe(flags.to_frame(), width="stretch")
    st.caption("A band that is too narrow raises false alarms in stable lines; a band that is too wide notices a change late. "
               "On Day 48 the band of 20% was set after seeing these lines, so it needs calibrating on more history.")

    st.subheader("Cumulative miss since March 30, 2026 (actual minus forecast, units)")
    st.altair_chart(
        alt.Chart(mon).mark_line(strokeWidth=2.2).encode(
            x=alt.X("week_start:T", title=None), y=alt.Y("cumulative_gap_units:Q", title="Units"),
            color=alt.Color("service_line:N", scale=LINE_SCALE, legend=None),
            tooltip=["week_start:T", "service_line", alt.Tooltip("cumulative_gap_units:Q", format=".0f")]).properties(height=280), width="stretch")

# ---- About -------------------------------------------------------------------------------------
with tab_about:
    st.subheader("What this dashboard is")
    st.markdown(
        "- **Data:** simulated weekly demand of four service lines (October 2023 to September 2026), cleaned on Day 45.\n"
        "- **Model:** a Poisson regression per line (trend, yearly season, campaign days, holidays), selected on a validation period on Day 47, "
        "scored once on 26 test weeks (WAPE 7.2% on the weekly total), with a level correction (the ratio of the actual to the fitted demand over the last 13 weeks).\n"
        "- **Assumptions:** campaigns run at the typical load of the last 52 weeks unless another plan is chosen; holidays follow the fixed calendar; revenue is units times the revenue per unit of the last 52 weeks.\n"
        "- **Limits:** the pattern of the history may not continue (it did not for two lines after June 1), the ranges cover ordinary randomness only, "
        "and the data is simulated, so the numbers show the workflow and not the real company.")
