from django.shortcuts import render

def detail(request, pk):
    item =get_object_or_404(Item, pk=pk)
