#!/usr/bin/env bash

chessboard solve --length=3 --height=3 --king=2 --rook=1 --silent

chessboard solve --length=4 --height=4 --rook=2 --knight=4 --silent

chessboard solve --length=1 --height=1 --queen=1 --silent
chessboard solve --length=2 --height=2 --queen=2 --silent
chessboard solve --length=3 --height=3 --queen=3 --silent
chessboard solve --length=4 --height=4 --queen=4 --silent
chessboard solve --length=5 --height=5 --queen=5 --silent
chessboard solve --length=6 --height=6 --queen=6 --silent
chessboard solve --length=7 --height=7 --queen=7 --silent
chessboard solve --length=8 --height=8 --queen=8 --silent
chessboard solve --length=9 --height=9 --queen=9 --silent

chessboard solve --length=5 --height=5 --king=2 --queen=2 --bishop=2 --knight=1 --silent
chessboard solve --length=6 --height=6 --king=2 --queen=2 --bishop=2 --knight=1 --silent
chessboard solve --length=7 --height=7 --king=2 --queen=2 --bishop=2 --knight=1 --silent
