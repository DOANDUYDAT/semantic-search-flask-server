import src.libs.vector_search as vector_search

loaded_model = vector_search.load_headless_pretrained_model()
loaded_model.save('pre-model.hdf5')