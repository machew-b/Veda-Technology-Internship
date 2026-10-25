"""Customer Segment Dashboard: Customer Segmentation & Service Recommendation System (Day 43).

Run from the repository root:

    streamlit run customer-segmentation-recommendation-system/app.py

The app reads the files saved on Day 42 in datasets/veda_customers/segments/.
All data is simulated (synthetic).
"""
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).resolve().parent.parent / "datasets" / "veda_customers" / "segments"

SEGMENTS = ["Engaged Learners", "Occasional Visitors", "New Customers", "Service-Focused Clients"]
# One fixed color per segment (the same colors as the static dashboard); the marker shape is a second cue
SEGMENT_COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#6250d6"]
SEGMENT_SCALE = alt.Scale(domain=SEGMENTS, range=SEGMENT_COLORS)
SEGMENT_SHAPES = alt.Scale(domain=SEGMENTS, range=["circle", "square", "triangle-up", "diamond"])

st.set_page_config(page_title="Customer Segment Dashboard", layout="wide")


@st.cache_data
def load_data():
    customers = pd.read_csv(DATA_DIR / "customers_segmented.csv", parse_dates=["signup_date"])
    recommendations = pd.read_csv(DATA_DIR / "service_recommendations.csv")
    profiles = pd.read_csv(DATA_DIR / "segment_profiles.csv")
    data = customers.merge(
        recommendations.drop(columns=["segment"]), on="customer_id", how="left")
    data["is_buyer"] = data["purchases"] > 0
    return data, profiles


def inr(value):
    """Format an amount in INR with a readable unit."""
    if value >= 1e6:
        return f"INR {value / 1e6:,.1f}M"
    if value >= 1e3:
        return f"INR {value / 1e3:,.1f}K"
    return f"INR {value:,.0f}"


data, profiles = load_data()
total_spend_all = data["total_spend_inr"].sum()

st.title("Customer Segment Dashboard")
st.caption("Veda Technology customers (simulated data, 5,000 customers). Segments come from K-Means "
           "clustering (Day 41); recommendations come from the rule-based logic of Day 42.")

# ---- Filters -----------------------------------------------------------------------------------
with st.sidebar:
    st.header("Filters")
    chosen_segments = st.multiselect("Segment", SEGMENTS, default=SEGMENTS)
    types = sorted(data["customer_type"].unique())
    chosen_types = st.multiselect("Customer type", types, default=types)
    channels = sorted(data["acquisition_channel"].unique())
    chosen_channels = st.multiselect("Acquisition channel", channels, default=channels)
    st.markdown("---")
    st.caption("The filters apply to every tab except the segment profiles, which always describe "
               "the full customer base.")

view = data[data["segment"].isin(chosen_segments)
            & data["customer_type"].isin(chosen_types)
            & data["acquisition_channel"].isin(chosen_channels)]

if view.empty:
    st.warning("No customers match the filters. Widen the selection in the sidebar.")
    st.stop()

# ---- KPI row -----------------------------------------------------------------------------------
survey = view["satisfaction_rating"].dropna()
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Customers", f"{len(view):,}", f"{len(view) / len(data) * 100:.0f}% of all customers", delta_color="off", delta_arrow="off")
k2.metric("Buyers", f"{view['is_buyer'].mean() * 100:.0f}%")
k3.metric("Total spending", inr(view["total_spend_inr"].sum()),
          f"{view['total_spend_inr'].sum() / total_spend_all * 100:.0f}% of all spending", delta_color="off", delta_arrow="off")
k4.metric("Median spending per customer", inr(view["total_spend_inr"].median()))
k5.metric("Satisfaction (1 to 5)", f"{survey.mean():.2f}" if len(survey) else "n/a",
          f"{len(survey) / len(view) * 100:.0f}% answered the survey", delta_color="off", delta_arrow="off")

tab_overview, tab_map, tab_profiles, tab_reco, tab_about = st.tabs(
    ["Overview", "Segment map", "Segment profiles", "Recommendations", "About"])

