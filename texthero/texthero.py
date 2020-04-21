from . import preprocessing
from . import representation
from . import visualization

def do_preprocess(df, text_columns='text', pipeline=None):
    return preprocessing.do_preprocess(df,text_columns, pipeline)

def do_tfidf(df, text_columns='text', max_features=100):
    return representation.do_tfidf(df, text_columns=text_columns, max_features=max_features)

def do_pca(df, vector_columns='tfidf_text', n_components=2):
    return representation.do_pca(df, vector_columns, n_components)

def do_nmf(df, vector_columns='tfidf_text', n_components=2):
    return representation.do_nmf(df, vector_columns, n_components)

def scatterplot(df, column, color=None, hover_data=['text']):
    return visualization.scatterplot(df, column, color, hover_data)