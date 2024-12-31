main: generate_tree generate_star
	manim -qk -p main.py

generate_tree:
	python3 parts/tree.py

generate_star:
	python3 parts/star.py