# ---- Overview ----------------------------------------------------------------------------------
with tab_overview:
    by_segment = view.groupby("segment").agg(
        customers=("customer_id", "count"),
        spending=("total_spend_inr", "sum"),
        buyers_pct=("is_buyer", lambda s: s.mean() * 100),
        avg_satisfaction=("satisfaction_rating", "mean"),
    ).reindex([s for s in SEGMENTS if s in chosen_segments]).reset_index()
    by_segment["share_of_customers"] = by_segment["customers"] / by_segment["customers"].sum() * 100
    by_segment["share_of_spending"] = by_segment["spending"] / by_segment["spending"].sum() * 100

    left, right = st.columns(2)
    with left:
        st.subheader("Share of customers and of spending")
        shares = by_segment.melt(id_vars="segment", value_vars=["share_of_customers", "share_of_spending"],
                                 var_name="measure", value_name="percent")
        shares["measure"] = shares["measure"].map({"share_of_customers": "Customers", "share_of_spending": "Spending"})
        st.altair_chart(
            alt.Chart(shares).mark_bar(cornerRadiusEnd=3, size=16).encode(
                y=alt.Y("segment:N", axis=alt.Axis(labelLimit=220), sort=SEGMENTS, title=None),
                yOffset=alt.YOffset("measure:N", sort=["Customers", "Spending"]),
                x=alt.X("percent:Q", title="% of the filtered customers"),
                color=alt.Color("segment:N", scale=SEGMENT_SCALE, legend=None),
                opacity=alt.Opacity("measure:N", scale=alt.Scale(domain=["Customers", "Spending"], range=[0.4, 1.0]),
                                    legend=alt.Legend(title=None, orient="bottom")),
                tooltip=["segment", "measure", alt.Tooltip("percent:Q", format=".1f")],
            ).properties(height=260), width="stretch")
        st.caption("Light bar: share of customers. Solid bar: share of total spending.")
    with right:
        st.subheader("Customers who have bought (%)")
        st.altair_chart(
            alt.Chart(by_segment).mark_bar(cornerRadiusEnd=3, size=22).encode(
                y=alt.Y("segment:N", axis=alt.Axis(labelLimit=220), sort=SEGMENTS, title=None),
                x=alt.X("buyers_pct:Q", title="% of the segment", scale=alt.Scale(domain=[0, 100])),
                color=alt.Color("segment:N", scale=SEGMENT_SCALE, legend=None),
                tooltip=["segment", alt.Tooltip("buyers_pct:Q", format=".1f", title="Buyers %"),
                         alt.Tooltip("avg_satisfaction:Q", format=".2f", title="Avg satisfaction")],
            ).properties(height=260), width="stretch")
        st.caption("Satisfaction is available only for customers who answered the survey.")

    st.subheader("Table view")
    table = by_segment.rename(columns={
        "segment": "Segment", "customers": "Customers", "spending": "Total spending (INR)",
        "buyers_pct": "Buyers (%)", "avg_satisfaction": "Avg satisfaction",
        "share_of_customers": "Share of customers (%)", "share_of_spending": "Share of spending (%)"})
    st.dataframe(table.round(1), hide_index=True, width="stretch",
                 column_config={"Customers": st.column_config.NumberColumn(format="%d"),
                                "Total spending (INR)": st.column_config.NumberColumn(format="localized")})

