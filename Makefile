##
## EPITECH PROJECT, 2021
## B-CNA-410-NCE-4-1-groundhog-melvyn.dubois
## File description:
## Makefile
##

NAME		=		groundhog

SRC			=		groundhog.py

$(NAME):
					cp $(SRC) binary.py
					mv binary.py groundhog
					chmod +x groundhog

all:				$(NAME)

clean:
					rm -rf groundhog

fclean:				clean

re:					fclean all

.PHONY: 			all clean fclean re