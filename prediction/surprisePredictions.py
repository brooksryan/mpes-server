import os

from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import evaluate
from surprise import accuracy


# UNCOMMENT FOR PREDICTIONS
# UNCOMMENT FOR PREDICTIONS
# UNCOMMENT FOR PREDICTIONS
# UNCOMMENT FOR PREDICTIONS
# UNCOMMENT FOR PREDICTIONS

# file_path = os.path.expanduser('~/workspace/MasterTickUploadSmaller.csv')

# reader = Reader(line_format='user item rating', sep=',',rating_scale=(-4,4))

# data = Dataset.load_from_file(file_path, reader=reader)

# data.split(n_folds=2)


# algo = SVD()
# evaluate(algo, data, measures=['RMSE', 'MAE'], verbose=True)

# # Retrieve the trainset.
# trainset1 = data.build_full_trainset()
# algo.fit(trainset1)

# testset = trainset1.build_testset()
# predictions = algo.test(testset)

# accuracy.rmse(predictions, verbose=True)



# def getThisUsersPredictions(userid,routeid):
    
#     thisUserId = userid
    
#     thisRouteId = routeid
    
#     thisPrediction = algo.predict(thisUserId, thisRouteId, 0)
    
#     print(thisPrediction)
    
#     return(thisPrediction)

# userid = str(002)
# itemid = str(7180259)

# print algo.predict(userid, 3073080, 5)