from giskard import demo

# Train your model
clf, df = demo.titanic()

# Fill in the artifacts needed to run the giskard app
artifacts = {"Model":{}, "Dataset":{}}

artifacts["Model"]["model"]=clf
artifacts["Model"]["model_type"]="classification"

artifacts["Dataset"]["df"]=df 
artifacts["Dataset"]["target"]="Survived"

return artifacts
