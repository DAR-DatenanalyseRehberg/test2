import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

st.set_page_config(page_title="meine erste streamlit app", layout="wide")

# streamlit run mein_dashboard.py

st.write("Wir bauen unsere erste Streamlit App")

st.title("Das ist die Überschrift FEHLER")


st.title("This is the app **title**")        # groesste Ueberschrift (Seitentitel)
st.header("This is the header")          # Abschnitts-Ueberschrift
st.markdown("This is **the** markdown")      # Text mit Markdown-Formatierung (**fett**, *kursiv*, ...)
st.subheader("This is the subheader")    # kleinere Unter-Ueberschrift
st.caption("This is the caption")        # kleiner, grauer Hinweistext
st.code("x = 2021")                      # Code-Block mit Syntax-Hervorhebung
st.latex(r''' a+a r^1+a r^2+a r^3 ''')   # mathematische Formel (LaTeX)


st.checkbox("Ja")
st.button("Klick Mich")
st.radio("Wähle das Geschlecht", ["Weiblich", "Männlich"])

st.progress(100)



st.success("Hurra fertig")

st.success("You did it!")                          # gruen: Erfolg
st.error("Error occurred")                         # rot: Fehler
st.warning("This is a warning")                    # gelb: Warnung
st.info("It's easy to build a Streamlit app")      # blau: Info-Hinweis
st.exception(RuntimeError("RuntimeError exception"))  # zeigt eine Exception formatiert an


st.sidebar.title("Sidebar Titel")
st.sidebar.markdown("HIer kommt der INhalt der Sidebar test")


rand = np.random.normal(1,2,size=20)
fig, ax =plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)   # Liniendiagramm

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)    # Balkendiagramm

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)   # Flaechendiagramm

# --- Altair-Diagramm (interaktiv, anpassbar) ----------------
# Altair ist deklarativ: man beschreibt, welche Spalte auf welche
# "Encoding" (x, y, Groesse, Farbe, Tooltip) abgebildet wird.
df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df).mark_circle().encode(
    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(chart, use_container_width=True)  # nutzt die volle Breite


df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)