# ---- Segment map -------------------------------------------------------------------------------
with tab_map:
    st.subheader("Customers in 2D (PCA of the six standardized clustering features)")
    st.caption("The two axes keep 59.6% of the variance of the six features, so segments that overlap here may "
               "still be separate in the full data.")
    focus = st.selectbox("Highlight one segment", ["All segments"] + SEGMENTS)
    plot = view.copy()
    if focus != "All segments":
        plot["shown"] = plot["segment"].where(plot["segment"] == focus, "Other segments")
        color = alt.Color("shown:N", scale=alt.Scale(domain=[focus, "Other segments"],
                                                     range=[SEGMENT_COLORS[SEGMENTS.index(focus)], "#c9c8c2"]),
                          legend=alt.Legend(title=None, orient="bottom"))
        opacity = alt.condition(alt.datum.shown == "Other segments", alt.value(0.25), alt.value(0.7))
        encodings = dict(color=color, opacity=opacity)
    else:
        encodings = dict(color=alt.Color("segment:N", scale=SEGMENT_SCALE, legend=alt.Legend(title=None, orient="bottom")),
                         shape=alt.Shape("segment:N", scale=SEGMENT_SHAPES, legend=None), opacity=alt.value(0.55))
    st.altair_chart(
        alt.Chart(plot).mark_point(size=22, filled=True).encode(
            x=alt.X("pc1:Q", title="PC1 (37.0% of the variance)"),
            y=alt.Y("pc2:Q", title="PC2 (22.6% of the variance)"),
            tooltip=["customer_id", "segment", "customer_type", "primary_interest",
                     alt.Tooltip("total_spend_inr:Q", format=",.0f", title="Spending (INR)"),
                     alt.Tooltip("silhouette:Q", format=".2f")],
            **encodings,
        ).properties(height=480).interactive(), width="stretch")

# ---- Segment profiles --------------------------------------------------------------------------
with tab_profiles:
    st.subheader("Segment profiles (full customer base)")
    fingerprint = profiles.set_index("segment").loc[SEGMENTS]
    behavior_columns = {
        "avg_visits": "Website visits", "avg_session_min": "Session (min)", "avg_pages": "Pages per visit",
        "avg_email_open_pct": "Email open rate (%)", "avg_days_inactive": "Days since last activity",
        "avg_inquiries": "Service inquiries", "avg_tickets": "Support tickets", "avg_tenure_days": "Tenure (days)",
        "customers": "Customers", "buyers_pct": "Buyers (%)", "median_spend_inr": "Median spending (INR)",
        "avg_spend_inr": "Average spending (INR)", "share_of_total_spend_pct": "Share of spending (%)",
        "avg_satisfaction": "Avg satisfaction", "business_customers_pct": "Business customers (%)",
        "top_interest": "Most common interest", "top_channel": "Most common channel",
    }
    profile_table = fingerprint[list(behavior_columns)].rename(columns=behavior_columns).T
    profile_table = profile_table.apply(lambda row: [f"{v:,.1f}" if isinstance(v, float) else str(v) for v in row], axis=1,
                                        result_type="expand")
    profile_table.columns = SEGMENTS
    st.dataframe(profile_table, width="stretch")   # text cells, because each row mixes numbers and labels

    st.subheader("What each segment needs")
    needs = {
        "Engaged Learners": "The next learning step (a more advanced program or an internship), and a referral invitation when satisfied.",
        "Occasional Visitors": "A re-engagement email that features an offer relevant to their interest. Low value, so keep the cost low.",
        "New Customers": "A welcome series that introduces the primary offer and aims at the first purchase.",
        "Service-Focused Clients": "An account manager, replies within 4 hours, IT and digital services proposed together, and service recovery when tickets pile up or satisfaction is low.",
    }
    for name in SEGMENTS:
        st.markdown(f"**{name}:** {needs[name]}")

