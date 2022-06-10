sphinx-apidoc -o . ../unit ../networking ../main.py ../game.py ../ui
sphinx-apidoc -o . ../networking
sphinx-build . ../build
