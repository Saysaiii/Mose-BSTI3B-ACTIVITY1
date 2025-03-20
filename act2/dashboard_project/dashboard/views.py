
from django.shortcuts import render

def dashboard_view(request):
    data = [
        {"title": "Users", "count": 50},
        {"title": "Orders", "count": 420},
        {"title": "Revenue", "count": 20450},
    ]
    return render(request, 'dashboard/dashboard.html', {'data': data})
