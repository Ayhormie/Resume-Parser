import make_tree
import query_tree




def parse_resumes():
    #run pyeparser code
    #save data to DB
    pass



def cluster_candidates(parsed_data, IDs):
    """
    Params:
      # parsed_data: array containing parsed resume data

      # IDs: list of corresponding ID #'s for parsed resume contents
    """
    make_tree.createTree(parsed_data, IDs)



def load_similar_candidates(target_ID, num_neighbors):
    """
    Params:
      # target_ID: ID number of target point

      # num_neighbors: number of closest points to return
    """
    query_tree.queryTree(target_ID, num_neighbors)
