# ---- Recommendations ---------------------------------------------------------------------------
with tab_reco:
    st.subheader("Recommendations for the filtered customers")
    c1, c2 = st.columns(2)
    with c1:
        family_mix = (view.groupby(["segment", "primary_family"]).size().rename("customers").reset_index())
        family_mix["percent"] = family_mix["customers"] / family_mix.groupby("segment")["customers"].transform("sum") * 100
        heat = alt.Chart(family_mix).encode(
            x=alt.X("primary_family:N", title=None, axis=alt.Axis(labelAngle=-30, labelLimit=150, labelOverlap=False),
                    sort=["Internship Programs", "Training Programs", "IT Services", "Digital Services"]),
            y=alt.Y("segment:N", title=None, sort=SEGMENTS, axis=alt.Axis(labelLimit=220)))
        cells = heat.mark_rect().encode(
            color=alt.Color("percent:Q", title="% of segment", scale=alt.Scale(scheme="blues", domain=[0, 60], clamp=True)),
            tooltip=["segment", "primary_family", alt.Tooltip("percent:Q", format=".0f"), "customers"])
        labels = heat.mark_text(fontSize=13).encode(
            text=alt.Text("percent:Q", format=".0f"),
            color=alt.condition(alt.datum.percent > 32, alt.value("white"), alt.value("#0b0b0b")))
        st.altair_chart((cells + labels).properties(height=260, title="Primary offer family by segment (% of segment)"),
                        width="stretch")
    with c2:
        conf = view.groupby(["segment", "confidence"]).size().rename("customers").reset_index()
        conf["percent"] = conf["customers"] / conf.groupby("segment")["customers"].transform("sum") * 100
        st.altair_chart(
            alt.Chart(conf).mark_bar(cornerRadiusEnd=2).encode(
                y=alt.Y("segment:N", axis=alt.Axis(labelLimit=220), title=None, sort=SEGMENTS),
                x=alt.X("percent:Q", title="% of segment", stack="zero"),
                color=alt.Color("confidence:N", title="Confidence", sort=["High", "Medium", "Low"],
                                scale=alt.Scale(domain=["High", "Medium", "Low"], range=["#104281", "#6da7ec", "#cde2fb"])),
                order=alt.Order("confidence:N", sort="ascending"),
                tooltip=["segment", "confidence", alt.Tooltip("percent:Q", format=".0f"), "customers"],
            ).properties(height=240, title="Recommendation confidence"), width="stretch")
    st.caption("Confidence only says how clearly the customer belongs to its segment and whether the interest is known. "
               "It is not the probability that the customer accepts the offer.")

    st.subheader("Look up one customer")
    wanted = st.text_input("Customer ID", value="C00001", help="For example C00001 to C05000").strip().upper()
    match = data[data["customer_id"] == wanted]
    if match.empty:
        st.info("No customer with that ID.")
    else:
        row = match.iloc[0]
        a, b = st.columns(2)
        with a:
            st.markdown(f"**Segment:** {row['segment']}  \n**Customer type:** {row['customer_type']}  \n"
                        f"**Primary interest:** {row['primary_interest']}  \n**Channel:** {row['acquisition_channel']}  \n"
                        f"**Total spending:** INR {row['total_spend_inr']:,.0f}  \n**Support tickets:** {row['support_tickets']}")
        with b:
            st.markdown(f"**Primary offer:** {row['primary_offer']} ({row['primary_family']})  \n"
                        f"**Cross-sell offer:** {row['cross_sell_offer']} ({row['cross_sell_family']})  \n"
                        f"**Action:** {row['action']}  \n**Confidence:** {row['confidence']}  \n"
                        f"**Rules applied:** {row['rules_applied']}")
        st.caption(row["reason"])

    st.subheader("Download")
    export = view[["customer_id", "segment", "primary_family", "primary_offer", "cross_sell_family", "cross_sell_offer",
                   "action", "confidence", "rules_applied", "reason"]]
    st.download_button("Download the filtered recommendations (CSV)", export.to_csv(index=False).encode("utf-8"),
                       file_name="filtered_recommendations.csv", mime="text/csv")

# ---- About -------------------------------------------------------------------------------------
with tab_about:
    st.subheader("About this dashboard")
    st.markdown("""
- **Data:** 5,000 simulated customers (Day 40), cleaned and clustered with K-Means into four groups (Day 41),
  named and given recommendations (Day 42).
- **Segments:** the groups are partly built into the simulation, the average silhouette is only 0.29, and the
  Service-Focused Clients are the least sharply defined group, so treat the segments as a useful grouping and not as
  proof that real customers fall into exactly four types.
- **Recommendations:** rule-based. The data has no record of which offers customers accepted, so the
  recommendations cannot be scored and should be tested in real campaigns.
- **Offers inside a family** are ranked by demand because the selection, completion, and conversion rates of the offers
  do not differ significantly.
""")
