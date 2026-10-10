import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="World Population Analytics",
    page_icon="🌍",
    layout="wide"
)

DATA = Path(__file__).resolve().parent.parent / "data" / "processed" / "clean_world_population.csv"

st.markdown("""
<style>
.stApp {
    background: #0b1220;
    color: #f1f5f9;
}
[data-testid="stMetric"] {
    background: #162238;
    border: 1px solid #293b56;
    padding: 18px;
    border-radius: 14px;
}
[data-testid="stMetricLabel"] { color: #a9bbd4; }
[data-testid="stMetricValue"] { color: #ffffff; }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA)
    df.columns = [
        c.strip().lower().replace(" ", "_").replace("%", "pct")
        for c in df.columns
    ]

    # Accommodate common names used in population datasets.
    aliases = {
        "population": "population_2023",
        "pop": "population_2023",
        "yearly_change_pct": "yearly_change",
        "yearly_change_percent": "yearly_change",
        "net_change": "net_change",
        "net_migrants": "migrants",
        "net_migration": "migrants",
        "fert_rate": "fertility_rate",
        "fert_rate_": "fertility_rate",
        "fert_rate": "fertility_rate",
        "urban_population_pct": "urban_population",
        "world_share_pct": "world_share",
        "land_area_km2": "land_area",
        "density_per_km2": "density",
    }
    df = df.rename(columns={
        c: aliases[c] for c in df.columns if c in aliases
    })

    for col in df.columns:
        if col != "country":
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(",", "", regex=False)
                .str.replace("%", "", regex=False)
                .replace({"N.A.": None, "N.A": None, "nan": None, "": None}),
                errors="coerce"
            )

    if "country" not in df.columns:
        st.error("Could not find a country column in the CSV.")
        st.stop()

    df["country"] = df["country"].astype(str).str.strip()
    return df.dropna(subset=["country"])


df = load_data()

required = ["population_2023", "density", "fertility_rate",
            "median_age", "yearly_change"]
missing = [c for c in required if c not in df.columns]

if missing:
    st.error(
        f"Missing expected columns: {', '.join(missing)}. "
        f"Columns found: {', '.join(df.columns)}. "
        "Please share this message so we can adjust the column mapping."
    )
    st.stop()

st.title("🌍 World Population Analytics")
st.caption("2023 demographic insights | Interactive country-level exploration")

with st.sidebar:
    st.header("Dashboard filters")

    search = st.text_input("Search country")

    countries = sorted(df["country"].dropna().unique())
    selected = st.multiselect("Select countries", countries)

    ages = df["median_age"].dropna()
    if not ages.empty and ages.min() < ages.max():
        age_range = st.slider(
            "Median age",
            float(ages.min()),
            float(ages.max()),
            (float(ages.min()), float(ages.max()))
        )
    else:
        age_range = None

    growth = st.selectbox(
        "Population growth",
        ["All", "Growing", "Shrinking"]
    )

filtered = df.copy()

if search:
    filtered = filtered[
        filtered["country"].str.contains(search, case=False, na=False)
    ]

if selected:
    filtered = filtered[filtered["country"].isin(selected)]

if age_range:
    filtered = filtered[
        filtered["median_age"].between(*age_range)
    ]

if growth == "Growing":
    filtered = filtered[filtered["yearly_change"] > 0]
elif growth == "Shrinking":
    filtered = filtered[filtered["yearly_change"] < 0]

if filtered.empty:
    st.warning("No countries match these filters. Adjust the sidebar.")
    st.stop()


def fmt_pop(value):
    if pd.isna(value):
        return "N/A"
    value = float(value)
    if abs(value) >= 1e9:
        return f"{value / 1e9:.2f}B"
    if abs(value) >= 1e6:
        return f"{value / 1e6:.2f}M"
    if abs(value) >= 1e3:
        return f"{value / 1e3:.1f}K"
    return f"{value:,.0f}"


st.subheader("Population overview")

a, b, c, d = st.columns(4)
a.metric("Countries / territories", f"{filtered['country'].nunique():,}")
b.metric("Total population", fmt_pop(filtered["population_2023"].sum()))
c.metric("Average median age",
         f"{filtered['median_age'].mean():.1f} years")
d.metric("Average fertility rate",
         f"{filtered['fertility_rate'].mean():.2f}")

e, f, g, h = st.columns(4)
e.metric("Average population", fmt_pop(filtered["population_2023"].mean()))
f.metric("Average yearly change",
         f"{filtered['yearly_change'].mean():.2f}%")
g.metric("Shrinking countries",
         f"{(filtered['yearly_change'] < 0).sum():,}")
h.metric("Highest population", fmt_pop(filtered["population_2023"].max()))

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Top 10 most populated countries")
    top = filtered.nlargest(10, "population_2023").sort_values(
        "population_2023"
    )
    fig = px.bar(
        top, x="population_2023", y="country",
        orientation="h", color="population_2023",
        color_continuous_scale="Blues",
        template="plotly_dark",
        labels={"population_2023": "Population", "country": ""}
    )
    fig.update_layout(
        height=430, coloraxis_showscale=False,
        paper_bgcolor="#0b1220", plot_bgcolor="#0b1220"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Population share: top 10")
    top = filtered.nlargest(10, "population_2023")
    fig = px.pie(
        top, names="country", values="population_2023",
        hole=0.55, template="plotly_dark"
    )
    fig.update_layout(
        height=430, paper_bgcolor="#0b1220"
    )
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)

with left:
    st.subheader("Countries with highest growth")
    growth_data = filtered.nlargest(10, "yearly_change").sort_values(
        "yearly_change"
    )
    fig = px.bar(
        growth_data, x="yearly_change", y="country",
        orientation="h", color="yearly_change",
        color_continuous_scale="Teal",
        template="plotly_dark",
        labels={"yearly_change": "Yearly change (%)", "country": ""}
    )
    fig.update_layout(
        height=430, coloraxis_showscale=False,
        paper_bgcolor="#0b1220", plot_bgcolor="#0b1220"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Fertility vs median age")
    fig = px.scatter(
        filtered, x="median_age", y="fertility_rate",
        size="population_2023", color="yearly_change",
        hover_name="country",
        color_continuous_scale="RdYlGn",
        template="plotly_dark",
        labels={
            "median_age": "Median age",
            "fertility_rate": "Fertility rate",
            "yearly_change": "Yearly change (%)"
        }
    )
    fig.update_layout(
        height=430, paper_bgcolor="#0b1220",
        plot_bgcolor="#0b1220"
    )
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)

with left:
    st.subheader("World population map")
    fig = px.choropleth(
        filtered, locations="country",
        locationmode="country names",
        color="population_2023",
        hover_name="country",
        color_continuous_scale="Blues",
        template="plotly_dark"
    )
    fig.update_layout(
        height=480, paper_bgcolor="#0b1220",
        geo=dict(
            bgcolor="#0b1220",
            showframe=False,
            showcoastlines=True,
            showland=True,
            landcolor="#162238"
        )
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Top 10 population density")
    dense = filtered.nlargest(10, "density").sort_values("density")
    fig = px.bar(
        dense, x="density", y="country",
        orientation="h", color="density",
        color_continuous_scale="Purples",
        template="plotly_dark",
        labels={"density": "People per km²", "country": ""}
    )
    fig.update_layout(
        height=480, coloraxis_showscale=False,
        paper_bgcolor="#0b1220", plot_bgcolor="#0b1220"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Country explorer")

display = filtered.sort_values(
    "population_2023", ascending=False
)
st.dataframe(display, use_container_width=True, hide_index=True)

st.download_button(
    "Download filtered data as CSV",
    data=display.to_csv(index=False).encode("utf-8"),
    file_name="world_population_filtered.csv",
    mime="text/csv"
)

st.caption(
    "Source: supplied World Population 2023 dataset. "
    "Map coverage depends on country-name matching."
)
