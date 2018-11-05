def mk_source_dir(source="90_1FM", 
  date_string="ISO_8601String", 
  max_days=10):
  """
  test_mkdir(source+date_string)
  
  after looking for other directories 
  in cwd with names beginning with source 
  and deleting the oldest if the 
  number of such >= max_days.  
  """  
  import os
  
  try: 
    newdir = source + date_string
#    print('newdir = ', newdir)
    os.mkdir(newdir)
  except FileExistsError:
    pass

# Now delete the oldest if there are 
# more than max_days
  
  # https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory#973488
  next_walk = next(os.walk('.'))[1]
  # next_walk should all be directories
  
  source_walk = []
  source_date = []
#  len_source = len(source)
  for x in next_walk:
    if source == x[:len(source)]:
      source_walk.append(x)
      source_date.append(os.path.getctime(x))
      
  n_source = len(source_walk)
  print("n_source = ", n_source, 
      ";  max_days = ", max_days)

  if n_source >= max_days: 
    oldest = source_date.index(min(source_date))
    print("oldest =", source_walk[oldest], 
        ", with cdate = ", source_date[oldest])
    import shutil
    shutil.rmtree(source_walk[oldest]) 
  
