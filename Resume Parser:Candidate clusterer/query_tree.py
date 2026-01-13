import pickle 
import boto3




def loadTree():
    """
    Returns:
      # tuple cointaining KDTree and dataframe loaded from pickle files
    """
    # TODO: replace with DB query
    with open(r"tree.pickle", "rb") as input_file:
      tree = pickle.load(input_file)
    with open(r"df.pickle", "rb") as input_file2:
      df = pickle.load(input_file2)
    
    # bucket = 'your_bucket_name'
    # key = 'your_pickle_filename.pkl'
    # s3 = boto3.resource('s3')
    # tree = pickle.load(s3.Bucket(bucket).Object(key).get()['Body'].read())
    # df = pickle.load(s3.Bucket(bucket).Object(key).get()['Body'].read())


    return (tree, df)


def queryTree(target_ID, num_neighbors):
    """
    Params:
      # target_ID: (int) ID # of target point

      # num_neighbors: (int) Number of nearest neighbors to find
    
    Returns:
      # closest_points: List containing ID #'s of closest points to given datapoint
    """
    try:
      tree, df = loadTree()
    except:
      print("unable to load tree from DB")
    dist, ind = tree.query([df.iloc[target_ID]], k=num_neighbors+1)
    closest_points = list(ind[0])
    closest_points.remove(target_ID)
    print(closest_points)
    return closest_points