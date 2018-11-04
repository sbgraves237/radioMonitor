def test_mkdir(DIRECTORY_NAME):
  import os
  try: 
    os.mkdir(DIRECTORY_NAME)
  except FileExistsError:
    pass
