import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
from fastai.vision.all import load_learner

p = "train/export.pkl"
learn_inf = load_learner(p)

whos_that_pokemon, _, prob = learn_inf.predict('pikachu01.jpg')
print(f"it's: {whos_that_pokemon}")
