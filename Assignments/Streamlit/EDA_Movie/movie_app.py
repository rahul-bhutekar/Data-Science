import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecs

from ydata_profiling import ProfileReport
import sweetviz as sv

from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components


with st.sidebar:
    with st.header('# EDA for Movie dataset'):
        st.markdown('# :mag: EDA for Movie dataset')
        
    with st.sidebar.header('Show Code'):
        add_radio = st.radio(
            "Show Code for this EDA at the bottom of the page?",
            ("Yes", "No")
        )

st.title('Movie EDA Streamlit :movie_camera::sunglasses:')
st.divider()


st.markdown('#### :red[:hash: read file using *read_csv* function: ] :orange[pd.read_csv(), head()] ')
df = pd.read_csv('../dataset/Movie.csv')
st.table(df.head())


st.markdown('#### :red[:hash: summary statistics for numeric data types: ] :orange[df.describe()] ')
st.table(df.describe())


st.markdown('#### :red[:hash: data type of each column: ] :orange[df.dtypes] ')
st.table(df.dtypes)


st.markdown('#### :red[:hash: summary of the data: *column names, total no.of non-null values, data types, memory usage*: ] :orange[df.info()] ')
st.write(df.info())


st.markdown('#### :red[:hash: number of rows and columns: ] :orange[df.shape] ')
st.write(df.shape)

st.markdown('#### :red[:hash: count of duplicate rows: ] :orange[df.duplicated()] ')
st.write(df[df.duplicated()].shape)



st.header('Outlier detection :smiley:', divider='rainbow')

import plotly.express as px

st.header('_Bar graph - Movies :movie_camera:_')
fig_movie = px.bar(df['movie'])
st.plotly_chart(fig_movie, use_container_width=True)


st.header('_Bar graph - Rating :star:_')
fig_rating, ax = plt.subplots()
ax.hist(df['rating'], bins=20)
st.pyplot(fig_rating)

# using other varibale as dataframe
data = df
data_box = data.dropna()

st.header('_Box Plot - Movie:movie_camera:_')
fig_box_movie = px.box(df, y="movie", notched=True, points="all")
st.plotly_chart(fig_box_movie, use_container_width=True)


st.header('_Box Plot - Rating:star:_')
fig_box_rating = px.box(df, y="rating", notched=True)
st.plotly_chart(fig_box_rating)


st.header('_Heatmap1 :fire:_')
import seaborn as sns
cols = data.columns
colors = ['#000099', '#ffff00']
fig, ax = plt.subplots()
sns.heatmap(data[cols].isnull(), cmap=sns.color_palette(colors), ax=ax)
st.write(fig)


st.header('_Heatmap2 :fire:_')
fig_heatmap = px.imshow(df)
st.plotly_chart(fig_heatmap)


st.header('_Scatter Plot :star2:_')
fig_scatterPlot = px.scatter(df, x='userId', y='rating', color='movie')
st.plotly_chart(fig_scatterPlot, use_container_width=True)

# generating dummy values for 'movie' column
st.header('_Correlation :white_circle:_')
data_cleaned = pd.get_dummies(data, columns=['movie'])
st.write(data_cleaned.corr())


st.header('_EDA with libraries 	:v:_')
st.divider()


st.markdown('### EDA using library: *ydata_profiling*')
report = ProfileReport(df, title="Movie EDA Report")
st_profile_report(report)

st.markdown('### EDA using library: *sweetviz*')

def st_sweetviz_displayHTML(html_page):
    report_file = codecs.open(html_page, 'r')
    page = report_file.read()
    components.html(page, width=700, height=500, scrolling=True)

sweet_report = sv.analyze(df)
sweet_report.show_html(filepath='./eda-movies-sweetviz-report.html', open_browser=False, layout='vertical', scale=1.0)
st_sweetviz_displayHTML('./eda-movies-sweetviz-report.html')

if add_radio == 'Yes':
    code = '''
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import codecs

    from ydata_profiling import ProfileReport
    import sweetviz as sv

    from streamlit_pandas_profiling import st_profile_report
    import streamlit.components.v1 as components


    with st.sidebar:
        with st.header('# EDA for Movie dataset'):
            st.markdown('# EDA for Movie dataset')
            
        with st.sidebar.header('Show Code'):
            add_radio = st.radio(
                "Show Code for this EDA at the bottom of the page?",
                ("Yes", "No")
            )

    st.title('Movie EDA Streamlit :movie_camera::sunglasses:')
    st.divider()


    st.markdown('#### :red[:hash: read file using *read_csv* function: ] :orange[pd.read_csv(), head()] ')
    df = pd.read_csv('../dataset/Movie.csv')
    st.table(df.head())


    st.markdown('#### :red[:hash: summary statistics for numeric data types: ] :orange[df.describe()] ')
    st.table(df.describe())


    st.markdown('#### :red[:hash: data type of each column: ] :orange[df.dtypes] ')
    st.table(df.dtypes)


    st.markdown('#### :red[:hash: summary of the data: *column names, total no.of non-null values, data types, memory usage*: ] :orange[df.info()] ')
    st.write(df.info())


    st.markdown('#### :red[:hash: number of rows and columns: ] :orange[df.shape] ')
    st.write(df.shape)

    st.markdown('#### :red[:hash: count of duplicate rows: ] :orange[df.duplicated()] ')
    st.write(df[df.duplicated()].shape)


    import plotly.express as px

    st.header('Outlier detection :smiley:', divider='rainbow')
    st.header('_Bar graph_')


    st.markdown('#### :red[:movie_camera: Movies] ')
    fig_movie = px.bar(df['movie'])
    st.plotly_chart(fig_movie, use_container_width=True)

    st.markdown('#### :red[:star: Rating] ')
    fig_rating, ax = plt.subplots()
    ax.hist(df['rating'], bins=20)
    st.pyplot(fig_rating)

    # using other varibale as dataframe
    data = df
    data_box = data.dropna()

    st.markdown('#### :red[ Box Plot - Movie:movie_camera:] ')
    fig_box_movie = px.box(df, y="movie", notched=True, points="all")
    st.plotly_chart(fig_box_movie, use_container_width=True)

    st.markdown('#### :red[Box Plot - Rating:star:] ')
    fig_box_rating = px.box(df, y="rating", notched=True)
    st.plotly_chart(fig_box_rating)


    st.markdown('#### :red[Heatmap :fire:] ')
    import seaborn as sns
    cols = data.columns
    colors = ['#000099', '#ffff00']
    fig, ax = plt.subplots()
    sns.heatmap(data[cols].isnull(), cmap=sns.color_palette(colors), ax=ax)
    st.write(fig)

    st.markdown('#### :red[Scatter Plot :star2:] ')
    fig_scatterPlot = px.scatter(df, x='userId', y='rating', color='movie')
    st.plotly_chart(fig_scatterPlot, use_container_width=True)


    st.markdown('## EDA with libraries 	:v:')
    st.divider()


    st.markdown('### EDA using library: *ydata_profiling*')
    report = ProfileReport(df, title="Movie EDA Report")
    st_profile_report(report)

    st.markdown('### EDA using library: *sweetviz*')

    def st_sweetviz_displayHTML(html_page):
        report_file = codecs.open(html_page, 'r')
        page = report_file.read()
        components.html(page, width=700, height=500, scrolling=True)

    sweet_report = sv.analyze(df)
    sweet_report.show_html(filepath='./eda-movies-sweetviz-report.html', open_browser=False, layout='vertical', scale=1.0)
    st_sweetviz_displayHTML('./eda-movies-sweetviz-report.html')
    '''
    st.markdown('# Code')
    st.code(code, language='python')

