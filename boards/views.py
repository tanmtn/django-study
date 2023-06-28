from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from reviews.models import Review

# Create your views here.
def show_board(request):
    return HttpResponse("show board123123123")

def all_board(request):
    # boards = Board.objects.all()

    return HttpResponse("All board")


# localhost:8000/board/1/asd
def make_board(request, board_id, board_content):

    return HttpResponse(f"Make board/ id: {board_id} / content: {board_content}")

# Rendering
def show_all_board(request):
    
    boards = Board.objects.all()

    return render(request, "all_boards.html", {"datas": boards, "status":"success"})

# Rendering
def show_board_reviews(request):

    reviews = Review.objects.all()
    
    return render(request, "reviews.html", {"datas": reviews, "status":"success"})

