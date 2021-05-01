##  Solve some problems from hacker rank


### Setting up env
    python -m virtualenv .hacker
    source .hacker/bin/activate
    
### basic git setup
    git init
    git add README.md
    git commit -m "......"
    git branch -M main
    git remote add origin https://github.com/msashish/hackerRank.git
    git push -u origin main
    
    
### Testing solutions automatically
    python -m unittest tests/test_plus_minus.py
    python -m unittest tests/test_diagonal_difference.py
    
### Run all test cases
    python -m unittest discover tests
    
### Testing solutions manually
    python solutions/diagonal_difference.py
    python solutions/plus_minus.py