import malih_parser
import pandas as pd
import re


def cleanResume(resumeText):
    resumeText = re.sub(',+', ' ', resumeText)  # remove commas
    resumeText = re.sub('nan', '', resumeText)  # remove nan
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

def main():


    # --------- code to be replaced by database query ------------
    df = pd.read_csv("./example.csv")
    df = pd.DataFrame(df.iloc[:,[2,3,8]])
    df.insert(len(df.columns), "all_contents", "", True)
    all_contents_column = []
    for index in df.index:
        row = df.iloc[index] 
        rows_contents = []
        for i in range(len(df.columns)): 
            rows_contents.append(str(row[i]))
        all_contents_column.append(" ".join(rows_contents))
    df['all_contents'] = all_contents_column
    df['all_contents'] = df['all_contents'].apply(lambda x: cleanResume(x))
    parsed_data = df['all_contents'].values
    IDs = [1,2,3,5,6,7,8,9,10,11,12,13,14,15,16]
    # ---------- code to be replaced by database query ----------


    malih_parser.cluster_candidates(parsed_data, IDs)
    malih_parser.load_similar_candidates(14, 6)
    


if __name__ == "__main__":
    main()