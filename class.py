import pandas as pd
#from jsonify import convert
 
from flask import Flask, request,json, jsonify
app = Flask(__name__)


@app.route('/get')
def get_data():
    data = pd.read_csv('class_data.csv')
    ls= list(data.to_dict("index").values())
    #convert.jsonify('class_data')
    return json.dumps(ls)

@app.route('/post',methods=['POST'])
def post_data():
    data = request.get_json()
    df = pd.read_csv('class_data.csv')
    new_dict= df.to_dict("index")
    list_of_df=list(new_dict.values())
    created_df={}
    created_df['index']=(list_of_df[-1]['index']+1)
    combined_data={**created_df, **data}
    df =df.append(combined_data, ignore_index=True )
    print(df)
    df.to_csv('class_data.csv', index=None, header=True)
    
    #convert.jsonify('class_data')
    return jsonify({"index":created_df["index"]})
    


if __name__ == '__main__':
    app.run(debug= True)
