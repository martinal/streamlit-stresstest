How to use:

- Open a terminal and cd to repository root dir

- Create minimal venv with:
  ```./install.sh```

- Run streamlit with:
  ```./run.sh```

- Wait for streamlit to load in browser

- Open another terminal in the repository root dir and run:
  ```python scripts/simulate_edits.py```


Now lean back and watch streamlit getting stress tested for race conditions.
Hopefully the following two kinds of errors show themselves:

```
────────────────────────── Traceback (most recent call last) ───────────────────────────
  /.../streamlit-stresstest/venv/lib/python3.10/site-packages/streamlit/runtime/scriptrunner/script_runner.py:565 in _run_script                                        
                                                                                        
  /.../streamlit-stresstest/main.py:5 in <module>                                   
                                                                                        
     2 # print("Top of main", sys.modules.get("mylib") is not None)                     
     3 import streamlit as st                                                           
     4 st.write("Loading main", sys.modules.get("mylib") is not None)                   
  ❱  5 import mylib                                                                     
     6 st.write("mylib.f()", mylib.f(), sys.modules.get("mylib") is not None)           
     7 # print("Bottom of main", sys.modules.get("mylib") is not None)                  
     8                                                                                  
  in _find_and_load:1027                                                                
  in _find_and_load_unlocked:1006                                                       
  in _load_unlocked:699                                                                 
────────────────────────────────────────────────────────────────────────────────────────
KeyError: 'mylib'
```

```
────────────────────────── Traceback (most recent call last) ───────────────────────────
  /.../streamlit-stresstest/venv/lib/python3.10/site-packages/streamlit/runtime/scriptrunner/script_runner.py:565 in _run_script                                        
                                                                                        
  /.../streamlit-stresstest/main.py:6 in <module>                                   
                                                                                        
     3 import streamlit as st                                                           
     4 st.write("Loading main", sys.modules.get("mylib") is not None)                   
     5 import mylib                                                                     
  ❱  6 st.write("mylib.f()", mylib.f(), sys.modules.get("mylib") is not None)           
     7 # print("Bottom of main", sys.modules.get("mylib") is not None)                  
     8                                                                                  
     9 st.write('414')                                                                  
────────────────────────────────────────────────────────────────────────────────────────
AttributeError: module 'mylib' has no attribute 'f'
```
