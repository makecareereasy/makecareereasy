from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def pay(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 100

        client = razorpay.Client(
            auth=("rzp_test_PbdaHI5LqDSOAQ", "CcvAgMgRnfE13YfUentADHyH"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'stripe/razor.html')

@csrf_exempt
def success(request):
    return render(request, "stripe/success.html")