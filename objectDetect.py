from roboflow import Roboflow
rf = Roboflow(api_key="ASz2gIqAlmd4jq39ET2z")
project = rf.workspace("roboflow-gw7yv").project("website-screenshots")
dataset = project.version(1).download("yolov5")

