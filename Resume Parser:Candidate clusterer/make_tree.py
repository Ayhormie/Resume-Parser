import pandas as pd
import umap.umap_ as umap
import pickle 
import boto3
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial import KDTree


def get_umap(data, c=None, n_neighbors=4, min_dist=0.2, n_components=2, metric='cosine'):
    """
    Params:
        # data: one hot encoded ndarray for all words in word_vectorizer
    
    Returns:
        # u: numpy ndarray containing x,y values of datapoints
    """
    fit = umap.UMAP(
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        n_components=n_components,
        metric=metric,
        )
    u = fit.fit_transform(data)
    return u


def makeTree(arr_of_points):
    """
    Params:
        # arr_of_points: ndarray coitaining x,y values for points in our model

    Returns:
        # tree: KDTree obj representation of array of datapoints
    """
    tree = KDTree(arr_of_points)
    return tree


def saveTree(tree, points_df):
    """
    Params:
        # tree: KDTree object

        # points_df: Dataframe representation of points and their corresponding IDs
    """
    # TODO: replace with call to DB
    with open(r"tree.pickle", "wb") as output_file:
        pickle.dump(tree, output_file)
    with open(r"df.pickle", "wb") as output_file2:
        pickle.dump(points_df, output_file2)

    # bucket = 'your_bucket_name'
    # tree_key = 'your_pickled_tree_filename.pkl'
    # df_key = 'your_pickled_df_filename.pkl'
    # pickled_tree = pickle.dump(tree)
    # pickled_df = pickle.dump(points_df)
    
    # s3_resource = boto3.resource('s3')
    # s3_resource.Object(bucket, tree_key).put(Body=pickled_tree)
    # s3_resource.Object(bucket, df_key).put(Body=pickled_df)
    




def createTree(resume_arr, ID_list):
    """
    Params:
      # resume_arr: array containing cleaned & parsed resume data pulled from DB

      #ID_list: array containing resume_arr's corresponding ID #'s from DB
    """

    # create word vector
    word_vectorizer = TfidfVectorizer(
        sublinear_tf=True,
        stop_words='english')
    word_vectorizer.fit(resume_arr)
    X = word_vectorizer.transform(resume_arr)

    # create umap representation of vector
    data = X.toarray()
    umap = get_umap(data)

    # create KDTree and dataframe to keep track of point/ID pairs
    points_df = pd.DataFrame(index=ID_list)
    points_df['umap_0'] = umap[:,0]
    points_df['umap_1'] = umap[:,1]   
    kdtree_arr = points_df.to_numpy()
    tree = makeTree(kdtree_arr)

    #save tree to DB
    try:
        saveTree(tree, points_df)
    except:
        print("unable to save tree to DB")
